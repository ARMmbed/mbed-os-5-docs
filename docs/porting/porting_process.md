# Porting to mbed OS 5.0

This section provides detailed information on porting process your board to mbed OS 5.0.

We recommend getting familiar with Git and branching. If you are not too sure, see [here](http://learngitbranching.js.org/).

## Getting ready to port

### Setting up your environment


mbed OS 5.0 supports the following compiler versions:

- GCC ARM Embedded – 4.9.3
- ARM Compiler 5/ARMCC (as used by Keil MDK) – uVision 5.20, ARM Compiler 5.06 update 1,2,3
- ICCARM used in IAR Workbench – IAR Embedded Workbench for ARM V7.60.2.11341

For development you will need:

- [Python 2.7.11](https://www.python.org/downloads/release/python-2711/). You'll need Python on your machine to install mbed CLI and the other prerequisites to make much further progress. For more information, see the [Quick guide to mbed CLI page](Docs/Build_Tools/CLI.md).
- [pip 0.8.0](https://pypi.python.org/pypi/pip)
- GCC ARM Embedded Compiler:
  - [Mac OS X and Windows Installer](https://launchpad.net/gcc-arm-embedded/4.9).
  - Ubuntu Linux 14.04:

        sudo apt-get remove binutils-arm-none-eabi gcc-arm-none-eabi
        sudo apt-get autoremove
        sudo add-apt-repository ppa:terry.guo/gcc-arm-embedded
        sudo apt-get update
        sudo apt-get install gcc-arm-none-eabi=4.9.3.2015q3-1trusty1

- [Keil MDK-ARM](http://www.keil.com/download/product/) - optional.
- [IAR for ARM](https://www.iar.com/iar-embedded-workbench/#!?architecture=ARM) - optional.
- [Git](https://git-scm.com/downloads). After installing Git, you should configure it to use the credential store as explained [here](https://help.github.com/articles/caching-your-github-password-in-git/). This will give you easy access to our private repos.

- [mbed CLI](https://github.com/ARMmbed/mbed-cli) - our tool for delivering mbed OS, invoking code compilation, testing and exporting to desktop tools. 

	You can install it using the following command:

        sudo pip install mbed-cli

	Once installed, it can be invoked using the commands `mbed` or `mbed-cli`.


To verify your installations, check each component's version:

| Command                    | Correct version    |
|----------------------------|--------------------|
| git --version              | > 2.0              |
| hg --version               | > 3.0              |
| python --version           | 2.7.11             |
| pip --version              | > 8.0              |
| mbed --version             | > 0.8.0            |
| arm-non-eabi-gcc --version | > 4.9 series < 5.0 |


### Fetching the source to start porting

To get the full mbed OS source:

``` bash
cd /wherever/you/do/development
mbed new porting #mbed is an alias for the mbed-cli tool
cd porting
```

These steps create a directory called "porting" and fetch the full mbed OS code base to that directory. We need to call mbed CLI from within our project directory, so we use `cd` to enter it.

We're now ready to start working on our project.

Please check out the EPR release branch:

```bash
cd mbed-os
mbed update mbed-os-5.0.1-epr
```

And finally, install all Python development requirements:

```bash
pip install -r core/requirements.txt
```

To verify this all worked:

- On Windows:  `type core.lib`
- On Unix: `cat core.lib`

For both, the result should be `https://github.com/mbedmicro/mbed#ce830296d0297a8da543c24134bf859710fd7698`

**Warning:** Do not edit this by hand if you get a different result!

### Replacing the default mbed library with your development version

mbed OS includes a reference to a 'core' library, which is the mbed SDK (mbed drivers, hardware abstraction, and target implementations).   

It isn't practical to make all our changes on the mainline `mbedmicro/mbed` repository, so we need to make a fork of this repository and point our local mbed OS porting project at this development fork.

Because `core` is a dependency of `mbed-os` (via the `core.lib` link inside mbed-os), you also need to change that `.lib` file:

1. Remove the existing dependency on the `core` repository:

        mbed remove core

1. Add a dependency on your fork of the mbed repository:

        mbed add https://github.com/<developername>/mbed core
    
Now your local copy of `mbed-os` is pointing to your clone of the `core` repository and you are ready to start porting.

You will need to contact your ARM mbed partner lead to get a branch created in mbed-os against which you can make these pull requests. This will enable system-wide CI and testing.

### Building the tests for the first time on a known-good platform

When porting, the most common task is to build the full mbed OS test suite and run the tests to verify your port. So even before you start porting, it's a good idea to run the tests to make sure you're correctly set up for that.

Start by building for a known-good platform. If you have a platform that you know works well on developer.mbed.org, then you can build for it. If not, we recommend you try the FRDM-K64F.

You can list all the supported platforms by adding the `--supported` option to the `mbed compile` command. Note that this will not actually run the compilation, just report a table of possible combinations of boards (`-m`) and toolchains (`-t`):

```bash
mbed compile --supported
```

When you've chosen a supported combination of target and toolchain, run the mbed test command. By default, running `mbed test` will build *and* attempt to run the tests:

```bash
mbed test -m K64F -t GCC_ARM
```

You can add the `--compile` command to indicate that you do not want to run the tests. Likewise, the `--run` command tells the tool to only run the tests (and not recompile).

#### Setting the chosen target and toolchain as default

By running the following commands you can set the default target and toolchain for mbed CLI commands:

```bash
mbed target <YOUR_TARGET>
mbed toolchain <YOUR_TOOLCHAIN>
```
Now you can just run `mbed` commands without explicitly specifying the `–m` and `–t` arguments.

**Note:** These parameters are saved for each project, so you don't need to reset them every time you restart mbed CLI or change projects.

#### Running just one test

There are many tests and they take a long time to run. If you’d like to run just a single test (for example, to quickly prove the sanity of your environment):

```bash
mbed test --run -n mbed-os-tests-integration-threaded_blinky
```

## Building and testing for a new target

Once you have verified that you can run the tests on your platform for a known-good board, you are ready to start porting to a new target, as explained below. Then see the [Greentea page](../Testing/Porting.md) for instructions for creating and running tests.


# mbed OS 5.0 Porting Guide

To port mbed OS 5.0 to your device, you need to:

1. [Port the OS core](Core_port.md). The easiest way to port is to [copy definitions from another device](#copying-from-an-existing-device). If you cannot find a suitable source to copy from, you'll have to do a [full port](#porting-from-scratch).
1. Port the [security modules](#security-releated-porting).
1. Port the [connectivity modules](#connectivity-related-porting) your hardware needs.

Please use the [mbed CLI](../Build_Tools/CLI.md) build system and [test as you work](../Testing/Porting.md).


## Porting option 1: copying from an existing device

The process for porting a new device from an existing one:

1. **Derivative target definitions:** your source device provides a set of definitions that form an mbed OS target. You may have to edit some of them to match your own device.
1. **Peripheral configuration:** edit definitions for pin names, external xtal and so on.
1. [Use Greentea to test](../Testing/Porting.md) your port.

## Porting option 2: from scratch

If there is no device to copy from, you'll have to do a [full port](Core_port.md):

1. Port [CMSIS-CORE](CMSIS_CORE.md).
1. Port [mbed HAL](HAL.md).
1. Port [mbed RTOS](RTOS.md) (based on CMSIS-RTOS standard).
1. [Use Greentea to test](../Testing/Porting.md) your CMSIS, HAL and RTOS ports.

The full process is [here](Core_port.md).

## Security related porting

When you have the mbed OS core working, port the security modules:

- [uVisor](../uVisor/Porting.md).
- [mbed TLS](../TLS/Porting.md).

## Connectivity related porting

Depending on what your hardware offers, port one or more of the connectivity modules:

- [BLE](../Connect/BLE.md).
- Ethernet and WiFi through the [Network Socket API](../Connect/Network_Socket.md).
- [15.4 for 6LoWPAN/Thread](../Connect/15_4.md).


## Testing your port

See the [Greentea page](../Testing/Porting.md) for more information.



## Further reading

[TODO: replace all links]

- [mbed CLI](https://github.com/ARMmbed/mbed-cli).
- [DAPLink Interface Firmware](https://github.com/mbedmicro/DAPLink).
- [Greentea and HTrun](https://github.com/ARMmbed/EPR-Getting-Started/blob/master/Docs/Testing/Porting.md).
- [Project Generator](https://github.com/project-generator/project_generator/wiki).

