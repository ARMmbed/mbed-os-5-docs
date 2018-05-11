# Mbed LoRaWAN Solution

## LoRaWAN Network Architecture
 
 A LoRaWAN network consists of three basic network elements:
 
 1. Device
 2. Base station 
 3. Network Server
 
 Base station is essentially transparent, its job is simply to speak LoRa with the devices in its coverage area. The real network control lies in the cloud, i.e., the Network Server. 
 You can think of a LoRaWAN as a network with virtualized network layer. Devices talk to the Network Server using LoRaWAN protocol hence making a LoRaWAN network. If there are multiple Base Stations listening to your Device, all of them forward your packet to the Network Server which means that a LoRaWAN device is not localized to a certain cell. 

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lorawan_nwk_arch.png)<span>Figure 1: General Network Architecture</span></span>

Usually the network topology looks like a one-hop star network, however there may be cases when there is a repeater involved in the radio path working as a middle-man between Base Station and the Device. More than one repeater is not allowed by the current standard specification.  

## LoRaWAN Standard Specifications

LoRa Alliance is responsible for standardizing LoRaWAN protocol and until now there has been two major officially released standard specifications and a few fix versions.

* LoRaWAN Specification v1.0.X
* LoRaWAN Specification v1.1

Specification v1.0 and v1.0.X are essentially similar with a few differences. The latest specification v1.1 is largely different in terms of how network control expresses itself. Some of the salient features in v1.1 are the improved security primitives and the support for roaming. All the specifications are supposed to be backwards compatible. These standard documents are augmented with Regional Parameters Specifications which address the regional constraints pertaining to radio regulations across the world. 

## LoRaWAN Device Classes

LoRaWAN specifications define three distinct types of Device Classes.

* Class A
* Class B
* Class C

A LoRaWAN Device always starts as a Class A Device. It can later switch to another class if required. However, Class B and Class C are mutually exclusive.  

### Class A

Class A is a mandatory Device Class. All LoRaWAN devices must implement a Class A. This class includes battery powered sensors/actuators with no latency constraints. This is the most energy efficient communication Class. 

In Class A, a communication cycle is always initiated by the Device. When a Device transmits a datagram, it opens two receive wndows after specific delays. Timings of these delays and the lengths of receive windows themselves are subjected to regional constraints. The transmission on the other hand is need based. However, it is scheduled or transmitted based upon the duty cycle restrictions following an Aloha like mechanism.  

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/class_a_timing.png)<span>Figure 2: Class A timing diagram</span></span>

### Class B

Class B devices allow for receive slots at scheduled times. For this purpose, the Base Station sends out a time synchronous beacon. This makes sure that at this particular time, the receiver, i.e., the Device is listening. The Class B devices are suitable for latency constrained devices and the devices use slotted communication synchronized with the network beacon. 

The Base Stations transmit a beacon every 128 seconds and all Class B nodes are assigned a time slot within the 128 second cycle and are told when to listen. You can, for instance, tell a node to listen every tenth time slot, and when this comes up, it allows for a downlink message to be transmitted. However this example is just for the purpose of understanding, in actuality, the slots are systematically randomized every beacon period.  

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/class_b_timing.png)<span>Figure 3: Class B timing diagram</span></span>

Each beacon is preceded by Beacon Guard time and no ping slot can be placed in that time period. A ping slot is a 30ms long unit which can be assigned to a Class B device. Beacon Reserved is a time period when the actual beacon is sent. Beacon Window is the time period when ping slots can be opened and assigned. 

* Beacon Period = 128 seconds
* Beacon Reserved = 2.120 seconds
* Beacon Guard = 3 seconds
* Beacon Window = 122.880 seconds

In total there can be 4096, 30ms long ping slots in the Beacon Window. 

**NOTE: Currently Mbed LoRaWAN Stack doesn't support Class B.**

### Class C

Class C devices are supposed to be main powered or that kind of devices who have sufficient amount of power supply available. These devices tend to remain in listening mode always when they are not transmitting. 

Class C devices will listen at RX2 window as often as possible. So such devices need to open an RX2 window immediately after the transmission before opening an RX1 window, i.e., the RECV_DELAY1 time is used for listening on RX2. At the end of RX1 window, the device opens a continuous RX2 window until another transmission is supposed to happen. 

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/class_c_timing.png)<span>Figure 4: Class C timing diagram</span></span>

