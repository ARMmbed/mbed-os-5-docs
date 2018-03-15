<h2 id="quadspi-port">QuadSPI</h2>

QSPI HAL defines API for targets that contain QSPI capable peripheral. The QSPI interface is often used for data storage.

### Assumptions

#### Defined behavior

- a target implementaion should cover the most of QSPI frame format (some targets might not provide the flexibility for setting all frame parameters)
- command transfer - a target might provide additional API for sending device specific commands. In case it does not, it can be implemented via read/write functions

#### Undefined behavior

- Calling any function other than `qspi_init` before the initialization of the QSPI

#### Dependency

QSPI peripheral

### Implementing QuadSPI

The target needs to define `qspi_s` structure - target specific QSPI object, enable QSPI in targets.json file `device_has` and implement QSPI HAL functions defined in `hal/qspi_api.h` header file.

`qspi_write` and `qspi_read` are used for data transfers. For communicating with device, `qspi_command_transfer` should be used.

### Testing

To be implemented
