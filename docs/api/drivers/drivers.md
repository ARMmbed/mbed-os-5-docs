## Drivers overview

Driver APIs include analog and digital inputs and outputs on development boards, as well as digital interfaces, which allow your board to interface with a computer or external devices. With these drivers, you can read or set the voltage of analog pins, control digital pins individually or as a grouped value and trigger an event when a digital input pin changes value. You can also control the frequency and mark to space ratio of a digital pulse wave (or train).

### Blocking nature

For every driver, there is a required blocking API. Many drivers also have optional nonblocking APIs. The difference between blocking and nonblocking APIs lies in their behavior. Blocking APIs block all following tasks until the current task completes. Nonblocking APIs, however, don't block execution. Instead, nonblocking APIs allow remaining tasks to continue.

A benefit of blocking APIs is that they can make development easier. They allow for linear programming and straightforward debugging. 

To optimize the benefits from blocking APIs, be sure to use multiple threads. Don't mix blocking and nonblocking APIs because it can lead to complications in your code and can make debugging more confusing. 

<!---add design patterns about HAL, drivers working together, attach programming model/design pattern that sticks you in interrupt context, all blocking by nature, blockwise or bulk transfers, play down asynchronous natures, focus on blocking--->