## LoRaWAN Connection Types
There are two methods defined by the LoRaWAN specification for connecting to an access network.

* OTAA (Over the air activation) 
* ABP (Activation by personalization)

### OTAA (Over the air activation) 
OTAA consists of an exchange of MAC messages between the Device and Network Server. A `JOIN REQUEST` is sent by the Device to Network Server containing an App EUI, a Device EUI and Device Nonce (random value). Device EUI is like a MAC address and uniquely identifies the Device in the network. App EUI is the application identifier allocated to the device by the Network Server (out of band fashion). The `JOIN REQUEST` is sent unencrypted to the Network Server. In response the Network Server sends a `JOIN ACCEPT` message to the Device which is encrypted by using yet another key, the App Key which is provided to the Device (out of band) just like App EUI by the Network provider. The Device then uses this App Key, App Nonce (random value or unique to the network provider), network ID and Device Nonce (another random value) to locally compute Network Session Key and App Session Key. 

### ABP (Activation by personalization)
Personalized devices have security keys stored in NVRAM (preferably a secure element) and these keys are supposed to be burnt to the device at the time of manufacturing.  

Devices configured with ABP are considered connected devices as they don't need to negotiate with the network and hence can communicate with the network right away. The entities stored in the device consists of a device address, and two session keys (network session key and app session key).

## LoRaWAN Data Message Types
There are two types of data messages that can be sent using LoRaWAN protocol. 

* Unconfirmed messages (fire and forget type of datagrams)
* Confirmed messages (requires acknowledgement) from the other end.

For Confirmed messages, going out to the network, i.e., transmitted by the device, an acknowledgement should be sent by the Network Server within the two RX windows opened by the Device. If no ack was received, the Device should wait for a time period equal to a given ack timeout and then retry.

## Arm Mbed LoRaWAN Stack
Arm Mbed OS comes loaded with a tiny, secure, thread safe LoRaWAN stack (following v1.0.2 of LoRaWAN specification) with very simple, intuitive APIs and a large developer base to boast. 

### Design Architecture
The stack is layered in logical order and is highly configureable currently supporting Class A and Class C of LoRaWAN devices. 

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/class_structure_lorawan.png)<span>Figure 5: Mbed LoRaWAN stack class hierarchy</span></span>

There are four design components comprising Arm Mbed LoRaWAN solution that enrich the application with all the necessary tools to operate as a LoRaWAN Device. 

* Mbed LoRa radio driver: constructed by the application and passed down to stack.
* Mbed LoRaWAN Stack, MAC controller layer: controls the over all operation of the stack.  
* Mbed LoRaWAN Stack, PHY layer: computes and provides the regional PHY parameters for processing by MAC controller layer. 
* An `EventQueue` shared between application and the stack for synchronization. It is required that the application constructs an `EventQueue` object and passes it down to stack. 

Let's have a look at the items described above and discuss how all of this is tethered together neatly.

#### Mbed LoRa Radio Driver

Mbed LoRa radio drivers reside out of the Mbed OS tree. Arm provides support for `SX1272` and `SX1276` LoRa radios which are the most widely used LoRa end-device radio chipsets.  

