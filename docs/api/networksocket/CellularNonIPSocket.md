# Non-IP cellular socket

The CellularNonIPSocket class provides, through standard socket `send` and `recv` member functions, the ability to send and receive 3GPP non-IP datagrams (NIDD) using our cellular IoT feature. This feature is implemented in the [`ControlPlane_netif`](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_control_plane__netif.html) class.

The constructor takes no parameters. To initialize the socket on a specified NetworkInterface, you must call the `open` method, which takes a CellularContext pointer.

[`CellularContext`](https://os.mbed.com/docs/development/mbed-os-api-doxy/_cellular_context_8h.html) sets up the modem into the Control Plane optimization mode of operation if it is requested and if the cellular network supports it.

Control plane optimization is a new feature for cellular IoT (CIoT). With it, the device can use cellular control channels for data communications, to save power and resources by using less radio signaling.

Note: <span class="notes">**Note:** Non-IP use usually requires integration to a cellular operator messaging service. The service supports a web API to send to and receive the non-IP using devices.</span>

You can request Control Plane optimization mode either with CellularDevice's [`create_context`](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_cellular_device.html#a43b9e992dff1cb5d880acec576e9d06f) or by configuring it in the cellular `mbed_lib.json`:

```json
{
    "name": "cellular",
    "config": {
        "control-plane-opt": {
            "help": "Enables control plane CIoT EPS optimisation",
            "value": true
        }
    }
}
```

## CellularNonIPSocket class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_cellular_non_i_p_socket.html)

## CellularNonIPSocket example

The following code demonstrates how to create and use a cellular non-IP socket:

```

#include "mbed.h"
#include "CellularNonIPSocket.h"
#include "CellularDevice.h"

// Network interface
NetworkInterface *iface;

int main() {
    // Bring up the cellular interface
    iface = CellularContext::get_default_nonip_instance();
    MBED_ASSERT(iface);

    // sim pin, apn, credentials and possible plmn are taken automatically from json when using NetworkInterface::set_default_parameters()
    iface->set_default_parameters();

    printf("Cellular Non-IP Socket example\n");
    if(NSAPI_ERROR_OK != iface->connect() || NSAPI_STATUS_GLOBAL_UP != iface->get_connection_status()) {
        printf("Error connecting\n");
        return -1;
    }

    CellularNonIPSocket sock;

    nsapi_error_t retcode = sock.open((CellularContext*)iface);

    if (retcode != NSAPI_ERROR_OK) {
        printf("CellularNonIPSocket.open() fails, code: %d\n", retcode);
        return -1;
    }

    const char *send_string = "TEST";

    if(0 > sock.send((void*) send_string, sizeof(send_string))) {
        printf("Error sending data\n");
        return -1;
    }

    printf("Success sending data\n");

    char recv_buf[4];
    if(0 > sock.recv((void *)recv_buf, sizeof(recv_buf))) {
        printf("Error receiving data\n");
        return -1;
    }

    printf("Success receiving data\n");

    // Close the socket and bring down the network interface
    sock.close();
    iface->disconnect();
    return 0;
}

```
