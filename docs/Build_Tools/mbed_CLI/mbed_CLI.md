# Getting Started with mbed OS using the command line interface

To get started with mbed OS using our command line interface (mbed CLI), we're going to build a program called Blinky to blink an LED on your board.

The mbed CLI is designed so that you can easily work on code in your desktop. It lets you clone code, compile it, pull and push it, as well as carry out other operations.

## Installing mbed CLI

### Requirements 

Make sure you’ve installed the following software:

* Python (tested with [2.7](https://www.python.org/download/releases/2.7/) and [3.5](https://www.python.org/downloads/release/python-350/)).
* [Git](https://git-scm.com/), and optionally [Mercurial](https://www.mercurial-scm.org/).</br>Tip: remember that the directories containing the executables of ``hg`` and ``git` need to be in your system's PATH.
* [GCC ARM Embedded](https://launchpad.net/gcc-arm-embedded).

You also need to install two Python packages:


```
$  pip install colorama
$  pip install jinja2`
```

### Installing

To install mbed CLI:

1. Open a terminal.

1. Clone the repository [https://github.com/ARMmbed/mbed-cli](https://github.com/ARMmbed/mbed-cli):

    ``$ git clone https://github.com/ARMmbed/mbed-cli``

1. Navigate to the ``mbed-cli`` folder.

1. Install *mbed-cli* as a Python package:

    ``$ python setup.py install`` 

<span class="tips">**Tip:** (on Linux/Mac, you may need to run this command with ``sudo``)</span>

## Importing Blinky

Use `mbed import` to clone an existing program (or library) and all its dependencies to your machine:

```
$ mbed import https://developer.mbed.org/teams/Morpheus/code/blinky/
$ cd Blinky
```

## Building Blinky

### Toolchain location

After importing a program or creating a new one, you need to tell mbed CLI where to find the toolchains that you want to use for compiling your source tree. mbed CLI gets this information from the file `mbed_settings.py`, which is automatically created at the top of your cloned repository (if it doesn't already exist). 

<span class="tips">**Tip:** ``mbed_settings.py`` holds the location of your build tools, but doesn't force mbed CLI to use one or the other - you can select a different tool each time you build.</span>

To set the location of your build tools: 

* If you want to use the [armcc toolchain](https://developer.arm.com/products/software-development-tools/compilers/arm-compiler-5/downloads), set ``ARM_PATH`` to the *base* directory of your armcc installation (example: c:\software\armcc5.06). The recommended version of the armcc toolchain is 5.06 (5.05 will very likely work too).
* If you want to use the [GCC ARM Embedded toolchain](https://launchpad.net/gcc-arm-embedded), set ``GCC_ARM_PATH`` to the *binary* directory of your GCC ARM installation (example: c:\software\GNUToolsARMEmbedded\4.82013q4\bin). Use versions 4.8 or 4.9 of GCC ARM Embedded, but **not** version 5.0 or any version above it.

### Compiling your program

Use `mbed compile` to compile the code:

```
$ mbed compile -t ARM -m K64F -j 0
```

The arguments for `compile` are:

* `-m <mcu>` to select a compilation target. At the moment, the only supported value for `mcu` is `K64F` (for the FRDM_K64F board).
* `-t <toolchain>` to select a toolchain, where `toolchain` can be either ARM (armcc compiler) or GCC_ARM (GNU ARM Embedded). Don't forget to set their location in ``mbed_settings.py``, as explained above.
* `-j <jobs>` (optional) to use multiple threads on your machine to compile the source. Use 0 to infer the number of threads from the number of cores on your machine, or an actual number to specify the maximum number of threads.
* `-c ` (optional): will build from scratch; a clean build or rebuild.

The compiled binary (and ELF image) can be found in the `.build` subdirectory of your program.

## Running Blinky

Finally, run Blinky on your K64F board:

1. Plug your board into your computer and it will appear as a USB drive.

1. Drag and drop your ``blinky.bin`` file onto the drive. 

1. Your board should blink the RGB LED.
