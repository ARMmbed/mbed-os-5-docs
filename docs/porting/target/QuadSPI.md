<h1 id="quadspi-port">QuadSPI (QSPI) </h1>

Implementing QSPI enables Mbed OS to communicate with compliant external SPI devices much faster than with standalone SPI due to the inclusion of up to four data lines between the host and a device.

The most common use case is for external memory to use as additional data storage.

## Assumptions

### Defined behavior

- A target implementation covers most of the QSPI frame format (some targets might not provide the flexibility for setting all frame parameters).
- Command transfer - A target might provide additional functions for sending device-specific commands. If it does not, you can implement it using read and write functions. (This is target or driver dependent.)

### Undefined behavior

- Calling any function other than `qspi_init` before the initialization of the QSPI.

### Dependency

QSPI peripheral

## Implementing QSPI

You can implement your own QSPI by pulling in the following API header file:

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_q_s_p_i.html)

The target needs to define the `qspi_s` structure - target specific QSPI object.

The target needs to define the QSPI interface pin names:

- `QSPI_FLASHn_XXX` for pins connected to onboard flash memory.
- `QSPIn_XXX` for pins routed out to external connector.

`n` is the interface index, typically `1` if single QSPI interface available.

```
QSPIn_IO0
QSPIn_IO1
QSPIn_IO2
QSPIn_IO3
QSPIn_SCK
QSPIn_CSN

QSPI_FLASHn_IO0
QSPI_FLASHn_IO1
QSPI_FLASHn_IO2
QSPI_FLASHn_IO3
QSPI_FLASHn_SCK
QSPI_FLASHn_CSN
```

Functions to implement:

```
qspi_status_t qspi_init(qspi_t *obj, PinName io0, PinName io1, PinName io2, PinName io3, PinName sclk, PinName ssel, uint32_t hz, uint8_t mode);
qspi_status_t qspi_free(qspi_t *obj);
qspi_status_t qspi_frequency(qspi_t *obj, int hz);
qspi_status_t qspi_write(qspi_t *obj, const qspi_command_t *command, const void *data, size_t *length);
qspi_status_t qspi_command_transfer(qspi_t *obj, const qspi_command_t *command, const void *tx_data, size_t tx_size, void *rx_data, size_t rx_size);
qspi_status_t qspi_read(qspi_t *obj, const qspi_command_t *command, void *data, size_t *length);

```

Use `qspi_write` and `qspi_read` for data transfers. To communicate with a device, use `qspi_command_transfer`.

To enable the QSPI HAL, define `QSPI` in the targets.json file inside `device_has`:

```
"TARGET_NAME": {
   "device_has": ["QSPI"]
}
```

## Testing

The Mbed OS HAL provides a set of conformance tests for the QSPI interface.

<span class="notes">**Note:** QSPI HAL tests require QSPI Flash pins to be defined.</span>

You can use these tests to validate the correctness of your implementation. To run the QSPI HAL tests, use the following command:

```
mbed test -t <toolchain> -m <target> -n tests-mbed_hal-qspi
```
