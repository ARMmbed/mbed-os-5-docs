## Gap

Generic Access Profile is the layer of the stack that handles connectivity tasks. This includes link establishment and termination, advertising and scanning.

Devices with data to publish can use GAP to advertise. They can either include the data in the advertisement itself, inside the scan response, or leave it to be queried by a peer device after connection has been established.

The other side of the process is the act of scanning which listens for advertisements, allows us to query the advertisers for more data via a scan request or to connect in order to query the GATT server on the peer device for the data we want.

Advertising, scanning and communicating all have parameters that let the user find a compromise between desired power consumption levels and latency and efficiency of these processes. 

### Gap class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/class_gap.html)

### Gap example

Here is an example demonstrating how to use the Gap API to advertise, scan, connect and disconnect and how parameters influence efficiency of these actions.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-GAP/)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-GAP)
