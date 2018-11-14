## Cellular TCP sockets

Establishing a cellular connection to the network with Mbed OS only requires the following operations:

```
OnboardCellularInterface iface;

/* Set Pin code for SIM card */
iface.set_sim_pin(PIN_CODE);

/* Set network credentials here, for example the APN */
iface.set_credentials(CREDENTIALS);

/* Connect */
iface.connect()
```

This example demonstrates how to establish a connection and proceed to a simple TCP echo test:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/CellularTCP/)](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/CellularTCP/main.cpp)
