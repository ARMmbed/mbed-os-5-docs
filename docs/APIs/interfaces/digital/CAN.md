# CAN

CAN or Controller-Area Network is a bus standard designed to allow microcontrollers and devices to communicate with each other without a host computer.

## Hello World!

This example sends from one CAN bus (can1) an counter while it is listen on the other CAN bus (can2) to receive a packet. Each bus controller should be connected to a CAN bus transceiver. These should be connected together at a CAN bus.

In order to use CAN, you need transceivers, which change the digital signal (RD/TD), outputted by the LPC1768 into a differential signal, which is transmitted along the CAN bus to the other nodes. As well as this, you need two 120 Ohm terminating resistors at either end of the bus. Without both the transceivers and the terminating resistors, the bus will not work properly. Below is an example circuit, which demonstrates how to set up a CAN bus, which simply loops the data between the mbed LPC1768's two CAN buses.

<span class="images">![](../Images/can.png)</span>

<span class="notes">**Note:** If using the LPC1768, or the LPC11C1X series, the transceivers are not included on the chip, so the two transceivers are required. However, if you are using the LPC11C2X series, you do not need transceivers, as they are already present on the chip. In both cases, you need terminating resistors. </span> 

<span class="warnings">**Warning:** The mbed's pins are 5V tolerant, so this example will work. However, do not assume that the chip you are using has 5V tolerant pins, so consult with the user manual/datasheet of your device to check this. If it is not 5V tolerant, a logic level converter can be used, to lower the logic levels to 3.3V logic. </span>

```
#include "mbed.h"

Ticker ticker;
DigitalOut led1(LED1);
DigitalOut led2(LED2);
CAN can1(p9, p10);
CAN can2(p30, p29);
char counter = 0;

void send() {
    printf("send()\n");
    if(can1.write(CANMessage(1337, &counter;, 1))) {
        printf("wloop()\n");
        counter++;
        printf("Message sent: %d\n", counter);
    } 
    led1 = !led1;
}

int main() {
    printf("main()\n");
    ticker.attach(&send;, 1);
    CANMessage msg;
    while(1) {
        printf("loop()\n");
        if(can2.read(msg)) {
            printf("Message received: %d\n", msg.data[0]);
            led2 = !led2;
        } 
        wait(0.2);
    }
}
```

## API

API summary

[![View code](https://www.mbed.com/embed/?type=library)](https://developer.mbed.org/users/mbed_official/code/mbed/docs/tip/classmbed_1_1CAN.html) 

## Details

The CAN Interface can be used on mbed pins p9/p10 and p30/p29

<span class="images">![](../Images/small_pin_out.png)</span>

The CAN Interface can be used to write data words out of a CAN port and will return the data received from another CAN device. The CAN clock frequency can be configured.

## Resources

  * [Wikipedia](http://en.wikipedia.org/wiki/Controllerarea_network)
