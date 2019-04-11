# Troubleshooting common issues

When you start using Mbed OS, you may find small challenges in a few cases. This section includes a list of issues that Mbed OS users frequently encounter. It also includes steps you can take to prevent and overcome these problems.

## Use the latest tools

### Mbed CLI

If you are using an old version of Mbed CLI, you may see compile-time errors. Make sure `mbed-cli` is working correctly and you are using the [latest version](https://github.com/ARMmbed/mbed-cli/releases). You can check the version of `mbed-cli` by writing:

 ```
 mbed --version
 ```

 If this version is old, update it:

 ```
 pip install mbed-cli --upgrade
 ```

### Compiler versions

Mbed OS 5 can be built with various toolchains. Make sure you are using the latest versions of the toolchains. You can find the currently supported versions on [our tools page](../tools/index.html).

### Compiler licenses

If using Keil MDK (Arm Compiler) or IAR, make sure you have a license installed. For example, [MDK-Lite](http://www.keil.com/arm/mdk.asp) has a 32 KB restriction on code size.

## Investigate whether the Mbed OS application is crashing

- Examine or undo any recent code change you made to see if it is the cause of the crash.
- Build using the development or [debug build profile](../tools/build-profiles.html), so the serial port shows any errors in your program.
- Enable debug prints for components that have them.

## Take these steps if no output is shown in the serial port

If you see no output, this can indicate a serial port problem. Find the reason for such a problem by completing the following steps:

1. Make sure your serial port terminal is using the same baudrate as that being configured by the Mbed OS application.
1. Reopen the serial port.
1. Type into the terminal, and verify the activity light on your board blinks.

## Advanced debugging your application

There might be cases when finding the root cause of the problem requires more investigation and the use of addition debug tools. You can export the project to a third party IDE and use the Mbed interface port of your Mbed board to download and execute the Mbed OS application step by step. Read on to be guided through this process.
