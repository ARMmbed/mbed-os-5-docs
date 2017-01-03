# Your first application

We have an example application called Blinky that you can use to get to know mbed OS and the development tools. It's one of the simplest examples of mbed OS. It shows the use of a DigitalOut object to represent an LED and the ``wait()`` call. This is good practice because if there were other threads, they could be scheduled and run while the first thread is waiting.

You can try any of these tools:

* [mbed CLI](blinky_cli.md).
* [mbed Online Compiler](blinky_compiler.md).

## What the tools do

All of the development tools perform the same process:

* Bring the mbed OS source code from GitHub, along with all dependencies.
* Compile your code with the mbed OS code so that you have a single file to flash to your board.
* Allow you to set a build target, so the compiled code matches your hardware (and development toolchain, if you're using mbed CLI).

## Before you begin

Please create a [developer account on mbed](https://developer.mbed.org/account/signup/).

You might want to read the page [explaining how to connect your board to your computer](serial_communication.md) - especially if you're using Windows.
