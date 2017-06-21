## Compiling code with mbed CLI

### Toolchain selection

After importing a program or creating a new one, you need to tell mbed CLI where to find the toolchains that you want to use for compiling your source tree.

There are multiple ways to configure toolchain locations:
* `mbed_settings.py` file in the root of your program. The tools will automatically create this file if it doesn't already exist. 
* The mbed CLI configuration.
* Setting an environment variable.
* Adding directory of the compiler binary to your PATH.

Methods for configuring toolchains that appear earlier in the above list override methods that appear later.

#### Through mbed_settings.py

Edit `mbed_settings.py` to set your toolchain:

* To use the [ARM Compiler toolchain](https://developer.arm.com/products/software-development-tools/compilers/arm-compiler-5/downloads), set `ARM_PATH` to the *base* directory of your ARM Compiler installation (example: C:\Program Files\ARM\armcc5.06). The recommended version of the ARM Compiler toolchain is 5.06.
* To use the [GNU ARM Embedded toolchain (GCC) version 6](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads), set `GCC_ARM_PATH` to the *binary* directory of your GCC ARM installation (example: C:\Program Files\GNU Tools ARM Embedded\6 2017q2\bin). Use version 6 of GCC ARM Embedded; version 5.0 or any older version might be incompatible with the tools.
* To use the [IAR EWARM toolhain](https://www.iar.com/iar-embedded-workbench/#!?architecture=ARM), set `IAR_PATH` to the *base* directory of your IAR installation. Use versions 7.80 of IAR EWARM; prior versions might be incompatible with the tools.

Because `mbed_settings.py` contains local settings (possibly relevant only to a single OS on a single machine), you should not check it into version control. 

#### Through mbed CLI configuration

You can set the ARM Compiler  5 location via the command:

```
$ mbed config -G ARM_PATH "C:\Program Files\ARM"
[mbed] C:\Program Files\ARM now set as global ARM_PATH
```

The `-G` switch tells mbed CLI to set this as a global setting, rather than local for the current program.

Supported settings for toolchain paths are `ARM_PATH`, `GCC_ARM_PATH` and `IAR_PATH`.

You can see the active mbed CLI configuration via:

```
$ mbed config --list
[mbed] Global config:
ARM_PATH=C:\Program Files\ARM\armcc5.06
IAR_PATH=C:\Program Files\IAR Workbench 7.0\arm

[mbed] Local config (D:\temp\mbed-os-program):
No local configuration is set
```

More information about mbed CLI configuration is available in the [configuration section](#mbed-cli-configuration) of this document.

#### Setting environment variable

For each of the compilers, `mbed compile` checks a corresponding environment variable for the compiler's location. The environment variables are as follows:
* `MBED_ARM_PATH`: The path to the *base* directory of your ARM Compiler installation. This should be the directory containing the directory containing the binaries for `armcc` and friends.
* `MBED_IAR_PATH`: The path to the *base* directory of your IAR EWARM Compiler installation. This should be one directory containing the directory containing the binaries for `iccarm` and friends.
* `MBED_GCC_ARM_PATH`: The path to the *binary* directory of your GCC ARM Embedded Compiler installation. This should be the directory containing the binaries for `arm-none-eabi-gcc` and friends.

#### Compiler detection through the `PATH`

If none of the above are configured, the `mbed compile` command will fall back to checking your `PATH` for an executable that is part of the compiler suite in question. This check is the same as a shell would perform to find the executable on the command-line. When `mbed compile` finds the executable it is looking for, it uses the location of that executable as the appropriate path except in the case of GCC, which will not use a path.

### Compiling your program

Use the `mbed compile` command to compile your code:

```
$ mbed compile -t ARM -m K64F
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

The arguments for *compile* are:

* `-m <MCU>` to select a target. If `detect` or `auto` parameter is passed to `-m`, then mbed CLI detects the connected target.
* `-t <TOOLCHAIN>` to select a toolchain (of those defined in `mbed_settings.py`, see above). The value can be `ARM` (ARM Compiler 5), `GCC_ARM` (GNU ARM Embedded) or `IAR` (IAR Embedded Workbench for ARM).
* `--source <SOURCE>` to select the source directory. The default is `.` (the current directory). You can specify multiple source locations, even outside the program tree.
* `--build <BUILD>` to select the build directory. Default: `BUILD/` inside your program root.
* `--profile <PATH_TO_BUILD_PROFILE>` to select a path to a build profile configuration file. Example: mbed-os/tools/profiles/debug.json.
* `--library` to compile the code as a [static .a/.ar library](#compiling-static-libraries).
* `--config` to inspect the runtime compile configuration (see below).
* `-S` or `--supported` shows a matrix of the supported targets and toolchains.
* `-f` or `--flash` to flash/program a connected target after successful compile.
* `-c ` to build from scratch, a clean build or rebuild.
* `-j <jobs>` to control the compile processes on your machine. The default value is 0, which infers the number of processes from the number of cores on your machine. You can use `-j 1` to trigger a sequential compile of source code.
* `-v` or `--verbose` for verbose diagnostic output.
* `-vv` or `--very_verbose` for very verbose diagnostic output.

You can find the compiled binary, ELF image, memory usage and link statistics in the `BUILD` subdirectory of your program.

For more information on build profiles, see [our build profiles](https://docs.mbed.com/docs/mbed-os-handbook/en/latest/dev_tools/build_profiles/) and [toolchain profiles](https://docs.mbed.com/docs/mbed-os-handbook/en/latest/advanced/toolchain_profiles/) pages.

### Compiling static libraries

You can build a static library of your code by adding the `--library` argument to `mbed compile`. Static libraries are useful when you want to build multiple applications from the same mbed OS codebase without having to recompile for every application. To achieve this:

1. Build a static library for mbed-os.
2. Compile multiple applications or tests against the static library:

```
$ mbed compile -t ARM -m K64F --library --no-archive --source=mbed-os --build=../mbed-os-build
Building library mbed-os (K64F, ARM)
[...]
Completed in: (47.4)s

$ mbed compile -t ARM -m K64F --source=mbed-os/TESTS/integration/basic --source=../mbed-os-build --build=../basic-out
Building project basic (K64F, ARM)
Compile: main.cpp
Link: basic
Elf2Bin: basic
Image: ../basic-out/basic.bin

$ mbed compile -t ARM -m K64F --source=mbed-os/TESTS/integration/threaded_blinky --source=../mbed-os-build --build=..\/hreaded_blinky-out
Building project threaded_blinky (K64F, ARM)
Compile: main.cpp
Link: threaded_blinky
Elf2Bin: threaded_blinky
Image: ../threaded_blinky-out/threaded_blinky.bin
```

### Compile configuration system

The [compile configuration system](https://docs.mbed.com/docs/mbed-os-handbook/en/5.3/advanced/config_system/) provides a flexible mechanism for configuring the mbed program, its libraries and the build target.

#### Inspecting the configuration

You can use `mbed compile --config` to view the configuration:

```
$ mbed compile --config -t GCC_ARM -m K64F
```

To display more verbose information about the configuration parameters, use `-v`:

```
$ mbed compile --config -t GCC_ARM -m K64F -v
```

It's possible to filter the output of `mbed compile --config` by specifying one or more prefixes for the configuration parameters that mbed CLI displays. For example, to display only the configuration defined by the targets:

```
$ mbed compile --config -t GCC_ARM -m K64F --prefix target
```

You may use `--prefix` more than once. To display only the application and target configuration, use two `--prefix` options:

```
$ mbed compile --config -t GCC_ARM -m K64F --prefix target --prefix app
```

### Compile-time customizations

#### Macros

You can specify macros in your command-line using the -D option. For example:

```
$ mbed compile -t GCC_ARM -m K64F -c -DUVISOR_PRESENT
```

#### Compiling in debug mode

To compile in debug mode (as opposed to the default *develop* mode), use `--profile mbed-os/tools/profiles/debug.json` in the compile command-line:

```
$ mbed compile -t GCC_ARM -m K64F --profile mbed-os/tools/profiles/debug.json
```

<span class="tips">**Tip:** If you have files that you want to compile only in debug mode, put them in a directory called `TARGET_DEBUG` at any level of your tree (then use `--profile` as explained above).
</span>

### Automating toolchain and target selection

Using `mbed target <target>` and `mbed toolchain <toolchain>`, you can set the default target and toolchain for your program. You won't have to specify these every time you compile or generate IDE project files.

You can also use ``mbed target detect``, which detects the connected target board and uses it as a parameter to every subsequent compile and export.

### Exporting to desktop IDEs

If you need to debug your code, you can export your source tree to an IDE project file to use the IDE's debugging facilities. mbed CLI supports exporting to Keil uVision, IAR Workbench, a Makefile using GCC ARM, Eclipse using GCC ARM and other IDEs.

For example, to export to uVision, run:

```
$ mbed export -i uvision -m K64F
```

mbed CLI creates a `.uvprojx` file in the projectfiles/uvision folder. You can open the project file with uVision.
