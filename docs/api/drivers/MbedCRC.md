# MbedCRC

The MbedCRC Class provides support for Cyclic Redundancy Check (CRC) algorithms. MbedCRC is a template class with polynomial value and polynomial width as arguments.

You can use the `compute` API to calculate CRC for the selected polynomial. If data is available in parts, you must call the `compute_partial_start`, `compute_partial` and `compute_partial_stop` APIs in the proper order to get the correct CRC value. You can use the `get_polynomial` and `get_width` APIs to learn the current object's polynomial and width values.

ROM polynomial tables are for supported 8/16-bit CCITT, 16-bit IBM and 32-bit ANSI polynomials. By default, ROM tables are used for CRC computation. If ROM tables are not available, then CRC is computed at runtime bit by bit for all data input.

For platforms that support [hardware CRC](mbedcrc.html), the MbedCRC API replaces the software implementation of CRC to take advantage of the hardware acceleration the platform provides.

## MbedCRC class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.0/mbed-os-api-doxy/structcrc__mbed__config.html)

## MbedCRC examples

### Example 1

Below is a CRC example to compute 32-bit CRC.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-CRC_ex_1/tree/v6.0)](https://github.com/ARMmbed/mbed-os-snippet-CRC_ex_1/blob/v6.0/main.cpp)

### Example 2

Below is a 32-bit CRC example using `compute_partial` APIs.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-CRC_ex_2/tree/v6.0)](https://github.com/ARMmbed/mbed-os-snippet-CRC_ex_2/blob/v6.0/main.cpp)

### Example 3

Below is a CRC example for the SD driver.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-CRC_ex_3/tree/v6.0)](https://github.com/ARMmbed/mbed-os-snippet-CRC_ex_3/blob/v6.0/main.cpp)

## Related content

- [Hardware CRC](mbedcrc.html).
