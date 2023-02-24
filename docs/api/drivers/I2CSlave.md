# I2CSlave

Use I2C Slave to communicate with I2C Master.

Synchronization level: not protected.

<span class="notes">**Note:** Remember that you need a pull-up resistor on sda and scl. All drivers on the I2C bus are required to be open collector, and so it is necessary to use pull-up resistors on the two signals. A typical value for the pull-up resistors is around 2.2k ohms, connected between the pin and 3v3. </span>

## I2CSlave class reference

<span class="notes">**Note:** The Arm Mbed API uses 8 bit addresses, so make sure to left-shift 7 bit addresses by 1 bit before passing them. </span>

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.16/mbed-os-api-doxy/classmbed_1_1_i2_c_slave.html)

## I2CSlave example

Try this example to see how an I2C responder works.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-I2CSlave/tree/v6.7)](https://github.com/ARMmbed/mbed-os-snippet-I2CSlave/blob/v6.7/main.cpp)
