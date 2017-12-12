## AnalogIn

Use the AnalogIn API to read an external voltage applied to an analog input pin. `AnalogIn()` reads the voltage as a fraction of the system voltage. The value is a floating point from `0.0`(VSS) to `1.0`(VCC). For example, if you have a 3.3V system and the applied voltage is 1.65V, then `AnalogIn()` reads `0.5` as the value.

<span class="notes">**Note:**  Only certain pins are capable of making these measurements, so check the pinmap of your board for compatible pins.</span>

### AnalogIn class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/v5.7/mbed-os-api-doxy/classmbed_1_1_analog_in.html)

### AnalogIn hello, world

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/AnalogIn_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/AnalogIn_HelloWorld/file/77750f8cba47/main.cpp)

### AnalogIn examples

#### Example one

Control an R/C servo with analog input.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/AnalogIn_ex_1/)](https://os.mbed.com/teams/mbed_example/code/AnalogIn_ex_1/file/490818b6238b/main.cpp)

#### Example two

This example shows AnalogIn reading 16-bit normalized samples.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/AnalogIn_ex_2/)](https://os.mbed.com/teams/mbed_example/code/AnalogIn_ex_2/file/cb98929b3895/main.cpp)
