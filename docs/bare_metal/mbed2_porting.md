# Porting a target from Mbed OS 2 to Mbed OS 6 bare metal

The Mbed OS bare metal profile offers the same functionality as Mbed OS 2 and allows targets to access features that we have added to more recent versions of Mbed OS. At the same time, it removes the RTOS and provides fewer features than Mbed OS 6, so it's smaller and therefore suitable for ultraconstrained devices.

This document describes how to configure an Mbed OS 2 target for bare metal, and validate the port.

<span class="tips">**Tips:** For general porting information, please [see our porting guide](../porting/index.html).</span>

## Configuring your target

The configure your target:

1. Clone [mbed-os-example-blinky-baremetal](https://github.com/ARMmbed/mbed-os-example-blinky-baremetal).
1. Edit `targets.json`. In this step, you will configure your target to support Mbed OS 6 and add bare metal configuration parameters.
1. Build and run the example. In this step, you will troubleshoot any issues and validate the configuration by running the example successfully.

### Clone mbed-os-example-blinky-baremetal

1. Run the following command:

    ```
    git clone https://github.com/ARMmbed/mbed-os-example-blinky-baremetal
    ```

1. Change directory:

    ```
    cd mbed-os-example-blinky-baremetal
    ```

### Edit targets.json

Find your target in `mbed-os/targets/targets.json` and update its configuration as described below.

Configure your target to support Mbed OS 6:

1. Remove the `release_versions` property; it is no longer required:

    ```json
    "release_versions": ["2"]
    ```

1. To indicate that the application profile supported by this target is bare metal, add the `supported_application_profiles` property:

    ```json
    "supported_application_profiles" : ["bare-metal"]
    ```

1. Override `supported_c_libs` property to link with the smaller C libraries. The default for all targets is defined as follows:

    ```json
    "supported_c_libs": {
        "arm":  ["std"],
        "gcc_arm":  ["std", "small"],
        "iar": ["std"]
    }
    ```

    Both the ARM and GCC_ARM toolchains support optimized versions of the C standard libraries - microlib and newlib-nano, respectively. We recommend using them with the bare metal profile for lower memory footprints. Ultraconstrained targets should override `supported_c_libs`:

    ```json
    "supported_c_libs": {
        "arm":  ["small"],
        "gcc_arm":  ["small"]
    }
    ```

    <span class="notes">**Note:** The IAR toolchain does not have a small C library.</span>

    For each toolchain, if there is enough memory to link with the standard library, add the corresponding `std` library to the list. For example:

    ```json
    "supported_c_libs": {
        "arm":  ["std", "small"],
        "gcc_arm":  ["std", "small"],
        "iar": ["std"]
    }
    ```

    <span class="notes">**Note:** For ARM, your target scatter file needs to have a two-region memory model. If the build system throws an error ("presence of undefined symbols `Image$$ARM_LIB_HEAP$$ZI$$Base`, `Image$$ARM_LIB_HEAP$$ZI$$Length`, `Image$$ARM_LIB_HEAP$$ZI$$Limit`") when compiling with microlib, you can find more information [in the small C libraries documentation](../bare-metal/using-small-c-libraries.html).</span>

1. We recommend that ultraconstrained devices running bare metal applications link with the small C libraries by default. To indicate which C library should be used by the build tools, set the `c_lib` property:
    - If your target has `"default_lib": "small"` defined, then replace it with `"c_lib" : "small"`.
    - Otherwise, add `"c_lib" : "small"`.

    <span class="notes">**Note:** If a toolchain does not support a small C library and `c_lib` is set to `small`, the build tools will revert to linking with the standard C library (provided that it is listed in `supported_c_libs` for the given toolchain).</span>

1. If `default_toolchain` is set to `uARM`, then
    1. Replace it with `ARM`.
    1. Remove `uARM` from `supported_toolchains`.
        Support for the uARM toolchain, which is the ARM toolchain with microlib, has been removed. Setting `c_lib` to `small`, as explained above, ensures that microlib is used when the ARM toolchain is selected.

    <span class="notes">**Note:** As mentioned above, to successfully build with microlib, the target must define a two-region memory model. You might need to replace the content of the `TOOLCHAIN_ARM_STD` linker file with that of `TOOLCHAIN_ARM_MICRO`, which includes a two-region memory model linker file.</span>

1. If your board does not have a low power ticker, ensure that tickless is enabled using the microsecond ticker:

    ```json
    "overrides": {
        "tickless-from-us-ticker": true
    }
    ```

    - By default, all bare metal targets are configured to have a boot stack size of 0x1000 (4,096 bytes). If this is too much for your target, you will need to override the stack allocation to match your target's available RAM.

    The stack size is configured by setting a value for the `boot-stack-size` attribute; this value must be a multiple of 8 for alignment purposes. We recommend that you reduce the boot stack size to 0x400 (1,024 bytes) if your target has 8KB of RAM and to 0x300 (768 bytes) if your target has 4KB of RAM.

    ```json
    "overrides": {
        "boot-stack-size": "0x400"
    }
    ```

### Build and run the Blinky bare metal example

Build the application and program your target:

```
mbed compile -m <YOUR_TARGET> -t <TOOLCHAIN> --flash --sterm
```

The application running on the target should print a text on the console. Repeat for all supported toolchains.

Troubleshoot any issue.

## Validating the port

To validate the bare metal target configuration, execute the Mbed OS Greentea test suite with the bare metal profile. This profile causes Greentea to skip a subset of the tests, either because the underlying functionality has not been ported to bare metal or because some tests require RTOS features (for examples, more complex tests based on multi-threading). It performs all the tests compatible with bare metal.

If you haven't used Greentea before, [you can learn more in our documentation](../debug-test/greentea-testing-applications.html).

1. Change directory:

    ```
    cd mbed-os
    ```

1. Execute the Greentea test suite with the bare metal configuration for the supported toolchains:

    ```
    mbed test -m <YOUR_TARGET> -t <TOOLCHAIN> --app-config TESTS/configs/baremetal.json
    ```

    <span class="tips">**Tip:** You can append `--compile` and fix build issues before running tests with `--run`.</span>

1. All tests should pass (or be automatically skipped), unless the target being ported is ultraconstrained (with 32KB or less of flash memory) - in which case linking may fail for _a few_ tests. For example:

    ARM toolchain:
    ```
    Error: L6407E: Sections of aggregate size 0x318 bytes could not fit into .ANY selector(s).
    ```

    GCC_ARM toolchain:
    ```
    region `FLASH' overflowed by 792 bytes
    ```

    Please ignore tests with similar errors.

Further optimisations for targets with small flash memories:
- Append `--profile release` to the command above. Use of the release profile helps keep some tests within the size limit.
- Save additional memory by using a [minimal console](https://github.com/ARMmbed/mbed-os-example-blinky-baremetal#using-a-minimal-console) to remove file handling functionality from the system I/O retarget code.

    Modify `TESTS/configs/baremetal.json` for your target:

    ```json
    {
        "target_overrides": {
            "YOUR_TARGET": {
                "platform.stdio-minimal-console-only": true
            }
        }
    }
    ```
