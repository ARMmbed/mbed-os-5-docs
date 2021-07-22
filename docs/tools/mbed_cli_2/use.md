# Use

For help:

- To get help for all commands, use:

    ```
    mbed-tools --help
    ```

- To get help for a specific command, use `mbed-tools <command> --help`. For example, for helping with listing connected devices (the `detect` command):

    ```
    mbed-tools detect --help
    ```

## Create a project

You can create a new project or create a local copy of one of our example applications.

### Create a new project

To create a new Mbed OS project in a specified path:

- To create the project and download a new copy of Mbed OS (latest official release):

    ```
    mbed-tools new <PATH>
    ```

    The path can be:

    - Absolute. `new` will create the folder if it doesn't exist.
    - Relative:

        - If you have already created a project folder, you can use `.`

        - If you want the `new` command to create a project folder, use `.\<folder-name>`.

- To create a project without downloading a copy of Mbed OS (reuse an existing copy):

    ```
    mbed-tools new -c <PATH>
    ```

### Use an example application

To create a local copy of an example application, use the `import` command with the example name listed below:

```
mbed-tools import <example> <PATH>
```

- [mbed-os-example-blinky](https://github.com/ARMmbed/mbed-os-example-blinky)
- [mbed-os-example-ble](https://github.com/ARMmbed/mbed-os-example-ble) - use the BLE Advertising example.
- [mbed-os-example-cellular](https://github.com/ARMmbed/mbed-os-example-cellular)
- [mbed-os-example-devicekey](https://github.com/ARMmbed/mbed-os-example-devicekey)
- [mbed-os-example-kvstore](https://github.com/ARMmbed/mbed-os-example-kvstore)
- [mbed-os-example-lorawan](https://github.com/ARMmbed/mbed-os-example-lorawan)
- [mbed-os-example-mbed-crypto](https://github.com/ARMmbed/mbed-os-example-mbed-crypto)
- [mbed-os-example-nfc](https://github.com/ARMmbed/mbed-os-example-nfc)
- [mbed-os-example-sockets](https://github.com/ARMmbed/mbed-os-example-sockets)

Mbed CLI 2 will automatically use a shallow clone of git repositories whenever
it can (with `import`, `deploy`, and other applicable commands) to speed up
library and application management tasks. This will provide you with a local
copy of a git repository that contains only a single branch. If you'd like to
`git checkout` other versions manually, you'll need to convert your local
repository into a complete copy using `git fetch --unshallow`.

### Use a specific Mbed program library

A Mbed program can use library dependencies at the revision specified in the ".lib" files.
This ensures all dependencies are resolved and the versions are synchronised to the version specified in the library reference.

    ```
    mbed-tools deploy <PATH>
    ```

    - `<path>`: Path to the Mbed project [default: CWD]

- To force overwrite local uncommitted changes of the library dependencies.

    ```
    mbed-tools deploy -f
    ```

## Configure the project

Each project depends on two sets of configurations:

- The project's environment variables. You can use the default values.
- The Mbed OS configuration system. You must set up your target and toolchain.

### (Optional) Project environment variables

Mbed CLI 2 has two environment variables that you can set for a project:

- `MBED_API_AUTH_TOKEN`: Token to access private board information stored for a vendor team.
- `MBED_DATABASE_MODE`: Use online or offline mode. Possible values:
    - `AUTO`: Search the offline database first; search the online database only if the board wasn't found offline. This is the default value.
    - `ONLINE`: Alway use the online database.
    - `OFFLINE`: Always use the offline database.

You can set these variables either directly, using environment variables, or indirectly using a `.env` file containing the variable definitions:

```
VARIABLE1=<value>
VARIABLE2=<value>
```

Environment variables take precedence, meaning values previously set in your environment will override the values set in the file.

<span class="warning">**Warning**: Do not upload `.env` files containing private tokens to version control. If you use this package as a dependency for your project, please ensure to include the
`.env` in your `.gitignore`.</span>

### Mbed OS configuration

The Mbed OS configuration system parses the configuration files in your project (mbed_lib.json, mbed_app.json and targets.json) for a particular target and toolchain, and outputs a CMake script. The build system uses this script to build for your target, using your toolchain.

<span class="tips">**Tip:** If you're rebuilding for the same target and toolchain, you can keep using the same CMake script, so you won't have to use the `configure` command again for each build. If you change any of mbed_lib.json, mbed_app.json, targets.json, your target or your toolchain, run the `configure` command again to generate a new CMake script.</span>

1. Check your board's build target name.

    Connect your board over USB and run the `detect` command:

    ```
    mbed-tools detect

    Board name    Serial number             Serial port             Mount point(s)    Build target(s)    Interface Version
    ------------  ------------------------  ----------------------  ----------------  -----------------  -------------------
    FRDM-K64F     024002017BD34E0F862DB3B7  /dev/tty.usbmodem14402  /Volumes/MBED     K64F               0221
    ```
1. To prepare the Mbed configuration information for use with a specific target and toolchain, navigate to the project's root folder and run:

    ```
    mbed-tools configure -m <target> -t <toolchain>
    ```

    - The supported targets are `K64F`, `DISCO_L475VG_IOT01A`, `NRF52840_DK`
    - The supported toolchains are listed [in the build tools overview](../build-tools/index.html).

    Example for FRDM-K64F and GCC:

    ```
    mbed-tools configure -m K64F -t GCC_ARM
    mbed_config.cmake has been generated and written to '/Users/UserName/Development/Blinky/cmake_build/K64F/develop/GCC_ARM/mbed_config.cmake'
    ```

## Configure and build in a single step

You can use a single command to configure (set up your target and toolchain) and build the project at once:

```
mbed-tools compile -m <target> -t <toolchain>
```

- `-t`: The toolchain you are using to build your project.
- `-m`: A build target for an Mbed-enabled device.

Example for [DISCO-L475VG-IOT01A](https://os.mbed.com/platforms/ST-Discovery-L475E-IOT01A/) and GCC:

```
mbed-tools compile -m DISCO_L475VG_IOT01A -t GCC_ARM
```


## Build the project with CMake (advanced)

We'll show how to build your project using CMake directly, which provides you
with the full capabilities of CMake. You are no longer limited by what Mbed CLI
2 has to offer.

For this example, we'll use the `GCC_ARM` toolchain with the Mbed target
`DISCO_L475VG_IOT01A`.

To use CMake to build your application:

1. Navigate to the project's root folder.
1. Translate from the Mbed configuration system to a form CMake can understand:

   ```
   mbed-tools configure -m DISCO_L475VG_IOT01A -t GCC_ARM
   ```

   This will create a build folder at `cmake_build/DISCO_L475VG_IOT01A/develop/GCC_ARM`

1. Set the build parameters:

   ```
   cmake -S . -B cmake_build/DISCO_L475VG_IOT01A/develop/GCC_ARM -GNinja
   ```
   - `-S <path-to-source>`: Path to the root directory of the CMake project.
     We use `.` to indicate we're building from the current directory.
   - `-B <path-to-build-directory>`: Path to the
     build output directory. If the directory doesn't already exist, CMake
     will create it. We use `cmake_build/DISCO_L475VG_IOT01A/develop/GCC_ARM`
     as the output directory name. We match the path Mbed CLI 2 would use, so
     we don't need to manually move around the `mbed-tool configure` output
     `mbed_config.cmake`.
   - `-GNinja`: To use the Ninja build tool. You can tell CMake to use another
     build tool using any [CMake
     Generator](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html)
     your version of CMake supports. We like to use Ninja because it is fast.

1. Build:

   ```
   cmake --build cmake_build/DISCO_L475VG_IOT01A/develop/GCC_ARM
   ```

   Alternatively, if you are using the Ninja build tool (`-GNinja in the
   previous step`) and which to run it yourself, which you may want to do if
   you'd like to limit the number of jobs ninja uses (`ninja -j 1`) or pass
   other custom options (`ninja --help`)

   ```
   ninja -C cmake_build/DISCO_L475VG_IOT01A/develop/GCC_ARM
   ```

   The build generates two files in the build output directory
   (`cmake_build/DISCO_L475VG_IOT01A/develop/GCC_ARM` in this example): HEX and
   BIN.

   Which format you flash to your device depends on your requirements. For
   example, use the BIN file if you want to completely replace the contents of
   the flash device. If you want to retain some of the flash devices contents,
   you'll need to flash to an address other than the flash's starting address,
   so you'll need to use the HEX file (which contains the starting address).
   Note that we assume your board is running DAPLink for flash programming. If
   you are using another tool, please check your tool's documentation for file
   type support.

1. Drag and drop the generated file to your board.

### Building for multiple targets

You can build an Mbed project for multiple targets, with different profiles and toolchains, without affecting other builds. The `compile` subcommand will create and build into a different subdirectory for each combination:

```
cmake_build/<target>/<profile>/<toolchain>/
```

## Iterative builds on configured projects

If you have already made a build for the Mbed target and toolchain that you're using, `compile` will perform an iterative build.

To force a rebuild of the project for a target and toolchain, include the --clean argument:

```
mbed-tools compile -m <target> -t <toolchain> --clean
```

## Flashing the built program

You can flash the built program to the connected target by adding the -f/--flash argument to the compile command:

```
mbed-tools compile -m <target> -t <toolchain> -f
```

## Opening a serial terminal

You can open a serial terminal to the connected target by adding the `--sterm` argument to the compile command:

```
mbed-tools compile -m K64F -t GCC_ARM --sterm --baudrate 9600
```

When the terminal is running you can enter CTRL+H to show the help menu.

## Logging

To specify the log level, use the verbose logging option (`-v`) before the first argument:

- If you don't use `-v`, the log will show only errors.
- `-v`: Warning and errors.
- `-vv`: Information, warning and errors.
- `-vvv`: Debug, information, warning and errors.

For example:

```
mbed-tools -vv configure -m <target> -t <toolchain>
```
