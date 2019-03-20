## Arm Mbed tools

The Arm Mbed OS ecosystem includes many tools designed to work with Mbed OS and projects that use Mbed OS throughout the development process. With our development tools, Arm Mbed Studio, Arm Mbed CLI and the Arm Mbed Online Compiler, you can create, import and build projects. You can compile with any of our supported toolchains and debug with the many IDEs we support. DAPLink and pyOCD let you program and debug your many devices. For validation of your project, you can test your code with Greentea, `htrun` and utest. This section covers all of these tools related to Mbed OS.

#### Development tool options

The three Mbed OS development tools are Mbed Studio, Mbed CLI and the Mbed Online Compiler. All of the development tools perform the same process:

- Bring the Mbed OS source code from GitHub or `mbed.com`, along with all dependencies.
- Compile your code with Mbed OS for a target, so you have a single file to flash to your board.

We developed Mbed OS 5 using the Mbed CLI tool, which is a Python program that coordinates builds and fetches all the dependencies of an Mbed OS application. As this runs on your local development machine, you also need compilers and other build tools installed.

`os.mbed.com` provides the tools, libraries and programs that work with Mbed OS 5, so you can also use Mbed Studio or the Mbed Online Compiler for building Mbed OS 5 examples and programs. Beginning developers or those who are not comfortable with the command-line may prefer Mbed Studio or the Online Compiler. Furthermore, you can use the exporters to third party development tools that were part of the Arm Mbed OS 2 ecosystem.

##### Arm Mbed CLI

We created the Mbed command-line tool (Mbed CLI), a Python-based tool, specifically for Mbed OS 5. For more information, see the [Mbed CLI page](../tools/developing-mbed-cli.html).

##### Compiler versions

Mbed OS 5 can be built with various toolchains. The currently supported versions are:

- [Arm Compiler 6.11 (default ARM toolchain)](https://developer.arm.com/products/software-development-tools/compilers/arm-compiler/downloads/version-6), also included in [Keil MDK 5.27](http://www2.keil.com/mdk5/).
- [Arm Compiler 5.06 update 6 (to be deprecated in the future)](https://developer.arm.com/products/software-development-tools/compilers/arm-compiler-5/downloads).
- [GNU Arm Embedded version  6 (6-2017-q1-update)](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads).
- [IAR Embedded Workbench 8.32.1](https://www.iar.com/iar-embedded-workbench/tools-for-arm/arm-cortex-m-edition/).

##### Arm Mbed Studio

Mbed Studio is our new in-house desktop IDE. Mbed Studio is now available to anyone with an Mbed account as a public beta. You can download it for Windows and Mac, and access the documentation at [os.mbed.com/studio](https://os.mbed.com/studio).

Mbed Studio is designed to speed up your development flow and provide functionality that helps you to get the most out of Mbed OS. To complement our popular Online Compiler and command line tools we want to give you the tooling you need in a desktop IDE to have a quick development, debug and deploy cycle when you build your next product.

##### Arm Mbed Online Compiler

The Mbed Online Compiler is our in-house IDE and should be familiar to anyone who's been working with Mbed for a while. It switches the backing toolchain based on the architecture version:

| Architecture version | Compiler |
|----                  |----           |
| Arm v6M       | `Arm Compiler 6.11` or `Arm Compiler 5.06 update 6` based on the ARM toolchain supported by the target (see `supported_toolchains` in [Adding and configuring targets](../reference/adding-and-configuring-targets.html)) |
| Arm v7M       | `Arm Compiler 6.11` or `Arm Compiler 5.06 update 6` based on the ARM toolchain supported by the target (see `supported_toolchains` in [Adding and configuring targets](../reference/adding-and-configuring-targets.html)) |
| Arm v7A       | `Arm Compiler 6.11` |
| Arm v8M       | `Arm Compiler 6.11` |

For more information, please see the [Online Compiler page](developing-mbed-online-compiler.html).

<span class="note"> **Note:** Arm Compiler 6 is the default ARM toolchain for Mbed OS development. Most Mbed OS platforms are already compatible with Arm Compiler 6. Some existing targets still supporting Arm Compiler 5 will also be migrated to ARM Compiler 6 in the future. Please be aware that you must use Arm Compiler 6 for future development, and we will validate all code contributions to Mbed OS with Arm Compiler 6. </span>

##### Third party development tools

You can export your project from any of our tools to third party tools. For instructions, as well as tool-specific information, see the [Exporting to third party toolchains page](exporting.html).

<div style="background-color:#F3F3F3; text-align:left; vertical-align: middle; padding:15px 30px;"> Note: We encourage you to switch to Arm Compiler 6 soon because we will deprecate Arm Compiler 5 support in the future. However, if you need to update to Mbed OS 5.12 but still require compiling with Arm Compiler 5 until you are in possession of Arm Compiler 6, we provide methods to override the Arm toolchain version. If you do this, your target may not be able to compile with Arm Compiler 5, or you may see undefined behaviors.

To force Arm Compiler 5, you can use the following options:

- Create or update your `mbed_app.json` as below. This is the recommended method for applications to use Arm Compiler 5.

```
{
  "target_overrides": {
      "*": {
          "target.supported_toolchains": ["ARMC5", "GCC_ARM", "IAR"]
      }
  }
}
```

- For porting a target that cannot use Arm Compiler 6 at this time, modify the `supported_toolchains` entry in `targets.json` to replace all `ARM` and `ARMC6` entries with `ARMC5`:  

```
"MY_TARGET_NAME": {
        "supported_form_factors": [...],
        "core": "Cortex-M4",
        "supported_toolchains": ["ARMC5", "GCC_ARM", "IAR"],
        ...
}
```
</div> 
