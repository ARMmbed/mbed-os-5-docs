<h1 id="using-small-c-libraries">Using small C libraries in Mbed OS</h1>

If your application does not use a RTOS then you should build it in the bare metal mode to achieve memory savings. Both the `ARM` and `GCC_ARM` toolchains support code optimised versions of their C standard libraries, `microlib` and `newlib-nano`. It is safe to use these smaller C libraries in bare metal mode and we recommend using them. Note that a Mbed OS application can build with these libraries in non bare metal mode but you need to be aware of some restrictions in their usage, in particular in regard to thread-safety, as will be described later.

You can build with the smaller C libraries by creating a `mbed_app.json` with the following contents:

 ```
 {
  "requires": ["bare-metal"],
  "target_overrides": {
    "*": {
      "target.default_lib": "small"
    }
  }
}
```

This will link your application with `microlib` in the case of the `ARM` toolchain and `newlib-nano` for the `GCC_ARM` toolchain.

## Newlib-nano

[Newlib-nano](https://community.arm.com/developer/ip-products/system/b/embedded-blog/posts/shrink-your-mcu-code-size-with-gcc-arm-embedded-4-7) is an open source C library targeting embedded microcontrollers. It is based on newlib but is much smaller in size. One restriction is that newlib-nano is not thread-safe and should not be used by an application that uses the RTOS.

## ARM microlib

Microlib is an alternative library to the default C library. It is intended for use with deeply embedded applications that must fit into extremely small memory footprints.
These applications do not run under an operating system. More information can be found [here](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0808e/chr1358938937854.html).

### Differences between ARM C standard library and microlib
There are a number of differences between microlib and the default C library. Follow [this link](https://developer.arm.com/docs/100073/0613/the-arm-c-micro-library/differences-between-microlib-and-the-default-c-library) for a complete list.

In particular:
* Microlib has no reentrant variant. Microlib does not provide mutex locks to guard against code that is not thread-safe.
* Microlib does not support selectable one or two region memory models as the standard library does. Microlib provides only the two region memory model with separate stack and heap regions.

Since 5.12, Mbed OS supports a two region memory model for heap and stack. This means that the same scatter file can be used with both  ARM C standard library and microlib.

### Scatter file for ARM toolchain
By default, only a few targets have been tested with microlib. If your target has not been tested then the build system will throw an error. In that case, you need to check if the ARM scatter file for your target supports the two region memory model i.e. are `ARM_LIB_HEAP` and `ARM_LIB_STACK` regions defined? This file is located in `targets/.../device/TOOLCHAIN_ARM_STD/your_target_scatter_file.sct`)
   * If yes then the scatter file can be used unmodified for microlib.
   * If no then check if your target was ported to uARM:
      * If yes then replace the `TOOLCHAIN_ARM_STD` scatter file with `../TOOLCHAIN_ARM_MICRO/microlib_scatter_file.sct`
      * If no then you need to update the scatter file to use the two region memory model. More information on the two region memory model can be found [here](https://github.com/ARMmbed/mbed-os/blob/master/docs/design-documents/platform/memory-model/ram_memory_model.md#proposed-ram-memory-model). An example of a scatter file updated for the two region memory model can be found [here](https://github.com/ARMmbed/mbed-os/pull/9571/files?file-filters%5B%5D=.sct#diff-0ce0bec61a6d5ac63ab5ae3afcfe7119).

Once you have completed the steps above, add `small` to the `supported_c_libs` parameter for your target in `targets.json`:
```
"supported_c_libs": {
    "arm": ["std", "small"],
    "gcc_arm": ["std", "small"],
    "iar": ["std"]
}
```

### Note on uARM toolchain
The uARM toolchain is the ARMC6 toolchain with the ARM microlib, the C micro-library. This toolchain will be deprecated after 5.15.
