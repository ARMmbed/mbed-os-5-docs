# Introduction to mbed OS 5.0

Welcome to the mbed OS 5.0 User Guide. 

If you're an experienced mbed applications developer, you might want to dive straight into the [API pages](APIs/intro.md) to see what's changed, or take a look at our new [build tools](build_tools/options.md). If you're building your own hardware, check out the [hardware and porting section of this guide](porting/background.md).

If you're new to all this, continue reading.

## What do you do with mbed OS?

mbed OS lets you write applications that run on embedded devices, by providing the layer that interprets your application's code in a way the hardware can understand.

Your application code - written in C++ - uses the *application programing interfaces* (APIs) presented by mbed OS to receive information from the hardware and send instructions to it. This means you don't need to understand how the hardware works to be able to control it. It also means that you can run your code on different hardware without having to make any adjustments - mbed OS does the adjustments for you.

### Two types of developer

You may be interested in mbed OS if you're:

* Developing applications for embedded devices. Most of this guide is for you, because it focuses on how you use the mbed OS APIs to create the features your application needs.

* Developing hardware for embedded devices, or trying to add mbed OS support for your existing hardware.

In both cases, we make some assumptions: you are familiar with C++ and with using APIs. You have a basic understanding of embedded devices or the Internet of Things, and you're here to learn how to create features you've already designed, not how to design them.

### Where to start

The easiest way to work with mbed OS is using one of our build tools. We've set up an example that you can try with each tool:

* Our online IDEs let you write and build applications for multiple devices. You can choose between our in-house [mbed Online Compiler](build_tools/online_comp.md) and [mbed Studio](build_tools/studio.md), which is based on the Cloud9 IDE.
* You can also use [mbed CLI](build_tools/cli.md), our command line tool. This requires having a toolchain installed on your machine. 
* If you're working with offline tools, we have [exporting instructions for the most popular ones](build_tools/offline.md).

You might want to review our [glossary](getting_started/glossary.md).

#### How to continue

When you've tried our example and picked your work environment, it's time to learn how mbed OS and its tools enable the features your application needs:

* You can read [the general introduction to the APIs](APIs/intro.md), or jump straight into one of the APIs from the left-hand navigation.

* Try one of the [advanced tutorials](advanced/intro.md), which cover concepts like debugging and version control.



