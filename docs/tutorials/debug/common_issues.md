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

### Identify license issues

[Add content about how to identify license issues here.]

### Device crashing

[Add content about how to prevent and overcome situations when a device crashes here.]

### No output is shown (serial port problem)

[Add content about how to prevent and overcome situations]

### Enable debug trace on serial port

[Add content about how and when to enable debug trace on serial port.]

[Add any other relevant topics.]
