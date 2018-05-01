<h2 id="quadspi-port">QuadSPI</h2>

Implementing QSPI enables Mbed OS to communicate with external memories much faster than via SPI. Because the communication can be up to four lines between the host and a device.

The most common use case is an external memory to use as additional data storage.

<span class="warnings">**Warning:** We are changing the QSPI HAL API in an upcoming release of Mbed OS. You can find details on how it may affect you in the [Implementing the QSPI API](#implementing-the-qspi-api) section.</span>

### Assumptions

#### Defined behavior

- A target implementaion covers most of the QSPI frame format (some targets might not provide the flexibility for setting all frame parameters).
- Command transfer - A target might provide additional functions for sending device-specific commands. If it does not, you can implement it using read and write functions. (This is target or driver dependent.)

#### Undefined behavior

- Calling any function other than `qspi_init` before the initialization of the QSPI.

#### Dependency

QSPI peripheral

### Implementing QuadSPI

To make sure your platform is ready for the upcoming changes, you need to implement the future API and submit it in a separate pull request. You can find the API and specification for the new QuadSPI API in the following header file:

[![View code](https://www.mbed.com/embed/?type=library)](https://os-doc-builder.test.mbed.com/docs/development/feature-hal-spec-qspi-doxy/classmbed_1_1_q_s_p_i.html)

The target needs to define the `qspi_s` structure - target specific QSPI object.

Functions to implement:

```
qspi_status_t qspi_init(qspi_t *obj, PinName io0, PinName io1, PinName io2, PinName io3, PinName sclk, PinName ssel, uint32_t hz, uint8_t mode);
qspi_status_t qspi_free(qspi_t *obj);
qspi_status_t qspi_frequency(qspi_t *obj, int hz);
qspi_status_t qspi_write(qspi_t *obj, const qspi_command_t *command, const void *data, size_t *length);
qspi_status_t qspi_command_transfer(qspi_t *obj, const qspi_command_t *command, const void *tx_data, size_t tx_size, void *rx_data, size_t rx_size); 
qspi_status_t qspi_read(qspi_t *obj, const qspi_command_t *command, void *data, size_t *length);

```

Use `qspi_write` and `qspi_read` for data transfers. For communicating with a device, use `qspi_command_transfer`.

To enable the QSPI HAL, define `QSPI` in the targets.json file inside `device_has`:

```
"TARGET_NAME": {
   "device_has": ["QSPI"]
}
```

### Testing

To be implemented
