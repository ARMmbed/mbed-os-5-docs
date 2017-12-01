## Troubleshooting common issues when getting started

When you start using Mbed OS, you may find small challenges in a few cases. This section includes a list of issues that Mbed OS users frequently encounter. It also includes steps you can take to prevent and overcome these problems.

### Use the latest tools

#### Mbed CLI

If you are using an old version of Mbed CLI, you may see compile-time errors. Make sure `mbed-cli` is working correctly and you are using the [latest version](https://github.com/ARMmbed/mbed-cli/releases).
You can check the version of `mbed-cli` by writting:

 ```
 mbed --version
 ```

 If this version is old, update it:

 ```
 pip install mbed-cli --upgrade
 ```

#### Compiler versions

Mbed OS 5 can be built with various toolchains. Make sure you are using the latest versions of the toolchains.
The currently supported versions are:
https://os.mbed.com/docs/v5.6/tools/index.html

#### Compiler licenses

If using Keil MDK (Arm Compiler) or IAR, make sure you have a license installed.
For example, [MDK-Lite](http://www.keil.com/arm/mdk.asp) has a 32 KB restriction on code size.

### Investigate whether the Mbed OS application is crashing

- Examine or undo any recent code change you made to see if it is the cause of the crash.
- Build using the development or [debug build profile](https://os.mbed.com/docs/v5.6/tools/build-profiles.html), so any errors in your program get shown on the serial port.
- Enable debug prints for components which have them.

### Take these steps if no output is shown is serial port

If you see no output, this can indicate a serial port problem. Find the reason for such problem by completing the following steps:

1. Make sure your serial port terminal is using the same baudrate as being configured by the Mbed OS application.
1. Reopen the serial port.
1. Type into the terminal, and verify the activity light on your board blinks.

### Advanced debugging your application

There might be cases where finding the root cause of the problem requires a bit more investigation and make use of addition debug tools.
You can export the project to a 3rd party IDE and use the Mbed interface port of your Mbed board to download and execute the Mbed OS application step by step. Read the folloging tutorial that guides you through this process:
https://os.mbed.com/docs/v5.6/tutorials/debugging.html


