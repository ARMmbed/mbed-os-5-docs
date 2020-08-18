# New tools - draft

<!--this currently duplicates the intro in the general Tools Intro page-->

Starting with version 6.x, Mbed OS is moving from Mbed CLI to a new build tool: <!--that has no proper name yet-->. It uses Ninja as a build system, and CMake to generate the build environment and manage the build process in a compiler-independent manner. <!--need better phrasing-->

Mbed Tools parses the Mbed OS build configuration and outputs it to a format CMake can read. It also provides a use friendly interface to CMake and Ninja so you can configure, generte and execute builds with a single command.


<span class="notes">**Note:** You'll still need Mbed CLI for older versions of Mbed OS (6.x and older). You can install both tools side by side.</span>

# Install or upgrade

Mbed Tools is a Python package called `mbed-tools`, so you can install it with pip.
<!--other than being a super vague name, it's a problem that it's a single tool with a plural name. "Mbed Tools is"  just parses as an error!-->

<span class="tips">**Tip:** We recommend using a virtual environment to avoid any Python dependency conflicts. We recommend the [Pipenv](https://github.com/pypa/pipenv/blob/master/README.md) tool to manage your virtual development environment.

## Prerequisite

- Python 3. Install for [Windows](https://docs.python.org/3/using/windows.html), [Linux](https://docs.python.org/3/using/unix.html) or [macOS](https://docs.python.org/3/using/mac.html).
- Pip (if not included in your Python installation). [Install for all operating systems](https://pip.pypa.io/en/stable/installing/).
- CMake. [Install version 3.18.1 or newer for all operating systems](https://cmake.org/install/).
- Ninja [Install version 1.0 or newer for all operating systems](https://github.com/ninja-build/ninja/wiki/Pre-built-Ninja-packages).
<!--are there versions for cmake and ninja?-->

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

Use pip to upgrade:

```
python -m pip install mbed-tools --upgrade
```

# Use

To get help for a specific command, use `mbed-tools <command> --help`. For example, for helping with listing connected devices (the `devices` command):

```
mbed-tools devices --help
```

## Create a new project

To create a new Mbed OS project in a specified path:

- To create the project and download a new copy of Mbed OS (latest official release):

    ```
    mbed-tools init <PATH>
    ```

- To create a project without downloading a copy of Mbed OS (reuse an existing copy):

    ```
    mbed-tools init -c <PATH>
    ```

    <!--so how do I tell it where the existing copy is? In Mbed Studio you have to explicitly "tell it" where the local copy is-->

## List connected devices

To list devices connected over USB:

```
mbed-tools devices
```

<!--why? what do I do with this info? is this for the config?-->

## Set environment variables

<!--like what? when? why? should this be with installation instructions?-->

To override default environment variables:

```
mbed-tools env
```

## Configure Mbed OS

<!--I don't understand what this actually does. Does it generate a config file? why do I need to do this? what does "for use with" mean - do I use Mbed Tools with the target and toolchain, or am I configuring Mbed OS itself? Do I always have to do this before I build, or can I do it at the same time as the build, or can I just skip it sometimes?-->

To prepare the Mbed configuration information for use with a specific target and toolchain:

```
mbed-tools configure -m <target> -t <toolchain>
```

Currently the supported targets are `K64F`, `DISCO_L475VG_IOT01A`, `NRF52840_DK`

<!--just for configuring, or can you only build with those?-->

## Build using CMake

After preparing the Mbed configuration information, you can use CMake to build your application:<!--can, but don't have to? what are the other options?-->

```console
cmake -S . -B cmake_build -GNinja -DCMAKE_BUILD_TYPE=<profile>
cmake --build cmake_build
```
<!--what are all the other parameters?-->
<!--what does the first command do, and what does the second one do?-->
- We recommend using a dedicated **cmake_build** folder to keep things organised.<!--so do I replace cmake_build with a new value?-->
- The `profile` value can be `release`, `debug` or `develop`.<!--same as normal, or something specific to CMake? https://os.mbed.com/docs/mbed-os/v6.2/program-setup/build-profiles-and-rules.html-->

<!--what does this generate and where? is this where we add instructions for flashing the board?-->

## Example applications

<!--can I create a new one or do I have to use an example? I'm asking because these were listed as part of the build instructions file, I think-->

- [mbed-os-example-blinky](https://github.com/ARMmbed/mbed-os-example-blinky)
- [mbed-os-example-ble/BLE_Button](https://github.com/ARMmbed/mbed-os-example-ble/tree/master/BLE_Button)
- [mbed-os-example-cellular](https://github.com/ARMmbed/mbed-os-example-cellular)
- [mbed-os-example-devicekey](https://github.com/ARMmbed/mbed-os-example-devicekey)
- [mbed-os-example-kvstore](https://github.com/ARMmbed/mbed-os-example-kvstore)
- [mbed-os-example-lorawan](https://github.com/ARMmbed/mbed-os-example-lorawan)
- [mbed-os-example-mbed-crypto](https://github.com/ARMmbed/mbed-os-example-mbed-crypto)
- [mbed-os-example-nfc](https://github.com/ARMmbed/mbed-os-example-nfc)
- [mbed-os-example-sockets](https://github.com/ARMmbed/mbed-os-example-sockets)
