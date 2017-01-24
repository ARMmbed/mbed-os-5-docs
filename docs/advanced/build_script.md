# mbed OS build script environment
## Introduction
mbed test framework allows users to test their mbed devices’ applications, build mbed OS library, rerun tests, run mbed OS regression, add new tests and receive all the results automatically. Everything occurs on your machine, so you have full control over compilation and the tests you run.

It uses Python 2.7 programming language to drive all tests, so make sure to install Python 2.7 and include it in your system PATH. To compile mbed OS and tests, you will need one or more supported compilers installed on your system.

To follow this introduction, you should:
* Know what mbed OS is in general.
* Know how to install Python 2.7 and ARM target cross compilers.
* Have C/C++ programming experience and be willing to learn a bit about Python. 

## Test automation
Our test framework allows users to run tests on their machines (hosts) in a fully automated manner. All you need to do is prepare two configuration files.

## Test automation limitations
Note that for tests that require connected external peripherals, such as Ethernet, SD flash cards, external EEPROM tests and loops, you need to:

* Modify test source code to match components' pin names to actual mbed board pins where peripheral is connected or
* Wire your board the same way test defines it.

## Prerequisites
mbed test suite and build scripts are Python 2.7 applications and require Python 2.7 runtime environment and [setuptools](https://pythonhosted.org/an_example_pypi_project/setuptools.html) to install dependencies.

You need:
* Installed [Python 2.7](https://www.python.org/download/releases/2.7) programming language.
* Installed [setuptools](https://pythonhosted.org/an_example_pypi_project/setuptools.html#installing-setuptools-and-easy-install).
* Optionally, you can install [pip](https://pip.pypa.io/en/latest/installing.html), which is the PyPA recommended tool for installing Python packages from the command-line.

mbed OS in its repo root directory specifies `setup.py` file, which holds information about all packages that are dependencies for it. Installing all dependencies requires a few steps.

First, clone the mbed OS repo and go to the mbed OS repo's directory:
```
$ git clone https://github.com/mbedmicro/mbed.git
$ cd mbed
```

Second, invoke `setup.py`, so `setuptools` can install mbed OS's dependencies (external Python modules required by mbed OS):
```
$ python setup.py install
```
or 
```
$ sudo python setup.py install
```
when your system requires administrator rights to install new Python packages.

### Manual Python package dependency installation
In case you do not want to install the entire mbed package using `setuptools`, you can use the `requirements.txt` file and with the help of `pip` package manager, you can install only mbed's Python package dependencies:
```
$ pip install -r requirements.txt
```
## Prerequisites (manual Python package dependency installation)
**Please only read this chapter if you have problems installing mbed OS dependencies to Python packages**.

Below, you can find the list of mbed OS dependencies to Python modules with instructions about how to install them manually.

You can skip this part if you already installed [Python 2.7](https://www.python.org/download/releases/2.7) and [setuptools](https://pythonhosted.org/an_example_pypi_project/setuptools.html) and successfully [installed all dependencies](#prerequisites).

* Please make sure you've installed [pip](https://pip.pypa.io/en/latest/installing.html) or [easy_install](https://pythonhosted.org/setuptools/easy_install.html#installing-easy-install).
Note: Easy Install is a python module (easy_install) bundled with [setuptools](https://pythonhosted.org/an_example_pypi_project/setuptools.html#installing-setuptools-and-easy-install) that lets you automatically download, build, install and manage Python packages.

* Installed [pySerial](https://pypi.python.org/pypi/pyserial) module for Python 2.7.
You can install pySerial from PyPI, either by manually downloading the files and installing as described below or using:
```
$ pip install pyserial
```
or:
```
easy_install -U pyserial
```
* Installed [prettytable](https://code.google.com/p/prettytable/wiki/Installation) module for Python 2.7.
You can install prettytable from PyPI, either by manually downloading the files and installing as described below or using:
```
$ pip install prettytable
```
* Installed [IntelHex](https://pypi.python.org/pypi/IntelHex) module.
You can download IntelHex from https://launchpad.net/intelhex/+download or http://www.bialix.com/intelhex/.
If Python is properly installed on your platform, installation only requires running the following command from the root directory of the archive:
```
sudo python setup.py install
```
This will install the intelhex package into your system’s site-packages directory. After that is done, any other Python scripts or modules should be able to import the package using:
```
$ python
Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from intelhex import IntelHex
>>>
```
* You can check if you have correctly installed the above modules (or you already have them) by starting Python and importing both modules.
```
$ python
Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import serial
>>> import prettytable
>>> from intelhex import IntelHex
>>>
```
* Installed Git open source distributed version control system.
* Installed at least one of the supported by mbed OS workspace tools compilers: 

Compiler               | mbed OS Abbreviation  | Example Version
-----------------------|-----------------------|-----------
Keil ARM Compiler      | ARM, uARM             | ARM C/C++ Compiler, 5.03 [Build 117]
GCC ARM                | GCC_ARM               | gcc version 4.8.3 20131129 (release)
GCC CodeRed            | GCC_CR                | gcc version 4.6.2 20121016 (release)
IAR Embedded Workbench | IAR                   | IAR ANSI C/C++ Compiler V6.70.1.5641/W32 for ARM

* mbed board. You can find a list of supported platforms [here](https://mbed.org/platforms/).

### Getting mbed OS sources with test suite
You have already installed Python (with required modules) and at least one supported compiler you will use with your mbed board. Great!

Now you can get mbed OS with the test suite. Clone the latest mbed OS source code and configure the path to your compiler(s) in next few steps.

* Open console and run command below to clone the mbed OS repository hosted on [Github](https://github.com/mbedmicro/mbed).
```
$ git clone https://github.com/mbedmicro/mbed.git
Cloning into 'mbed'...
remote: Counting objects: 37221, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 37221 (delta 0), reused 0 (delta 0), pack-reused 37218
Receiving objects: 100% (37221/37221), 20.38 MiB | 511.00 KiB/s, done.
Resolving deltas: 100% (24455/24455), done.
Checking connectivity... done.
Checking out files: 100% (3994/3994), done.
```
* Now you can go to the mbed directory you cloned, and you can see the root directory structure of the mbed OS library sources. Type following commands:
```
$ cd mbed
$ ls
LICENSE  MANIFEST.in  README.md  libraries  setup.py  travis  tools
```
Directory structure we are interested in:
```
  mbed/tools/           - test suite scripts, build scripts etc.
  mbed/libraries/tests/           - mbed OS tests,
  mbed/libraries/tests/mbed/      - tests for mbed OS and peripherals tests,
  mbed/libraries/tests/net/echo/  - tests for Ethernet interface,
  mbed/libraries/tests/rtos/mbed/ - tests for RTOS. 
```

### Workspace tools
Workspace tools are a set of Python scripts used off-line by the mbed OS team to:
* Compile and build mbed OS.
* Compile and build libraries included in the mbed OS repo such sa ETH (Ethernet), USB, RTOS and CMSIS.
* Compile, build and run mbed OS tests.
* Run test regression locally and in CI server.
* Get library, target and test configuration (paths, parameters, names etc.).

### Configure workspace tools to work with your compilers
Before you can run your first test, you need to configure your test environment.
Tell the workspace tools where your compilers are.

* Please go to `mbed` directory and create an empty file called `mbed_settings.py`.
```
$ touch mbed_settings.py
```
* Populate this file with the Python code below: 
```python
from os.path import join
 
# ARMCC
ARM_PATH = "C:/Work/toolchains/ARMCompiler_5.03_117_Windows"
ARM_BIN = join(ARM_PATH, "bin")
ARM_INC = join(ARM_PATH, "include")
ARM_LIB = join(ARM_PATH, "lib")
 
ARM_CPPLIB = join(ARM_LIB, "cpplib")
MY_ARM_CLIB = join(ARM_PATH, "lib", "microlib")
 
# GCC ARM
GCC_ARM_PATH = "C:/Work/toolchains/gcc_arm_4_8/4_8_2013q4/bin"
 
# GCC CodeRed
GCC_CR_PATH = "C:/Work/toolchains/LPCXpresso_6.1.4_194/lpcxpresso/tools/bin"
 
# IAR
IAR_PATH = "C:/Work/toolchains/iar_6_5/arm"
 
SERVER_ADDRESS = "127.0.0.1"
LOCALHOST = "127.0.0.1"
 
# This is moved to separate JSON configuration file used by singletest.py
MUTs = {
}
```

Note: You need to provide the absolute path to your compiler(s) installed on your host machine. Replace corresponding variable values with paths to compilers installed in your system:
* `ARM_PATH` for armcc compiler.
* `GCC_ARM_PATH` for GCC ARM compiler.
* `GCC_CR_PATH` for GCC CodeRed compiler.
* `IAR_PATH` for IAR compiler. 

If, for example, you do not use the `IAR` compiler, you do not have to modify anything. Workspace tools will use `IAR_PATH` variable only if you explicitly ask for it from command-line. So do not worry and replace only paths for your installed compilers.

Note: Because this is a Python script and `ARM_PAT`, `GCC_ARM_PATH`, `GCC_CR_PATH` and `IAR_PATH` are Python string variables, please use double backlash or single slash as path's directories delimiter to avoid an incorrect path format. For example:
```python
ARM_PATH = "C:/Work/toolchains/ARMCompiler_5.03_117_Windows"
GCC_ARM_PATH = "C:/Work/toolchains/gcc_arm_4_8/4_8_2013q4/bin"
GCC_CR_PATH = "C:/Work/toolchains/LPCXpresso_6.1.4_194/lpcxpresso/tools/bin"
IAR_PATH = "C:/Work/toolchains/iar_6_5/arm"
```

Note: Settings in `mbed_settings.py` will overwrite variables with default values in `mbed/default_settings.py` file.

## Build mbed OS library from sources
Build mbed OS library offline from sources using your compiler. You have already cloned mbed OS sources; you have also installed compilers and added their paths to `mbed_settings.py`. You are now ready to use workspace tools script `build.py` to compile and build mbed OS from sources.

You are still using console. You should be already in `mbed/tools/` directory. If not, go to `mbed/tools/` and type this command:
```
$ python build.py -m LPC1768 -t ARM
```
or if you want to take advantage of multithreaded compilation, please use option `-j X` where `X` is the number of cores you want to use to compile mbed OS. See below:
```
$ python build.py -m LPC1768 -t ARM -j 4
Building library CMSIS (LPC1768, ARM)
Copy: core_ca9.h
Copy: core_caFunc.h
...
Compile: us_ticker_api.c
Compile: wait_api.c
Library: mbed.ar
Creating archive 'C:\temp\x\mbed\build\mbed\TARGET_LPC1768\TOOLCHAIN_ARM_STD\mbed.ar'
Copy: board.o
Copy: retarget.o

Completed in: (42.58)s

Build successes:
  * ARM::LPC1768
```
This command will build mbed OS for the [LPC1768](http://developer.mbed.org/platforms/mbed-LPC1768/) platform using the ARM compiler.

Look at the directory structure under `mbed/build/`. You can see for `LPC1768`, a new directory `TARGET_LPC1768` was created. This directory contains all build primitives.
Directory `mbed/TARGET_LPC1768/TOOLCHAIN_ARM_STD/` contains the mbed OS library `mbed.ar`. This directory structure also stores all needed headers, which you should use with `mbed.ar` when building your own software.
```
$ tree ./mbed/build/
Folder PATH listing
Volume serial number is 006C006F 6243:3EA9
./MBED/BUILD
+---mbed
    +---.temp
    ¦   +---TARGET_LPC1768
    ¦       +---TOOLCHAIN_ARM_STD
    ¦           +---TARGET_NXP
    ¦               +---TARGET_LPC176X
    ¦                   +---TOOLCHAIN_ARM_STD
    +---TARGET_LPC1768
        +---TARGET_NXP
        ¦   +---TARGET_LPC176X
        ¦       +---TARGET_MBED_LPC1768
        +---TOOLCHAIN_ARM_STD
```

Note: Why `LCP1768`? This example uses `LPC1768` because this platform supports all compilers, so you only need to specify the proper compiler.

If you are not using ARM Compiler, replace `ARM` with your compiler nickname: `GCC_ARM`, `GCC_CR` or `IAR`. For example, if you are using IAR, type this command:
```
$ python build.py -m LPC1768 -t IAR
```

Note: Workspace tools track changes in source code. If, for example, mbed OS or the test source code changes, `build.py` script recompiles the project with all dependencies. If there are no changes in code, consecutive mbed OS rebuilds using build.py will not rebuild project if this is not necessary. Try to run the last command once again. You can see script `build.py` will not recompile the project. (There are no changes): 
```
$ python build.py -m LPC1768 -t ARM
Building library CMSIS (LPC1768, ARM)
Building library MBED (LPC1768, ARM)

Completed in: (0.15)s

Build successes:
  * ARM::LPC1768
```

### build.py script

Build script located in mbed/tools/ is the core script solution to drive compilation, linking and building process for:

* mbed OS (with libs such as Ethernet, RTOS, USB and USB host).
* Tests, which you can also link with libraries such as RTOS or Ethernet.

Note: Test suite also uses the same build script, inheriting the same properties, such as auto dependency tracking and project rebuild, in case of source code changes.

Build.py script is a tool to build mbed OS for all available platforms using all supported by mbed cross-compilers. Script is using our workspace tools build API to create desired platform-compiler builds. Use script option `--h` (help) to check all script parameters.
```
$ python build.py --help
```

* The command-line parameter `-m` specifies the MCUs/platforms for which you want to build the mbed OS. More than one MCU(s)/platform(s) may be specified with this parameter using a comma as delimiter.
Example for one platform build:
```
$ python build.py -m LPC1768 -t ARM
```
or for many platforms:
```
$ python build.py -m LPC1768,NUCLEO_L152RE -t ARM
```

* Parameter `-t` defines which toolchain should be used for the mbed OS build. You can build mbed OS for multiple toolchains using one command. 
This example (note there is no space after each comma) compiles mbed OS for Freescale Freedom KL25Z platform using ARM and GCC_ARM compilers:
```
$ python build.py -m KL25Z -t ARM,GCC_ARM
```

* You can combine this technique to compile multiple targets with multiple compilers.
This example compiles mbed OS for Freescale's KL25Z and KL46Z platforms using ARM and GCC_ARM compilers:
```
$ python build.py -m KL25Z,KL46Z -t ARM,GCC_ARM
```

* Building libraries included in mbed OS's source code. Parameters `-r`, `-e`, `-u`, `-U`, `-d` and `-b` will add the `RTOS`, `Ethernet`, `USB`, `USB Host`, `DSP` and, `U-Blox` libraries respectively. 
This example builds the mbed OS library for NXP LPC1768 platform and the RTOS (`-r` switch) and Ethernet (`-e` switch) libraries.
```
$ python build.py -m LPC1768 -t ARM -r -e
Building library CMSIS (LPC1768, ARM)
Building library MBED (LPC1768, ARM)
Building library RTX (LPC1768, ARM)
Building library RTOS (LPC1768, ARM)
Building library ETH (LPC1768, ARM)

Completed in: (0.48)s

Build successes:
  * ARM::LPC1768
```

* If you’re unsure which platforms and toolchains are supported, please use switch `-S` to print a matrix of platform to compiler dependencies.
```
$ python build.py -S
+-------------------------+-----------+-----------+-----------+-----------+-----------+
| Platform                |    ARM    |    uARM   |  GCC_ARM  |    IAR    |   GCC_CR  |
+-------------------------+-----------+-----------+-----------+-----------+-----------+
| APPNEARME_MICRONFCBOARD | Supported |  Default  | Supported |     -     |     -     |
| ARCH_BLE                |  Default  |     -     | Supported | Supported |     -     |
| ARCH_GPRS               | Supported |  Default  | Supported | Supported | Supported |
...
| UBLOX_EVK_ODIN_W2       | Supported |  Default  | Supported | Supported |     -     |
| WALLBOT_BLE             |  Default  |     -     | Supported | Supported |     -     |
| XADOW_M0                | Supported |  Default  | Supported | Supported | Supported |
+-------------------------+-----------+-----------+-----------+-----------+-----------+
*Default - default on-line compiler
*Supported - supported off-line compiler

Total platforms: 90
Total permutations: 297
```

This list can be overwhelming, so please do not hesitate to use switch `-f` to filter the `Platform` column.
```
$ python build.py -S -f ^K
+--------------+-----------+---------+-----------+-----------+--------+
| Platform     |    ARM    |   uARM  |  GCC_ARM  |    IAR    | GCC_CR |
+--------------+-----------+---------+-----------+-----------+--------+
| K20D50M      |  Default  |    -    | Supported | Supported |   -    |
| K22F         |  Default  |    -    | Supported | Supported |   -    |
| K64F         |  Default  |    -    | Supported | Supported |   -    |
| KL05Z        | Supported | Default | Supported | Supported |   -    |
| KL25Z        |  Default  |    -    | Supported | Supported |   -    |
| KL43Z        |  Default  |    -    | Supported |     -     |   -    |
| KL46Z        |  Default  |    -    | Supported | Supported |   -    |
| NRF51_DK     |  Default  |    -    | Supported | Supported |   -    |
| NRF51_DK_OTA |  Default  |    -    | Supported |     -     |   -    |
+--------------+-----------+---------+-----------+-----------+--------+
*Default - default on-line compiler
*Supported - supported off-line compiler

Total platforms: 9
Total permutations: 28
```
You can also give only the platform name:
```
$ python build.py -S -f LPC1768
+----------+---------+-----------+-----------+-----------+-----------+
| Platform |   ARM   |    uARM   |  GCC_ARM  |    IAR    |   GCC_CR  |
+----------+---------+-----------+-----------+-----------+-----------+
| LPC1768  | Default | Supported | Supported | Supported | Supported |
+----------+---------+-----------+-----------+-----------+-----------+
*Default - default on-line compiler
*Supported - supported off-line compiler

Total platforms: 1
Total permutations: 6
```

* You can be more verbose `-v`, especially if you want to see each compilation or linking command that build.py is executing:
```
$ python build.py -t GCC_ARM -m LPC1768 -j 8 -v
Building library CMSIS (LPC1768, GCC_ARM)
Copy: LPC1768.ld
Compile: startup_LPC17xx.s
[DEBUG] Command: C:/Work/toolchains/gcc_arm_4_8/4_8_2013q4/bin\arm-none-eabi-gcc 
-x assembler-with-cpp -c -Wall -Wextra -Wno-unused-parameter -Wno-missing-field-initializers 
-fmessage-length=0 -fno-exceptions -fno-builtin -ffunction-sections -fdata-sections -MMD 
-fno-delete-null-pointer-checks -fomit-frame-pointer -mcpu=cortex-m3 -mthumb -O2 
-DTARGET_LPC1768 -DTARGET_M3 -DTARGET_CORTEX_M -DTARGET_NXP -DTARGET_LPC176X 
-DTARGET_MBED_LPC1768 -DTOOLCHAIN_GCC_ARM -DTOOLCHAIN_GCC -D__CORTEX_M3 -DARM_MATH_CM3 
-DMBED_BUILD_TIMESTAMP=1424903604.77 -D__MBED__=1 -IC:\Work\mbed\libraries\mbed\targets\cmsis 
-IC:\Work\mbed\libraries\mbed\targets\cmsis\TARGET_NXP 
-IC:\Work\mbed\libraries\mbed\targets\cmsis\TARGET_NXP\TARGET_LPC176X -IC:\Work\mbed\libraries\mbed\targets\cmsis\TARGET_NXP\TARGET_LPC176X\TOOLCHAIN_GCC_ARM 
-o C:\Work\mbed\build\mbed\.temp\TARGET_LPC1768\TOOLCHAIN_GCC_ARM\TARGET_NXP\TARGET_LPC176X\TOOLCHAIN_GCC_ARM\startup_LPC17xx.o 
C:\Work\mbed\libraries\mbed\targets\cmsis\TARGET_NXP\TARGET_LPC176X\TOOLCHAIN_GCC_ARM\startup_LPC17xx.s
[DEBUG] Return: 0
...
```

## Cppcheck analysis
[Cppcheck](http://cppcheck.sourceforge.net/) is a static analysis tool for C/C++ code. Unlike C/C++ compilers and many other analysis tools, it does not detect syntax errors in the code. Cppcheck primarily detects the types of bugs that the compilers normally do not detect. The goal is to detect only real errors in the code (in other words, have zero false positives).

Prerequisites:
* Please install `Cppcheck` on your system before you use it with build scripts.
* You should also add Cppcheck to your system path.

The `build.py` script supports switching between compilation, building and static code analysis testing. You can use switch `--cppcheck` to perform Cppcheck static code analysis. 

* When you are using --cppcheck switch, all macros, toolchain dependencies and so on are preserved, so you are sure you are checking exactly the same code you would compile for your application.

* Cppcheck analysis can take a few minutes on slower machines.

* Use switches `-t` and `-m` to define the toolchain and MCU (platform), respectively. Do the same in case of CppCheck analysis. Please note that build script can also compile and build the RTOS, Ethernet library and so on. If you want to check those, use the corresponding build script switches (such as `-r` and `-e`).

Example:
```
$ python build.py -t uARM -m NUCLEO_F334R8 --cppcheck
```

# make.py script
`make.py` is an `mbed/tools/` script used to build tests (we sometimes call them'programs') one by one manually. This script allows you to flash a board, execute and test it. However, this script is deprecated and will not be described here. Instead please use the `singletest.py` file to build mbed OS and tests and run automation for test cases included in `mbedmicro/mbed`.
Note: The `make.py` script depends on existing mbed OS and library sources, so you need to prebuild mbed OS and other libraries (such as the RTOS library) to link 'program' (test) with mbed OS and RTOS library. To prebuild mbed OS, please use `build.py` script.

Please see a few ways to use `make.py` with the Freedom K64F board.

* We need to build mbed OS (in directory `mbed/build/`:
```
$ python build.py -t GCC_ARM -m K64F -j 8
Building library CMSIS (K64F, GCC_ARM)
Building library MBED (K64F, GCC_ARM)

Completed in: (0.59)s

Build successes:
  * GCC_ARM::K64F
```
* We can print all 'programs' (test cases) `make.py` can build for us:
```
$ python make.py -L
.
[  0] MBED_A1: Basic
[  1] MBED_A2: Semihost file system
[  2] MBED_A3: C++ STL
[  3] MBED_A4: I2C TMP102
.
```
For example, 'program' under index `2` is `MBED_A3` test case we can build and flash onto the K64F board.
* Building test with `make.py` by specifying test case name with `-n` option:
```
$ python make.py -t GCC_ARM -m K64F -n MBED_A3
Building project STL (K64F, GCC_ARM)
Compile: main.cpp
[Warning] main.cpp@76: In function 'int main()': deprecated conversion from string constant to 'char*' [-Wwrite-strings]
.
.
.
[Warning] main.cpp@76: In function 'int main()': deprecated conversion from string constant to 'char*' [-Wwrite-strings]
Compile: test_env.cpp
Link: stl
Elf2Bin: stl
Image: C:\Work\mbed\build\test\K64F\GCC_ARM\MBED_A3\stl.bin
```
Because we previously have built mbed OS, we are now able to drive test case compilation and linking with mbed OS and produce `MBED_A3` test case binary in build directory:
```
C:\Work\mbed\build\test\K64F\GCC_ARM\MBED_A3\stl.bin
```

For more help, type `$ python make.py --help` in the command-line.

# project.py script
The `project.py` script exports test cases ('programs') from test case portfolio to off-line IDE. This exports test project to IDEs, such as:
* codesourcery.
* coide.
* ds5_5.
* emblocks.
* gcc_arm.
* iar.
* kds.
* lpcxpresso.
* uVision.

You can export the project using the command-line. Specify mbed platform name (option `-m`), your IDE (option `-i`) and the name of the project you want to export (option `-n` or (option `-p`).

In this example, you export your project, so you can work on it using GCC ARM cross-compiler. The building mechanism that drives the exported build is `Make`.
```
$ python project.py -m K64F -n MBED_A3 -i gcc_arm
Copy: test_env.h
Copy: AnalogIn.h
Copy: AnalogOut.h
.
.
.
Copy: K64FN1M0xxx12.ld
Copy: main.cpp

Successful exports:
  * K64F::gcc_arm       C:\Work\mbed\build\export\MBED_A3_gcc_arm_K64F.zip
```
You can see the exporter placed the compressed project export in a `zip` file in the `mbed/build/export/` directory.

The example export file `MBED_A3_gcc_arm_K64F.zip` structure:
```
MBED_A3
├───env
└───mbed
    ├───api
    ├───common
    ├───hal
    └───targets
        ├───cmsis
        │   └───TARGET_Freescale
        │       └───TARGET_MCU_K64F
        │           └───TOOLCHAIN_GCC_ARM
        └───hal
            └───TARGET_Freescale
                └───TARGET_KPSDK_MCUS
                    ├───TARGET_KPSDK_CODE
                    │   ├───common
                    │   │   └───phyksz8081
                    │   ├───drivers
                    │   │   ├───clock
                    │   │   ├───enet
                    │   │   │   └───src
                    │   │   ├───interrupt
                    │   │   └───pit
                    │   │       ├───common
                    │   │       └───src
                    │   ├───hal
                    │   │   ├───adc
                    │   │   ├───can
                    │   │   ├───dac
                    │   │   ├───dmamux
                    │   │   ├───dspi
                    │   │   ├───edma
                    │   │   ├───enet
                    │   │   ├───flextimer
                    │   │   ├───gpio
                    │   │   ├───i2c
                    │   │   ├───llwu
                    │   │   ├───lptmr
                    │   │   ├───lpuart
                    │   │   ├───mcg
                    │   │   ├───mpu
                    │   │   ├───osc
                    │   │   ├───pdb
                    │   │   ├───pit
                    │   │   ├───pmc
                    │   │   ├───port
                    │   │   ├───rcm
                    │   │   ├───rtc
                    │   │   ├───sai
                    │   │   ├───sdhc
                    │   │   ├───sim
                    │   │   ├───smc
                    │   │   ├───uart
                    │   │   └───wdog
                    │   └───utilities
                    │       └───src
                    └───TARGET_MCU_K64F
                        ├───device
                        │   ├───device
                        │   │   └───MK64F12
                        │   └───MK64F12
                        ├───MK64F12
                        └───TARGET_FRDM
```

After unpacking exporter `zip` file, you can go to the directory and see files inside MBED_A3 directory:
```
$ ls
GettingStarted.htm  Makefile  env  main.cpp  mbed
```
The exporter generated `Makefile`, so now you can build the software:
```
$ make -j 8
.
.
.
   text    data     bss     dec     hex filename
  29336     184     336   29856    74a0 MBED_A3.elf
```

Binary files now populate the root directory of the exporter project:
* MBED_A3.bin.
* MBED_A3.elf.
* MBED_A3.hex.
You also have the map file `MBED_A3.map` for your disposal.
```
$ ls
GettingStarted.htm  MBED_A3.bin  MBED_A3.elf  MBED_A3.hex  MBED_A3.map  Makefile  env  main.cpp  main.d  main.o  mbed
```

