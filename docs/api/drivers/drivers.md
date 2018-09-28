## Drivers overview

Drivers provide access to general purpose microcontroller hardware. Drivers typically access a microcontroller's hardware peripherals directly, and may form the lowest lever of a protocol or network stack.

The Mbed OS driver APIs include analog and digital inputs and outputs on development boards, as well as digital interfaces, which allow your board to interface with a computer or external devices. With these drivers, you can read or set the voltage of analog pins, control digital pins individually or grouped into a bus and trigger an event when more data is available on the bus. You can also control the frequency and mark to space ratio, or duty cycle, of a Pulse Width Modulated (PWM) digital output.

### Design patterns

[Note to self: Include content about our drivers working together and about other design patterns.]

### Blocking nature

For every driver, there is a required blocking API. Many drivers also have optional nonblocking APIs. The difference between blocking and nonblocking APIs lies in their behavior. Blocking APIs block the current thread until the API call completes. Nonblocking APIs, however, don't block execution. Instead, nonblocking API calls return a structure that indicates the status of the operation started.

A benefit of blocking APIs is that they can make development easier. Blocking APIs allow for programs structured linearly and straightforward debugging. In some situations, they can also increase speed.

To optimize for the benefits from blocking APIs, be sure to use multiple threads. Avoid mixing blocking and nonblocking APIs in the same thread as it can lead to complications in your code and can make debugging more confusing. 

[Note to self: Add something about blockwise or bulk transfers.]

### Attaching callbacks to drivers

Mbed OS drivers support an asynchronous, also called event-driven, paradigm, using the “attach” interface. You can use this interface to attach a callback function that drivers call during specific events.

For example, you can attach a callback function to be called when a driver receives a data received (RX) interrupt.

The callback is executed in a different context, and the callback function should be implemented with what’s permitted in that context. For example, if the callback happens in interrupt context, your callback implementation should only do operations permitted in interrupt context. To help with the implementation of callback functions, the software component or driver exporting the “attach” interface
documents the context in which the callbacks will be invoked.

<!---add design patterns about HAL, drivers working together, attach programming model/design pattern that sticks you in interrupt context, all blocking by nature, blockwise or bulk transfers, play down asynchronous natures, focus on blocking--->
