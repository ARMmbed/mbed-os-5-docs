<h2 id="quadspi-port">QuadSPI</h2>

QSPI HAL defines API for targets that contain QSPI capable peripheral. The QSPI interface is often used for data storage.

### Assumptions

#### Defined behavior

- a target implementaion should cover the most of QSPI frame format (some targets might not provide the flexibility for setting all frame parameters)
- command transfer - a target might provide additional API for sending device specific commands. In case it does not, it can be implemented via read/write functions (this is target/driver dependent)

#### Undefined behavior

- Calling any function other than `qspi_init` before the initialization of the QSPI

#### Dependency

QSPI peripheral

### Implementing QuadSPI

The target needs to define `qspi_s` structure - target specific QSPI object.

Functions to implement:

```
qspi_status_t qspi_init(qspi_t *obj, PinName io0, PinName io1, PinName io2, PinName io3, PinName sclk, PinName ssel, uint32_t hz, uint8_t mode);
qspi_status_t qspi_free(qspi_t *obj);
qspi_status_t qspi_frequency(qspi_t *obj, int hz);
qspi_status_t qspi_write(qspi_t *obj, const qspi_command_t *command, const void *data, size_t *length);
qspi_status_t qspi_command_transfer(qspi_t *obj, const qspi_command_t *command, const void *tx_data, size_t tx_size, void *rx_data, size_t rx_size); 
qspi_status_t qspi_read(qspi_t *obj, const qspi_command_t *command, void *data, size_t *length);

```

`qspi_write` and `qspi_read` are used for data transfers. For communicating with a device, `qspi_command_transfer` should be used.

To enable QSPI HAL, define `QSPI` in targets.json file inside `device_has`:

```
"TARGET_NAME": {
   "device_has": ["QSPI"]
}
```

### Testing

To be implemented
