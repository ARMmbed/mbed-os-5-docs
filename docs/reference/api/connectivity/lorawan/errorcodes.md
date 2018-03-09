<h2 id="lorawan-error-codes">Mbed LoRaWAN Stack error codes</h2>

All operations on `LoRaWANInterface` return an error code `lorawan_status_t` that reflects success or failure of the operation.

Here  is the list of error codes and their description.

| Error code    | Value | Description |
| --------------- | ------------- | ----------|
| `LORAWAN_STATUS_OK`| 0 | Service done successfully |
| `LORAWAN_STATUS_BUSY`| -1000|  Stack busy |
|`LORAWAN_STATUS_WOULD_BLOCK`| -1001 | Stack cannot send at the moment or have nothing to read|
| `LORAWAN_STATUS_SERVICE_UNKNOWN`| -1002 | Unknown service request |
| `LORAWAN_STATUS_PARAMETER_INVALID`| -1003 | Invalid parameter  |
| `LORAWAN_STATUS_FREQUENCY_INVALID`| -1004| Invalid frequency  |
| `LORAWAN_STATUS_DATARATE_INVALID` | -1005| Invalid frequency and datarate  |
| `LORAWAN_STATUS_FREQ_AND_DR_INVALID`| -1006| When stack was unable to send packet in TX window  |
|`LORAWAN_STATUS_NO_NETWORK_JOINED`| -1009 | Device is not part of a network yet (Applicable only for OTAA) |
|`LORAWAN_STATUS_LENGTH_ERROR`| -1010 | Payload lenght error |
| `LORAWAN_STATUS_DEVICE_OFF`| -1011 | The device is off, in other words, disconnected state |
| `LORAWAN_STATUS_NOT_INITIALIZED`| -1012| Stack not initialized  |
| `LORAWAN_STATUS_UNSUPPORTED`| -1013| Unsupported service |
| `LORAWAN_STATUS_CRYPTO_FAIL`| -1014| Crypto failure  |
|`LORAWAN_STATUS_PORT_INVALID`| -1015 | Invalid port |
|`LORAWAN_STATUS_CONNECT_IN_PROGRESS`| -1016 | Connection in progress (application should wait for CONNECT event) |
|`LORAWAN_STATUS_NO_ACTIVE_SESSIONS`| -1017 | No active session in progress |
|`LORAWAN_STATUS_IDLE`| -1018 | Stack idle at the moment|
