# Porting an Mbed OS 2 target to Mbed OS 6 bare metal

The Mbed OS bare metal profile removes the RTOS and provides fewer features compared to Mbed OS 6. This profile offers the same functionality as Mbed OS 2 and allows targets to access features that we have added to more recent versions of Mbed OS. This document describes how to configure an Mbed OS 2 target for bare metal and validate the port.

## Configuring your target

You will use the blinky bare metal Mbed OS example and make it run on your target. The configuration will be validated upon successful run of the example.

The main steps are:
1. Clone [mbed-os-example-blinky-baremetal](https://github.com/ARMmbed/mbed-os-example-blinky-baremetal).
1. Edit `targets.json`. In this step, you will configure your target to support Mbed OS 6 and add bare metal configuration parameters.
1. Build and run mbed-os-example-blinky-baremetal. In this step, you will validate the configuration and troubleshoot any issue.

### Clone mbed-os-example-blinky-baremetal

Run the following command:
- `git clone https://github.com/ARMmbed/mbed-os-example-blinky-baremetal`

And then change directory:
- `cd mbed-os-example-blinky-baremetal`

### Edit targets.json

Find your target in `mbed-os/targets/targets.json` and update its configuration as described below.

Configure your target to support Mbed OS 6:
- Remove the `release_versions` property as it is no longer required.
```
"release_versions": ["2"]
```

- Add the `supported_application_profiles` property to indicate that the application profile supported by this target is bare metal.
```
"supported_application_profiles" : ["bare-metal"]
```

- Override `supported_c_libs` property to link with the smaller C libraries. The default for all targets is defined as follows: 
```
"supported_c_libs": {
    "arm":  ["std"],
    "gcc_arm":  ["std", "small"],
    "iar": ["std"]
}
```

Both the ARM and GCC_ARM toolchains support optimized versions of the C standard libraries, microlib and newlib-nano respectively. We recommend using them with the bare metal profile to achieve lower memory footprints. Ultra constrained targets should override `supported_c_libs` as follows:
```
"supported_c_libs": {
    "arm":  ["small"],
    "gcc_arm":  ["small"]
}
```

For each toolchain, if there is enough memory to link with the standard library, add the corresponding "std" library to the list. For example:
```
"supported_c_libs": {
    "arm":  ["std", "small"],
    "gcc_arm":  ["std", "small"],
    "iar": ["std"]
}
```
<span class="notes">**Note:** For ARM, your target scatter file needs to have a two-region memory model. If the build system throws an error (presence of undefined symbols `Image$$ARM_LIB_HEAP$$ZI$$Base`, `Image$$ARM_LIB_HEAP$$ZI$$Length`, `Image$$ARM_LIB_HEAP$$ZI$$Limit`) when compiling with microlib, you can find more information [here](https://os.mbed.com/docs/mbed-os/v6.0-preview/reference/using-small-c-libraries.html).</span>

<span class="notes">**Note:** The IAR toolchain does not have a small C library.</span>

- Set the `c_lib` property to indicate which C library should be used by the build tools. If your target has `"default_lib": "small"` defined, then replace it with `"c_lib" : "small"`. Otherwise add `"c_lib" : "small"`. We recommend that ultra constrained devices running bare metal applications link with the small C libraries by default.

<span class="notes">**Note:** If a toolchain does not support a small C library and `c_lib` is set to `small`, the build tools will revert to linking with the standard C library, provided that it is listed in `supported_c_libs` for the given toolchain.</span>

- If `default_toolchain` is set to `uARM`, then replace it with `ARM` and remove `uARM` from `supported_toolchains`. Support for the uARM toolchain, which is the ARM toolchain with microlib, has been removed. Setting `c_lib` to `small` ensures that microlib is used when the ARM toolchain is selected.

<span class="notes">**Note:** As mentioned above, to successfully build with microlib, the target must define a two-region memory model. You might need to replace the content of the TOOLCHAIN_ARM_STD linker file with that of TOOLCHAIN_ARM_MICRO which includes a two-region memory model linker file.</span>

- If your board does not have a low power ticker, ensure that tickless is enabled using the microsecond ticker as follows:
```
"overrides": {
    "tickless-from-us-ticker": true
}
```

- It might be necessary to reduce the stack size allocated for your target if it does not have enough RAM. The stack size is configured by setting a value for the `boot-stack-size` attribute; this value must be a multiple of 8 for alignment purposes. By default all targets are configured to have a boot stack size of 0x1000 (4096 bytes) in bare metal. However, this must be overridden if inadequate for your target. We recommend to reduce the boot stack size to 0x400 (1024 bytes) if your target has 8KB of RAM and to 0x300 (768 bytes) if your target has 4KB of RAM.
```
"overrides": {
    "boot-stack-size": "0x400"
}
```

### Build and run mbed-os-example-blinky-baremetal

Build the application and program your target: `mbed compile -m <YOUR_TARGET> -t <TOOLCHAIN> --flash --sterm`.

The application running on the target should print a text on the console. Repeat for all supported toolchains.

Troubleshoot any issue.

## Validating the port

To validate the bare metal target configuration, you will execute the Mbed OS greentea test suite with the bare metal configuration. A subset of the tests are automatically skipped by the framework either because the underlying functionality has not been ported to bare metal or because some tests require RTOS features, for examples more complex tests based on multi-threading.

- First, change directory.
```
cd mbed-os
```
- Then execute the greentea test suite with the bare metal configuration for the supported toolchains.
```
mbed test -m <YOUR_TARGET> -t <TOOLCHAIN> --app-config TESTS/configs/baremetal.json
```
It can be useful to append `--compile` and fix build issues first before running tests with `--run`.

All tests should pass (or be automatically skipped).

Further optimisations for targets with small flash memories:
- Append `--profile release` to the command above. Use of the release profile helps keep some tests within the size limit.
- Save additional memory by using a [minimal console](https://github.com/ARMmbed/mbed-os-example-blinky-baremetal#using-a-minimal-console) to remove file handling functionality from the system I/O retarget code.

  Modify `TESTS/configs/baremetal.json` for your target:
```
{
    "target_overrides": {
        "YOUR_TARGET": {
            "platform.stdio-minimal-console-only": true
        }
    }
}
```
