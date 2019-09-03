## printf and reducing memory

The standard library family of `printf` (`printf`, `sprintf`, `fprintf` and so on) calls takes a lot of code space. This is because there are multiple format specifiers, and it is not possible to optimize the code at build time. Even a single `printf` call in your application pulls in the entire standard library.
 
A solution to reduce code space is to replace the standard `printf` calls with a smaller implementation.

Mbed OS provides the [`minimal-printf` library](https://github.com/ARMmbed/mbed-os/blob/master/platform/source/minimal-printf/README.md), which offers a subset of the `printf` features (not all format specifiers are supported). You can also achieve further flash savings if your application does not require 64-bit integers or floating point printing.

For a memory footprint comparison between standard `printf` and `minimal-printf`, please see our [Blinky size comparison](https://github.com/ARMmbed/mbed-os/tree/master/platform/source/minimal-printf#size-comparison).
