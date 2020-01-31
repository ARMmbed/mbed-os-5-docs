# Four ways to Blinky

## Busy Wait, Ticker, Threads & EventQueues

In this tutorial, we will take the introductory example from Mbed OS, the [mbed-os-example-blinky](https://github.com/ARMmbed/mbed-os-example-blinky), whose purpose is to blink an LED by using Busy Wait and we will gradually modify it to introduce three more different Mbed API's: `Ticker`, `Threads` and `EventQueues`. All will allow us to accomplish the same thing as we will see but there are differences in the way that these API's cater for battery consumption, something which is critical important when doing embedded programming.

<span class="notes">**Note:** In our examples we are using [STMicroelectronics DISCO-L475VG-IOT01A](https://os.mbed.com/platforms/ST-Discovery-L475E-IOT01A/) board, but you can use any board supported by Mbed, albeit with some modifications on `LED` and `BUTTONS` constants to correctly point to your specific board characteristics. The [Mbed boards page](https://os.mbed.com/platforms/) provides detailed descriptions and architectural diagrams for each board so you can use it as a reference.</span>

Let's start first with the most simplistic example that blinks an `LED` using a busy wait:

## Busy Wait

Here is a snippet of the code that actually does the blinking:

```C
1. #include "mbed.h"
2. 
3. // define the Serial object
4. Serial pc(USBTX, USBRX);
5. 
6. int main()
7. {
8.     // Initialise the digital pin LED1 as an output
9.     DigitalOut led(LED1);
10.     
11.     while (true) {
12.         led = !led;
13.         pc.printf("Blink! LED1 is now %d\r\n", led.read());
14.     }
15. }
```

<span class="images">![](../../images/blinky-busywait.gif)</span>

At [4] we initialize the [Thread](serial.html) object to allow serial communication with the the host PC (using USB) in order to print our debug messages. Then at [9] we use the [DigitalOut](digitalout.html) object to control the digital output (e.g. our LED) for switching it on and off. Finally at [11] the program enters a busy loop (using `while`) that repeatedly blinks the LED.

Albeit the code is simplistic it does allow us to highlight one important issue. The busy wait `while` loop causes the device to not go to sleep, wasting battery life. Although for the needs of this example it may be sufficient, avoiding busy wait loops and allowing the system to go to sleep as much as possible should be our uttermost goal.

Mbed as a multitasking operating system has many threads running in the background in order to support system services as well as run the actual user code. A partial list of threads can be summerized in the following list:

- The `Main thread` that executes the application `void main()` function as in our example.
- The `Idle thread` that is scheduled to run when there are no other threads available to run. The job of this thread is to ensure the device is put into sleep and save processor cycles with the ultimate goal to preserve battery life.
- The `Timer thread` that schedules repetive (or one-shot) functions to be called.

In our code we run in the context of the `Main` thread and since we have entered into an busy loop we don't allow the 'Idle thread' to kick-in and put the device to Sleep (or Deep Sleep) to preserve battery life.

Let's now see a different example of `blinky` this time using a [Ticker](ticker.html) object that setups a function to be called repeatedly and at a specified rate. This example will further help us highlight another important concept in Mbed, which is usually a source of confusion and results in runtime issues when programming with Mbed. 
 

## Ticker

Here is a snippet of the code:

```C
1. #include "mbed.h"
2. 
3. Ticker flipper;
4. DigitalOut led1(LED1);
5.  
6.  // define the Serial object
7. Serial pc(USBTX, USBRX);
8. 
9. void flip() {
10.     led1 = !led1;
11.     pc.printf("Blink! LED1 is now %d\r\n", led1.read());
12. }
13.  
14. int main() {
15.     led1 = 1;
16.     flipper.attach(&flip, 1.0); // the address of the function to be attached (flip) and the interval (1 seconds)
17.  }
```

The code is similar to the previous example but this time we use the [Ticker](ticker.html) object to schedule a repetitive function `flip()` [10] to blink the `LED` after one second. Uncomment line [11] and flash it to the device. The program starts and after blinking of `LED1`, execution halts with a system error.

Let's examine the error message:

```
Blink! LED1 is now 1
Blink! LED1 is now 0
Blink! LED1 is now 1
Blink! LED1 is now 0

++ MbedOS Error Info ++
Error Status: 0x80010133 Code: 307 Module: 1
Error Message: Mutex: 0x2000038C, Not allowed in ISR context
Location: 0x800A3E5
Error Value: 0x2000038C
Current Thread: rtx_idle  Id: 0x100018D0 Entry: 0x8007F81 StackSize: 0x380 StackMem: 0x10001958 SP: 0x20017EF0
For more info, visit: https://mbed.com/s/error?error=0x80010133&tgt=DISCO_L475VG_IOT01A
-- MbedOS Error Info --

= System will be rebooted due to a fatal error =
= Reboot count(=5) reached maximum, system will halt after rebooting
```

The reason of this can be traced on the fact that any code that runs in Mbed can be in two different context modes, either run within the context of `Interrupt mode` or in user `Thread mode` and there are specific restrictions on what code is allowed to do in each one. In the first case, the `Interrupt mode`, the developer should cater for:
	
-  the code should execute as fast as possible (without blocking) and return to `Thread mode`.
-  the code should not call library fuctions that are not designed to be called in `Interrupt mode`.

<span class="notes">**Note:** The [Thread safety page](thread-safety.html) in our documentation highlights the different API's that are allowed be called in each mode and can serve as a reference during your development.</span>

Coming back to the example above, you need to pay attention that the Ticker object schedules a function to be called in `Interrupt mode` and as such certain API functions won't work and will cause a system error. In our case the call to the Serial object method `printf` [12] is not allowed in `Interrupt` mode and thus the system error we receive.

<span class="notes">**Note:** The concepts of `Interrupt` mode or `Thread` mode in which your code runs and what is allowed to call is crucial to understand and you should always consult the documention to avoid unexpected runtime errors such as the one we faced in our sample code above.</span>

Comment out again line [11] and build and run the project. The system error should not occur now if you consult the console.

<span class="images">![](../../images/blinky-ticker.gif)</span>

Tickers in Mbed OS are hardware timers used to track small amounts of time (think us, ms, s, min; but usually not hours or data). Mbed has two classes of Tickers:

- _High-resolution microsecond tickers_ ([Timer](timer.html), [Timeout](timeout.html), [Ticker](ticker.html))
- _Low Power tickers_ ([LowePowerTimer](lowpowertimer.html), [LowePowerTimeout](lowpowertimeout.html), [LowePowerTicker](lowpowerticker.html))

The difference between the different classes of Tickers is the way they coooperate with the operating system to allow the device to enter either Sleep or Deep Sleep mode (for more gains in battery consuption). Usage of the low power class of Tickers will inform the operating system of your desire to enable Deep Sleep mode in your board, although enabling this depends on the specific environment and characteristics where your code runs. But it's helpful to know that there are options to enable this. For more information about Sleep and Deep Sleep, we would suggest to look at our documentation page [here](power-management-sleep.html) as well as watch our [Mbed Office Hours video](https://www.youtube.com/watch?v=OFfOlBaegdg&t=12s) where the concepts of Sleep and Deep Sleep are descibed in-depth.

Let's now rewrite the example above but this time utilizing Mbed's Thread API to schedule user Threads (which run in `Thread` mode) to achieve the blinking.


## Threads

Here is a snippet of the code:

```
1. #include "mbed.h"
2. 
3. // Blinking rate in milliseconds
4. #define BLINKING_RATE_LED1_MS                                                    500
5. #define BLINKING_RATE_LED2_MS                                                    1000
6. 
7. DigitalOut led1(LED1);
8. DigitalOut led2(LED2);
9. Thread thread;
10. 
11. // define the Serial object
12. Serial pc(USBTX, USBRX);
13. 
14. void led2_thread() {
15.     while (true) {
16.         led2 = !led2;
17.         pc.printf("Blink! LED2 is now %d\r\n", led1.read());
18.         thread_sleep_for(BLINKING_RATE_LED2_MS);
19.     }
20. }
21.  
22. int main() {
23.     thread.start(led2_thread);
24.     
25.     while (true) {
26.         led1 = !led1;
27.         pc.printf("Blink! LED1 is now %d\r\n", led1.read());
28.         thread_sleep_for(BLINKING_RATE_LED1_MS);
29.     }
30. }
```

<span class="images">![](../../images/blinky-threads.gif)</span>

Here we have two threads running, one is the `Main` thread which within an infinite loop blinks repeatedly the first `LED1` and second using Mbed Thread API we create a second thread [23] that blinks the second `LED2` by calling the `led2_thread` function [14]. Notice, that since we are running in `Thread mode` our call to Serials `printf` function [14] succeeds this time and no system error is generated.

Browsing the [Thread class](thread.html) API documentation you will notice the similarities in method names with similar functionality offered by other programming languages threading constructs. This is deliberately done such as a newcomer developer to Mbed would feel right at home with the Threading API.
	 
Threads are the most efficient way to run tasks in Mbed since the operating system internally contains optimizations for efficiently scheduling the tasks and putting the device as much as possible to sleep (or deep sleep).

Although dealing with thread creation and management can be powerfull, still requires a lot of carefully written code to cope with thread management and synchronization. In some use cases, a more simplistic API offering similar functionality with Threads but in a way that is more developer friendly and more familiar to recent advances in asyncronous programming can be preferrable. 

Welcome to the wonderful world of EventQueue's !


## EventQueue

The API documentation of [EventQueue class](eventqueue.html) describes it with the following:

<span class="notes">**Note:** The EventQueue class provides a flexible queue for scheduling events. You can use the EventQueue class for synchronization between multiple threads, or to move events out of interrupt context (deferred execution of time consuming or non-ISR safe operations).</span>

In simplest terms, the EventQueue allows the developer to queue events (e.g. functions) to be run at a later time and importantly outside of the `Interrupt` mode we descibed earlier. All events are scheduled to run in user `Thread` mode.

Here is a snippet of code that schedules to call `printf` once [9], in two seconds [10] and every second [11]. Notice that since we are running in user `Thread mode` we are allowed to call those library functions. Calling those functions in `Interrupt` mode would have resulted in a system error as we show previously.
 

```C
1. #include "mbed_events.h"
2. #include <stdio.h>
3. 
4. int main() {
5.     // creates a queue with the default size
6.     EventQueue queue;
7. 
8.     // events are simple callbacks
9.     queue.call(printf, "called immediately\n");
10.    queue.call_in(2000, printf, "called in 2 seconds\n");
11.    queue.call_every(1000, printf, "called every 1 seconds\n");
12. 
13.    // events are executed by the dispatch method
14.    queue.dispatch();
15. }
```

<span class="notes">**Note:** The [EventQueue API documentation](the-eventqueue-api.html) page and the [class reference page](eventqueue.html) host more in-depth details of the internal operation of EventQueue as well as providing several examples of its usage.</span>

Let's return to our blinky example and see how we can rewrite it to use the `EventQueue` class instead. 

```C
1. #include "mbed.h"
2. #include "mbed_events.h"
3. 
4. DigitalOut led1(LED1);
5. InterruptIn sw(USER_BUTTON);
6. EventQueue queue(32 * EVENTS_EVENT_SIZE);
7. Thread t;
8. 
9. // define the Serial object
10. Serial pc(USBTX, USBRX);
11. 
12. void rise_handler_user_context(void) {
13.     pc.printf("rise_handler_user_context in context %p\r\n", osThreadGetId());
14.     pc.printf("Blink! LED1 is now %d\r\n", led1.read());
15. }
16. 
17. void fall_handler_user_context(void) {
18.     pc.printf("fall_handler_user_context in context %p\r\n", osThreadGetId());
19.     pc.printf("Blink! LED1 is now %d\r\n", led1.read());
20. }
21. 
22. void rise_handler(void) {
23.     // Execute the time critical part first
24.     led1 = !led1;
25.     // The rest can execute later in user context (and can contain code that's not interrupt safe).
26.     // We use the 'queue.call' function to add an event (the call to 'rise_handler_user_context') to the queue.
27.     queue.call(rise_handler_user_context);
28. }
29. 
30. void fall_handler(void) {
31.     // Execute the time critical part first
32.     led1 = !led1;
33.     // The rest can execute later in user context (and can contain code that's not interrupt safe).
34.     // We use the 'queue.call' function to add an event (the call to 'fall_handler_user_context') to the queue.
35.     queue.call(fall_handler_user_context);
36. }
37. 
38. int main() {
39.     // Start the event queue
40.     t.start(callback(&queue, &EventQueue::dispatch_forever));
41.     pc.printf("Starting in context %p\r\n", osThreadGetId());
42.     // The 'rise' handler will execute in interrupt context
43.     sw.rise(rise_handler);
44.     // The 'fall' handler will execute in interrupt context
45.     sw.fall(fall_handler);
46. }
```

<span class="images">![](../../images/blinky-eventqueue.gif)</span>

In the `void main()` function we start the Event Dispatch Queue thread and we attach two interrupt handlers, `fall_handler()` and `rise_handler()` on a button press and release status respectively. Notice that both interrupt handlers will run in `Interrupt mode` and as such we need to be as fast as possible (critical path). For that reason a call to Serials `printf()` method is prohibited in this mode as we described in the previous section. For that reason, we split the critical and non-critical path to separate functions and with the aid of the `EventQueue` `call()` method we schedule the invocation of the non-critical path at user context (``Thread mode`` of the event dispatch queue thread itself).

Similar to Threads, EventQueues offer an efficient mechanism to schedule Tasks and allow the operating system to apply optimizations in order to conserve battery life. 

### Conclusions

In this tutorial we demonstrated four different ways to blink a led and in the process we exposed the different API provided by Mbed: `Ticker`, `Threads` and `EventQueues` and how each caters to preserve battery life. Further we highlighted the critical concept of `Interrupt` and `Thread` context modes and how it can lead to confusion and runtime errors if the user is not aware in which context the code runs on. We suggest the interesting reader to visit the [Mbed OS fundamentals](../program-setup/mbed-os-fundamentals.html) section on the Mbed documentation web site where the concepts of Threads and Thread safety is discussed in more detail, as well as visit the [Thread](thread.html) and [EventQueue](eventqueue.html) API documentation for a thorough description of those classes together with useful code snippets that demonstrate various features of the API.

## Related content

- [Mbed OS fundamentals](../program-setup/mbed-os-fundamentals.html).
- [Thread Safety Tutorial](thread-safety.html).
- [EventQueue tutorial](the-eventqueue-api.html).