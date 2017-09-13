#### UDPSocket

The [UDPSocket](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.6/api/classUDPSocket.html) class provides the ability to send packets of data over UDP, using the `sendto` and `recvfrom` member functions. Packets can be lost or arrive out of order, so we suggest using a TCPSocket (described below) when you require guaranteed delivery.
