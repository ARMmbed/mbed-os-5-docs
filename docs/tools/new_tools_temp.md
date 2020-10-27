# New tools - draft

<!--this currently duplicates the intro in the general Tools Intro page-->

Starting with version 6.x, Mbed OS is moving from Mbed CLI to a new build tool: <!--that has no proper name yet-->. It uses Ninja as a build system, and CMake to generate the build environment and manage the build process in a compiler-independent manner. <!--need better phrasing-->

Mbed Tools parses the Mbed OS build configuration and outputs it to a format CMake can read. It also provides a user friendly interface to CMake and Ninja so you can configure, generate and execute builds with a single command.

<span class="notes">**Note:** You'll still need Mbed CLI for older versions of Mbed OS (6.x and older). You can install both tools side by side.</span>

# Install or upgrade

Mbed Tools is a Python package called `mbed-tools`, so you can install it with pip.
<!--other than being a super vague name, it's a problem that it's a single tool with a plural name. "Mbed Tools is"  just parses as an error!-->

<span class="tips">**Tip:** We recommend using a virtual environment to avoid any Python dependency conflicts. We recommend the [Pipenv](https://github.com/pypa/pipenv/blob/master/README.md) tool to manage your virtual development environment.

## Prerequisite

- Python 3.6 or newer. Install for [Windows](https://docs.python.org/3/using/windows.html), [Linux](https://docs.python.org/3/using/unix.html) or [macOS](https://docs.python.org/3/using/mac.html).
- Pip (if not included in your Python installation). [Install for all operating systems](https://pip.pypa.io/en/stable/installing/).
- CMake. [Install version 3.18.1 or newer for all operating systems](https://cmake.org/install/).
- Ninja. [Install version 1.0 or newer for all operating systems](https://github.com/ninja-build/ninja/wiki/Pre-built-Ninja-packages).
- One of the support toolchains listed [in the build tools overview](../build-tools/index.html).

## Install

Use pip to install:

- To install the latest release:

    ```
    python -m pip install mbed-tools
    ```

- To install a specific version:

    ```
    python -m pip install mbed-tools==<version number in major.minor.patch format>
    ```

- To install a pre-release or development version:

    ```
    python -m pip install mbed-tools --pre
    ```

## Upgrade

Use pip to upgrade your version:

```
python -m pip install mbed-tools --upgrade
```

# Use

Currently, the new Mbed Tools supports three boards: `K64F`, `DISCO_L475VG_IOT01A` and `NRF52840_DK`.

For help:

- To get help for all commands, use:

    ```
    mbed-tools --help
    ```

- To get help for a specific command, use `mbed-tools <command> --help`. For example, for helping with listing connected devices (the `devices` command):

    ```
    mbed-tools devices --help
    ```

## Create a project

You can create a new project or create a local copy of one of our example applications.

### Create a new project

To create a new Mbed OS project in a specified path:

- To create the project and download a new copy of Mbed OS (latest official release):

    ```
    mbed-tools init <PATH>
    ```

    The path can be:
    - Absolute. `init` will create the folder if it doesn't exist.
    - Relative:

        If you have already created a project folder, you can use `.`

        If you want the `init` command to create a project folder, use `.\<folder-name>`.

### Use an example application

To create a local copy of an example application, use the `clone` command with the example name listed below:

```
mbed-tools clone <example> <PATH>
````

- [mbed-os-example-blinky](https://github.com/ARMmbed/mbed-os-example-blinky)
- [mbed-os-example-ble](https://github.com/ARMmbed/mbed-os-example-ble) - use the BLE LED example.
- [mbed-os-example-cellular](https://github.com/ARMmbed/mbed-os-example-cellular)
- [mbed-os-example-devicekey](https://github.com/ARMmbed/mbed-os-example-devicekey)
- [mbed-os-example-kvstore](https://github.com/ARMmbed/mbed-os-example-kvstore)
- [mbed-os-example-lorawan](https://github.com/ARMmbed/mbed-os-example-lorawan)
- [mbed-os-example-mbed-crypto](https://github.com/ARMmbed/mbed-os-example-mbed-crypto)
- [mbed-os-example-nfc](https://github.com/ARMmbed/mbed-os-example-nfc)
- [mbed-os-example-sockets](https://github.com/ARMmbed/mbed-os-example-sockets)


## Configure the project

Each project depends on two sets of configurations:

- The project's environment variables. You can use the default values.
- The Mbed OS configuration system. You must set up your target and toolchain.

### (Optional) Project environment variables

Mbed Tools has two environment variables that you can set for a project:

- `MBED_API_AUTH_TOKEN`: Token to access private board information stored for a vendor team.
- `MBED_DATABASE_MODE`: Use online or offline mode. Possible values:
    - `AUTO`: Search the offline database first; search the online database only if the board wasn't found offline. This is the default value.
    - `ONLINE`: Alway use the online database.
    - `OFFLINE`: Always use the offline database.

These variables can be set either directly via environment variables
or using a `.env` file containing the variable definitions as follows:

```
VARIABLE1=<value>
VARIABLE2=<value>
```

Environment variables take precedence, meaning the values set in the file will be overriden
by any values previously set in your environment.

**Warning**:
Do not upload `.env` files containing private tokens to version control.
If you use this package as a dependency of your project, please ensure to include the
`.env` in your `.gitignore`.

### Mbed OS configuration

The Mbed OS configuration system parses the configuration files in your project (mbed_lib.json, mbed_app.json and targets.json) for a particular target and toolchain, and outputs a CMake script. The build system uses this script to build for your target, using your toolchain.

<span class="tips">**Tip:** If you're rebuilding for the same target and toolchain, you can keep using the same CMake script, so you won't have to use the `configure` command again for each build. If you change any of mbed_lib.json, mbed_app.json, targets.json, your target or your toolchain, run the `configure` command again to generate a new CMake script.</span>

1. Check your board's build target name.

    Connect your board over USB and run the `devices` command:

    ```
    mbed-tools devices

    Board name    Serial number             Serial port             Mount point(s)    Build target(s)
    ------------  ------------------------  ----------------------  ----------------  -----------------
    FRDM-K64F     024002017BD34E0F862DB3B7  /dev/tty.usbmodem14402  /Volumes/MBED     K64F
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
    mbed_config.cmake has been generated and written to '/Users/UserName/Development/Blinky/.mbedbuild'
    ```

## Build the project

Use CMake to build your application:

1. Navigate to the project's root folder.
1. Set the build parameters:

    ```
    cmake -S . -B cmake_build -GNinja -DCMAKE_BUILD_TYPE=<profile>
    ```
    - `-S <path-to-source>`: Path to the root directory of the CMake project. We use `.` to indicate we're building from the current directory.
    - `-B <path-to-build>`: Path to the build output directory. If the directory doesn't already exist, CMake will create it. We use `cmake_build` as the output directory name; you can use a different name.
    - `-GNinja`: To use the Ninja tool.
    - `-DCMAKE_BUILD_TYPE`: Build type. The value (`profile`) can be `release`, `debug` or `develop`, as [explained in program setup](../program-setup/build-profiles-and-rules.html).

1. Build:

    ```
    cmake --build cmake_build
    ```

    This generates two files in the build output directory (`cmake_build` in this example): HEX and BIN.

    Which format you flash to your device depends on your requirements. For example, use the BIN file if you want to completely replace the contents of the flash device. If you want to retain some of the flash devices contents, you'll need to flash to an address other than the flash's starting address, so you'll need to use the HEX file (which contains the starting address). Note that we assume your board is running DAPLink for flash programming. If you are using another tool, please check your tool's documentation for file type support.

1. Drag and drop the generated file to your board.


## Mbed OS Configuration and building the project

We can use a single command which will configure (set up your target and toolchain) and build the project.

1. To build and configure:

    ```
    mbed-tools build -m <target> -t <toolchain>
    ```
    - -t: The toolchain you are using to build your app
    - -m: A build target for an Mbed-enabled device

    Example for FRDM-K64F and GCC:

    ```
    mbed-tools build -m K64F -t GCC_ARM
    ```

1. To perform an iterative build on previously configured target:

    ```
    mbed-tools build
    ```


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
