#### Cellular

The [CellularBase](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classCellularBase.html) provides a C++ API for connecting to the internet over a Cellular device.

Arm Mbed OS provides a reference implementation of CellularBase, which you can find [here](https://github.com/ARMmbed/mbed-os/tree/master/features/netsocket/cellular/generic_modem_driver).

##### API

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/classCellularBase.html)

##### Usage

To bring up the network interface:

1. Instantiate an implementation of the CellularBase class (for example, the [generic modem driver](https://github.com/hasnainvirk/mbed-os/blob/cellular_feature_br/features/cellular/TARGET_GENERIC_MODEM/generic_modem_driver/)).
1. Call the `connect(pincode, apn)` function with a PIN code for your SIM card and an APN for your network.
1. Once connected, you can use Mbed OS [network sockets](network_sockets.md) as usual.

##### Example: Connection establishment

This example establishes connection with the cellular network using Mbed OS CellularInterface.

```cpp
#include "mbed.h"
#include "OnboardCellularInterface.h"

/* SIM pin code goes here */
#define PIN_CODE    "1234"

/* Network credentials like APN go here, e.g.,
    "apn, username, password" */
#define CREDENTIALS "internet"

/* Number of retries */
#define RETRY_COUNT 3

OnboardCellularInterface iface;

nsapi_error_t do_connect()
{
    nsapi_error_t retcode;
    bool disconnected = false;
    uint8_t retry_counter = 0;

    while (!iface.is_connected()) {

        retcode = iface.connect();
        if (retcode == NSAPI_ERROR_AUTH_FAILURE) {
            printf("\n\nAuthentication Failure. Exiting application\n");
            return retcode;
        } else if (retcode != NSAPI_ERROR_OK) {
            printf("\n\nCouldn't connect: %d, will retry\n", retcode);
            retry_counter++;
            continue;
        } else if (retcode != NSAPI_ERROR_OK && retry_counter > RETRY_COUNT) {
            printf("\n\nFatal connection failure: %d\n", retcode);
            return retcode;
        }

        break;
    }

    printf("\n\nConnection Established.\n");

    return NSAPI_ERROR_OK;
}

int main()
{
    /* Set Pin code for SIM card */
    iface.set_sim_pin(PIN_CODE);

    /* Set network credentials here, e.g., APN*/
    iface.set_credentials(CREDENTIALS);

    printf("\n\nmbed-os-example-cellular, Connecting...\n");

    /* Attempt to connect to a cellular network */
    if (do_connect() == NSAPI_ERROR_OK) {
        printf("\n\nSuccess. Exiting \n\n");
        return 0;
    }

    printf("\n\nFailure. Exiting \n\n");
    return -1;
}
```

