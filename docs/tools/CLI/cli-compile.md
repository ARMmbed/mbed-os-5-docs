# Compiling mbed compile --library --no-archive

This section details some of the arguments available with the `mbed compile` command. Please run `mbed compile --help` to get a full list of arguments.

## Compiling your application

Use the `mbed compile` command to compile your code. Supply the `-m` and `-t` arguments to set your target and toolchain, respectively.

To find your board's target name, use `--supported`.

The valid toolchain values are:

| Argument value | Toolchain |
| --------- | --------- |
| `ARM` | Arm Compiler 5 or Arm Compiler 6 (whichever is installed) |
| `ARMC5` | Arm Compiler 5 |
| `ARMC6` | Arm Compiler 6 |
| `IAR` | IAR EWARM Compiler |
| `GCC_ARM` | GNU Arm Embedded Compiler (GCC) |

As an example, for the K64F and Arm Compiler:

```
$ mbed compile -m K64F -t ARM
Building project mbed-os-program (K64F, GCC_ARM)
Compile: aesni.c
Compile: blowfish.c
Compile: main.cpp
... [SNIP] ...
Compile: configuration_store.c
Link: mbed-os-program
Elf2Bin: mbed-os-program
+----------------------------+-------+-------+------+
| Module                     | .text | .data | .bss |
+----------------------------+-------+-------+------+
| Fill                       |   170 |     0 | 2294 |
| Misc                       | 36282 |  2220 | 2152 |
| core/hal                   | 15396 |    16 |  568 |
| core/rtos                  |  6751 |    24 | 2662 |
| features/FEATURE_IPV4      |    96 |     0 |   48 |
| frameworks/greentea-client |   912 |    28 |   44 |
| frameworks/utest           |  3079 |     0 |  732 |
| Subtotals                  | 62686 |  2288 | 8500 |
+----------------------------+-------+-------+------+
Allocated Heap: 65540 bytes
Allocated Stack: 32768 bytes
Total Static RAM memory (data + bss): 10788 bytes
Total RAM memory (data + bss + heap + stack): 109096 bytes
Total Flash memory (text + data + misc): 66014 bytes
Image: BUILD/K64F/GCC_ARM/mbed-os-program.bin
```

### Setting a default target

To set a default target, use the `mbed target` command with the name of your target (in this example, the K64F):

```
$ mbed target K64F
[mbed] Working path "C:\project" (program)
[mbed] K64F now set as default target in program "project"
```

Alternatively, pass `detect` instead of your target name to automatically use the target already connected to your computer:

```
$ mbed target detect
```

### Setting a default toolchain

To set a default toolchain, use the `mbed toolchain` command:

```
$ mbed toolchain GCC_ARM
[mbed] Working path "C:\project" (program)
[mbed] GCC_ARM now set as default toolchain in program "project"
```

### Performing a clean build

To rebuild the project, use the `-c/--clean` argument:

```
mbed compile -c
```

### Flashing the built program and monitor the target

You can flash the built program to the connected target by adding the `-f/--flash` argument to the `compile` command:

```
mbed compile -f
```

You can also read and write to the target's serial port by adding the `--sterm` argument (this can be chained with the `-f/--flash` argument):

```
mbed compile -f --sterm
```

## Build sources and output

### Source directories

By default, Mbed CLI includes the program's root directory and all its subdirectories as the source directory. To control which directories are used, use the `--source` argument. You can supply multiple `--source` arguments to include multiple directories:

```
$ mbed compile --source ./src --source ./lib
```

### Build directory

The default build directory is in the root of your project and is called `BUILD`. You can set the build directory with the `--build` argument:

```
$ mbed compile --build my_build
```

### Building a library

To build a static library instead of a linked executable, use the `--library` argument:

```
$ mbed compile --library
```

To suppress the creation of the `.a/.ar` archive (and instead leave the `.o` object files), use both the `--library` and `--no-archive` arguments:

   `mbed compile --library --no-archive`

## Build profiles

Build profiles control which arguments are passed to the compiler. For more information about build profiles, please see the [build profile documentation](../tools/build-profiles.html).

The default build profile is `develop`, which enables debug logging. There is also a `debug` profile, which enables debug symbols, and a `release` profile that disables debug logging (to reduce the program size).

To select a profile, use the `--profile` argument:

```
$ mbed compile --profile debug
```

## Configuration system

The Mbed OS configuration system customizes compile time configuration parameters. For more information, please see [the full configuration system documentation](../reference/configuration.html).

To view your current configuration, use `mbed compile --config` (use the `-v` argument to display more information):

```
$ mbed compile --config -t GCC_ARM -m K64F -v
```

To filter the output of `mbed compile --config`, specify one or more `--prefix` arguments for the configuration parameters that Mbed CLI displays. For example, to display only the configuration defined by the targets:

```
$ mbed compile --config -t GCC_ARM -m K64F --prefix target
```

You may use `--prefix` more than once. To display only the application and target configuration, use two `--prefix` options:

```
$ mbed compile --config -t GCC_ARM -m K64F --prefix target --prefix app
```

### Defining macros

To define macros when compiling, use the `-D` argument:

```
$ mbed compile -D MY_MACRO -D MY_VALUE=1
```
