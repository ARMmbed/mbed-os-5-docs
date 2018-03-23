## MbedCRC

MbedCRC Class provides software CRC generation algorithms. MbedCRC is template class with polynomial value and polynomial width as arguments.
`compute` API can be used to calculate CRC for the selected polynomial. In case data is available in parts `compute_partial_start`, `compute_partial`, and `compute_partial_stop` API's must be called in proper order to get correct CRC value.
`get_polynomial` and `get_width` API's can be used to know current objects polynomial and width values.

ROM polynomial tables are for supported 8/16-bit CCITT, 16-bit IBM and 32-bit ANSI polynomials. By default ROM tables will be used for CRC computation, if ROM tables are not available then CRC is computed runtime bit by bit for all data input.

### MbedCRC class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/5.8/mbed-os-api-doxy/classmbed_1_1_mbed_c_r_c.html)

### MbedCRC examples

#### Example 1

CRC example to compute 32-bit CRC.

[![View code](https://os.mbed.com/teams/mbed_example/code/CRC_example/)](https://os.mbed.com/teams/mbed_example/code/CRC_example/file/a9d9b5c4a32b/main.cpp/)


#### Example 2

32-bit CRC example using 'compute_partial` API's

[![View code](https://os.mbed.com/teams/mbed_example/code/CRC_partial_example/)](https://os.mbed.com/teams/mbed_example/code/CRC_partial_example/file/77ae554366b9/main.cpp/)


#### Example 3

CRC example for SD driver

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/CRC_eample_sd/)](https://os.mbed.com/teams/mbed_example/code/CRC_eample_sd/file/ee110889fa99/main.cpp)
