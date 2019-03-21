## Compile

### Compiling your application

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

- `-m <MCU>` selects a target. If `detect` or `auto` parameter is passed to `-m`, then Mbed CLI detects the connected target.
- `-t <TOOLCHAIN>` selects a toolchain defined in `mbed_settings.py`. The value can be `ARM` (Arm Compiler 6 or ARM Compiler 5), `ARMC5` (ARM Compiler 5), `ARMC6` (Arm Compiler 6), `GCC_ARM` (GNU Arm Embedded) or `IAR` (IAR Embedded Workbench for Arm).
   <span class="notes">**Note**: `mbed compile -t ARM` selects the Arm Compiler major version based on the Arm architecture version of your target and `supported_toolchains` configuration.
   Please see `supported_toolchains` in [Adding and configuring targets](../reference/adding-and-configuring-targets.html) and `Compiler versions` in [Arm Mbed tools](../tools/tools_intro.html) for more information on toolchain configuration and usage.</span>
- `--source <SOURCE>` selects the source directory. The default is `.` (the current directory). You can specify multiple source locations, even outside the program tree. Find more details about the `--source` switch in the [build rules documentation](../reference/mbed-os-build-rules.html).
- `--build <BUILD>` selects the build directory. Default: `BUILD/` inside your program root.
   <span class="notes">**Note**: `mbed compile` ignores the current build directory; creating multiple build directories leads to errors.</span>
- `--stats-depth <DEPTH>` summarizes memory statistics within the table printed after linking, the CSV map file and the JSON map file for paths with depth greater than `DEPTH`. Default: `2`.
- `--profile <PATH_TO_BUILD_PROFILE>` selects a path to a build profile configuration file. Example: `debug`. See the dedicated [build profile documentation](../tools/build-profiles.html) for more detail.
- `--library` compiles the code as a [static `.a/.ar` library](#compiling-static-libraries).
- `--no-archive` suppresses the creation of `.a/.ar` files created by `--library`, producing many `.o` files instead.
   <span class="notes">**Note**: This option does nothing without `--library`.</span>
- `--config` inspects the runtime compile configuration (see below).
- `-S` or `--supported` shows a matrix of the supported targets and toolchains.
- `-f` or `--flash` flashes/programs a connected target after successful compile.
- `-c ` builds from scratch, a clean build or rebuild.
- `-j <jobs>` controls the compile processes on your machine. The default value is 0, which infers the number of processes from the number of cores on your machine. You can use `-j 1` to trigger a sequential compile of source code.
- `-v` or `--verbose` shows verbose diagnostic output.
- `-vv` or `--very_verbose` shows very verbose diagnostic output.

You can find the compiled binary, ELF image, memory usage and link statistics in the `BUILD` subdirectory of your program.

For more information, please see [our build profiles](../tools/build-profiles.html) pages.

### Compiling static libraries

You can build a static library of your code by adding the `--library` argument to `mbed compile`. Static libraries are useful when you want to build multiple applications from the same Mbed OS codebase without having to recompile for every application. To achieve this:

1. Build a static library for `mbed-os`.
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

### The compile configuration system

The [compile configuration system](../tools/compile.html) provides a flexible mechanism for configuring the Mbed program, its libraries and the build target.

#### Inspecting the configuration

You can use `mbed compile --config` to view the configuration:

```
$ mbed compile --config -t GCC_ARM -m K64F
```

To display more verbose information about the configuration parameters, use `-v`:

```
$ mbed compile --config -t GCC_ARM -m K64F -v
```

It's possible to filter the output of `mbed compile --config` by specifying one or more prefixes for the configuration parameters that Mbed CLI displays. For example, to display only the configuration defined by the targets:

```
$ mbed compile --config -t GCC_ARM -m K64F --prefix target
```

You may use `--prefix` more than once. To display only the application and target configuration, use two `--prefix` options:

```
$ mbed compile --config -t GCC_ARM -m K64F --prefix target --prefix app
```

#### Compile-time customizations

##### Macros

You can specify macros in your command-line using the -D option. For example:

```
$ mbed compile -t GCC_ARM -m K64F -c -DUVISOR_PRESENT
```

##### Compile in debug mode

To compile in debug mode (as opposed to the default *develop* mode), use `--profile debug` in the compile command-line:

```
$ mbed compile -t GCC_ARM -m K64F --profile debug
```


#### Automate toolchain and target selection

Using `mbed target <target>` and `mbed toolchain <toolchain>`, you can set the default target and toolchain for your program. You won't have to specify these every time you compile or generate IDE project files.

You can also use `mbed target detect`, which detects the connected target board and uses it as a parameter to every subsequent compile and export.

#### Update programs and libraries

You can update programs and libraries on your local machine so that they pull in changes from the remote sources (Git or Mercurial).

As with any Mbed CLI command, `mbed update` uses the current directory as a working context. Before calling `mbed update`, you should change your working directory to the one you want to update. For example, if you're updating `mbed-os`, use `cd mbed-os` before you begin updating.

<span class="tips">**Tip: Synchronizing library references:** Before triggering an update, you may want to synchronize any changes that you've made to the program structure by running `mbed sync`, which updates the necessary library references and removes the invalid ones.</span>

##### Protect against overwriting local changes

The update command fails if there are changes in your program or library that `mbed update` could overwrite. This is by design. Mbed CLI does not run operations that would result in overwriting uncommitted local changes. If you get an error, take care of your local changes (commit or use one of the options below), and then rerun `mbed update`.
