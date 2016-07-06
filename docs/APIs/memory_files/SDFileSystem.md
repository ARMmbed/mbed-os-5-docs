#SDFileSystem

A library to allow SD Cards to be accessed as a filesystem, using an SPI interface.

This library supports:

* FAT12 / FAT16 / FAT32
* SD / SDHC cards up to 32Gb
* long filenames
* time stamp

## Hello World!

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/SDFileSystem_HelloWorld/)](https://developer.mbed.org/users/mbed_official/code/SDFileSystem_HelloWorld/file/tip/main.cpp) 

## Library

The SDFileSystem library, for accessing SD Cards using fopen, fprintf, etc. 

** MISSING LINK **

## Details

SD Cards are widely used by loads of devices for storage; phones, mp3 players, pc's etc. That means they are a very cheap option for storing large amounts of non-volatile data (i.e. the data is not lost when the power is removed). They should be ideal for data logging and storing audio/images.

SD and MMC cards support various protocols, but common to them all is one based on SPI. This is the one used here as, whilst not being the most high performance, it uses a generic SPI interface so will be more portable.

SD Cards are block devices. That means you read/write data in multiples of the block size (usually 512-bytes); the interface is basically "read from block address n", "write to block address m". Note that a filesystem (e.g. FAT) is an abstraction on top of this, and the disk itself knows nothing about the filesystem.

Based on a SparkFun MicroSD Breakout Board, here is the wiring that will work (you can obviously use either SPI port, and any DigitalOut):

<span class="images">![](../Images/microSD.png)</span>


    
    
    SparkFun MicroSD Breakout Board
    MicroSD Breakout    mbed
       CS  o-------------o 8    (DigitalOut cs)
       DI  o-------------o 5    (SPI mosi)
       VCC o-------------o VOUT
       SCK o-------------o 7    (SPI sclk)
       GND o-------------o GND  
       DO  o-------------o 6    (SPI miso)
       CD  o

<span class="warnings">**Warning:** Note that VCC is 3.3V from mbed's VOUT pin. Do not use 5V from mbed's VU pin. 5V power may damage the SD card. </span>   

The CD (card detect) pin is optional and not used in the example program, but it can be used to detect a card in the micro SD socket. CD connects to ground when no card is present. No connection is made once a card is inserted. It can be read using a DigitalIn pin, if the mode is set to PullUp.  

## Reference

* [SD Card Specification](http://www.sdcard.org/developers/tech/sdcard/pls/Simplified_Physical_Layer_Spec.pdf)
* Notes on the development of this library: [SDCards!](https://developer.mbed.org/users/simon/notebook/sdcards/)
* [SD association SD Card Formatter](https://www.sdcard.org/downloads/formatter_4/) \- SD cards come formatted, use this to reformat an SD card when needed
