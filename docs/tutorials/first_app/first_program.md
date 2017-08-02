## Your first application on the Arm Mbed tools

We have an example application called Blinky that you can use to get to know Arm Mbed OS and the development tools. It's one of the simplest examples of Mbed OS. It shows the use of a DigitalOut object to represent an LED and the `wait()` call. This is good practice because if there were other threads, they could be scheduled and run while the first thread is waiting.

You can use either of these tools:

* [Arm Mbed CLI](blinky_cli.md).
* [Arm Mbed Online Compiler](blinky_compiler.md).

### Before you begin

Please create a [developer account on Mbed](https://developer.mbed.org/account/signup/).

You might want to read the page [explaining how to connect your board to your computer](serial_communication.md) - especially if you're using Windows.
