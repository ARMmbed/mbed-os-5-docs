### CAN

Controller-Area Network (CAN) is a bus standard that allows microcontrollers and devices to communicate with each other without going through a host computer.

#### API

API summary

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/CAN_8h_source.html)

#### Hello World!

This example sends a counter from one CAN bus (can1) and listens for a packet on the other CAN bus (can2). Each bus controller should be connected to a CAN bus transceiver. These should be connected together at a CAN bus.

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed_example/code/CAN_ex_1/)](https://developer.mbed.org/teams/mbed_example/code/CAN_ex_1/file/5791101761f9/main.cpp)


#### Details

You can use the CAN interface to write data words out of a CAN port. It will return the data received from another CAN device. You can configure the CAN clock frequency.
