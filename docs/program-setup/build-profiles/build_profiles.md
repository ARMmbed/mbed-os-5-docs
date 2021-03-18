# Build profiles

Arm Mbed OS defines three collections of toolchain flags used during the build. These are __build profiles__.  The three build profiles are *develop*, *debug* and *release*. The Mbed Online Compiler uses the *develop* build profile. When building from Arm Mbed CLI, you may select the __build profile__ by passing your desired build profile, by name or path, to the `--profile` argument.

## Develop

- Small and fast code.
- Full error information. For example, asserts have file name and line number.
- Hard to follow code flow when using a debugger.
- Chip goes to sleep when idle:
   - Debugger is likely to drop connection.
   - Breaks the local file system on the [Arm Mbed interface](../introduction/index.html) on some boards.

## Debug

- Largest and slowest performance.
- Full error information. For example, asserts have file name and line number.
- Easy to step through code with a debugger.
- Disabled sleep mode.

<span class="notes">**Note:** The debug profile uses optimization flags that may cause unwanted behavior during debugging (such as out-of-order jumps and optimized-out variables). If this occurs, you can set the compiler to the lowest possible optimization setting (for example, change `-Og` to `-O0` for GCC). See your toolchain's documentation for more information.</span>

## Release

- Smallest code size and still fast.
- Minimal error information.
- Chip goes to sleep when going idle:
   - Debugger is likely to drop connection.
   - Breaks the local file system on the [Mbed interface](../introduction/index.html) on some boards.

### Custom profile

[Mbed CLI 1](TODO_CMAKE:../mbed_cli_1/build-system/build.html)
[Mbed CLI 2](TODO_CMAKE:../mbed_cli_1/build-system/toolchain.html)
