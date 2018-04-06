### Porting LoRaWAN stack & LoRa RF drivers

Mbed-OS contains a [native LoRaWAN stack (inside Mbed-OS tree)](https://github.com/ARMmbed/mbed-os/tree/master/features/lorawan) augmented with most commonly used [LoRa RF drivers (outside Mbed-OS tree)](https://github.com/ARMmbed/mbed-semtech-lora-rf-drivers). Arm encourages developers around the globe to contribute to any of the Mbed-OS features and functionality including LoRaWAN stack and related RF drivers using the general guidelines provided [here](https://os.mbed.com/docs/v5.8/reference/guidelines.html). 

The information contained in this section can be classified in two sub-sections:

1. Porting a LoRa RF driver for Arm Mbed LoRaWAN Stack or any other LoRaWAN stack if needed.

2. Porting a 3rd party LoRaWAN stack to Mbed-OS 

The idea is to achieve universal application portability, i.e., a single application is compatible with Arm Mbed LoRaWAN stack and any other 3rd party LoRaWAN stack harnessing Arm Mbed-OS. 

The whole porting process consists of two key ingredients:

* An implementation of [LoRaRadio](https://github.com/ARMmbed/mbed-os/blob/master/features/lorawan/LoRaRadio.h) class
* An implementation of [LoRaWANBase](https://github.com/ARMmbed/mbed-os/blob/master/features/lorawan/LoRaWANBase.h) class

**Note: Automated tests for LoRaWAN will be published soon. For Mbed Partners who are looking to start porting Lora drivers and wish to get started, please contact your Partner Lead.**

#### Porting a LoRa RF driver 

Arm Mbed-OS provides a generic API that serves as a template for any LoRa RF driver. [LoRaRadio](https://github.com/ARMmbed/mbed-os/blob/master/features/lorawan/LoRaRadio.h) is a pure virtual class and is an attempt to standardize the APIs across all LoRa radios. Any Mbed enabled LoRa radio driver implementation should present itself as a LoRaRadio. 

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lora_radio_inherit.png)<span>Figure 1. Existing Mbed LoRa RF drivers inherit from LoRaRadio class.</span></span>

For a reference implementation, please check the existing [LoRa RF drivers](https://github.com/ARMmbed/mbed-semtech-lora-rf-drivers). Construction of a LoRaRadio object is a matter of taste. You may notice that the existing reference drivers allow construction of the LoRaRadio object with full pin definitions, that is to make sure that the driver is usable across platforms with any pin combination. You are free to use any form of construction as long as you provide a LoRaRadio object down to the Arm Mbed LoRaWAN stack. Utilization of an instance of `LoRaRadio` class for a 3rd party LoRaWAN stack is beyond the scope of this documentation but it should be trivial. 

For API use cases, details, explanation and meaning please check the `LoRaRadio` class reference given below. Data structures provided in [LoRaRadio.h](https://github.com/ARMmbed/mbed-os/blob/master/features/lorawan/LoRaRadio.h) are carefully planned and designed. They carry most of the stuff you may ever need to write your LoRa RF driver with.
  

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_lo_ra_radio.html)

#### Porting a 3rd party LoRaWANStack 

The vision driving Arm Mbed-OS entails that we have one operating system for a myriad of IoT technologies encompassing a multitude of devices or platforms. However, it does not limit the user to design something specific or tailored to his/her needs. In the light of this vision, Arm Mbed LoRaWAN APIs are designed in such a way that a developer can totally replace the native Mbed-OS LoRaWAN stack with one of his/her own. 

In this sub-section, we will be discussing how a 3rd party LoRaWAN stack can seamlessly provide services to existing Mbed-OS LoRaWAN applications or could reuse applications with minimal effort in terms of code. 
<span class="notes">**Note:** The way a 3rd party LoRaWAN stack harnesses the powers of Arm Mbed-OS, i.e., synchronization methods (if using RTOS), timers, HAL etc is beyond the scope of this documentation.</span>

[LoRaWANBase](https://github.com/ARMmbed/mbed-os/blob/master/features/lorawan/LoRaWANBase.h) class is a pure virtual class providing user facing APIs for a LoRaWAN stack.
The native Arm Mbed LoRaWAN Stack implements `LoRaWANBase` as [LoRaWANInterface](https://github.com/ARMmbed/mbed-os/blob/master/features/lorawan/LoRaWANInterface.h) which then serves as a network interface for the application. Potentially, any developer or vendor can provide an implementation of `LoRaWANBase` and that particular implementation would serve as a network interface for the application. 

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lora_base.png)<span>Figure 2. Inheriting from LoRaWANBase to provide portable APIs.</span></span>

There can be many different flavours when it comes to devices supporting LoRaWAN technology. 

**Case 1: Design based on LoRa Chipset**

This design pattern follows the generic architecture with LoRa radio part based on the LoRa transceiver and antenna plus associated RF circuitry from any vendor. Developer chooses only LoRa radio chipset, LoRaWAN stack and application runs on the MCU. In this case, you can use any Mbed compatible LoRaWAN stack, i.e., the native Mbed-OS LoRaWAN stack or your ported LoRaWAN stack.    

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lora_radio_chipset.png)<span>Figure 3. Design based on LoRa RF chipset.</span></span>

**Case 2: Design based on LoRa Module**

A LoRa module means that the LoRa transceiver and an MCU  are bound together (not in same silicon package). This can be considered as a unit with all the connections between Radio and MCU, plus antenna and other RF circuitry dealt with already by the vendor for the developer. For a developer it means a board that contains a target MCU and RF transceiver integrated on the board (not on chip). Arm Mbed OS provides LoRaWAN stack and application developer can modify the example application for his/her needs.

**Case 3: Design based on LoRa RF-MCU**

An RF-MCU is an SoC including an MCU and LoRa transceiver on the same silicon package. From a developer’s point of view this design is identical to a module based design described in Case 2.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lora_module.png)<span>Figure 4. Design based on LoRa module (both as integrated on board and on chip).</span></span>


**Case 4: Design based on LoRa Modem**

A LoRa modem is a component that contains stack and RF circuitry as a full package, mostly wired to a host MCU. In this case, if the developer wishes to be compliant with the existing applications, he/she may choose to write an adapter layer which should be an implementation of `LoRaWANBase` and under the hood it could be AT commands to control the modem.    

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lora_modem.png)<span>Figure 5. Design based on LoRa Modem.</span></span>

Please follow the detailed reference of `LoRaWANBase` to understand what these APIs and related data structures mean and why are they designed in this way. 
You may notice that the `initialize(events::EventQueue *queue)` API is required to be implemented. The design philosophy involved in it is that we wish to support tiniest of devices with very little memory and an event queue shared between the application and network stack seems to be the best option in terms of memory. 

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_lo_ra_w_a_n_base.html)