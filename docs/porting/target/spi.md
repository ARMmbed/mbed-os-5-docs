<h1 id="spi-port">Serial Peripheral Interface (SPI)</h1>

The **Serial Peripheral Interface** allows you to send or receive a data stream over a synchronous serial interface made of 3 to 4 lines.

- MISO: Master in, slave out.
- MOSI: Master out, slave in.
- MCLK: Clock.
- SS: Slave select.

A typical use case of this interface is with SDCard, memory blocks and DACs or ADCs.

This highly configurable interface has elements you can adjust:

- Frame length.
- Clocks polarity and phase.

<span class="warnings">**Warning:** We are introducing the SPI API in an upcoming release of Mbed OS. This page documents code that exists on a feature branch of Mbed OS. You can find details on how it may affect you in the [implementing the SPI API](#implementing-the-spi-api) section.

## Assumptions

### Defined behaviors

- `spi_get_module()` returns the `SPIName` unique identifier to the peripheral associated to this SPI channel.
- `spi_get_capabilities()` fills the given `spi_capabilities_t` instance.
- `spi_get_capabilities()` should consider the `ssel` pin when evaluating the `support_slave_mode` capability.  
- If the given `ssel` pin cannot be managed by hardware in slave mode, `support_slave_mode` should be false.
- At least a symbol width of 8 bit must be supported.
- The supported frequency range must include the range 0.2-2 MHz.
- The shortest part of the duty cycle must not be shorter than 50% of the expected period.
- `spi_init()` initializes the pins leaving the configuration registers unchanged.
- `spi_init()` if `is_slave` is false:
   - If `ssel` is `NC`, the HAL implementation ignores this pin.
   - If `ssel` is not `NC`, then the HAL implementation owns the pin and its management.
- When managed by the HAL implementation, `ssel` is always considered active low.
- When the hardware supports the half-duplex (3-wire) mode, if `miso` (exclusive) or `mosi` is missing in any function that expects pins, the bus is assumed to be half-duplex.
- `spi_free()` resets the pins to their default state.
- `spi_free()` disables the peripheral clock.
- `spi_format()` sets:
   - The number of bits per symbol.
   - The mode:
     .0 Clock idle state is *low*, data are sampled when the clock becomes *active* (polarity = 0, phase = 0).
     .1 Clock idle state is *low*, data are sampled when the clock becomes *inactive* (polarity = 0, phase = 1). 
     .2 Clock idle state is *high*, data are sampled when the clock becomes *active* (polarity = 1, phase = 0).
     .3 Clock idle state is *high*, data are sampled when the clock becomes *inactive* (polarity = 1, phase = 1).
   - The bit ordering (lsb/msb first).
- `spi_format()` updates the configuration of the peripheral except the baud rate generator.
- `spi_frequency()` sets the frequency to use during the transfer.
- `spi_frequency()` returns the actual frequency that is used.
- `spi_frequency()` updates the baud rate generator leaving other configurations unchanged.
- `spi_init()`, `spi_frequency()` and `spi_format()` must be called at least once each before initiating any transfer.
- `spi_transfer()`:
   - Writes `tx_len` symbols to the bus.
   - Reads `rx_len` symbols from the bus.
   - If `rx` is NULL, then inputs are discarded.
   - If `tx` is NULL, then `fill_symbol` is used instead.
   - Returns the number of symbol clocked on the bus during this transfer.
   - Expects symbols types to be the closest stdint type bigger or equal to its size following the platform's endianness. For example:
      - 7bits => uint8_t.
      - 15bits => uint16_t.
      - 16bits => uint16_t.
      - 17bits => uint32_t.
   - In full-duplex mode:
      - If `rx_len` > `tx_len` then it sends `(rx_len-tx_len)` additional `fill_symbol` to the bus.
  - In half-duplex mode:
      - As master, `spi_transfer()` sends `tx_len` symbols and then reads `rx_len` symbols.
      - As slave, `spi_transfer()` receives `rx_len` symbols and then sends `tx_len` symbols.
- `spi_transter_async()` schedules a transfer to be process the same way `spi_transfer()` would have but asynchronously.
- `spi_transter_async()` returns immediately with a boolean indicating whether the transfer was successfully scheduled or not.
- The callback given to `spi_transfer_async()` is invoked when the transfer completes (with a success or an error).
- `spi_transfer_async()` saves the handler and the `ctx` pointer.
- The `ctx` is passed to the callback on transfer completion.
- Unless the transfer is aborted, the callback is invoked on completion. The completion may be when all symbols have been transmitted
  or when, in slave mode, the master deasserts the chip select.
- The `spi_transfer_async()` function may use the `DMAUsage` hint to select the appropriate asynchronous algorithm.
- The `spi_async_event_t` must be filled with the number of symbols clocked on the bus during this transfer and a boolean value indicated if an error has occurred.
- `spi_transfer_async_abort()` aborts an ongoing asynchronous transfer.

### Undefined behaviors

- Calling `spi_init()` multiple times on the same `spi_t` without `spi_free()`'ing it first.
- Calling any method other than `spi_init()` on an uninitialized or freed `spi_t`.
- Passing both `miso` and `mosi` as `NC` to `spi_get_module` or `spi_init`.
- Passing `miso` or `mosi` as `NC` on target that does not support half-duplex mode.
- Passing `mclk` as `NC`  to `spi_get_module` or `spi_init`.
- Passing an invalid pointer as `cap` to `spi_get_capabilities`.
- Passing pins that cannot be on the same peripheral.
- Passing an invalid pointer as `obj` to any method.
- Giving an `ssel` pin to `spi_init()` when using in master mode.  
- SS must be managed by hardware in slave mode and must **NOT** be managed by hardware in master mode.
- Setting a frequency outside of the range given by `spi_get_capabilities()`.
- Setting a frequency in slave mode.
- Setting `bits` in `spi_format` to a value out of the range given by `spi_get_capabilities()`.
- Passing an invalid pointer as `fill_symbol` to `spi_transfer` and `spi_transfer_async` while they would be required by the transfer (`rx_len != tx_len` or `tx==NULL`).
- Passing an invalid pointer as `handler` to `spi_transfer_async`.
- Calling `spi_transfer_async_abort()` while no asynchronous transfer is being processed (no transfer or a synchronous transfer).
- In half-duplex mode, any mechanism (if any is present) to detect or prevent collision is implementation defined.

### Other requirements

A target must also define these elements:

- `#define SPI_COUNT (xxxxxU)`.
- The number of SPI peripherals available on the device. A good place for that macro is `PeripheralNames.h` next to the `SPIName` enumeration.

<span class="notes">**Note:** You can find more details about the design choices in the [SPI design document](https://github.com/ARMmbed/mbed-os/blob/feature-hal-spec-spi/docs/design-documents/hal/0000-spi-overhaul.md).</span>

## Dependencies

Hardware SPI capabilities.

## Implementing the SPI API

You can find the API and specification for the SPI API in the following class reference:

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/development/feature-hal-spec-spi-doxy/classmbed_1_1_s_p_i.html)

To enable SPI support in Mbed OS, add the `SPI` label in the `device_has` option of the target's section in the `targets.json` file.
You can also add the `SPI_ASYNCH` label in the `device_has` option to enable the asynchronous API.

## Testing

The Mbed OS HAL provides a set of conformance tests for SPI. You can use these tests to validate the correctness of your implementation. To run the SPI HAL tests, use the following command:

```
mbed test -t <toolchain> -m <target> -n "tests-mbed_hal-spi*"
```

You can read more about the test cases:

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/development/feature-hal-spec-spi-doxy/group__hal__spi__tests.html)
