# USBHID

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_h_i_d.png)<span>USBHID class hierarchy</span></span>

You can use the USBHID class to turn an Mbed board into an HID (Human Interface Device) that can send and receive messages over USB. For example, you can define your own protocol and communicate between your computer and Mbed with all capabilities of USB communication. To use USBHID, you need a script running on the host side (computer). For example, on a Windows machine, you can use [pywinusb](https://github.com/rene-aguirre/pywinusb). For convenience, there is a Python script attached below that uses pywinusb that can be run on the host computer to send and receive data from the Mbed board.

## USBHID class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_h_i_d.html)

## USBHID example   

### main.cpp   

```C++
#include <stdio.h>

#include "mbed.h"
#include "drivers/USBHID.h"

// Declare a USBHID device
USBHID HID(8, 8, 0x1234, 0x0006, 0x0001, true);

HID_REPORT output_report = {
    .length = 8,
    .data = {0}
};
HID_REPORT input_report = {
    .length = 0,
    .data = {0}
};

DigitalOut led_out(LED1);

int main(void)
{
    while (1) {

        // Fill the report
        for (int i = 0; i < output_report.length; i++) {
            output_report.data[i] = rand() & UINT8_MAX;
        }

        // Send the report
        HID.send(&output_report);

        // Try to read a msg
        if (HID.read_nb(&input_report)) {
            led_out = !led_out;
            for (int i = 0; i < input_report.length; i++) {
                printf("%d ", input_report.data[i]);
            }
            printf("\r\n");
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
    print(f"Got message {data}")

'''
Gets all HIDs currently connected to host computer,
and sets the first device with string "mbed" in its
vendor name equal to variable mbed. This variable
will be used to send data to the Mbed board.
'''
all_hid_devices = hid.find_all_hid_devices()
mbed_devices = [d for d in all_hid_devices if "mbed" in d.vendor_name]

if mbed_devices is None:
    raise ValueError("No HID devices found")

# A buffer of bytes representing the values 1-8
# The first byte is the report ID which must be 0
buffer = [0, 1, 2, 3, 4, 5, 6, 7, 8]

mbed_devices[0].open()
# Set custom raw data handler
mbed_devices[0].set_raw_data_handler(on_data)

# Send the message to the Mbed board
out_report = mbed_devices[0].find_output_reports()
out_report[0].set_raw_data(buffer)
out_report[0].send()
```

## Related content

- [USBMouse](../apis/usbmouse.html).
- [USBKeyboard](../apis/usbkeyboard.html).
- [USBMouseKeyboard](../apis/usbmousekeyboard.html).
