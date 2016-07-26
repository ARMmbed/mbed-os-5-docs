# Introduction to the mbed OS 5.0 Handbook

Welcome to the mbed OS 5.0 User Guide. 

If you're an experienced mbed applications developer, you might want to dive straight into the [API Refrences][TODO: add link] to see what's changed, or take a look at our new [development tools](dev_tools/options.md). If you're building your own hardware, check out the [mbed OS Porting Guide][TODO: add link].

If you're new to all this, continue reading.

## What do you do with mbed OS?

mbed OS lets you write applications that run on embedded devices, by providing the layer that interprets your application's code in a way the hardware can understand.

Your application code - written in C++ - uses the *application programing interfaces* (APIs) presented by mbed OS to receive information from the hardware and send instructions to it. This means that a lot of the challenges in getting started with microcontrollers or integrating large amounts of software is already taken care of. 

## Two types of developer

You may be interested in mbed OS if you're:

* Developing applications for embedded devices. Most of this guide is for you, because it focuses on how you use the mbed OS APIs to create the features your application needs.

* Developing hardware for embedded devices, or trying to add mbed OS support for your existing hardware.

In both cases, we make some assumptions: you are familiar with C and C++ programming and with using APIs. You have a basic understanding of embedded systems or just want to learn.

## Where to start

The easiest way to work with mbed OS is using one of our development tools. We've set up an example that you can try with each tool:

* Our offline development tool is the [mbed CLI](dev_tools/cli.md), a command line tool. This requires having a toolchain installed on your computer. 
* Our online IDEs let you write and build applications using just a web browser and USB connection. You can choose between our in-house [mbed Online Compiler](dev_tools/online_comp.md) and [mbed Studio](dev_tools/studio.md), which is based on the Cloud9 IDE.
* If you're working with third party tools, we have [exporting instructions for the most popular ones](dev_tools/third_party.md).

## How to continue

When you've tried our example and picked your work environment, it's time to learn how mbed OS and its tools enable the features your application needs:

* You can read [the general introduction to the APIs](APIs/intro.md), or jump straight to the API References [TODO: add link].

* Try one of the [advanced tutorials](advanced/intro.md), which cover concepts like debugging and version control.

* We have a [forum](https://forums.mbed.com/) for questions and advice.
