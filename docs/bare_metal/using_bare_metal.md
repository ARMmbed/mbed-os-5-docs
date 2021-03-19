# Using the bare metal profile

This guide shows how to create a bare metal profile application, or move an existing Mbed 2 application to Mbed OS 6 bare metal:

1. By default, the build tool uses the full profile for all application builds. To use the bare metal profile, set up your application to override this default behaviour.
1. The bare metal profile uses a minimal set of default APIs. You can add additional ones [from the list of supported APIs](../bare-metal/index.html#features) if your application needs them.

Here is a code snippet that can work for both Mbed OS profiles; it prints text at regular intervals using the `EventQueue` class. You will create an application that uses this code, set it to use the bare metal profile, and add the non-default `EventQueue` class.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-EventQueue_ex_2/tree/v6.7)](https://github.com/ARMmbed/mbed-os-snippet-EventQueue_ex_2/blob/v6.7/main.cpp)

<span class="notes">**Note:** To be compatible with Arm microlib, a bare metal application should not return from `main()`. In this example, the `queue.dispatch_forever()` call never returns. For more details, see [Non-returning main()](../bare-metal/using-small-c-libraries.html).</span>

## Creating a bare metal application

[Mbed CLI 1](TODO_CMAKE: add link here)
[Mbed CLI 2](TODO_CMAKE: add link here)


