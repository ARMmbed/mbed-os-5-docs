### Drivers

Driver APIs include analog and digital inputs and outputs on development boards, as well as digital interfaces, which allow your board to interface with a computer or external devices. With these drivers, you can read or set the voltage of analog pins, control digital pins individually or as a grouped value and trigger an event when a digital input pin changes value. You can also control the frequency and mark to space ratio of a digital pulse wave (or train).

#### Analog I/O

* [AnalogIn](AnalogIn.md): read the voltage of an analog input pin.
* [AnalogOut](AnalogOut.md): set the voltage of an analog output pin.

#### Digital I/O

You can control the digital pins individually or as a grouped value.

##### Individual control

* [DigitalIn](DigitalIn.md): read a single digital input pin.
* [DigitalOut](DigitalOut.md): write to a single digital output pin.
* [DigitalInOut](DigitalInOut.md): read and write to a single bidirectional digital pin.

##### Grouped control

* Bus: flexible control of multiple pins:
	* [BusIn](BusIn.md): read multiple pins as a single value.
	* [BusOut](BusOut.md): write a single value to multiple pins.
	* [BusInOut](BusInOut.md): read and write to multiple bidirectional pins.
* Port: fast way to handle an underlying GPIO; this is less flexible than the bus because of the constraints the underlying GPIO ports impose:
	* [PortIn](PortIn.md): read multiple pins as a single value.
	* [PortOut](PortOut.md): write a single value to multiple pins.
	* [PortInOut](PortInOut.md): read and write to multiple bidirectional pins.

##### InterruptIn

[InterruptIn](InterruptIn.md) triggers an event when a digital input pin changes value.

##### PwmOut

[PwmOut](PwmOut.md) controls the frequency and mark to space ratio of a digital pulse wave (or train).

#### Digital interfaces

* [Serial](digital/Serial.md): generic asynchronous protocol.
* SPI: serial peripheral interface:
	* [SPI](digital/SPI.md): master.
	* [SPISlave](digital/SPISlave.md): slave.
* I2C: inter-integrated circuit:
	* [I2C](digital/I2C.md): master.
	* [I2CSlave](digital/I2CSlave.md): slave.
* [CAN](digital/CAN.md): connect two devices without using a computer.
