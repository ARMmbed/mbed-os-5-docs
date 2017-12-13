## Offline - Mbed CLI

### Setup
Please skip to the sub section for your host OS. The setup instructions will walk you through how to get mbed CLI installed locally on your system. 

[**Windows**](#windows) | [**OSX**](#mac-osx) | [**Linux**](#linux)

#### Windows

##### 1. Install mbed CLI

Download and run the [mbed CLI Windows .exe installer](https://github.com/ARMmbed/mbed-cli-windows-installer/releases).

You can check to make sure the mbed CLI installed correctly by running `mbed help`.

**Note:** the Windows installer only installs the ARM GCC toolchain, if you would like to compile using the ARM Compiler 5 or IAR, visit the links below:

  * [ARMCC ](https://developer.arm.com/products/software-development-tools/compilers/arm-compiler/downloads/version-5)  
  * [IAR](https://www.iar.com/iar-embedded-workbench/tools-for-arm/)  

##### 2. Setup Environment

Make sure the compiler is available in your global path:

  * ARM GCC: run `arm-none-eabi-gcc --version` from your command line
  * ARMCC:  run `armcc` with no arguments from your command line
  * IAR: run `iccarm --version` from your command line

#### Mac OSX

##### 1. Install Python & Pip

Mac OS X 10.8+ comes with Python 2.7 pre-installed by Apple. If you are running an earlier version of Mac OS X, download and install [Python 2.7.12+](https://www.python.org/downloads/mac-osx/).

To install Pip, run `sudo easy_install pip` from your command line.

##### 2. Install a Compiler

Download and install a compiler:

  * [ARM GCC ](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads)  
  * [ARMCC ](https://developer.arm.com/products/software-development-tools/compilers/arm-compiler/downloads/version-5)  
  * [IAR](https://www.iar.com/iar-embedded-workbench/tools-for-arm/)  

##### 3. Install mbed CLI

To install the mbed CLI, run `pip install mbed-cli` from your command line.

You can check to make sure the mbed CLI installed correctly by running `mbed help`.

##### 4. Setup Environment

Make sure the compiler is available in your global path:

  * ARM GCC: run `arm-none-eabi-gcc --version` from your command line
  * ARMCC:  run `armcc` with no arguments from your command line
  * IAR: run `iccarm --version` from your command line

#### Linux 

##### 1. Install Python & Pip

Download and install [Python 2.7.12+](https://www.python.org/downloads/source/) or run the following from your command line:

```console
$ sudo apt-get install python2.7
$ sudo apt-get install python-pip
$ sudo apt-get update
```

##### 2. Install a Compiler

Download and install a compiler:

  * [ARM GCC ](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads)  
  * [ARMCC ](https://developer.arm.com/products/software-development-tools/compilers/arm-compiler/downloads/version-5)  
  * [IAR](https://www.iar.com/iar-embedded-workbench/tools-for-arm/)  

##### 3. Install mbed CLI

To install the mbed CLI, run `pip install mbed-cli` from your command line.

You can check to make sure the mbed CLI installed correctly by running `mbed help`.

##### 4. Setup Environment

Make sure the compiler is available in your global path:

  * ARM GCC: run `arm-none-eabi-gcc --version` from your command line
  * ARMCC:  run `armcc` with no arguments from your command line
  * IAR: run `iccarm --version` from your command line

### Code

#### 1. Get the Code

From your command line, import the example:

```console
$ mbed import https://github.com/ARMmbed/mbed-os-example-blinky
$ cd mbed-os-example-blinky
```
  
#### 2. Compile and Program Board

Invoke `mbed compile` and specify the name of your platform and your installed toolchain (`GCC_ARM`, `ARM`, `IAR`). For example, for the K64F platform and ARM Compiler 5 toolchain:
  
```console
$ mbed compile --target K64F --toolchain ARM --flash
```  

The `--flash` argument will automatically flash the compiled program onto your board if it is connected to your computer. You can see which boards are connected with `mbed detect`. 

After the program has been flashed to the board, press the board's "reset" button and you should now see the LED blinking.

**Note** : you can get the name of the board plugged into your computer by running `mbed detect` and you can get a full list of supported toolchains / targets by running the `mbed compile --supported`


### Debug

#### Desktop IDE

To debug using a desktop IDE such as Keil uVision, IAR, or Eclipse you can use the `mbed export` command to generate project files. For example, for a K6F and Keil uVision:

```console
$ mbed export -i uvision -m K64F
```  
**NOTE** for a full list of exporters supported run the `mbed export --supported` command. 


#### Printf

Another way to do basic debugging is to use the `printf` command in your code, then read the output using a serial terminal such as [PuTTY](http://www.putty.org/) or [CoolTerm](http://freeware.the-meiers.org/). For example, add `printf("Hello World!\n\r");` to the top of your main function, then recompile the program and flash it to your device.

Invoke `mbed detect` from your command line to determine which communication port your board is connected to (i.e. `COM18`, `/dev/ttyACM0`, etc.). Unless otherwise specified, `printf` defaults to a baud rate/speed of `9600` on mbed OS.

### Further Reading

- Documentation
  - [Mbed OS API's](https://os.mbed.com/docs/v5.6/reference/apis.html) - List of all API's available in Mbed OS
  - [Peripheral Drivers](https://os.mbed.com/docs/v5.6/reference/drivers.html) - Traditional Driver API's (I2C, SPI, UART, ... etc)

- Tutorials
  - [Advanced Debugging](https://os.mbed.com/docs/v5.6/tutorials/debugging.html)
  - [Serial Communications](https://os.mbed.com/docs/v5.6/tutorials/serial-communication.html)
  - [Optimizing binary size](https://os.mbed.com/docs/v5.6/tutorials/optimizing.html)

- Other Resources 
  - [Components Database](https://os.mbed.com/components/) - libraries and example code for various hardware and software components
  - [Mbed OS Forum](https://os.mbed.com/forum/) - great resource full of knowledge and active user community. Ask your questions here first!
  - [Youtube Channel](http://youtube.com/armmbed) - videos and workshop content
