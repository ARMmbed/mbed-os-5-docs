# USBCDC_ECM

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_c_d_c___e_c_m.png)<span>USBCDC_ECM class hierarchy</span></span>

The USBCDC_ECM class emulates an Ethernet interface over USB. You can use the interface to send and receive Ethernet frames over USB.

## USBCDC_ECM class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_c_d_c___e_c_m.html)

Note: Windows doesn’t have native support for USB CDC-ECM model and thus requires third party drivers.

The example below sends an Ethernet frame that carries "Hello world" payload with a custom EtherType to the host PC. You can capture the frame by using a program called "Wireshark":

1. Flash the board, and ensure the target's USB is plugged into the PC.
2. Open Wireshark.
3. Click **Capture > Options** to select the correct capture interface.
4. Click **Capture > Start**.
5. Click captured packet from source address 12:34:56:78:9a:bc to see the "Hello world" payload.


## USBCDC_ECM example

```C++ TODO
#include "mbed.h"
#include "USBCDC_ECM.h"

/* Ethernet II frame */
typedef struct {
    uint8_t dst_mac[6];
    uint8_t src_mac[6];
    uint16_t eth_type;
    char payload[12];
} packet_t;

static packet_t packet = {
    .dst_mac = {0xff, 0xff, 0xff, 0xff, 0xff, 0xff},
    .src_mac = {0x12, 0x34, 0x56, 0x78, 0x9a, 0xbc},
    .eth_type = 0xaaaa, /* unused EtherType */
    .payload = "Hello world"
};

USBCDC_ECM ecm;

int main()
{
    while (true) {
        ecm.send((uint8_t *)&packet, sizeof(packet));
        wait(1.0);
    }
}

```
