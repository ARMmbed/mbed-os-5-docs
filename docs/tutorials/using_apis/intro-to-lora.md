<h1 id="LoRa-tutorial">Building a private LoRa network</h1>

There is a lot of interest in [LoRa](https://www.lora-alliance.org), a wide-area network solution that promises kilometers of range with low power consumption, a perfect fit for the Internet of Things. Telecom operators are rolling out LoRa networks, but because LoRa operates in the [open spectrum](https://en.wikipedia.org/wiki/ISM_band), you can also set up your own network. This article discusses what you need to build a private LoRa network and how to use the network to send data from an Arm Mbed end node to the cloud.

<span class="notes">**Note on LoRa vs. LoRaWAN:** Technically, this article explains how to build a LoRaWAN network. LoRa is the modulation technique used (PHY), and LoRaWAN is the network protocol on top of the physical layer (MAC).</span>

## What you need

A typical LoRa network consists of four parts: devices, gateways, a network service and an application:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lora1_2.png)<span>Topology of a LoRa network</span></span>

For hardware, you need devices and gateways, similar to how you would set up a Wi-Fi network. Gateways are simple: they scan the spectrum and capture LoRa packets. There is no gateway pinning here. Devices are not associated with a single gateway; thus, all gateways within range of a device receive the signal. The gateways then forward their data to a network service that handles the packet.

The network service deduplicates packets when multiple gateways receive the same packet, decrypts the message (everything is end-to-end encrypted) and handles LoRa features, such as adaptive data rating. It then forwards the decrypted data to your application. Often, network service providers allow you to run parts of the network - such as the application server, which decrypts the messages - yourself.

There are five requirements.

You need hardware:

- Gateways.
- Devices.

And you need software:

- Device firmware.
- A network service.
- An app.

This guide shows you:

- Which hardware you can buy.
- How to configure a gateway.
- How to write device firmware.
- How to set up a web application to show your LoRa traffic.

