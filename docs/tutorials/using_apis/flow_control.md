# Application flow control

You can use [Blinky](../quick-start/index.html), an example application you can use to get to know Arm Mbed OS and the development tools, to explore flow control and task management in Arm Mbed OS applications. We'll look at automated actions first, then move on to manual (user) actions.

## Automated actions

There are three main techniques to automatically blink an LED:

1. [Busy wait](#busy-wait)
1. [Ticker](#ticker)
1. [Thread](#thread)

### Busy wait

Busy wait is a method that blocks the processor for a period of time. This is an effective way to create time delays, but it’s inefficient because it wastes processor time and keeps the processor running at full power for the duration of the wait:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/tree/master/Flow-Control/Busy-Wait)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/Flow-Control/Busy-Wait/main.cpp)

Notice `printf()`; you can enable this by uncommenting the line (remove the `//`). `printf()` prints to the terminal, so you can use it to get debug information.

<span class="tips">**Tip:** We recommend using [CoolTerm](http://freeware.the-meiers.org/) because it works the same on Windows, Linux and macOS. Please see [our video about how to use CoolTerm](https://www.youtube.com/watch?v=jAMTXK9HjfU) to connect to your board and view the `printf()` statements. For more information, please see our [serial communication tutorials](../tutorials/serial-communication.html).</span>

### Ticker

Tickers and timers are another way of creating a time interval. These methods are somewhat better than busy wait because they allow other code to run while you are waiting. It is even possible, though nontrivial, to sleep during the wait period.

This example does not include sleeping:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/tree/master/Flow-Control/Ticker)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/Flow-Control/Ticker/main.cpp)

### Thread

Threads are the most efficient way to blink an LED. During the waiting period, it is possible to take advantage of Mbed OS optimizations to automatically conserve power and deal with other tasks. Although this is not the most visually appealing method, nor the simplest, it is the preferred way for large scale deployments:<!--why?-->

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/tree/master/Flow-Control/Thread)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/Flow-Control/Thread/main.cpp)

## Manual (user) actions

There are two ways to read input data: constantly poll the button in a busy wait or set an interrupt to trigger when pressed. This tutorial explores these methods below by using a DigitalIn pin from the button to control the application.

<span class="tips">**Tip:** You may need to change the `SW1` pin you set in these examples because the button on your board may be called something else. Please refer to the pin map on the [boards page](https://os.mbed.com/platforms/).</span>

### Busy wait button

You can wait for digital input the same way you waited for time to pass - using a `while()` loop. In the example below, the digital input is a button press, which causes the application to flash the LED and then wait for 1 second.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/tree/master/Flow-Control/Busy-Wait-Button)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/Flow-Control/Busy-Wait-Button/main.cpp)

Constantly poll the button to see whether it has a value that matches `button_press`. If it matches, toggle the LED, and wait 1 second.

`button_press` denotes the value the switch uses to represent the state *pushed*. Most switches are by default open (unpressed), so they read as 0 while pressed. If you see the LED blinking without the button being pressed, try changing `button_press` to `1`.

### Interrupt button

Interrupt-driven programming is one of the fundamental paradigms of microcontroller programming. Interrupts let you say "when that pin changes value, call this function". In other words, you can tell the MCU to call a function when the button is pressed. In this case, that function toggles the LED:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/tree/master/Flow-Control/Interrupt-Button)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/Flow-Control/Interrupt-Button/main.cpp)

In the code above, a heartbeat function runs on LED2, which lets you see that your code is running. Then you can connect an InterruptIn object to the button and set it so that when the button rises from 0 to 1, the toggle function is called; the function toggles LED1. This way, you can turn the LED on and off without needing to “waste” time waiting or actively polling an inactive button. The MCU is free to move on to other things.
