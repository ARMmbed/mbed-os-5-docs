# AnalogIn

Use the AnalogIn API to read an external voltage applied to an analog input pin. `AnalogIn()` reads the voltage as a fraction of the system voltage. The value is a floating point from `0.0`(VSS) to `1.0`(VCC). For example, if you have a 3.3V system and the applied voltage is 1.65V, then `AnalogIn()` reads `0.5` as the value.

One of the most common types of analog to digital converters used in microcontrollers today is called the successive-approximation ADC. Successive-approximation is a popular choice in modern microcontrollers because of the fact that it is accurate and low-power and takes up a small amount of space inside of the microcontroller.

Another fairly common type of ADC is the flash ADC. Flash ADCs offer the fastest analog to digital solution. However, because of the way that flash ADCs are built, they use a lot of power and take up a lot of space, in that they use many components.

The resolution for an ADC is the smallest distinguishable change in analog input that causes the digital output to change. For example, a 12-bit ADC in a 3.3V system has 4,096 distinguishable outputs. Therefore, the resolution of a 12-bit ADC is 3.3/4096 = 0.81mV. In an Mbed Enabled system where the digital result from the analog input is in the range of 0.0 to 1.0, a change of 0.81mV in the analog input results in a change in the digital output of 1.0/4096 = 0.00024.

<span class="notes">**Note:** Only certain pins are capable of making these measurements, so check the pinmap of your board for compatible pins.</span>

## AnalogIn class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_analog_in.html)

## AnalogIn hello, world

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/AnalogIn_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/AnalogIn_HelloWorld/file/04e47b45f593/main.cpp)

## AnalogIn examples

### Example one

Control an R/C servo with analog input.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/AnalogIn_ex_1/)](https://os.mbed.com/teams/mbed_example/code/AnalogIn_ex_1/file/64493a867413/main.cpp)

### Example two

This example shows AnalogIn reading 16-bit normalized samples.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/AnalogIn_ex_2/)](https://os.mbed.com/teams/mbed_example/code/AnalogIn_ex_2/file/803d1b3eb85e/main.cpp)