<span class="notes">**Note:** The frequency that LoRa uses differs among regions. Make sure your gateways and devices are legal in your jurisdiction. For example, use 915 MHz radios in the United States and 868 MHz radios in Europe. You can find more information in the [LoRaWAN regional parameters](http://net868.ru/assets/pdf/LoRaWAN-Regional-Parameters-v1.1rA.PDF) specification.</span>

### 1.1 - Choosing a gateway

You have [many choices in the gateways](https://www.loriot.io/lora-gateways.html) you can use, but we've had good experience with these three:

- [Kerlink Wirnet station](https://www.kerlink.com/product/wirnet-station/). Expensive (around 1,200 euros) but great build quality and range.
- [MultiTech conduit](http://www.multitech.com/brands/multiconnect-conduit). About 1/3 of the price of the Kerlink (about 450 euros) and good for smaller setups. MultiTech also has a [rugged outdoor](http://www.multitech.com/brands/multiconnect-conduit-ip67) version. Make sure you also order the LoRa mCard.
- Building your own with a Raspberry Pi and an [IMST iC880A](http://shop.imst.de/wireless-modules/lora-products/8/ic880a-spi-lorawan-concentrator-868-mhz) concentrator. At about 150 euros, this is a cost-efficient option.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lora5.jpg)<span>Self-built LoRa gateway based on Raspberry Pi 2 and IMST iC880A. Total cost is about 150 euros.</span></span>

For development purposes, one gateway is enough, but in a production deployment, you need at least two because there will always be dark spots in your network.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lora18.jpg)<span>Kerlink Wirnet station overlooking the Oslo fjord.</span></span>

### 1.2 - Choosing a device

You also need to build devices. If you use Mbed OS (and you should), you can either use:

- A development board with a LoRa transceiver:
    - [L-Tek FF1705](https://os.mbed.com/platforms/L-TEK-FF1705/).
    - [MultiTech xDot](https://os.mbed.com/platforms/MTS-xDot-L151CC/).
    - [MultiTech mDot](https://os.mbed.com/platforms/MTS-mDot-F411/) and the [UDK2 board](http://www.digikey.com/product-detail/en/multi-tech-systems-inc/MTUDK2-ST-MDOT/591-1278-ND/5247463).
    - [MultiTech mDot EVB](https://os.mbed.com/platforms/mdotevb/).
    - [B-L072Z-LRWAN1 LoRa®Discovery kit](https://os.mbed.com/platforms/ST-Discovery-LRWAN1/).
- An Mbed OS 5 Enabled development board together with a LoRa shield:
    - [SX1272MB2xAS](https://os.mbed.com/components/SX1272MB2xAS/) - shield based on the SX1272 transceiver.
    - [SX1276MB1xAS](https://os.mbed.com/components/SX1276MB1xAS/) - shield based on the SX1276 transceiver.

This tutorial applies to all combinations listed above.

<span class="notes">**Note:** When ordering hardware, always make sure you get the variant that works in your region (for example 868 MHz in Europe and 915 MHz in the US).</span>

### 1.3 - Network server

For software, you need a server that understands the LoRa protocol and can interpret the data the device sends. It's possible to use your own (Semtech can give you its reference implementation if you sign an NDA), but there are also companies building LoRa network servers as a service, handling everything on your behalf. This article uses [The Things Network](https://www.thethingsnetwork.org), an open source, globally distributed network service that also has a free hosted community edition.

Because a network server only processes your data and doesn't store it, you need a somewhere to store your messages, as well. The Things Network allows you to hook into its service through an MQTT client and forward your data to the cloud service of your choice (or straight to your application).

## 2. Setting up the gateway

You now need to configure the gateway by installing software to scan the spectrum and forward all LoRa packets to the network server. Below are setup instructions for the three gateways suggested earlier.

### 2.1 - Prerequisites

#### Kerlink Wirnet stations

Follow the instructions in [this document](https://www.thethingsnetwork.org/docs/gateways/kerlink/config.html).

#### MultiTech Conduit

The conduit is configured with DHCP disabled, so you need to enable this first. There are two options to do this: either through Ethernet or through micro-USB.

**Using Ethernet**

1. Connect to the conduit over Ethernet (from the conduit to your computer).
1. Set a static IP address of 192.168.2.2 for your computer.
1. Set a static IP address of 192.168.2.1 as your router.
1. Log in through SSH to 192.168.2.1 with the username `root` and password `root`.

**Over micro-USB**

1. Connect to the conduit using a micro-USB cable.
1. The gateway appears as a serial device.
1. You can use a program such as [GNU Screen](https://www.gnu.org/software/screen/) or [PuTTY](http://putty.org) to log into the gateway with the username `root` and password `root`.

<span class="notes">**Note if logging in fails:** If logging in as `root` fails but you can log in with the username `admin` and the password `admin`, you are running the AEP firmware. To proceed, update your gateway firmware to mLinux. Use [these instructions](http://www.multitech.net/developer/software/mlinux/using-mlinux/flashing-mlinux-firmware-for-conduit/).</span>

Now that you are connected, you can set up the gateway:

1. Enable DHCP by following Step 4 in [this document](http://www.multitech.net/developer/software/mlinux/getting-started-with-conduit-mlinux/).
1. Connect the gateway over Ethernet to your router.
1. Verify that the gateway is connected to the internet (for example, by running `ping 8.8.4.4`).

#### Raspberry Pi

Follow the instructions in [this document](https://github.com/ttn-zh/ic880a-gateway/wiki).

### 2.2 - Registering the gateway

1. [Sign up](https://console.thethingsnetwork.org) for an account at The Things Network.
1. You're redirected to the dashboard page.
1. Click **Gateways**.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn1.png)</span>

1. Click **Register gateway**.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn2.png)</span>

1. Fill in the details of your gateway.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn3.png)<span>Gateway details: The Things Network uses the gateway location to create coverage maps, so make sure the location is set correctly.</span></span>

1. If you use the Kerlink Wirnet station:
    - Tick **I'm using the legacy packet forwarder**.
    - Under **Gateway EUI**, enter the EUI of the gateway (printed on the box).

1. If you use the Raspberry Pi:
    - Tick **I'm using the legacy packet forwarder**.
    - Under **Gateway EUI**, enter the EUI that printed when you called `install.sh` in step 2.1.

1. Click **Register gateway**.
1. You have created the gateway.

If you use the MultiTech conduit, you need the 'Gateway key' to authenticate the gateway to the network. Copy it.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn4.png)</span>

### 2.3 - Installing the packet forwarder

#### Kerlink Wirnet station or Raspberry Pi

No further action required. The gateway shows as 'Connected' in the TTN console.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn7.png)<span>Connected!</span></span>

#### MultiTech conduit

1. On the gateway, run:

    ```
    $ wget https://github.com/kersing/multitech-installer/raw/master/installer.sh
    $ sh installer.sh
    ```

1. A wizard starts. Answer the questions.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn5.png)</span>

1. After the gateway reboots, log back in.
1. Then run (again):

    ```
    $ sh installer.sh
    ```

1. Fill in the remaining questions.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn6.png)<span>Wizard (2) for configuring the MultiTech Conduit</span></span>

1. After this, the gateway shows as **Connected** in the TTN console.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn7.png)<span>Connected!</span></span>

## 3. Building a device

This section explains how to build a device that can send sensor data over the LoRa network. For example, you can create a motion sensor using a [PIR sensor](https://www.adafruit.com/products/189) (less than 10 euros). Of course, you can use any other sensor.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lora6.jpg)<span>PIR sensor hooked up to a Nordic Semiconductor nRF51-DK with a SX1276 LoRa shield</span></span>

### 3.1 - Some notes on writing firmware

#### Restrictions on sending data

You cannot send data constantly because of spectrum regulations. Although the spectrum that LoRa uses is unlicensed, it is regulated. For example, in Europe, there are duty cycle limitations of 1% - meaning you can only send 1% of the time. In the US, there's dwell time, which requires you to wait at least 400 ms between transmissions. If you violate these regulations, your data transmission fails. How fast you are allowed to send data depends on the spread factor you use. With a higher spread factor, it takes longer to send a message - though the chance that a gateway receives it increases. However, you need to wait longer before you can send data again. During development, you can set the spread factor to SF7 (the lowest), so you can send every 6-7 seconds.

LoRaWAN has a feature called Adaptive Data Rating (ADR), through which the network can control the spread factor. You probably want this enabled.

#### Blocked pins

A disadvantage of the SX1272 and SX1276 LoRa shields is that they block a lot of pins. You can solder new headers on the back of the shield to add new peripherals, or use a microcontroller such as the nRF51-DK or a NUCLEO board that has more pins available than just the Arduino headers.

### 3.2 - Registering the device on The Things Network

LoRaWAN uses an end-to-end encryption scheme that uses two session keys. The network server holds one key, and the application server holds the other. (In this tutorial, TTN fulfils both roles). These session keys are created when the device joins the network. For the initial authentication with the network, the application needs its device EUI, the EUI of the application it wants to join (referred to as the application EUI) and a preshared key (the application key).

The device EUI and application EUI are globally unique identifiers. You can buy a block of EUIs from the [IEEE](http://standards.ieee.org/develop/regauth/tut/eui.pdf). Modules often already come with an EUI, which is printed on the device. If you're using a radio shield you can use an EUI from The Things Network's block.

<span class="notes">**Note:** In LoRaWAN 1.1, the join key replaces the application key, and the join server handles the initial authentication. However, at the time of writing, this is not implemented on The Things Network.</span>

Register the device in The Things Network, and generate some keys:

1. Go to [The Things Network console](https://console.thethingsnetwork.org).
1. Click **Applications**.
1. Click **Add application**.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn8.png)</span>

1. Fill in the details of your application, and click **Add application**.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn9.png)<span>Filling in the application details in The Things Network.</span></span>

1. You're redirected to the application page. Under **Devices**, click **Register device**.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn10.png)</span>

1. If your device has an EUI printed on it, enter this in **Device EUI**.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn11.png)<span>The device EUI is often printed on the module or on the box.</span></span>

1. If your device does not have an EUI printed on it, press the **generate** button to allocate an EUI from a block owned by The Things Network. Do **not** make an EUI up; it must be globally unique.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn12.png)</span>

1. Fill in the rest of the details, and click **Register**.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn13.png)</span>

1. The device page opens. It contains the keys that your device uses when authenticating with the network. Click the `<>` button to get the keys as a byte array. This makes it easy to copy the keys into code.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn14.png)</span>

Now that the device is registered in The Things Network, you can start writing code!

### 3.3 - Importing the demo application

Mbed comes with the Arm Mbed Online Compiler, which you can use to build applications without needing to install anything on your computer. (Mbed also has [offline tools](../tools/index.html)).

1. [Sign up](https://os.mbed.com/account/signup/?next=%2F) for an account on Arm Mbed, which hosts the Online Compiler.
1. Find your development board on [the platforms page](https://os.mbed.com/platforms/).
1. Click **Add to your Mbed Compiler**.
1. Go to [mbed-os-example-lorawan](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-lorawan/).
1. Click **Import this program**.
1. You're redirected to the Online Compiler, where you can give the program a name.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lora7_2.png)<span>Importing a program to get started</span></span>

<span class="notes">**Note:** Make sure you select the correct board in the top right corner of the compiler.</span>

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lora8_2.png)<span>Selecting the correct board</span></span>

### 3.4 - Setting keys

In the Online Compiler:

1. Open `mbed_app.json`. This file contains the configuration for the application and holds the authentication keys.
1. If you have a SX1272 or SX1276 **shield** (not if you have a module), set your radio type under `lora-radio`.
1. Under `lora.device-eui`, enter the device EUI from the TTN console.
1. Under `lora.application-eui`, enter the application EUI from the TTN console.
1. Under `lora.application-key`, enter the application key from the TTN console.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn15.png)<span>Correct keys set in `mbed_app.json`</span></span>

1. Under `lora.phy` specify the channel plan for your region. A list of possible values is listed under '[Selecting a PHY'](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-lorawan/) in the docs.

#### Sending the value of the PIR sensor

To send the current value of the PIR sensor (whether it sees movement), in the Online Compiler:

1. Open `main.cpp`.
1. Replace the function `send_message()` with:

    ```cpp TODO
    static void send_message() {
        static InterruptIn pir(D5); // If you hooked the sensor up to a different pin, change it here

        // create a one-byte payload which contains whether the PIR sensor is *high* or *low*
        uint8_t buffer[] = { pir.read() };
        int16_t retcode = lorawan.send(LORAWAN_APP_PORT, buffer, sizeof(buffer), MSG_CONFIRMED_FLAG);

        if (retcode == 0) {
            printf("Sent message over LoRaWAN successfully!\n");
        }
        else {
            printf("Failed to send message (duty-cycle violation?) (%d)\n", retcode);
        }
    }
    ```

### 3.5 - Verifying the setup

Now you can verify whether the setup works by flashing this application to your board.

1. In the Online Compiler, click the **Compile** button.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lora10.png)<span>Compile button</span></span>

1. When compilation succeeds, the compiler sends a file to your computer.
1. Plug your development board into the computer (over micro-USB) to mount it as a USB mass storage device. In most cases, you do not need a driver, but you can find drivers [here](windows-serial-driver.html).
1. Once the device mounts, drag the compiled file onto the board. This causes the device to boot. You can then see the device joining and then sending messages in the The Things Network console, under the **Data** tab:

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn19.png)<span>We've got data!</span></span>

<span class="notes">**Note 1:** You can hook a [serial monitor](serial-comm.html) up to the development board (baud rate 115,200) to see debugging messages.</span>

<span class="notes">**Note 2:** No data in the **Data** tab? Verify that the gateway can receive messages. In the TTN console, go to your gateway, and see if any data comes through under the **Traffic** tab. If you see your device there but not under the device page, the keys are probably wrong.</span>

#### Sending manually

By default, the application sends data automatically. If you want to change this, remove this line from `main.cpp`:

```cpp NOCI
ev_queue.call_every(TX_TIMER, send_message);
```

Call `send_message` whenever you want (for example after the state of the sensor changes). Note that you still need to adhere to the duty cycle, so you may not be able to send data immediately.

### 3.6 - Relaying data back to the device

You can also send data back to the device. Because LoRaWAN (in Class-A mode, which you're using here) is not continuously connected to the network, you need to wait for a receive (RX) window to occur to receive data. An RX window opens after a transmission. So you need to *send* to the network before you can receive a message. If you send a message from The Things Network to your device, the network automatically queues the message and delivers it in the next RX window.

You can toggle the LED on your development board over LoRa. In the Online Compiler:

1. Open `main.cpp`.
1. Replace the `receive_message` function with:

    ```cpp TODO
    static void receive_message() {
        static DigitalOut led(LED1, 0); // the LED under control, default value of 0

        int16_t retcode = lorawan.receive(LORAWAN_APP_PORT, rx_buffer,
                                          LORAMAC_PHY_MAXPAYLOAD,
                                          MSG_CONFIRMED_FLAG|MSG_UNCONFIRMED_FLAG);

        // ignore errors while retrieving
        if (retcode < 0) return;

        led = rx_buffer[0]; // set the value of the LED depending on the first byte in the message

        printf("Received %d bytes: ", retcode);
        for (uint8_t i = 0; i < retcode; i++) {
            printf("%x", rx_buffer[i]);
        }
        printf("\n");
    }
    ```

    <span class="notes">**Note:** On some development boards, writing `0` to the LED turns them on. On others, writing `1` does this. It depends on the wiring of the board.</span>

1. Compile, and flash the application.
1. When the device is back online, use the The Things Network console to queue a message. Go to your device page, and under **Downlink**, select port **21** and data `01`. Then press **Send**.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn16.png)<span>Queuing a downlink message over port 21</span></span>

1. After the next transmission, the LED toggles, and a message appears on the serial console. Try the same thing now by sending `0`.

## 4. Getting your data out of the The Things Network

The system works and sends data in two directions, but the data is not stored anywhere. You can change that. The Things Network offers a data API to get the data out of the network. You can then store it on your own servers or forward it to a cloud service.

For this tutorial, we built a small web application that listens for events from the movement sensors and shows an overview of all sensors. To use this application, you need a recent version of [Node.js](https://nodejs.org) installed on your computer.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lora19.png)<span>Demo application</span></span>

To build this application, first grab an access key from The Things Network:

1. Go to your application in the TTN console.
1. Locate your **Application ID**, and make note of it.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn17.png)</span>

1. Locate your **Access Key**, click the **show** button and make note of it, as well.

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ttn18.png)</span>

Now clone, the demo application, and run it.

1. [Download the demo application](https://github.com/ARMmbed/lora-docs/archive/master.zip), and extract it.
1. In the unzipped application, locate `ttn-node-app/server.js`, and paste your Application ID and Access Key on lines 1 and 2.
1. Open a terminal - or command prompt - and navigate to the folder where you unzipped the application.
1. Run:

    ```
    $ cd ttn-node-app
    $ npm install
    $ node server.js
    ```

   This shows:

    ```
    Connecting to the The Things Network data channel...
    Connected to The Things Network data channel
    Retrieving devices...
    Retrieved devices (2)
    Web server listening on port 5270!
    ```

1. Now, open a web browser, and navigate to http://localhost:5270 to see the application running.

## 5. Recap

LoRa/LoRaWAN is a technology with which anyone can set up a network and start building long-range IoT devices with a relatively small investment. We hope this guide helped you get started, and we would love to see what you build with LoRa and Mbed.

### More material

- [Webinar: getting started with LoRa using Arm Mbed and The Things Network](https://pages.arm.com/2017-10-29-webinar-registration.html).
- [Mbed OS LoRaWAN stack documentation](../apis/lorawan.html).
- [Firmware updates over LoRaWAN](https://os.mbed.com/blog/entry/firmware-updates-over-lpwan-lora/).
- [Presentations from The Things Conference](https://www.youtube.com/playlist?list=PLM8eOeiKY7JUhIyxWWU2-qziejDbBg-pf).
