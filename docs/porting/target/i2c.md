## Inter-Integrated Circuit (I2C)

I2C is a serial protocol for two-wire interface to connect low-speed devices
in embedded systems. The I2C API allows control and configuration of this
interface.

The interface is made up of two lines for all communication:
  - SCL: Serial Clock
  - SDA: Serial Data

#### Defined Behaviours

- `i2c_init`:
  - Initialises the peripheral pins specified in the input parameters.
  - Initialises the peripheral in master mode if `is_slave` is false.
  - Initialises the peripheral in slave mode if `is_slave` is true and `supports_slave_mode` is true.
- `i2c_free`:
  - Resets the pins used to initialise the peripheral to their default state.
  - Disables the peripheral clock.
- `i2c_get_capabilities`:
  - Fills the contents of the `i2c_capabilities_t` parameter
- `i2c_frequency`:
  - Sets the frequency to use for the transfer.
  - Must leave all other configuration unchanged.
- `i2c_timeout`:
  - Sets the clock stretching timeout to use for the following transfers.
  - If the timeout is set to 0, disables clock stretching.
- `i2c_write`:
  - Writes `length` number of symbols to the bus.
  - Returns the number of symbols sent to the bus.
  - Returns an error status if transfer fails.
  - Generates a stop condition on the bus at the end of the transfer if `stop` parameter is true.
  - Handles transfer collisions and loss of arbitration if the platform supports multimaster in hardware.
  - The transfer will timeout and return `I2C_ERROR_TIMEOUT ` if the slave stretches the clock for longer than the configured timeout duration.
- `i2c_read`:
  - Reads `rx_len` symbols from the bus.
  - Returns the number of symbols received from the bus.
  - Returns an error code if transfer fails.
  - Handles transfer collisions and loss of arbitration if the platform supports multimaster in hardware.
  - The transfer will timeout and return `I2C_ERROR_TIMEOUT ` if the slave stretches the clock for longer than the configured timeout duration.
- `i2c_start`:
  - Generates I2C START condition on the bus in master mode.
  - Does nothing if called when the peripheral is configured in slave mode.
- `i2c_stop`:
  - Generates I2C STOP condition on the bus in master mode.
  - Does nothing if called when the peripheral is configured in slave mode.
- `i2c_slave_receive`:
  - Indicates which mode the peripheral has been addressed in.
  - Returns not addressed when called in master mode.
- `i2c_slave_address`:
  - Sets the address of the peripheral to the `address` parameter.
  - Does nothing if called master mode.
- `i2c_transfer_async`:
  - Returns immediately with a `bool` indicating whether the transfer was successfully scheduled or not.
  - The callback given to `i2c_transfer_async` is invoked when the transfer finishes.
  - Must save the handler and context pointers inside the `obj` pointer.
  - The context pointer is passed to the callback on transfer completion.
  - The callback must be invoked on completion unless the transfer is aborted.
  - `i2c_async_event_t` must be filled with the number of symbols sent to the bus during transfer.
- `i2c_abort_async`:
  - Aborts any on-going async transfers.

#### Undefined Behaviours

- Use of a `null` pointer as an argument to any function.
- Calling any `I2C` function before calling `i2c_init` or after calling `i2c_free`.
- Initialising the `I2C` peripheral with invalid `SDA` and `SCL` pins.
- Initialising the peripheral in slave mode if slave mode is not supported, indicated by `i2c_get_capabilities`.
- Operating the peripheral in slave mode without first specifying and address using `i2c_address`
- Setting an address using `i2c_address` after initialising the peripheral in master mode.
- Setting an address to an `I2C` reserved value.
- Setting an address larger than the 7-bit supported maximum if 10-bit addressing is not supported.
- Setting an address larger than the 10-bit supported maximum.
- Setting a frequency outside the supported range given by `i2c_get_capabilities`
- Using the device in a multimaster configuration when `supports_multimaster_mode` is false.
- Setting the timeout outside the supported range given by `i2c_get_capabilities`.
- Specifying an invalid address when calling any `read` or `write` functions.
- Setting the length of the transfer or receive buffers to larger than the buffers are.
- Passing an invalid pointer as `handler` to `i2c_transfer_async`.
- Calling `i2c_transfer_abort` when no transfer is currently in progress.

### Notes

You can find more details about the design choices on the [HAL RFC #01](https://github.com/ARMmbed/mbed-os/blob/master/hal/rfcs/0001-i2c-overhaul.md).

### Dependencies

Hardware I2C capabilities.

### Implementing the I2C API

You can find the API and specification for the I2C API in the following class reference:

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/feature-i2c-doxy/classmbed_1_1_i_2_c.html)

To enable I2C support in Mbed OS, add the `I2C` label in the `device_has` option of the target's section in the `targets.json` file.

You can also add the `I2C_ASYNCH` label in the `device_has` option to enable the asynchronous API,
and `I2CSLAVE` to enable the I2CSlave API.

### Testing

The Mbed OS HAL provides a set of conformance tests for I2C. You can use these tests to validate the correctness of your implementation. To run the I2C HAL tests, use the following command:

```
mbed test -t <toolchain> -m <target> -n "tests-mbed_hal-i2c*"
```

You can read more about the test cases:

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/feature-hal-i2c-doxy/group__hal__i2c__tests.html)

