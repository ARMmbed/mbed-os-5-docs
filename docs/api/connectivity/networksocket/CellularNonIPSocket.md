# Non-IP cellular socket

<span class="images">![](https://os.mbed.com/docs/mbed-os/v6.1/mbed-os-api-doxy/classmbed_1_1_cellular_non_i_p_socket.png)<span>CellularNonIPSocket class hierarchy</span></span>

The CellularNonIPSocket class provides, through standard socket `send` and `recv` member functions, the ability to send and receive 3GPP non-IP datagrams (NIDD) using our cellular IoT feature. This feature is implemented in the [`ControlPlane_netif`](../mbed-os-api-doxy/classmbed_1_1_control_plane__netif.html) class.

The constructor takes no parameters. To initialize the socket on a specified NetworkInterface, you must call the `open` method, which takes a CellularContext pointer.

[`CellularContext`](../mbed-os-api-doxy/_cellular_context_8h.html) sets up the modem into the Control Plane optimization mode of operation if it is requested and if the cellular network supports it.

Control plane optimization is a new feature for cellular IoT (CIoT). With it, the device can use cellular control channels for data communications, to save power and resources by using less radio signaling.

Note: <span class="notes">**Note:** Non-IP use usually requires integration to a cellular operator messaging service. The service supports a web API to send to and receive the non-IP using devices.</span>

You can request Control Plane optimization mode either with CellularDevice's [`create_context`](../mbed-os-api-doxy/classmbed_1_1_cellular_device.html#a43b9e992dff1cb5d880acec576e9d06f) or by configuring it in the cellular `mbed_lib.json`:

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

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.1/mbed-os-api-doxy/classmbed_1_1_cellular_non_i_p_socket.html)

## CellularNonIPSocket example

The following code demonstrates how to create and use a cellular non-IP socket:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-CellularNonIPSocket/tree/v6.1)](https://github.com/ARMmbed/mbed-os-snippet-CellularNonIPSocket/blob/v6.1/main.cpp)
