## Bare-metal APIs
<h3 id="analog-i-o">Analog I/O</h3>
<ul><li>AnalogIn - Read the voltage applied to an analog input pin
</li><li>AnalogOut - Set the voltage of an analog output pin
</li></ul>
<h3 id="digital-i-o">Digital I/O</h3>
<ul><li>DigitalIn -  Configure and control a digital input pin.
</li><li>DigitalOut -  Configure and control a digital output pin.
</li><li>DigitalInOut - Bi-directional digital pins
</li></ul>
<ul><li>BusIn -  Flexible way to read multiple DigitalIn pins as one value
</li><li>BusOut - Flexible way to write multiple DigitalOut pins as one value
</li><li>BusInOut - Flexible way to read/write multiple DigitalInOut pins as one value
</li></ul>
<ul><li>PortIn -  Fast way to read multiple DigitalIn pins as one value
</li><li>PortOut - Fast way to write multiple DigitalOut pins as one value
</li><li>PortInOut - Fast way to read/write multiple DigitalInOut pins as one value
</li></ul>
<ul><li>PwmOut - Pulse-width modulated output
</li></ul>
<ul><li>InterruptIn -  Trigger an event when a digital input pin changes.
</li></ul>
<h3 id="timers">Timers</h3>
<ul><li>Timer - Create, start, stop and read a timer
</li><li>Timeout - Call a function after a specified delay
</li><li>Ticker - Repeatedly call a function
</li></ul>
<ul><li>wait - Wait for a specified time
</li><li>time - Get and set the realtime clock
</li></ul>
<h3 id="digital-interfaces">Digital Interfaces</h3>
<ul><li>Serial -  Serial/UART bus
</li></ul>
<ul><li>SPI - SPI bus master
</li><li>SPISlave - SPI bus slave
</li></ul>
<ul><li>I2C - I²C bus master
</li><li>I2CSlave - I²C bus slave
</li></ul>
<ul><li>CAN - Controller-area network bus
</li></ul>