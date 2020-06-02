<h1 id="usb-overview">USB components overview</h1>

The Universal Serial Bus (USB) is the most widely used bus in today's computer. USB has been designed to standardize connections between the computer and peripherals. For example, keyboards, mice, USB audio devices, printers, scanners, disk drives and cameras can use the same bus to exchange data with a computer.

This document refers to the Mbed OS classes providing USB peripheral functionality as USB components. These USB components inherit from USBDevice and provide specific USB peripherial functionality. Below is information common to all of the Mbed OS USB components and how to use them.

## Component construction

Constructing a USB component with the default parameters perform initialization for you. Once the constructor is finished then the device is ready to be used. This process:

- Selects the built-in USBPhy for your hardware.
- Starts the USB connection sequence.
- Blocks until everything is ready.

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

The first optional parameter to the constructor of all USB components is a bool that specifies whether the USB component should connect and block until ready. By default, this value is `true`. When set to `false`, USB still selects the built-in USBPhy for your hardware, but it does not block or start the connection sequence. This is useful when you do not want to connect USB at boot.

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

The constructors mentioned so far use the default built-in USBPhy as the back end. To allow support for boards without a built-in USBPhy, all USB components provide a second constructor, which takes a USBPhy as one of its parameters. You can use this to pass an off-chip USBPhy into any of the USB clases. This constructor does not connect or block, so you must do this elsewhere.

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

## USB component state

The `connect()` and `disconnect()` functions control the state of the physical USB line to the host. When a device is connected, it is visible to the host PC to which it is attached. Once connected, the host PC must finish setup.

USB components provide at least one service. When a service is available for use, it is `ready`. For example, the USBSerial component enters the `ready` state after a serial port has been opened on the host PC. To determine whether a USB component's service is ready, you can use the `ready()` function. It returns `true` if the USB component is ready for use and `false` otherwise. Some components provide multiple services, such as USBAudio, which can send or receive data and has two separate ready functions - `read_ready()` and `write_ready()`. Furthermore, for each `ready()` function, there is also a corresponding `wait_ready()` function, which you can use to block until the USB component's service is available.

## USB component and power saving

Some instantiated USB components prevent devices from going to deep sleep because their `USBPhyHw` implentation holds a deep sleep lock. You can temporarily disable USB using `USBDevice::deinit()` to permit deep sleep. However, you must make sure all the data transfers have concluded to avoid any data corruption. The USB host controls the enumeration process, so it chooses when and how to restore the device. Even if the device state is returned to what it was before the disconnect, the host PC software may not be where it left off - for example, you may need to reopen a serial port.

You can use `USBDevice::connect()` to resume USB component operation when USB power is detected after it was previously suspended through `USBDevice::deinit()`.
