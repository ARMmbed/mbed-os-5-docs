## Configuring the hardware

### Selecting your radio

6LoWPAN network uses IEEE 802.15.4 radios and therefore, operates on one of the following unlicensed frequency bands:

- 868.0–868.6 MHz: Europe, allows one communication channel (2003, 2006, 2011[4]).
- 902–928 MHz: North America, up to ten channels (2003), extended to thirty (2006).
- 2400–2483.5 MHz: worldwide use, up to sixteen channels (2003, 2006).

The data rate varies from 20 kbit/s to 250 kbit/s. Consider the data rate available per node when designing the application. Basically, the data rate is divided between all nodes in the network. Allocate roughly half of the channel capacity for signalling purposes. Each hop requires retransmisson of the packet.

![Datarate](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/bw.png)

<span class="tips">**Rule of thumb:** The bandwidth per node is divided by the number of nodes in the network and the number of hops.</span>

### File system

Thread network stack can write network configuration settings to the file system and read them in the following startup. The size of the Thread configuration settings is a few thousand bytes. You can store network configuration settings to the file system when:

 1. You enable the file system as instructed in the [Mbed OS storage documentation](../apis/storage.html).
 1. You set the file system root path to the Thread network stack by calling the function `ns_file_system_set_root_path(root-path)`. Do this before starting the Thread stack to read possible configuration settings in the first power up.

Depending on the selected file system, the application may need to format the file system before you can use it.
