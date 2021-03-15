## Introduction

### Overview and assumptions

Platform code should be portable across different Mbed supported boards with the same hardware capabilities or interfaces.

This document provides general developer guidelines on pin names that apply to all boards but it's not specific to any type of connector.

Note there might be separate documents for pin names that apply to specific connectors.

## Standard Pin Names

### LEDs

Available onboard LEDs are defined as `LEDx` e.g. `LED1`, `LED2`, ...

The detection of available LEDs at application level can be done as follows:

    #ifdef LED1
        DigitalOut myLED(LED1);
        myLED = 1;
    #endif 

Alternatively, if the usage of an LED is required, then the application can detect its availability and generate an error accordingly:

    #ifndef LED1
        #error This application requires the availability of an LED
    #endif

It's possible to define new names of LEDs related to its properties, like color or functionality. They can be defined as aliases in the application as shown below:

    #define RED_LED    LED1
    #define STATUS_LED LED2 

However, these names do not apply to all boards and hence should not be used in official example applications.

### Buttons

Buttons that are available on a board will be defined as `BUTTONx` e.g. `BUTTON1`, `BUTTON2`, ...

The detection of available buttons at application level can be done as follow:

    #ifdef BUTTON1
        DigitalIn myBUTTON(BUTTON1);
        int input = myBUTTON.read();
    #endif 

Alternatively, if the usage of a button is required, then the application can detect its availability and generate an error accordingly:

    #ifndef BUTTON1
        #error This application requires the availability of a button
    #endif 

It's possible to define new names of buttons related to its properties. It's recommended to add a comment with a description. They can be defined as aliases at application level as shown below:

    #define PUSH_BUTTON BUTTON1 // Momentary push Button

However, these names do not apply to all boards and hence should not be used in official example applications.

### UART

Every Mbed board includes a serial interface to the host PC, which allows the console to print useful information about the application.

The pins for the main serial interface are defined as `CONSOLE_TX` and `CONSOLE_RX`.
