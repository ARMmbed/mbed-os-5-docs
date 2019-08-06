# USBHID

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_h_i_d.png)<span>USBHID class hierarchy</span></span>

You can use the USBHID class to turn an Mbed board into an HID (Human Interface Device) that can send and receive messages over USB. For example, you can define your own protocol and communicate between your computer and Mbed with all capabilities of USB communication. To use USBHID, you need a script running on the host side (computer). For example, on a Windows machine, you can use [pywinusb](https://github.com/rene-aguirre/pywinusb). For convenience, there is a Python script attached below that uses pywinusb that can be run on the host computer to send and receive data from the Mbed board.

## USBHID class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_h_i_d.html)

## USBHID example   

### main.cpp   

```C++ TODO
#include "mbed.h"
#include "USBHID.h"

//We declare a USBHID device. By default input and output reports are 64 bytes long.
USBHID hid(true, 8, 8);

Serial pc(USBTX, USBRX);

//This report will contain data to be sent
HID_REPORT send_report;
HID_REPORT recv_report;

DigitalOut l1(LED1);

int main(void) {
    send_report.length = 8;

    while (1) {

        //Fill the report
        for (int i = 0; i < send_report.length; i++)
            send_report.data[i] = rand() & 0xff;

        //Send the report
        hid.send(&send_report);

        //try to read a msg
        if(hid.read_nb(&recv_report)) {
            l1 = !l1;
            for(int i = 0; i < recv_report.length; i++) {
                pc.printf("%d ", recv_report.data[i]);
            }
            pc.printf("\r\n");
        }
    }
}
```   

### USBHID.py   

To use this script, first flash the Mbed board with the code above. Connect the target's USB to the host computer. Then run this script. The script will send 8 bytes of data (1 2 3 4 5 6 7 8) to the Mbed board and will read and print the data sent to the host computer by the Mbed board.   

```Py
from pywinusb import hid

# Whenever the host computer receives data from the
# Mbed board, the received data is printed
def on_data(data):
    print("Got message %s" % data)

'''
Gets all HIDs currently connected to host computer,
and sets the first device with string "mbed" in its
vendor name equal to variable mbed. This variable
will be used to send data to the Mbed board.
'''
all_devices = hid.find_all_hid_devices()
mbeds = [dev for dev in all_devices if dev.vendor_name.find("mbed") >= 0]
if len(mbeds) == 0:
    print("No HID devices found")
    exit(-1)
mbed = mbeds[0]

# Sends 8 bytes of data to the Mbed board
# The Mbed board should receive the data "1 2 3 4 5 6 7 8"
mbed.open()
mbed.set_raw_data_handler(on_data)
message = bytearray(9)
message[1] = 1
message[2] = 2
message[3] = 3
message[4] = 4
message[5] = 5
message[6] = 6
message[7] = 7
message[8] = 8

mbed.find_output_reports()[0].send(message)

```   

## Related content

- [USBMouse](../apis/usbmouse.html).
- [USBKeyboard](../apis/usbkeyboard.html).
- [USBMouseKeyboard](../apis/usbmousekeyboard.html).
