# Setting up your environment

This section explains how to set up your development environment to port to mbed OS.

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

     ```bash
     sudo apt-get remove binutils-arm-none-eabi gcc-arm-none-eabi
     sudo apt-get autoremove
     sudo add-apt-repository ppa:terry.guo/gcc-arm-embedded
     sudo apt-get update
     sudo apt-get install gcc-arm-none-eabi=4.9.3.2015q3-1trusty1
     ```
- [Keil MDK-ARM](http://www.keil.com/download/product/) - optional.
- [IAR for ARM](https://www.iar.com/iar-embedded-workbench/#!?architecture=ARM) - optional.
- [Git](https://git-scm.com/downloads). After installing Git, you should configure it to use the credential store as explained [here](https://help.github.com/articles/caching-your-github-password-in-git/). This will give you easy access to our private repos.

- [mbed CLI](https://github.com/ARMmbed/mbed-cli) - our tool for delivering mbed OS, invoking code compilation, testing and exporting to desktop tools. 

	You can install it using the following command:

	``` bash
	sudo pip install mbed-cli
	```

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
