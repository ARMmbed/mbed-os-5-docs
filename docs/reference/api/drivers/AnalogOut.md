## AnalogOut

Use the AnalogOut interface to set the output voltage of an analog output pin specified as a percentage or as an unsigned short. Mbed OS provides separate APIs to use percentage or range. Mbed OS supports a minimum resolution of 0.0 (VSS) to 1.0 (VCC), though the actual resolution supported is VCC/65,536V.

<span class="notes">**Note:** Not all pins are capable of being AnalogOut, so check the pinmap for your board.</span>

### AnalogOut class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_analog_out.html)

### AnalogOut hello, world

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/AnalogOut_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/AnalogOut_HelloWorld/file/a32148e02ecf/main.cpp)

### AnalogOut example

Create a sine wave.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/AnalogOut_ex_1/)](https://os.mbed.com/teams/mbed_example/code/AnalogOut_ex_1/file/066510b55650/main.cpp)
