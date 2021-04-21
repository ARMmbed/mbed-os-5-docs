# USBCDC_ECM

<span class="images">![](https://os.mbed.com/docs/mbed-os/v6.10/mbed-os-api-doxy/class_u_s_b_c_d_c___e_c_m.png)<span>USBCDC_ECM class hierarchy</span></span>

The USBCDC_ECM class emulates an Ethernet interface over USB. You can use the interface to send and receive Ethernet frames over USB.

One application in which you can use this class is a USB to Ethernet adapter. If you add an IP stack and web server on top of this class, you can also create a USB web server that allows you to configure a USB device and to view data using a web browser.

## USBCDC_ECM class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.7/mbed-os-api-doxy/class_u_s_b_c_d_c___e_c_m.html)

<span class="notes">**Note:** Because Windows doesn’t provide native support for the USB CDC-ECM model, you must use third party drivers to use this class on Windows.</span>

## USBCDC_ECM example

The example below sends an Ethernet frame that carries "Hello world" payload with a custom EtherType to the host PC. You can capture the frame by using a program called "Wireshark":

1. Flash the board, and ensure the target's USB is plugged into the PC.
2. Open Wireshark.
3. Click **Capture > Options** to select the correct capture interface.
4. Click **Capture > Start**.
5. Click captured packet from source address 12:34:56:78:9a:bc to see the "Hello world" payload.


[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-USBCDC_ECM/tree/v6.10)](https://github.com/ARMmbed/mbed-os-snippet-USBCDC_ECM/blob/v6.10/main.cpp)
