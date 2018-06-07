## Bluetooth overview

Bluetooth low energy (BLE) is a low power wireless technology standard for personal area networks. BLE, unlike the classic Bluetooth standard, reduces power consumption, allowing your BLE device to run for months or years on a coin-cell battery. Typical applications of BLE are health care, fitness trackers, beacons, smart home, security, entertainment, proximity sensors, industrial and automotive.

Arm Mbed BLE, also called `BLE_API`, is the Bluetooth Low Energy software solution for Mbed. Many targets support Mbed BLE. Developers can use it to create new BLE applications.

BLE is a method of transferring small amounts of data. If you have an input method, such as a sensor or button, your BLE device can receive input and transfer it to a phone, tablet or PC. With the advent of BLIP - Bluetooth IP Support - it can also transfer input directly to the internet. You can then use it to store or analyze the information and send commands back to the device.

This two-way communication means you can use a single device to send information and perform actions based on that information. You could [water your garden](http://www.hosepipeban.org.uk/hosepipe-ban-current-situation/) when the ground is dry, put a beacon with your details on your dog's collar or flash a light when a car comes too close to your bicycle.

<span class="images">![BLE layout](../Introduction/Images/BLEsample.png)<span>A BLE setup requires a board with BLE support and a way to control it, for example a phone app or a local touchscreen.</span></span>

### Displaying information

The first thing you can do with a BLE device is display information. You can do that with lights or a [display](http://developer.mbed.org/components/cat/display/), or you can send the information to a nearby Bluetooth-enabled device, such as a mobile phone.

The information can be sensor input - for example, you could display the speed as provided by an [accelerometer](http://developer.mbed.org/components/cat/sensors-motion/) - or static information that you've programmed onto the device, such as your own details. 

### Processing information 

The two most common sources of information that you may want to process are sensors and user input. In either case, there are two main paradigms for processing:

1. *Local processing* means the device itself processes the data and determines what to do. One example is a thermostat, which knows to turn the heat on or off according to a room temperature input and doesn't need instructions from anywhere.

1. *Remote processing* means that you send data to a different device to be handled there. You then either wait for instructions from the remote device or go on gathering and sending data. For example, if you're trying to predict tomorrow's weather, the device sends data (temperature, barometric pressure and so on) to a computer that can analzse it. Then the local device doesn't need the processing power to run a weather program.

BLE is intended for low power, battery-operated devices, so typical applications will not perform complex processing on the device - processing burns through batteries. Applications will instead export the data to be processed remotely, and wait for a response.

### Sending or storing information

If you want a small and power-efficient device, you probably don't want to store too much locally. Instead, send your information to a server (or even your own computer, if it's set up correctly).

Because of restrictions on energy use in radio operation BLE is a short-range method, so you'll be able to send information over BLE only if your device and your destination are quite close. The range is a few dozen meters. If they're further away, you'll need to use Ethernet (regular cable connection), WiFi or radio.

### Working with apps or websites

So if you can't store or process too much information with a BLE device, what is it good for?

The simplest way to use BLE is to advertise a small bit of information to any device in the area, without becoming interactive. For example, you could notify every user entering your shop that you'll be open till late this evening. There is no need for any response from the users - it's similar to putting a notice on your door. Users will only need a phone app to see these advertisements as notifications. The key thing is that this app will not need to be specific to your project - the same notification app can work with any BLE device; there are several [generic apps](http://www.nordicsemi.com/eng/Products/nRFready-Demo-APPS) that can do this.

If an advertisement-only solution isn’t enough, you can have a transactional interaction (the fancy way of saying “conversation”) between a client and a device over a BLE connection. This usually requires a custom mobile or web-based app, although some generic apps may be enough to get you off the ground. In addition to handling the data, the app may provide users with an interface through which they can send commands to the BLE device. A very common example is mobile fitness apps that get your heart rate information from a BLE-based heart rate monitor. The heart rate monitor doesn't store or process information - it just gets your heart rate and sends it to the app. The app displays the heart rate and gives you some control of the BLE device.

### The physical web and beacons

Physical Web brings devices to the internet via websites (rather than device-specific applications), by using BLE as a business card that includes a link to the website. Interactions with the device are then performed via the website. Using websites rather than apps means that users don't have to install a new app for every device they want to interact with; the interaction is easier and more immediate.

The method used to provide the link is called a beacon. Beacons can be attached to anything that you might want to provide information about, or that you can provide any sort of interface for.

For example, the beacon can be attached to a vending machine. It will send you to a web interface that gives you control of the machine. It can let you make a large purchase (providing sodas for several people in one transaction) by letting you select several options and pay for them all at once.

### How a BLE device gets internet access

At the moment, BLE devices don't have independent internet access. To get internet access, you can do one of two things:

1. You can give your board a secondary communication method, like Ethernet or Wi-Fi. Do note that this can easily double the price of the board. 

1. The BLE device can get internet over its BLE connection to a mobile phone. This means that when the phone terminates the BLE connection, the BLE device will lose its internet access. This doesn't require additional hardware, so it doesn't affect the price of the board, but it does mean that for the device to have constant internet access it will need a phone (or BLE-enabled computer) next to it.

In the future, we may find routers that accept BLE connections, in the same way that they currently accept Wi-Fi connections.

#### Getting started

1. Choose an [Arm Mbed board that supports BLE](https://os.mbed.com/platforms/?mbed-enabled=15&connectivity=3), such as the [NRF51-DK](https://os.mbed.com/platforms/Nordic-nRF51-DK/).

	If your platform doesn't support BLE but is compatible with the Arduino UNO R3 connector, you can use an extension board such as the [X-NUCLEO-IDB05A1](https://os.mbed.com/components/X-NUCLEO-IDB05A1-Bluetooth-Low-Energy/) to add BLE capabilities to your development board.

1. Install a BLE scanner on your phone. It allows you to track all BLE activities from your embedded application. This is a mandatory tool for BLE software development:

    - [nRF Connect](https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp) for Android.

    - [LightBlue](https://itunes.apple.com/gb/app/lightblue-bluetooth-low-energy/id557428110?mt=8) for iPhone.

1. Compile and run our BLE samples:

    - **Arm Mbed OS 5 samples** are available on [os.mbed.com](https://os.mbed.com/teams/mbed-os-examples/) and [GitHub](https://github.com/ARMmbed/mbed-os-example-ble):
        - The [beacon](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-Beacon/) example is a good starting point; it demonstrates how you can create a BLE beacon with just a few lines of code.  
        - The [heart rate monitor](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-HeartRate/) example demonstrates how to build a heart rate sensor that can be connected and monitored by a BLE client such as your phone.
        - The [LED](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-LED/) and [LED blinker](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-LEDBlinker/) are a single example, which demonstrates how a client (LED) and a server (LED blinker) work together over BLE.

    <span>**Tip:** Despite the differences between the different Mbed OS versions, there is only **one** version of Mbed BLE, and it is easy to move code from one version of the OS to another. Choose the sample you use according to the version of Mbed OS supported by your development board.</span>

#### Going further

- The Mbed BLE [API reference](/docs/development/reference/ble.html) offers the full details of the API.

- The Mbed BLE [online community](https://os.mbed.com/teams/Bluetooth-Low-Energy/community/) is also a great place to ask questions and share your knowledge.
