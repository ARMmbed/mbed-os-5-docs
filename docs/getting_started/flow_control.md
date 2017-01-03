# Application flow control and task management 

We can use Blinky to explore flow control and task management in mbed OS applications. We'll look at automated actions first, then move on to handling user actions.

## Flow control for automated actions

If we want to automatically blink an LED, we have three main techniques:

1. [Busy wait](#busy-wait)
1. [Ticker](#ticker)
1. [Thread](#thread) 

### Busy wait

Busy wait is a method that blocks the processor for a period of time. This is an effective way to create time delays, but it’s inefficient because it wastes processor time and keeps the processor running at full power for the duration of the wait:

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed-Workshops/code/Workshop-1-Example-1/)](https://developer.mbed.org/teams/mbed-Workshops/code/Workshop-1-Example-1/file/tip/main.cpp)

Notice `printf()`; you can enable this by uncommenting the line (remove the `//`). `printf()` prints to the terminal, so you can use it to get debug information. We recommend using [CoolTerm](http://freeware.the-meiers.org/), as it works the same on Windows, Linux and OS X. [Here is a handy video on how to use CoolTerm](https://www.youtube.com/watch?v=jAMTXK9HjfU) to connect to your board and view the `printf()` statements. 

### Ticker

Tickers and timers are another way of creating a time interval. These methods are somewhat better than busy wait because they allow other code to run while you are waiting. It is even possible, though non-trivial, to sleep during the wait period.

Here is an example that doesn't include sleeping:

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed-Workshops/code/Workshop-1-Example-2/)](https://developer.mbed.org/teams/mbed-Workshops/code/Workshop-1-Example-2/file/tip/main.cpp)

### Thread 

Threads are the most efficient way to blink an LED. During the waiting period, it is possible to take advantage of mbed OS optimizations to automatically conserve power and deal with other tasks. While this is not the most visually appealing method, nor the simplest, it is the preferred way for large scale deployments:

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed-Workshops/code/Workshop-1-Example-3/)](https://developer.mbed.org/teams/mbed-Workshops/code/Workshop-1-Example-3/file/tip/main.cpp)

## Flow control for manual actions

Let’s try using a DigitalIn pin from the button to control the application. There are two ways to read input data: we can either constantly poll the button in a busy wait, or set an interrupt to trigger when pressed. We’ll explore these methods below. 

### Busy wait button

We can wait for digital input the same way we waited for time to pass - using a `while()` loop. In the example below the digital input is a button press, which causes the application to flash the LED and then wait for 1 second. 

<span class="tips">**Tip:** You may need to change the `SW1` pin, as the button on your board may be called something else. Please refer to the pinmap on the [Boards page](https://developer.mbed.org/platforms/). </span>

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed-Workshops/code/Workshop-1-Example-4/)](https://developer.mbed.org/teams/mbed-Workshops/code/Workshop-1-Example-4/file/tip/main.cpp)

We constantly poll the button to see whether it has a value that matches `button_press`. If it matches, we toggle the LED and wait 1 second. 

`button_press` is used to denote what value the switch uses to represent the state *pushed*. Most switches are by default open (unpressed), so they will read as 0 while pressed. If you see your LED blinking without the button being pressed - try changing `button_press` to `1`.

### Interrupt button

An alternative way to poll the button is to use an interrupt. Interrupts let you say `when that pin changes value, call this function`. In other words, we can tell the MCU to call a function when the button is pressed. In our case, that function toggles the LED: 

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed-Workshops/code/Workshop-1-Example-5/)](https://developer.mbed.org/teams/mbed-Workshops/code/Workshop-1-Example-5/file/tip/main.cpp)

In the code above a heartbeat function runs on LED2, which lets you see that your code is running. Then we connect an InterruptIn object to the button and set it so that when the button rises from 0 to 1, the toggle function is called; the function toggles LED1. This way we can turn the LED on and off as needed, without needing to “waste” our time waiting or actively polling an inactive button. We (or rather - the MCU) are free to move on to other things . 

Interrupt driven programming is one of the fundamental paradigms of microcontroller programming. 
