# Application flow control

We can use Blinky to explore flow control and task management in Arm Mbed OS applications. We'll look at automating actions with delays first, then move on to handling user actions.

## Automating actions with delays

If we want to automatically blink an LED, we have four main techniques:

1. [Wait API](#wait-api)
1. [Ticker and Timeout](#ticker-and-timeout)
1. [Thread](#thread)
1. [EventQueue](#eventqueue)

The techniques cater to different requirements for precision, efficiency and context.

### Wait API

The Wait API creates delays by actively blocking the execution for a period of time. It uses the busy wait strategy - internally running a loop until the end of the period.

Here is an example that uses `wait_us()` of the API to wait a number of microseconds:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Flow-Control-Busy-Wait)](https://github.com/ARMmbed/mbed-os-snippet-Flow-Control-Busy-Wait/blob/v6.0/main.cpp)

The processor is active for the entire duration, so the Wait API is suitable when you need short delays (nanoseconds to a few microseconds) without triggering [sleep modes](../apis/power-management-sleep.html) which have some wake-up latencies. It is also safe to use in interrupt contexts. However, we do not recommend busy waiting for longer delays, during which the system may not be able to switch to other tasks or save power as it cannot sleep.

For longer delays - millisecond to seconds - use one of the other techniques. 

### Ticker and Timeout

[Tickers](../apis/ticker.html) and [Timeouts](../apis/timeout.html) are non-blocking, interrupt-based ways of creating a time interval - your code continues to execute or sleep when there is nothing to do. The difference is that Tickers are recurring whereas Timeouts are one-off.

Here is an example that uses a ticker object:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Flow-Control-Ticker)](https://github.com/ARMmbed/mbed-os-snippet-Flow-Control-Ticker/blob/v6.0/main.cpp)

<span class="warnings"> **Warning:** A ticker/timeout's handlers are executed in interrupt contexts and thus, like any interrupt handlers, should return quickly and not use `printf` or APIs that are not intended for interrupts.</span>

If you don't need the precision of a high-frequency Ticker or Timeout, we recommend that you use [LowPowerTicker](../apis/lowpowerticker.html) or [Low Power Timeout](../apis/lowpowertimeout.html) instead. The low power classes inform the operating system you want to allow deep sleep mode on your system. Note that entering deep sleep also depends on the specific environment and characteristics of your system, not just your API selection. For more information about sleep and deep sleep, please refer to our [documentation about power management](../apis/power-management-sleep.html) and our [Mbed Office Hours video](https://www.youtube.com/watch?v=OFfOlBaegdg&t=12s).

### Thread

If your application is running in RTOS mode then [Threads](../apis/thread.html) are another efficient way to blink an LED. During the waiting period, it is possible to take advantage of Mbed OS optimizations to automatically conserve power and deal with other tasks. This makes Threads the most efficient way to run tasks in Mbed OS.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Flow-Control-Thread)](https://github.com/ARMmbed/mbed-os-snippet-Flow-Control-Thread/blob/v6.0/main.cpp)


### EventQueue

The [EventQueue](../apis/eventqueue.html) class uses the `call_every()` function to schedule repeated actions:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/Tutorials_UsingAPIs/Flow-Control-EventQueue)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/Tutorials_UsingAPIs/Flow-Control-EventQueue/main.cpp)

For one-off delays, use `call_in()`. Just as with Ticker and Timeout, if no threads are running during a wait, the system enters [sleep or deep sleep mode](../apis/power-management-sleep.html). A major advantage of EventQueue over Ticker and Timeout is that the handler is called in the same context as the EventQueue is dispatched (thread, in the case of RTOS), so interrupt-related restrictions (such as no `printf` oand no `Mutex`) do not apply.

## Handling user actions

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

## Further reading

- [Power optimization](../apis/platform-concepts.html)
