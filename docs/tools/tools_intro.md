# Arm Mbed tools

The Arm Mbed OS ecosystem includes many tools designed to work with Mbed OS and projects that use Mbed OS throughout the development process. With our development tools, Arm Mbed Studio, Arm Mbed CLI and the Arm Mbed Online Compiler, you can create, import and build projects. You can compile with any of our supported toolchains and debug with the many IDEs we support. DAPLink and pyOCD let you program and debug your many devices. For validation of your project, you can test your code with Greentea, `htrun` and utest. This section covers all of these tools related to Mbed OS.

## Development tool options

The three Mbed OS development tools are Mbed Studio, Mbed CLI and the Mbed Online Compiler. All of the development tools perform the same process:

- Bring the Mbed OS source code from GitHub or `mbed.com`, along with all dependencies.
- Compile your code with Mbed OS for a target, so you have a single file to flash to your board.

We developed Mbed OS using the Mbed CLI tool, which is a Python program that coordinates builds and fetches all the dependencies of an Mbed OS application. As this runs on your local development machine, you also need compilers and other build tools installed.

`os.mbed.com` provides the tools, libraries and programs that work with Mbed OS, so you can also use Mbed Studio or the Mbed Online Compiler for building Mbed OS examples and programs. Beginner developers or those who are not comfortable with the command-line may prefer Mbed Studio or the Online Compiler.

## Arm Mbed Online Compiler

The Mbed Online Compiler is our in-house IDE and should be familiar to anyone who's been working with Mbed for a while. It uses the Arm Compiler 6.

For more information, please see the [Online Compiler page](../build-tools/mbed-online-compiler.html).

## Command line tools

Mbed OS has two versions of its command line tool:

- For 6.5 and newer, use Mbed CLI 1 or Mbed CLI 2.
- For 6.4 and older, use Mbed CLI 1.

You can have both tools installed side by side, so you can work with multiple versions of Mbed OS.

### Mbed CLI 2 - Mbed OS 6.5 and newer

Starting with version 6.5, Mbed OS is moving to Mbed CLI 2. It uses Ninja as a build system, and CMake to generate the build environment and manage the build process in a compiler-independent manner.

Mbed CLI 2 parses the Mbed OS build configuration and outputs it to a format CMake can read. It also provides a user friendly interface to CMake and Ninja so you can configure, generate and execute builds with a single command.

For more information, see the [Mbed CLI 2 page](../build-tools/mbed-cli-2.html).

<span class="notes">**Note:** You'll still need Mbed CLI 1 for older versions of Mbed OS (6.4 and older). You can install both tools side by side.</span>

### Mbed CLI 1 - Mbed OS 6.4 and older

A Python-based tool, specifically for Mbed OS. For more information, see the [Mbed CLI 1 page](../build-tools/mbed-cli-1.html).

### Compiler versions

You can build Mbed OS with the Arm Compiler and GNU Arm Embedded toolchains. The currently supported versions are:

| Compiler| Download location | Name in Mbed CLI |
| --- | --- | --- |
| Arm Compiler 6.16 (default ARM toolchain) | - A paid version is available as [Arm Compiler 6.16 Professional](https://developer.arm.com/products/software-development-tools/compilers/arm-compiler/downloads/version-6). </br> - A paid version is also included in [Keil MDK 5.34](https://www.keil.com/update/relnotes/MDK534.htm) | `ARM` |
| GNU Arm Embedded version 10 (10.3-2021.07) | [GNU Arm Embedded version 10 (10.3-2021.07)](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads) | `GCC_ARM` |

<span class="notes">**Note**: Mbed OS 6 does not support Arm Compiler 5, IAR or uARM.</span>

## Arm Mbed Studio

Mbed Studio is our new desktop IDE and is available to anyone with an Mbed account. You can [download it for Windows, Linux and Mac](https://os.mbed.com/docs/mbed-studio/current/installing/index.html), and access the documentation at [os.mbed.com/docs/mbed-studio](https://os.mbed.com/docs/mbed-studio/).

To complement our popular Mbed Online Compiler and command-line tools, we created Mbed Studio, the tooling you need in a desktop IDE to have a quick development, debug and deploy cycle when you build your next product. Mbed Studio speeds up your development flow and provides functionality that helps you get the most out of Mbed OS.

## Exporting to third party development tools

You can export your project from any of our tools to third party tools. For instructions, as well as tool-specific information, see the [Exporting to third party toolchains page](../build-tools/third-party-build-tools.html).
