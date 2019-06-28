# Bluetooth overview

Bluetooth low energy (BLE) is a low power wireless technology standard for personal area networks. BLE, unlike the classic Bluetooth standard, reduces power consumption, allowing your BLE device to run for months or years on a coin-cell battery. Typical applications of BLE are health care, fitness trackers, beacons, smart home, security, entertainment, proximity sensors, industrial and automotive.

This two-way communication means you can use a single device to send information and perform actions based on that information. You could [water your garden](http://www.hosepipeban.org.uk/hosepipe-ban-current-situation/) when the ground is dry, put a beacon with your details on your dog's collar or flash a light when a car comes too close to your bicycle.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/BLEsample.png)<span>A BLE setup requires a board with BLE support and a way to control it, for example a phone app or a local touchscreen.</span></span>

Arm Mbed BLE, also called `BLE_API`, is the Bluetooth Low Energy software solution for Mbed. Many targets support Mbed BLE. Developers can use it to create new BLE applications.

## Displaying information

The first thing you can do with a BLE device is display information. You can do that with lights or a [display](http://developer.mbed.org/components/cat/display/), or you can send the information to a nearby Bluetooth-enabled device, such as a mobile phone.

The information can be sensor input - for example, you could display the speed as provided by an [accelerometer](http://developer.mbed.org/components/cat/sensors-motion/) - or static information that you've programmed onto the device, such as your own details. 

## Processing information 

The two most common sources of information that you may want to process are sensors and user input. In either case, there are two main paradigms for processing:

1. *Local processing* means the device itself processes the data and determines what to do. One example is a thermostat, which knows to turn the heat on or off according to a room temperature input and doesn't need instructions from anywhere.

1. *Remote processing* means that you send data to a different device to be handled there. You then either wait for instructions from the remote device or go on gathering and sending data. For example, if you're trying to predict tomorrow's weather, the device sends data (temperature, barometric pressure and so on) to a computer that can analyze it. Then the local device doesn't need the processing power to run a weather program.

BLE is intended for low power, battery-operated devices, so typical applications will not perform complex processing on the device - processing burns through batteries. Applications will instead export the data to be processed remotely, and wait for a response.

## Sending or storing information

For a small and power-efficient device, don't store information locally. Instead, send it to a server.

Because of restrictions on energy use in radio operation, BLE is a short-range method, so you can send information over BLE only if your device and your destination are a few dozen meters apart or closer. If they're farther, you need to use Ethernet, Wi-Fi or radio.

## Working with apps or websites

One way to use BLE is to advertise information to any device in the area without becoming interactive. For example, you could notify every user entering your shop that you'll be open until late this evening. There is no need for any response from the users - it's similar to putting a notice on your door. Users only need a phone app to see these advertisements as notifications. What's key is that this app does not need to be specific to your project - the same notification app can work with any BLE device; there are several generic apps that can do this.

If an advertisement-only solution isn’t enough, you can have a transactional interaction (the fancy way of saying “conversation”) between a client and a device over a BLE connection. This usually requires a custom mobile or web-based app, though some generic apps may be enough to start. In addition to handling the data, the app may provide you with an interface through which you can send commands to the BLE device. A common example is mobile fitness apps that receive your heart rate information from a BLE-based heart rate monitor. The heart rate monitor doesn't store or process information - it just receives your heart rate and sends it to the app. The app displays the heart rate and gives you some control of the BLE device.

## The physical web and beacons

The physical web brings devices to the internet using websites (rather than device-specific applications), by using BLE as a business card that includes a link to the website. Interactions with the device are then performed using the website. Using websites rather than apps means that users don't have to install a new app for every device they want to interact with; the interaction is easier and more immediate.

The method used to provide the link is called a beacon. You can attach beacons to anything you want to provide information about or that you can provide any sort of interface for.

For example, you can attach the beacon to a vending machine. It sends you to a web interface that gives you control of the machine. It can let you make a large purchase (providing sodas for several people in one transaction) by letting you select several options and pay for them all at once.

## How a BLE device gets internet access

At the moment, BLE devices don't have independent internet access. To get internet access, you can do one of two things:

1. You can give your board a secondary communication method, such as Ethernet or Wi-Fi. This can easily double the price of the board.

1. The BLE device can use a gateway (which can be a mobile phone) to exchange data with the internet. The gateway needs to adapt the protocols used because BLE is a non-IP technology. This means that when the phone terminates the BLE connection, the BLE device loses its internet access. This doesn't require additional hardware, so it doesn't affect the price of the board. However, for the device to have constant internet access, it needs a phone (or BLE-enabled computer) next to it.

In the future, routers may accept BLE connections in the same way that they currently accept Wi-Fi connections.
