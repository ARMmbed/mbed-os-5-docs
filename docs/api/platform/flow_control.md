# Application flow control

We can use Blinky to explore flow control and task management in Arm Mbed OS applications. We'll look at automated actions first, then move on to handling user actions.

## Flow control for delayed actions

If we want to automatically blink an LED, we have four main techniques:

1. [Busy wait](#busy-wait)
1. [Ticker, Timeout](#ticker-timeout)
1. [Thread](#thread)
1. [EventQueue](#eventqueue)

All above techniques accomplish delays but cater to different requirements for precision, efficiency and context.

<span class="tips">**Tip:** You may want to read the [power optimization](../apis/platform-concepts.html) tutorial to understand how to achieve power savings. </span>

### Busy wait

Busy wait is a method that blocks the processor for a period of time. The processor runs at full power for the duration of the wait:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Flow-Control-Busy-Wait)](https://github.com/ARMmbed/mbed-os-snippet-Flow-Control-Busy-Wait/blob/v6.0/main.cpp)

Notice `wait_us()` - it is part of the [Wait API](../mbed-os-api-doxy/group__platform__wait__api.html) to busy wait a given number of microseconds.

The Wait API is an ISR-safe way to create short delays of nanoseconds to a few microseconds. However, we do not recommend busy waiting for longer delays.

The following techniques are better suited for milliseconds to seconds delays which apply to our example's use case.

### Ticker, Timeout

Tickers and Timeouts are non-blocking, interrupt-based ways of creating a time interval - your code continues to execute or sleep when there is nothing to do. The difference is that Tickers are recurring whereas Timeouts are one-off.

Here is an example that uses a ticker object:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Flow-Control-Ticker)](https://github.com/ARMmbed/mbed-os-snippet-Flow-Control-Ticker/blob/v6.0/main.cpp)

<span class="warnings"> **Warning:** A ticker/timeout's handlers are executed in ISR context and thus, like any ISR handlers, should return quickly and not use `printf` or APIs that are not intended for ISRs.</span>

If you don't need the precision of a high-frequency ticker or timeout, we recommend that you use LowPowerTicker or LowPowerTimeout instead. These allow the system to be put in deep sleep mode.

- _High-resolution microsecond ticker/timeout_ ([Ticker](ticker.html), [Timeout](timeout.html))
- _Low Power ticker/timeout_ ([LowPowerTicker](lowpowerticker.html), [LowPowerTimeout](lowpowertimeout.html))

Usage of the low power classes will inform the operating system of your desire to allow Deep Sleep mode on your system, although actually entering deep sleep depends on the specific environment and characteristics of your system. For more information about Sleep and Deep Sleep, please refer to our [documentation page](power-management-sleep.html) as well as watch our [Mbed Office Hours video](https://www.youtube.com/watch?v=OFfOlBaegdg&t=12s) where the concepts of Sleep and Deep Sleep are described in-depth.

### Thread

If your application is running in RTOS mode then [Thread](../apis/thread.html)s are another efficient way to blink an LED. During the waiting period, it is possible to take advantage of Mbed OS optimizations to automatically conserve power and deal with other tasks.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Flow-Control-Thread)](https://github.com/ARMmbed/mbed-os-snippet-Flow-Control-Thread/blob/v6.0/main.cpp)

Threads are the most efficient ways to run tasks in Mbed OS since the operating system internally contains optimizations for efficient scheduling of tasks and maximizing the system's sleep time.

### EventQueue

The [EventQueue](../apis/eventqueue.html) class has a simple-to-use `call_every()` function to schedule repeated actions:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/Tutorials_UsingAPIs/Flow-Control-EventQueue)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/Tutorials_UsingAPIs/Flow-Control-EventQueue/main.cpp)

<span class="tips">**Tip:** For one-off delays, use `call_in()`.

Just as with Ticker/Timeout, if no threads are running during a wait, the system enters sleep mode.</span>

A major advantage of EventQueue over [Ticker/Timeout](#ticker-timeout) is that the handler is called in the same context (thread, in the case of RTOS) where the EventQueue is dispatched, thus ISR-related restrictions (e.g. no `printf`, no `Muxex` usage, etc.) do not apply.

## Flow control for manual actions

Let’s use a DigitalIn pin from the button to control the application. There are two ways to read input data: we can either constantly poll the button, or set an interrupt to trigger when pressed. We’ll explore these methods below.

### Active polling button

We can wait for digital input the same way we waited for time to pass - using a `while()` loop. In the example below the digital input is a button press, which causes the application to flash the LED and then wait for one second.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Flow-Control-Active-Polling-Button)](https://github.com/ARMmbed/mbed-os-snippet-Flow-Control-Active-Polling-Button/blob/v6.0/main.cpp)

We constantly poll the button to see whether it has a value that matches `BUTTON_PRESS`. If it matches, we toggle the LED and wait one second.

`BUTTON_PRESS` is used to denote what value the switch uses to represent the state *pushed*. Most switches are by default open (unpressed), so they will read as 0 while pressed. If you see your LED blinking without the button being pressed - try changing `BUTTON_PRESS` to `1`.

### Interrupt button

An alternative way to poll the button is to use an interrupt. Interrupts let you say `when that pin changes value, call this function`. In other words, we can tell the MCU to call a function when the button is pressed. In our case, that function toggles the LED:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Flow-Control-Interrupt-Button)](https://github.com/ARMmbed/mbed-os-snippet-Flow-Control-Interrupt-Button/blob/v6.0/main.cpp)

In the code above a heartbeat function runs on LED2, which lets you see that your code is running. Then we connect an InterruptIn object to the button and set it so that when the button rises from 0 to 1, the toggle function is called; the function toggles LED1. This way the application can turn the LED on and off as needed, without needing to “waste” time waiting or actively polling an inactive button. The MCU is free to move on to other things .

Interrupt driven programming is one of the fundamental paradigms of microcontroller programming.
