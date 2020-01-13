# Drivers overview

Drivers provide access to general purpose microcontroller hardware. Drivers typically access a microcontroller's hardware peripherals directly, and may form the lowest lever of a protocol or network stack.

The Mbed OS driver APIs include analog and digital inputs and outputs on development boards, as well as digital interfaces, which allow your board to interface with a computer or external devices. With these drivers, you can read or set the voltage of analog pins, control digital pins individually or grouped into a bus and trigger an event when more data is available on the bus. You can also control the frequency and mark to space ratio, or duty cycle, of a Pulse Width Modulated (PWM) digital output.

## Blocking nature

By default, all Mbed OS driver APIs are blocking. In the drivers, blocking APIs cause the current thread to wait until the hardware operation completes. Blocking APIs simplify control flow, allow for linearly structured programs and make debugging intuitive. We suggest using blocking APIs as a starting point. You should only consider more complex APIs if the blocking APIs do not satisfy your requirements.

Mbed OS is built around an RTOS, and to complement this, the drivers are thread safe. This means that if you use multiple drivers in a blocking manner, as long as the drivers are in separate threads, their operations can still be carried out in parallel. When a driver blocks a thread, the RTOS either switches to any nonblocked threads or sleeps. This means that in most cases, an application using blocking APIs has the same advantages as one using nonblocking APIs.

In some cases, the drivers provide nonblocking APIs. These APIs configure hardware to run in the background of the processor, without blocking a thread. Nonblocking drivers signal through the attach function once the background operation is complete.

## Attaching callbacks to drivers

In Mbed OS, the standard API for asynchronous events is the attach function. You can use the attach function to attach a callback function. Drivers call the attached callback function during specific events. You can use this to learn when the state of a nonblocking operation changes or whether other asynchronous events occur.

For example, you can attach a callback function on a [Serial](serial.html) object, which the Serial object calls when the serial line receives a packet on the RX line.

One important thing to note is that when you attach callbacks with this function, the driver calls them in interrupt context. Interrupt context runs at a higher priority than any thread, which means that any code called from the attach callback must be interrupt safe. This excludes any blocking APIs such as blocking drivers, malloc, and mutexes. Or you risk preventing other high-priority interrupts from running, which may break other parts of the OS.

When you need to call code that’s not interrupt safe from interrupt context, you must first defer from the interrupt context to a thread. The easiest way to defer to a thread is to signal a waiting thread through a [Semaphore](semaphore.html). In more complex use cases, you can use an [EventQueue](eventqueue.html) to manage multiple events at once.