Arm Mbed OS contains a pure virtual class `LoRaRadio` which is used to inherit from and provide an Mbed LoRa radio driver to compliment Mbed applications and Mbed LoRaWAN Stack. A complete reference to `LoRaRadio` class can be found here [LoRaRadio API reference](https://os-doc-builder.test.mbed.com/docs/development/reference/loraradio-api.html) . Existing implementations of `LoRaRadio` can be found here [Mbed LoRa radio drivers](https://github.com/ARMmbed/mbed-semtech-lora-rf-drivers).

These drivers are designed in a way that they support both RTOS and non-RTOS environments. For RTOS case, the drivers defer interrupts using a thread and signalling mechanism for deferred processing. For non-RTOS case, the driver shares the user thread. A 3rd party driver which is an implementation of `LoRaRadio` class can use any of the sync methods provided by Mbed OS and is free to use any transport for register access internally. The most important things ofcourse are:

* The availability of the public APIs outlined by `LoRaRadio`
* Acquiring `radio_events_t` from the MAC controller layer.

`radio_events_t` is a set of Mbed callbacks which point to the methods in the MAC controller layer to process interrupts generated by the radio. When the application constructs a `LoRaRadio` object and passes it down the stack, the MAC controller layer binds `radio_events_t` with the corresponding interrupt processors. All a radio driver needs to do is to accept `radio_events_t` and invoke appropriate callback for a particular interrupt. 

##### Example: Constructing a LoRaRadio object
Application constructs `LoRaRadio` object and passes it down to the stack.
```C
SX1272_LoRaRadio radio(PIN_NAMES,...);
LoRaWANInterface lorawan(radio);
```

##### Example: Internal handling of `radio_events_t`
The stack sets callbacks in `radio_events_t` structure and provides these callbacks to the radio driver. 
```C
// setting up callbakcs in radio_events_t
radio_events.tx_done = mbed::callback(this, &LoRaWANStack::tx_interrupt_handler);
radio_events.rx_done = mbed::callback(this, &LoRaWANStack::rx_interrupt_handler);
radio_events.rx_error = mbed::callback(this, &LoRaWANStack::rx_error_interrupt_handler);
radio_events.tx_timeout = mbed::callback(this, &LoRaWANStack::tx_timeout_interrupt_handler);
radio_events.rx_timeout = mbed::callback(this, &LoRaWANStack::rx_timeout_interrupt_handler);

_loramac.bind_radio_driver(radio);

radio.lock();
// actual initialization of the radio driver with the radio_events_t
radio.init_radio(&radio_events);
radio.unlock();
```
##### Example: Radio generating interrupt
Radio driver uses the callbacks provided to it in the form `radio_events_t` to notify the the upper layers to post process an interrupt.

```C
if (signal & GENERATE_TX_DONE) {
	radio_events->tx_done();
}
```

#### Mbed LoRaWAN Stack: MAC controller layer
MAC controller layer itself consists of various smaller units. Each and every unit is designed to perform a specific task. 
 
##### LoRaWANStack class 

`LoRaWANStack` class is the supervisory unit. It runs the state machine of the stack. At one end it provides a glue layer for the `LoRaWANInterface` which in turn provides a network interface to the application, and at the other end it controls the division of labour among other units of the system. This class is responsible for handling interrupts generated by the radio driver, managing states and delegating jobs asked by the application to the next lower unit, i.e., `LoRaMac` class. 

##### LoRaMac class
`LoRaMac` class constitutes the core MAC functionality. It performs the operations delegated by the `LoRaWANStack` and hoists appropriate flags for various MAC indications or confirmations which need further post processing. This class is also resposible for keeping track of timers using `LoRaWANTimer`, performing crypto operations using `LoRaMacCrypto`, processing MAC commands using `LoRaMacCommand` and processing channel plans using `LoRaMacChannelPlan` classes. In a nutshell, `LoRaMac` class processes jobs using smaller units, provides indications or confirmations of the operations performed to the `LoRaWANStack`.
Although the interrupts are handled in the `LoRaWANStack` which is being done just to drive the state machine with the least number of events or callback paths, the actual controll of PHY layer (`LoRaPHY`) lies with `LoRaMac`. It encodes and writes to the physical radio using `LoRaPHY` class on the TX data path and decodes on the RX data path. 

##### LoRaWANTimer class
Keeps the time base for the stack. It actually extracts the system time base from the `EventQueue` for simplicity. 

##### LoRaMacCrypto class
`LoRaMacCrypto` class is used for encoding and decoding LoRaWAN packets using Mbed TLS. 

##### LoRaMacCommand class
`LoRaMacCommand` class is used to process incoming MAC commands from the network and produces appropriate responses for those MAC commands in the outgoing messages. 

##### LoRaMacChannelPlan class
`LoRaMacChannelPlan` class is used to facilitate channel planning for a given `LoRaPHY`. 

#### Mbed LoRaWAN Stack: PHY layer
The stack features an abstract class `LoRaPHY` which provides PHY layer APIs to upper layers. There are ten implementations of the `LoRaPHY` class shown in Figure. 5 as per definitions provided in LoRaWAN Regional Parameters Specification (complementary document to LoRaWAN Specification v1.0.2).

The implementations of the `LoRaPHY` declare there parameters in a structure which are then used by the APIs to compute various system parameters for the upper layer. They may override a method provided by `LoRaPHY` if needed, otherwise an implementation provided in the `LoRaPHY` will be used. 

At the moment, it's not possible to change a PHY on the runtime. A PHY layer must be selected before compiling the application using Mbed configuration system, e.g., 

```json

"target_overrides": {
	 "*": {
	 	"lora.phy": { 
	 		"help": "LoRa PHY region: EU868, AS923, AU915, 	CN470, CN779, EU433, IN865, KR920, US915, US915_HYBRID",
	 		"value": "EU868"
	 		}
	    }
 }
``` 
#### Event Queue

Arm Mbed LoRaWAN stack is designed to be event driven. To reduce complexity of the overall system, we chose to use an Event Queue which is passed by the application to the stack and this event queue is hence shared by both. This ensures that the both stack and application run in same context. 

There are certian events which are sent from the application in response to various network level operations. For a detailed discussion of these events please visit [LoRaWAN events documentation](https://os-doc-builder.test.mbed.com/docs/development/reference/lorawanevents-api.html). 

### Connection Procedure

In this section we will look at flows and corresponding state changes in the Mbed LoRaWAN stack relating to the network connection paradigm. For detailed API reference for connection procedure, please visit [LoRaWANInterface API documentation](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_lo_ra_w_a_n_interface.html). Look for `connect()` or `connect(lorawan_connect_t)` APIs.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/connect_sm.png)<span>Figure 6: Connection Paradim Flow</span></span>

The Arm Mbed LoRaWAN Stack will send a `CONNECTED` event to the application once the activation is completed. The stack will retry a specific number of times before sending a `JOIN_FAILURE` event to the application if no `JOIN ACCEPT` message was received.

### Sending Messages

For detailed API reference for outgoing messages, please visit [LoRaWANInterface API documentation](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_lo_ra_w_a_n_interface.html). Look for `send()` API. For example:

```C
/**send an Unconfirmed message*/
lorawan.send(port, data, length, MSG_UNCONFIRMED_FLAG);
```

Flows for sending an Unconfirmed or Confirmed message look like this:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/tx_unconfirmed_sm.png)<span>Figure 7: Unconfirmed Message Flow</span></span>

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/tx_confirmed_sm.png)<span>Figure 8: Confirmed Message Flow</span></span>

