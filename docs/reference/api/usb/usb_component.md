## USB components overview

The Universal Serial Bus (USB) is the most widely used bus in today's computer. USB has particularly been designed to standardize connections between the computer and peripherals. For instance, keyboards, mice, USB audio devices, printers, scanners, disk drives or cameras can use the same bus to exchange data with a computer.

In this document the mbed-os classes providing USB peripheral functionality as mentioned above are referred to as USB components. These USB components inherit from USBDevice and provide specific USB peripherial functionality. Below is information common to all of mbed-os's USB components and how to use them.

### Component construction

Constructing a USB component with the default parameters perform initialization for you. Once the constructor is finished then the device is ready to be used. This process consists of:
- Selects the built-in USBPhy for your hardware
- Starts the USB connection sequence
- Blocks until everything is ready

An example of USBKeyboard's default constructor:
```
#include "mbed.h"
#include "USBKeyboard.h"

// Default constructor to connect and block until ready
USBKeyboard key;

int main(void)
{
    while (1) {
        key.printf("Hello World\r\n");
        wait(1);
    }
}
```

The first optional parameter to the constructor of all USB components is a bool which specifies if the USB component should connect and block until ready. By default this value is `true`. When set to `false` USB will still select the built-in USBPhy for your hardware, but will not block or start the connection sequence. This is useful when you do not want to connect USB at boot.

An example of using the connect parameter to connect after boot:
```
#include "mbed.h"
#include "USBKeyboard.h"

USBKeyboard key(false);

int main(void)
{
    // Start the USB connect sequence
    key.connect();

    // Block until ready
    key.wait_ready();

    while (1) {
        key.printf("Hello World\r\n");
        wait(1);
    }
}
```

The constructors mentioned so far use the default built-in USBPhy as the backend. To allow support for boards without a built-in USBPhy all USB components provide a second constructor which takes a USBPhy as one of its parameters. This can be used to pass in an off-chip USBPhy into any of the USB clases. This constructor does not connect or block so this must be done elsewhere.

An example of using the secondary constructor to explicitly pass in a USBPhy:
```
#include "mbed.h"
#include "USBKeyboard.h"
#include "usb_phy_api.h"

USBPhy *phy = get_usb_phy();
USBKeyboard key(phy);

int main(void)
{
    // Start the USB connect sequence
    key.connect();

    // Block until ready
    key.wait_ready();

    while (1) {
        key.printf("Hello World\r\n");
        wait(1);
    }
}
```

### USB component state

The state of the physical USB line to the host are controlled by the `connect()` and `disconnect()` functions. When a device is connected it is visible to the host PC it is attached to. Once connected it is up to the host PC to finish setup.

USB components provide one or more service. When a service is available for use it is `ready`. For example the USBSerial component enters the `ready` state after a serial port has been opened on the host PC. To check if a USB component's service is ready the `ready()` function can be used. It returns true if the USB component is ready for use or false otherwise. Some components provide multiple services, such as USBAudio which can send or receive data and has two separate ready functions - `read_ready()` and `write_ready()`. Furthermore, for each `ready()` function there is also a corresponding `wait_ready()` function which can be used to block until the USB component's service is available.
