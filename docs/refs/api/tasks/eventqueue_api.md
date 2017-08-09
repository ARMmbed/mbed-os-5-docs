#### EventQueue API

[TO-DO: Combine and rewrite the text below to create one comprehensive document about the EventQueue, when combined with the event loop section above. The source of the below text is: https://developer.mbed.org/blog/entry/Simplify-your-code-with-mbed-events/.]

[`mbed-events`](https://github.com/ARMmbed/mbed-events) is an eventing system that can run in an RTOS thread. Using an event loop is useful to defer execution of code to a different context. An example would be to defer execution from an interrupt context (ISR) to the main loop, or to defer execution from the high-priority thread to a lower priority thread.

== Calling printf in an interrupt context ==

The following program has probably been written by anyone learning how to program microcontrollers. It registers an interrupt handler when a button is pressed, and then calls `printf` from the ISR.

**Naive approach**

<<code>>
#include "mbed.h"

DigitalOut led(LED1);
InterruptIn btn(SW2);

void do_something() {
  led = !led;
  printf("Toggle LED!\r\n"); // CRASH! Blocking call in ISR...
}

int main() {
  btn.fall(&do_something);

  while (1) { }
}
<</code>>

When you compile this code with ARMCC, the program crashes right after toggling the LED. This is because calls to stdio (like `printf`) are [guarded by mutexes](https://developer.mbed.org/handbook/CMSIS-RTOS) in the ARM C standard library, and mutex functions [cannot be called from an ISR](https://www.keil.com/pack/doc/cmsis/RTOS/html/group__CMSIS__RTOS__MutexMgmt.html). We can get around this by signalling the main thread from the ISR and do the `printf` call in there. That's especially confusing when teaching beginners, as now we need to explain the concept of [Sempahores](https://developer.mbed.org/handbook/RTOS#semaphore) or [Mailboxes](https://developer.mbed.org/handbook/RTOS#mail), as well.

While using a semaphore works, it's a lot more unclear, and we need to build a state machine to determine why the semaphore was released if we're adding more interrupts. Preferably we'd also run this in a separate thread.

With `mbed-events`, we can easily spin up a new RTOS thread with the event loop running in it, and we can defer from ISR to that thread in one line of code.

**Using mbed-events**

<<code>>
#include "mbed.h"

DigitalOut led(LED1);
InterruptIn btn(SW2);

// create an event queue
EventQueue queue;

void do_something() {
  // this now runs in the context of eventThread, instead of in the ISR
  led = !led;
  printf("Toggle LED!\r\n");
}

int main() {
  // create a thread that'll run the event queue's dispatch function
  Thread eventThread;
  eventThread.start(callback(&queue, &EventQueue::dispatch_forever));

  // wrap calls in queue.event to automatically defer to the queue's thread
  btn.fall(queue.event(&do_something));

  while (1) {}
}
<</code>>

When the interrupt fires, it automatically defers calling the `do_something` function to the other thread, from where it's safe to call `printf`. In addition, you don't need to taint the main thread's main loop with program logic.

== Manually deferring from ISR to a thread ==

The downside of this approach is that both the toggling of the LED and the `printf` call are now executed outside the ISR and thus are not guaranteed to run immediately. You can work around this by toggling the LED from the ISR, then manually deferring the printf event to the thread.

<<code>>
#include "mbed.h"

DigitalOut led(LED1);
InterruptIn btn(SW2);

EventQueue queue;

void do_something_outside_irq() {
  // this does not run in the ISR
  printf("Toggle LED!\r\n");
}

void do_something_in_irq() {
  // this runs in the ISR
  led = !led;

  // then defer the printf call to the other thread
  queue.call(&do_something_outside_irq);
}

int main() {
  Thread eventThread;
  eventThread.start(callback(&queue, &EventQueue::dispatch_forever));

  btn.fall(&do_something_in_irq);

  while (1) {}
}
<</code>>

== Mixing high priority and low priority events ==

You can differentiate between the importance of events by using multiple threads that run with different priorities. You can easily add a [Ticker](https://developer.mbed.org/handbook/Ticker) to the program, which toggles LED2 every second, which runs with a higher priority than the `printf` calls by creating a second event queue.

<<code>>
#include "mbed.h"

DigitalOut led1(LED1);
DigitalOut led2(LED2);
InterruptIn btn(SW2);

EventQueue printfQueue;
EventQueue eventQueue;

void blink_led2() {
  // this runs in the normal priority thread
  led2 = !led2;
}

void print_toggle_led() {
  // this runs in the lower priority thread
  printf("Toggle LED!\r\n");
}

void btn_fall_irq() {
  led1 = !led1;

  // defer the printf call to the low priority thread
  printfQueue.call(&print_toggle_led);
}

int main() {
  // low priority thread for calling printf()
  Thread printfThread(osPriorityLow);
  printfThread.start(callback(&printfQueue, &EventQueue::dispatch_forever));

  // normal priority thread for other events
  Thread eventThread(osPriorityNormal);
  eventThread.start(callback(&eventQueue, &EventQueue::dispatch_forever));

  // call blink_led2 every second, automatically defering to the eventThread
  Ticker ledTicker;
  ledTicker.attach(eventQueue.event(&blink_led2), 1.0f);

  // button fall still runs in the ISR
  btn.fall(&btn_fall_irq);

  while (1) {}
}
<</code>>

== Conclusion ==

`mbed-events` makes it easier to defer calls from one context to another, whether it's from an ISR back to a user thread, or from one thread to another. It also makes it easy to prioritise certain events over other events, and does not require you to write your own state machine or taint your main loop. Because it's a one-liner (wrap the callback in ##queue.event()##) to wrap a call that would normally run in an ISR, it's also very friendly for beginners.

-

The EventQueue has no concept of event priority. If you schedule events to run at the same time, the order in which the events run relative to one another is undefined. The EventQueue only schedules events based on time. If you want to separate your events into different priorities, you must instantiate an EventQueue for each priority. You must appropriately set the priority of the thread dispatching each EventQueue instance.

#### EventQueue implementation

[A document about the particular features and peculiarities of the implementation of the EventQueue.]
