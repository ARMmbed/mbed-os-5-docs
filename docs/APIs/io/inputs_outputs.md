# Handling inputs and outputs

Inputs and outputs on development boards are either analog or digital.

## Analog I/O

These APIs read or set the voltage of analog pins:

* [AnalogIn](AnalogIn.md) - read the voltage of an analog input pin.
* [AnalogOut](AnalogOut.md) - set the voltage of an an along output pin.

## Digital I/O

Digital pins can be controlled individually or as a grouped value.

### Individual control

* [DigitalIn](DigitalIn.md): read a single digital input pin.
* [DigitalOut](DigitalOut.md): write to a single digital output pin.
* [DigitalInOut](DigialInOut.md): read and write to a single bi-directional digital pin.

### Grouped control

* Bus: flexible control of multiple pins:
	* [BusIn](BusIn.md): read multiple pins as a single value.
	* [BusOut](BusOut.md): write a single value to multiple pins.
	* [BusInOut](BusInOut.md): read and write to multiple bi-directional pins.
* Port: fast way to handle an underlying GPIO; this is less flexible than the bus because of the constraints imposed by the underlying GPIO ports:
	* [PortIn](PortIn.md): read multiple pins as a single value.
	* [PortOut](PortOut.md): write a single value to multiple pins.
	* [PortInOut](PortInOut.md): read and write to multiple bi-directional pins.

### InterruptIn

[InterruptIn](InterruptIn.md) triggers an event when a digital input pin changes value.

### PwmOut

[PwmOut](PwmOut.md) controls the frequency and mark to space ratio of a digital pulse wave (or train).
