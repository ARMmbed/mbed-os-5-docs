<h1 id="i2c-port">Inter-integrated circuit (I2C) </h1>

I2C is a serial protocol for two-wire interface to connect low-speed devices in embedded systems. The I2C API allows control and configuration of this interface.

The interface is made up of two lines for all communication:

- Serial Clock (SCL).
- Serial Data (SDA).

<span class="warnings">**Warning:** We are introducing the I2C API in an upcoming release of Mbed OS. This page documents code that exists on a feature branch of Mbed OS. You can find details on how it may affect you in the [implementing the I2C API](#implementing-the-i2c-api) section.

## Defined behaviors

- `i2c_init`:
   - Initializes the peripheral pins specified in the input parameters.
   - Initializes the peripheral in master mode if `is_slave` is false.
   - Initializes the peripheral in slave mode if `is_slave` is true and `supports_slave_mode` is true.
   - Initializes all `i2c_t` object fields.
- `i2c_free`:
   - Resets the pins used to initialize the peripheral to their default state.
   - Disables the peripheral clock.
- `i2c_get_capabilities`:
   - Fills the contents of the `i2c_capabilities_t` parameter.
- `i2c_frequency`:
   - Sets the frequency to use for the transfer.
   - Returns the actual frequency used.
   - Must leave all other configuration unchanged.
- `i2c_set_clock_stretching`:
   - Enables or disables clock stretching for the peripheral when in slave mode.
   - Does nothing when called in master mode.
- `i2c_timeout`:
   - Sets the transmision timeout to use for the following blocking transfers.
   - If the timeout is not set, the default timeout is used.
   - Default timeout value is based on I2C frequency and computed as triple the amount of time it takes to send data over I2C.
- `i2c_write`:
   - Writes `length` number of symbols to the bus.
   - Returns the number of symbols sent to the bus.
   - Returns an error code if transfer fails.
   - Generates a stop condition on the bus at the end of the transfer if `stop` parameter is true.
   - Handles transfer collisions and loss of arbitration if the platform supports multimaster in hardware.
   - The transfer times out and returns `I2C_ERROR_TIMEOUT ` if the transfer takes longer than the configured timeout duration.
- `i2c_read`:
   - Reads `length` symbols from the bus.
   - Returns the number of symbols received from the bus.
   - Returns an error code if transfer fails.
   - Generates a stop condition on the bus at the end of the transfer if `stop` parameter is true.
   - Handles transfer collisions and loss of arbitration if the platform supports multimaster in hardware.
   - The transfer times out and returns `I2C_ERROR_TIMEOUT ` if the transfer takes longer than the configured timeout duration.
- `i2c_start`:
   - Generates I2C START condition on the bus in master mode.
   - Does nothing if called when the peripheral is configured in slave mode.
- `i2c_stop`:
   - Generates I2C STOP condition on the bus in master mode.
   - Does nothing if called when the peripheral is configured in slave mode.
- `i2c_slave_status`:
   - Indicates in which mode the peripheral has been addressed.
   - Returns not addressed when called in master mode.
- `i2c_slave_address`:
   - Sets the address of the peripheral to the `address` parameter.
   - Does nothing if called in master mode.
- `i2c_transfer_async`:
   - Returns immediately with a `bool` indicating whether the transfer was successfully scheduled.
   - The callback given to `i2c_transfer_async` is invoked when the transfer finishes or error occurs.
   - Must save the handler and context pointers inside the `obj` pointer.
   - The context pointer is passed to the callback on transfer completion.
   - The callback must be invoked on completion unless the transfer is aborted.
   - May handle transfer collisions and loss of arbitration if the platform supports multimaster in hardware and enabled in API.
   - `i2c_async_event_t` must be filled with the number of symbols sent to the bus during transfer.
- `i2c_abort_async`:
   - Aborts any ongoing async transfers.

## Undefined behaviors

- Use of a `null` pointer as an argument to any function.
- Calling any `I2C` function before calling `i2c_init` or after calling `i2c_free`.
- Initializing the `I2C` peripheral with invalid `SDA` and `SCL` pins.
- Initializing the peripheral in slave mode if slave mode is not supported, indicated by `i2c_get_capabilities`.
- Operating the peripheral in slave mode without first specifying and address using `i2c_slave_address`.
- Setting an address using `i2c_slave_address` after initializing the peripheral in master mode.
- Setting an address to an `I2C` reserved value.
- Setting an address larger than the 7-bit supported maximum if 10-bit addressing is not supported.
- Setting an address larger than the 10-bit supported maximum.
- Setting a frequency outside the supported range given by `i2c_get_capabilities`.
- Using the device in a multimaster configuration when `supports_multimaster_mode` is false.
- Specifying an invalid address when calling any `read` or `write` functions.
- Setting the length of the transfer or receive buffers to larger than the buffers are.
- Passing an invalid pointer as `handler` to `i2c_transfer_async`.
- Calling `i2c_transfer_abort` when no transfer is currently in progress.

## Notes

You can find more details about the design choices in the [HAL code design document](https://github.com/ARMmbed/mbed-os/blob/feature-i2c/docs/design-documents/hal/0001-i2c-overhaul.md).

## Dependencies

Hardware I2C capabilities.

## Implementing the I2C API

You can find the API and specification for the I2C API in the following class reference:

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.3/feature-i2c-doxy/classmbed_1_1_i2_c.html)

To enable I2C support in Mbed OS, add the `I2C` label in the `device_has` option of the target's section in the `targets.json` file.

You can also add the `I2C_ASYNCH` label in the `device_has` option to enable the asynchronous API,
and `I2CSLAVE` to enable the I2CSlave API.

## Testing

The Mbed OS HAL provides a set of conformance tests for I2C. You can use these tests to validate the correctness of your implementation. To run the I2C HAL tests, use the following command:

```
mbed test -t <toolchain> -m <target> -n "tests-mbed_hal_fpga_ci_test_shield-i2c"
```

You can read more about the test cases:

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.3/feature-i2c-doxy/group__hal__i2c__tests.html)
