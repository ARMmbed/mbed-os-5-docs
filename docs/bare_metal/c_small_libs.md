<h1 id="using-small-c-libraries">Using small C libraries in Mbed OS bare metal</h1>
<!--I think this needs to be mentioned in the usage guide from PR 1305-->

We recommend using small C libraries with the bare metal profile. These are versions of the C standard library that do not include thread safety features; they are suitable for a non-RTOS profile like bare metal, and their size is much better suited for an ultraconstrained hardware.

Both the `ARM` and `GCC_ARM` toolchains support code-optimized versions of their C standard libraries, `microlib` and `newlib-nano`.

## Building with the small C libraries

You can build with the smaller C libraries by creating an `mbed_app.json` with the following contents:

 ```
 {
  "requires": ["bare-metal"],
  "target_overrides": {
    "*": {
      "target.c_lib": "small"
    }
  }
}
```

This links your application with `microlib` for the `ARM` toolchain and `newlib-nano` for the `GCC_ARM` toolchain.

<span class="notes">**Note:** If your application uses the Arm microlib, it should not return from `main()`. Please see [non-returning main() below](#non-returning-main) for advice.</span>

## Newlib-nano

[Newlib-nano](https://community.arm.com/developer/ip-products/system/b/embedded-blog/posts/shrink-your-mcu-code-size-with-gcc-arm-embedded-4-7) is an open source C library targeting embedded microcontrollers. It is based on newlib but is much smaller. One restriction is that newlib-nano is not thread-safe, so an application that uses the RTOS should not use it.

## Arm microlib

Microlib is an alternative library to the default C library. It is intended for deeply embedded applications that must fit into extremely small memory footprints.

These applications do not run under an operating system. You can find more information at the [Arm developer documentation](https://developer.arm.com/docs/100073/0613/the-arm-c-micro-library).

### Differences between Arm C standard library and microlib

To see a complete list of the differences between microlib and the default C library, please see the [Arm developer documentation](https://developer.arm.com/docs/100073/0613/the-arm-c-micro-library/differences-between-microlib-and-the-default-c-library).

In particular:

- Microlib has no re-entrant variant. Microlib does not provide mutex locks to guard against code that is not thread-safe.
- Microlib does not support selectable one- or two-region memory models as the standard library does. Microlib provides only the two-region memory model with separate stack and heap regions.

Mbed OS supports a two-region memory model for heap and stack. This means you can use the same scatter file with both the Arm C standard library and microlib.

### Scatter file for Arm toolchain

By default, only a few targets have been tested with microlib. If your target has not been tested, the build system will throw an error. In that case, you need to check if the Arm scatter file for your target supports the two-region memory model. In other words, are the `ARM_LIB_HEAP` and `ARM_LIB_STACK` regions defined? This file is located in `targets/.../device/TOOLCHAIN_ARM_STD/your_target_scatter_file.sct`):

   - If yes, you can use the scatter file unmodified for microlib.
   - If no, check if your target was ported to uARM:
      - If yes, replace the `TOOLCHAIN_ARM_STD` scatter file with `../TOOLCHAIN_ARM_MICRO/microlib_scatter_file.sct`.
      - If no, you need to update the scatter file to use the two-region memory model. You can find more information on the two-region memory model in the [design document](https://github.com/ARMmbed/mbed-os/blob/master/docs/design-documents/platform/memory-model/ram_memory_model.md#proposed-ram-memory-model). For more details, see this example of a [scatter file updated for the two-region memory model](https://github.com/ARMmbed/mbed-os/pull/9571/files?file-filters%5B%5D=.sct#diff-0ce0bec61a6d5ac63ab5ae3afcfe7119).

After you have completed the steps above, add `small` to the `supported_c_libs` parameter for your target in `targets.json`:

```
"supported_c_libs": {
    "arm": ["std", "small"],
    "gcc_arm": ["std", "small"],
    "iar": ["std"]
}
```

### Non-returning main()

Arm microlib doesn't support returning from `main()`; attempting to return from `main()` causes a bare metal application to crash. Here we show two ways to prevent this.

#### Sleeping in a loop

One recommended technique is to sleep in a loop at the end of `main()`:
```
while (true) {
    sleep();
}
```

This is energy efficient compared to an empty `while (true) {}` loop, which keeps the processor running. A loop is still needed, because `sleep()` returns after the system is woken up by an interrupt.

#### Dispatching an EventQueue

If your application is based on an `EventQueue`, dispatching it at the end of `main()` works as well:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-EventQueue_ex_2/blob/v6.13/)](https://github.com/ARMmbed/mbed-os-snippet-EventQueue_ex_2/blobl/v6/13/main.cpp)

The call to `queue.dispatch_forever()` never returns, as long as you don't break the dispatch anywhere. The `EventQueue` class puts the system to sleep to save energy between events.

### Note on uARM toolchain

The uARM toolchain is the ARMC6 toolchain with the Arm microlib, the C micro-library. This toolchain will be deprecated after 5.15.
