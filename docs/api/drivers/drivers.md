## Drivers overview

Drivers provide access to general purpose microcontroller hardware. Drivers typically don't require software stacks but can be the signaling foundation of protocol stacks and networking stacks. 

The Mbed OS driver APIs include analog and digital inputs and outputs on development boards, as well as digital interfaces, which allow your board to interface with a computer or external devices. With these drivers, you can read or set the voltage of analog pins, control digital pins individually or as a grouped value and trigger an event when a digital input pin changes value. You can also control the frequency and mark to space ratio of a digital pulse wave (or train).

### Design patterns

[Note to self: Include content about our drivers working together and about other design patterns.]

### Blocking nature

For every driver, there is a required blocking API. Many drivers also have optional nonblocking APIs. The difference between blocking and nonblocking APIs lies in their behavior. Blocking APIs block all following tasks until the current task completes. Nonblocking APIs, however, don't block execution. Instead, nonblocking APIs allow remaining tasks to continue.

A benefit of blocking APIs is that they can make development easier. They allow for linear programming and straightforward debugging. In some situations, they can also increase speed.

To optimize the benefits from blocking APIs, be sure to use multiple threads. Don't mix blocking and nonblocking APIs because it can lead to complications in your code and can make debugging more confusing. 

[Note to self: Add something about blockwise or bulk transfers.]

### Attach programming model

[Note to self: Add content about this design pattern sticking you in interrupt context.]

<!---add design patterns about HAL, drivers working together, attach programming model/design pattern that sticks you in interrupt context, all blocking by nature, blockwise or bulk transfers, play down asynchronous natures, focus on blocking--->
