## Hardware CRC - Porting Guide

The Hardware CRC HAL API provides a low-level interface to the Hardware CRC
module of a target platform. Implementing the Hardware CRC API is not mandatory,
but implementing it you can gain the performance benefits of using hardware
acceleration for CRC calculations, if the API is not implemented the CRC API
will fallback to using table and bitwise CRC implementations.

#### Assumptions

##### Defined Behaviour

* Calling hal_crc_compute_partial_start() multiple times will override the
  current CRC configuration and calculation.

* The current intermediate calculation is lost if the module is reconfigured
  with hal_crc_compute_partial_start().

* hal_crc_compute_partial() does nothing if either the buffer is undefined or
  the size is equal to 0.

* hal_crc_compute_partial() is safe to call multiple times. The new data is
  appended to the current calculation.

* hal_crc_is_supported must return false if the the platform cannot support the
  initial/final values or data reflection in/out that is required by the input
  polynomial.

##### Undefined Behaviour

* Calling the hal_crc_get_result() function multiple times is undefined. The
  contents of the result register after it has been read is platform-specific.
  The HAL API makes no assumptions what the register contains so it is not safe
  to call this multiple times.

* Calling the hal_crc_partial_start() function with a polynomial unsupported by
  the current platform is undefined. Polynomial support should be checked before
  this function is called.

* Calling the hal_crc_compute_partial() function before calling
  hal_crc_partial_start() is undefined. The Hardware CRC module must be
  configured correctly using the start function before writing data to it.

#### Dependencies

Hardware CRC module in MCU that supports at least one of the following defined
polynomials: `POLY_8BIT_CCITT, POLY_7BIT_SD, POLY_16BIT_CCITT, POLY_16BIT_IBM,
POLY_32BIT_ANSI `

#### Implementing the CRC API

You can find the API and specification for the Hardware CRC API in the following
header file:

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/feature-hal-spec-crc-doxy/classmbed_1_1_crc.html)

To enable Hardware CRC support in Mbed OS, add the `CRC` label in the
`device_has` option of the target's section in the `targets.json` file.

#### Testing

The Mbed OS HAL API provides a set of conformance tests for Hardware CRC. You
can use these tests to validate the correctness of your implementation. To run
the Hardware CRC HAL tests use the following command:

```
mbed test -t <toolchain> -m <target> -n "tests-mbed_hal-crc*"
```

You can read more about the test cases here:

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/feature-hal-spec-crc-doxy/classreset__reason_1_1_crc_test.html)
