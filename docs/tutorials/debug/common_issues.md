## Debugging common issues when getting started

When you start using Mbed OS, you may need to debug challenges that you have not seen before. This section includes a list of issues that Mbed OS users frequently encounter. It also includes steps you can take to prevent and overcome these problems.

### Use the latest tools

#### Mbed CLI

If you are using an old version of Mbed CLI, you may see compile-time errors. Make sure `mbed-cli` is working correctly and its version is newer than `1.0.0`.

 ```
 mbed --version
 ```

 If not, update it:

 ```
 pip install mbed-cli --upgrade
 ```

#### Compiler versions

Mbed OS 5 can be built with various toolchains. The currently supported versions are:

- Arm compiler 5.06 update 3.
- GNU Arm Embedded version 6.
- IAR Embedded Workbench 7.8.

### Debug device crashing

- Examine or undo any recent code change you made to see if it is the cause of the crash.
- Build using the development or debug build profile, so any errors in your program get shown on the serial port.
- Enable debug prints for components which have them.

### Take these steps if no output is shown

If you see no output, this can indicate a serial port problem. Debug such a problem by completing the following steps:

1. Make sure your serial port has the same baudrate as your device.
1. Reopen the serial port.
1. Type into the terminal, and verify the activity light on your board blinks.
