## Your First Arm Mbed Application

We have an example application called Blinky that you can use to get to know Arm Mbed OS and the development tools. It's one of the simplest examples of Mbed OS. It shows the use of a DigitalOut object to represent an LED and the `wait()` call. This is good practice because if there were other threads, they could be scheduled and run while the first thread is waiting.

You can use either of these tools:

* [Arm Mbed CLI](https://os.mbed.com/docs/v5.4/tools/offline.html#mbed-cli).
* [Arm Mbed Online Compiler](https://os.mbed.com/docs/v5.4/tools/online.html#arm-mbed-online-compiler-1).

### Before you begin

Please create a [developer account on Mbed](https://developer.mbed.org/account/signup/).

You might want to read the page [explaining how to connect your board to your computer](/docs/v5.4/tutorials/serial-communication.html) - especially if you're using Windows.
