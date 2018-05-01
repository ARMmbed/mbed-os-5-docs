## The `EventQueue.background` method

An [event queue](/docs/development/tutorials/the-eventqueue-api.html) moves tasks from one **execution context** to another **execution context**.

In the embedded space, developers use the event queue to move IRQs from high-priority interrupt context to a low-priority threaded context:

``` cpp
EventQueue equeue;

// example function
void print_callback() {
    printf("hi!\n");
}

// high priority interrupt context
void irq() {
    // we use the "call" method to pass the callback_function to a different execution context
    equeue.call(print_callback);
}

// low priority threaded context
int main() {
    // hardware timer, can only execute code in interrupt context
    Timer timer;
    timer.attach_ms(irq, 100);

    // dispatch events in our current context
    equeue.dispatch();
}
```

This example assigns the execution context for events by calling the `dispatch` function. `dispatch` runs the event queue in the current execution context, in this case the low-priority thread.

However, `dispatch` has a downside: It consumes the whole thread. While you're running `dispatch`, you can't execute anything else.

Passing a timeout to `dispatch` lets you get your execution context back for periodic events:

``` cpp
// low priority threaded context
int main() {
    // hardware timer, can only execute code in interrupt context
    Timer timer;
    timer.attach_ms(irq, 100);

    while (true) {
        // dispatch events in our current context for 100 ms
        equeue.dispatch(100);

        // super fancy status update system
        led = !led;
    }
}
```

You can even pass 0 ms to execute any pending events and return immediately, which lets you spend all of your time blinking the LED.

However, that's still rather limiting. If you want to do stuff in your thread, execute events _and_ sleep, you need to learn how long to sleep from the event queue. However, because any IRQ can update the event queue, the time to sleep can change, so you also need a way to receive notifications when a new sleep time has been decided.

This is the use case for the event queue `background` function.

``` cpp
/** Background an event queue onto a single-shot timer-interrupt
 *
 *  When updated, the event queue calls the provided update function
 *  with a timeout indicating when the queue should be dispatched. A
 *  negative timeout is passed to the update function when the
 *  timer-interrupt is no longer needed.
 *
 *  Passing a null function disables the existing update function.
 *
 *  The background function allows an event queue to take advantage of
 *  hardware timers or other event loops, allowing an event queue to be
 *  run in the background without consuming the foreground thread.
 *
 *  @param update   Function called to indicate when the queue should be
 *                  dispatched
 */
void background(mbed::Callback<void(int)> update);
```

The `background` function is a way of allowing the event queue to tell you when it can sleep. You can use `background` and `dispatch` together to run an event queue in the "background" of an execution context, without completely consuming the context.

This looks like the following:

``` cpp
// sleeping stuff so we're not burning fuel all the time
int sleep_time = -1;
Semaphore sleep_sema;
void sleep_callback(int new_sleep_time) {
    // update sleep_time
    sleep_time = new_sleep_time;

    // go ahead and wake up thread so it can sleep for new sleep_time
    sleep_sema.signal();
}

// low priority threaded context
int main() {
    // hardware timer, can only execute code in interrupt context
    Timer timer;
    timer.attach_ms(irq, 100);

    // attach our sleep callback so we get sleep updates
    equeue.background(sleep_callback);

    while (true) {
        // dispatch any pending events
        equeue.dispatch(0);

        // super duper fancy status update system
        led = !led;

        // go to sleep until next event
        sleep_sema.wait(sleep_time);        
    }
}
```

Now you will execute events, toggle your LED and sleep all using just one execution context.

The `background` function handles all of the corner cases for you, such as canceling events and nested events, so as long as you call dispatch after the timeout, everything works.

<span class="notes">**Note:** When the event queue _doesn't_ have a timeout, the callback is passed the value `-1` (which is the same as `osWaitForever`). In this example, passing `-1` to the semaphor wait returns the behavior you want, but sometimes you need to treat this as a special case. Also, the event queue passes `-1` at destruction time.</span>

That while loop resembles an event queue by itself. Although you can use the `background` function to run one event queue in another event queue's context, it's complicated enough that it is wrapped up in `background`'s sister function: `chain`:

``` cpp
/** Chain an event queue onto another event queue
 *
 *  After chaining a queue to a target, calling dispatch on the target
 *  queue also dispatches events from this queue. The queues use
 *  its own buffers, and you must handle events independently.
 *
 *  A null queue as the target unchains the existing queue.
 *
 *  The chain function allows you to compose multiple event queues,
 *  sharing the context of a dispatch loop while still being managed
 *  independently.
 *
 *  @param target   Queue that dispatches this queue's events as a
 *                  part of its dispatch loop
 */
void chain(EventQueue *target);
```

With `chain`, you can rewrite [a blinking light example](mbed-os-quick-start.html) to use its own event queue:

``` cpp
// your own event queue
EventQueue blinky_equeue(2*EVENTS_EVENT_SIZE);

// status update
void blink() {
    led = !led;
}

// low priority threaded context
int main() {
    // hardware timer, can only execute code in interrupt context
    Timer timer;
    timer.attach_ms(irq, 100);

    // chain your event queue onto this new event queue for the blinking lights
    equeue.chain(&blinky_equeue);

    // blink our led every 100 ms
    blinky_equeue.call_every(100, blink);

    // dispatch our root event queue
    blinky_equeue.dispatch();
}
```

You want to tightly control the memory consumption of each event loop.

Consider an example Sonar class driven by a complicated FSM that I'm too lazy to write:

``` cpp
class Sonar {
    Sonar(EventQueue *parent_queue=mbed_event_queue()) {
        // attach our sonar FSM to the provided event queue, defaulting to the global mbed event queue
        _equeue.chain(parent);
    }

    EventQueue _equeue(SONAR_EVENTS * EVENTS_EVENT_SIZE);
}
```

Normally, when you pass around an event queue, you need to track how many events could be allocated at once. However, if you chain event queues together, the parent no longer needs to care about the child's quantity of events, as long as it gives the child the hook to dispatch its own event queue (1 event for the child's chain call).

In this way, you can pass the decision of execution context entirely up to your caller:

``` cpp
// create three sonars using your event queue
EventQueue queue(3 * EVENTS_EVENT_SIZE);
Sonar s1(&queue)
Sonar s2(&queue);
Sonar s3(&queue);

int main() {
    // dispatch all of your sonars at once
    queue.dispatch();
}
```

<span class="notes">**Note:** This is a form of controlling execution context _explicitly_. In Mbed OS, you can also control execution context _implicitly_ by creating different threads for each sonar. The decision for which one to use is left up to you.</span>