For an Unconfirmed message, the stack sends a `TX_DONE` event to the application when a transmission has happened and both RX window slots are elapsed (in Class C right after transmission as RX2 never gets elapsed in Class C).

In case of a Confirmed message, the stack sends a `TX_DONE` event to the application when the ack is received. If no ack is received, the stack automatically retries for a given number of times adapting data rates if necessary. 

A `TX_TIMEOUT` or a `TX_FALURE` event will be generated in case of error in TX data path.

### Receiving Messages

For detailed API reference for outgoing messages, please visit [LoRaWANInterface API documentation](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_lo_ra_w_a_n_interface.html). Look for `receive()` APIs. 

There are two types of `receive()` methods in the stack. One is Posix like and you need to tell at what port (instead of a socket ID in Posix format) you wish to receive to, e.g.,

```C

/**this means receive any confirmed or unconfirmed message at port my_port*/
lorawan.receive(my_port, buffer, length, MSG_UNCONFIRMED|MSG_CONFIRMED_FLAG);

// OR

/** Port and flags are given out*/
lorawan.receive(data, length, port_out, flags_out);
```

Receive APIs will return `LORAWAN_STATUS_WOULD_BLOCK` if there is nothing to read at the moment. The application is informed by `RX_DONE` event when the stack receives something for the application. In response to this event, application can choose to use any of the receive methods given above to retrieve received data.

The flow for reception looks like this:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/recv_sm.png)<span>Figure 9: Receive Message Flow</span></span>

### Automatic Handling of Pending Data & MAC Commands

By default the stack handles the case automatically if there is any pending data at the Network Server side waiting to be delivered to the Device or if there are any MAC command responses which require an immediate uplink. 

* When there is pending data indicated by fPending bit set in the previous downlink message sent by Network Server, the stack will automatically generate an empty outgoing message, if not configured otherwise. Application will not receive a `TX_DONE` in this case. The application may receive subsequent `RX_DONE` events as per reception of the pending data.

* If a MAC command requires an immediate response, the stack will generate an empty uplink automatically if not configured otherwise. `TX_DONE` event will be supressed as it was an automatic uplink.

While the automatic uplink transaction is taking place, user will get a `LORAWAN_STATUS_WOULD_BLOCK` error message if he/she attempts to do a data uplink.

Application can modify this behaviour and choose not to sent automatic uplinks by turning this feature off, for example:

```json
"lora.automatic-uplink-message": {
        "help": "Stack will automatically send an uplink message when lora server requires immediate response",
        "value": false
 }

``` 

