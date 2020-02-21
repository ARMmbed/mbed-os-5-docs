# Bare metal APIs

Mbed OS bare metal supports the following APIs:

<h2 id="analog-i-o">Analog I/O</h2>

- AnalogIn - Read the voltage applied to an analog input pin.
- AnalogOut - Set the voltage of an analog output pin.

<h2 id="digital-i-o">Digital I/O</h2>

- DigitalIn - Configure and control a digital input pin.
- DigitalOut - Configure and control a digital output pin.
- DigitalInOut - Bidirectional digital pins.

- BusIn - Flexible way to read multiple DigitalIn pins as one value.
- BusOut - Flexible way to write multiple DigitalOut pins as one value.
- BusInOut - Flexible way to read and write multiple DigitalInOut pins as one value.

- PortIn - Fast way to read multiple DigitalIn pins as one value.
- PortOut - Fast way to write multiple DigitalOut pins as one value.
- PortInOut - Fast way to read and write multiple DigitalInOut pins as one value.

- PwmOut - Pulse-width modulated output.

- InterruptIn - Trigger an event when a digital input pin changes.

<h2 id="timers">Timers</h2>

- Timer - Create, start, stop and read a timer.
- Timeout - Call a function after a specified delay.
- Ticker - Repeatedly call a function.

- Wait - Wait for a specified time.
- Time - Get and set the realtime clock.

<h2 id="digital-interfaces">Digital Interfaces</h2>

- Serial - Serial/UART bus.

- SPI - SPI bus master.
- SPISlave - SPI bus slave.

- I2C - I²C bus master.
- I2CSlave - I²C bus slave.

- CAN - Controller-area network bus.
