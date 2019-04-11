# CAN

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_c_a_n.png)<span>CAN class hierarchy</span></span>

Controller-Area Network (CAN) is a bus standard that allows microcontrollers and devices to communicate with each other without going through a host computer.

<span class="notes">**Note:** You can use the CAN interface to write data words out of a CAN port. It will return the data received from another CAN device. You can configure the CAN clock frequency.</span>

## CAN class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_c_a_n.html)

## CAN hello, world

This example sends a counter from one CAN bus (can1) and listens for a packet on the other CAN bus (can2). Each bus controller should be connected to a CAN bus transceiver. These should be connected together at a CAN bus.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/CAN_ex_1/)](https://os.mbed.com/teams/mbed_example/code/CAN_ex_1/file/d6cbcdb04ada/main.cpp)
