# Compile

The following section goes into detail about some of the arguments available with the `mbed compile` command. Please run `mbed compile --help` locally to get a full list of arguments.

## Compile your application

Use the `mbed compile` command to compile your code. Supply the `-m` and `-t` arguments to set your target and toolchain respectively:

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
### Set the target

You can set the default target with the `mbed target` command to avoid having to supply the `-m` argument:

```
$ mbed target K64F
[mbed] Working path "C:\project" (program)
[mbed] K64F now set as default target in program "project"
```

Mbed CLI can detect the target connected to the system and use that as the build target. Enable this behavior by setting the target to `detect` or `auto`.

### Set the toolchain

You can set the default target with the `mbed toolchain` command to avoid having to supply the `-t` argument:

```
$ mbed target GCC_ARM
[mbed] Working path "C:\project" (program)
[mbed] GCC_ARM now set as default toolchain in program "project"
```

The valid toolchain values are as follows:

| Argument value | Toolchain |
| --------- | --------- |
| `ARM` | Arm Compiler 5 or Arm Compiler 6 (based on environment) |
| `ARMC5` | Arm Compiler 5 |
| `ARMC6` | Arm Compiler 6 |
| `IAR` | IAR EWARM Compiler |
| `GCC_ARM` | GNU Arm Embedded Compiler (GCC) |

### Perform a clean build

To rebuild the project, use the `-c/--clean` argument:

```
mbed compile -c
```

### Flash and monitor the target with the built program

You can flash a connected target with the built program by adding the `-f/--flash` argument:

```
mbed compile -f
```

You can also read and write to the target's serial port by adding the `--sterm` argument (this can be chained with the `-f/--flash` argument):


## Build sources and output


### Source directories

Mbed CLI includes the program's root directory as the source directory as well as all subdirectories. You can control what directories are used by using the `--source` argument. You can supply multiple `--source` arguments to include multiple directories:

```
$ mbed compile --source ./src --source ./lib
```

### Build directory

The default build directory is in the root of your project in a directory called `BUILD`. You can set the build directory `--build` argument:

```
$ mbed compile --build my_build
```

### Build profiles

Build profiles are used to control what arguments are passed to the compiler. For more information about build profiles, please see the [build profile documentation](../tools/build-profiles.html).

The default build profile is set to `develop`, which enables debug logging. There is also a `debug` profile (for enabling debug symbols) and a `release` profile (for disabling debug logging, saving program size). This is controlled with the `--profile` argument:

```
$ mbed compile --profile debug
```

### Build a library

If you wish to build a static library instead of a linked executable, you can use the `--library` argument:

```
$ mbed compile --library
```

To suppress the creation of the `.a/.ar` archive (and instead leave the `.o` object files), use the `--no-archive` argument in addition to the `--library` argument. 

## Configuration system

You can use `mbed compile --config` to view the configuration (use the `-v` argument to display more information):

```
$ mbed compile --config -t GCC_ARM -m K64F -v
```

It's possible to filter the output of `mbed compile --config` by specifying one or more `--prefix` arguments for the configuration parameters that Mbed CLI displays. For example, to display only the configuration defined by the targets:

```
$ mbed compile --config -t GCC_ARM -m K64F --prefix target
```

You may use `--prefix` more than once. To display only the application and target configuration, use two `--prefix` options:

```
$ mbed compile --config -t GCC_ARM -m K64F --prefix target --prefix app
```

### Define macros

Define macros when compiling by using the `-D` argument:

```
$ mbed compile -D MY_MACRO -D MY_VALUE=1
```