#mbed SDK Porting

The porting of the mbed SDK to a new target is divided in four steps:

* Add the new target to the build system
* Add a CMSIS module for the given target
* Implement the mbed HAL API for the given target
* Validate the new target with the test suite

The source code of the mbed SDK (tools + libraries) is available in [this repository](https://github.com/mbedmicro/mbed).

Before starting the mbed SDK porting, you might want to familiarize with the [mbed library internals](Going_Further/Lib_Internals/) first.

For discussing the development of the mbed SDK itself (Addition/support of microcontrollers/toolchains, build and test system, Hardware Abstraction Layer API, etc) please join our [mbed-devel mailing list](https://groups.google.com/forum/?fromgroups#!forum/mbed-devel).

##Coding style

mbed SDK coding style is described in detail in mbed SDK team's wiki page, please visit for further details [mbed SDK coding style](/Going_Further/Coding_Style/).

##Build System

You can get an introduction about the mbed SDK command line tools, from a user perspective, reading the [mbed-tools handbook page](/Going_Further/Tools/).

Adding a new target to the build system is as easy as adding a new ``Target`` class to this python module: [workspace_tools/targets.py](https://github.com/mbedmicro/mbed/blob/master/workspace_tools/targets.py).

For example, this is the Target class for the LPC1768:

```python

	class LPC1768(Target):
		def __init__(self):
			Target.__init__(self)

			self.core = "Cortex-M3"

			self.extra_labels = ['LPC176X']

			self.supported_toolchains = ["ARM", "GCC_ARM", "GCC_CS", "GCC_CR", "IAR"]
```

An instance of this new ``Target`` class has to be added to the ``TARGETS`` list:

```python

	TARGETS = [
		LPC2368(),
		LPC1768(),
		LPC11U24(),
		KL25Z(),
		LPC812(),
		LPC4088(),	
		LPC4330(),
	]
```

The target and toolchain specified for a given build define a set of ``TARGET_`` and ``TOOLCHAIN_`` "labels". For example:

```

	Targets:
  		* LPC1768 : ['TARGET_LPC1768', 'TARGET_M3', 'TARGET_LPC176X']
  		* LPC11U24: ['TARGET_LPC11U24', 'TARGET_M0', 'TARGET_LPC11UXX']
  		* KL25Z   : ['TARGET_KL25Z', 'TARGET_M0P']

	Toolchains:
  		* ARM    : ['TOOLCHAIN_ARM_STD', 'TOOLCHAIN_ARM']
 		* uARM   : ['TOOLCHAIN_ARM_MICRO', 'TOOLCHAIN_ARM']
  		* GCC_ARM: ['TOOLCHAIN_GCC_ARM', 'TOOLCHAIN_GCC']
  		* IAR    : ['TOOLCHAIN_IAR']
```

When the build system scans for resources to be compiled, it filters out all the ``TARGET_`` and ``TOOLCHAIN_`` directories that are not in the set of "labels" defined by the current build.

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
**IDE:**  You can develop the code for adding support for a new target in you favourite IDE. As a starting point, you can export the following program to one of the supported [offline toolchains](Going_Further/Export/): [Hello World using the mbed library sources](http://developer.mbed.org/users/mbed_official/code/mbed-src-program/).
</span>

##CMSIS Module

Each target has its standalone CMSIS directory under its vendor directory, for example:

* [libraries/mbed/targets/cmsis/Freescale/TARGET_KL25Z](https://github.com/mbedmicro/mbed/blob/master/libraries/mbed/targets/cmsis/Freescale/TARGET_KL25Z).
* [libraries/mbed/targets/cmsis/NXP/TARGET_LPC176X](https://github.com/mbedmicro/mbed/blob/master/libraries/mbed/targets/cmsis/NXP/TARGET_LPC176X).

###CMSIS Sources

There are three sources for a "cmsis" module used by an mbed target.

The ARM CMSIS-CORE module is providing the files that are specific to the Cortex-M cores:

* ``core_cmFunc.h``
* ``core_cmInstr.h``
* ``cortex_cm0.h`` / ``cortex_cm0plus.h`` / ``core_cm3.h`` / ``cortex_cm4.h``

The Silicon Vendor is providing the files for the startup, system initialization, the structures and addressed of the peripherals registers, for a given DEVICE:

* ``startup_DEVICE.s``
* ``system_DEVICE.c``
* ``system_DEVICE.h``
* ``DEVICE.h``

The mbed SDK has to provide additional files to dynamically set the vector table  and to configure the [memory model](/Going_Further/Mem_Mo/) for the given C standard library:

* ``cmsis_nvic.c``
* ``cmsis_nvic.h``
* ``sys.cpp``
* ``TARGET.sct``
* ``cmsis.h``

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
**Info: CMSIS sources**
Usually, silicon vendors provide source packages containing both the CMSIS-CORE and the CMSIS device specific files.
</span>

##mbed HAL

Each target does have a standalone directory containing the implementation of the mbed HAL API, for example:

* [libraries/mbed/targets/hal/Freescale/TARGET_KL25Z](https://github.com/mbedmicro/mbed/blob/master/libraries/mbed/targets/hal/Freescale/TARGET_KL25Z).
* [libraries/mbed/targets/hal/NXP/TARGET_LPC176X](https://github.com/mbedmicro/mbed/blob/master/libraries/mbed/targets/hal/NXP/TARGET_LPC176X).

Probably the most important file, at the beginning of a port to a new target, is [device.h](https://github.com/mbedmicro/mbed/blob/master/libraries/mbed/targets/hal/NXP/TARGET_LPC176X/device.h).

``device.h`` contains all the defines that enable/disable the inclusion of a certain set of peripherals in the mbed library.

When you start a port for a new target, setting all these defines to ``0`` will quickly allow you to compile the whole mbed library and start running tests.

Currently, the bare minimum you should implement to start running the first tests is:

* [GPIO API](https://github.com/mbedmicro/mbed/blob/master/libraries/mbed/hal/gpio_api.h)
* [us ticker API](https://github.com/mbedmicro/mbed/blob/master/libraries/mbed/hal/us_ticker_api.h):
	* ``void us_ticker_init(void);``
	* ``uint32_t us_ticker_read(void)``

Having this initial block in place will allow you to run simple programs like the mbed ``hello world``:


```c

	#include "mbed.h"

	DigitalOut myled(LED1);

	int main() {
		while(1) {
			myled = 1;
			wait(0.2);	
			myled = 0;
			wait(0.2);
		}
	}
```

This is the full list of the mbed drivers API that could be potentially implemented for a target:

* [analogin_api.h](https://github.com/mbedmicro/mbed/tree/master/libraries/mbed/hal/analogin_api.h)
* [analogout_api.h](https://github.com/mbedmicro/mbed/tree/master/libraries/mbed/hal/analogout_api.h)
* [can_api.h](https://github.com/mbedmicro/mbed/tree/master/libraries/mbed/hal/can_api.h)
* [ethernet_api.h](https://github.com/mbedmicro/mbed/tree/master/libraries/mbed/hal/ethernet_api.h)
* [gpio_api.h](https://github.com/mbedmicro/mbed/tree/master/libraries/mbed/hal/gpio_api.h)
* [gpio_irq_api.h](https://github.com/mbedmicro/mbed/tree/master/libraries/mbed/hal/gpio_irq_api.h)
* [|i2c_api.h](https://github.com/mbedmicro/mbed/tree/master/libraries/mbed/hal/i2c_api.h)
* [pinmap.h](https://github.com/mbedmicro/mbed/tree/master/libraries/mbed/hal/pinmap.h)
* [port_api.h](https://github.com/mbedmicro/mbed/tree/master/libraries/mbed/hal/port_api.h)
* [pwmout_api.h](https://github.com/mbedmicro/mbed/tree/master/libraries/mbed/hal/pwmout_api.h)
* [rtc_api.h](https://github.com/mbedmicro/mbed/tree/master/libraries/mbed/hal/rtc_api.h)
* [serial_api.h](https://github.com/mbedmicro/mbed/tree/master/libraries/mbed/hal/serial_api.h)
* [sleep_api.h](https://github.com/mbedmicro/mbed/tree/master/libraries/mbed/hal/sleep_api.h)
* [spi_api.h](https://github.com/mbedmicro/mbed/tree/master/libraries/mbed/hal/spi_api.h)
* [us_ticker_api.h](https://github.com/mbedmicro/mbed/tree/master/libraries/mbed/hal/us_ticker_api.h)

##Testing

The mbed SDK provides a test system to validate the addition of your new target.

You may want to familiarize with the command line interface and structure of the test system reading the [mbed-tools handbook page](/Going_Further/Tools/#test-system).

The description of the tests aimed at validating the mbed SDK are prefixed with the string ``MBED:``.

<span style="background-color:lightyellow; color:black; display:block; height:100%; padding:10px">
**Warning:** You will need to edit the source code of many of the tests adding, under conditional compilation, the pinout of your new target board.
</span>

<span style="background-color:lightyellow; color:black; display:block; height:100%; padding:10px">
**Warning:** Not all the tests are yet automated presenting a clear ``{success}` or ``{failure}`` result string. Some of the tests still require additional instrumentation like a logic analyser and human intervention to verify the output.
</span>

###Smoke Test

``[ 0] MBED: Basic`` is the first [smoke test](http://en.wikipedia.org/wiki/Smoke_testing#Software_development) that represents the basis to execute all the other tests in the mbed SDK suite. 

```c

	#include "test_env.h"

	int main() {
		notify_completion(true);
	}
```

This is an example command line test run:

```
	
	mbed> python workspace_tools\make.py -m LPC1768 -t ARM -s COM41 -d E:\ -p 0

	>>> BUILD PROJECT: BASIC (LPC1768, ARM)
	Compile: main.cpp
	Compile: test_env.cpp
	Link: basic
	Elf2Bin: basic
	Image: C:/Users/emimon01/mbed/build\test\LPC1768\ARM\MBED_A1\basic.bin
	{success}
	{end}
```

###C/C++ environment initialization

* ``MBED: Heap & Stack`` - setting of the single area memory model with heap and stack collision detection.
* ``MBED: C++`` - initialization of static C++ objects

##Digital I/O and IRQ

For this set of tests you will need to connect together a pair of pins:

* ``MBED: DigitalInOut`` - Setting digital I/O functionality, direction and value.
* ``MBED: InterruptIn`` - Triggering and handling of GPIO IRQs

###Timing functionalities

For this set of functionalities it is preferable to use a logic analyser to verify the correctness of the time intervals. Ideally the following tests should be repeated changing the time periods across a wide time interval (from micro-seconds, to seconds):

* ``MBED: Time us`` - simple us_ticker init/read functionality
* ``MBED: Ticker 2`` - correct triggering of timing events

###PWM

For this set of functionalities it is preferable to use a logic analyser to verify the correctness of the time intervals. Ideally the following tests should be repeated changing the time periods across a wide time interval (from micro-seconds, to seconds):

* ``MBED: PWM`` - PWM

###I2C

The I2C tests require the wiring of additional peripherals:

* ``MBED: I2C TMP102`` - [TMP102 Temperature Sensor](http://developer.mbed.org/cookbook/TMP102-Temperature-Sensor)
* ``MBED: I2C MMA7660`` - [MMA7660 Accelerometer](http://developer.mbed.org/cookbook/MMA7660-Accelerometer)
* ``MBED: I2C SRF08`` - [SRF08 Ultrasonic Ranger](http://developer.mbed.org/cookbook/SRF08-Ultrasonic-Ranger)

###SPI

The SPI tests require the wiring of additional peripherals:

* ``MBED: SPI ADXL345`` - See [ADXL345 Accelerometer](http://developer.mbed.org/cookbook/ADXL345-Accelerometer)
* ``MBED: SD File System`` - See [SDFileSystem](http://developer.mbed.org/handbook/SDFileSystem)

###UART

The basic UART functionalities are used to communicate the results of all the other test, but the following tests are stressing some of the other UART APIs:

* ``MBED: Serial Echo at 115200`` - change baud rate to 115200 and test transmission
* ``MBED: Serial Interrupt`` and ``MBED: Serial Interrupt 2`` - serial tx/rx interrupt handlers

###ADC/DAC

This test relies on a connection among one ADC pin and one DAQ pin on the same target:

* ``MBED: Analog``

###Port

Testing the Port API requires connecting at least a couple of pins from a port to a couple of pins in another port:

* ``MBED: PortInOut``

### RTC

* ``MBED: RTC``

###Sleep

* ``MBED: Sleep``
* ``MBED: Sleep Timeout``

###Semihosting

The following tests are used to verify the semihosting functionalities that may be provided by the "mbed interface"

* ``MBED: semihost file system`` - Local file system
* ``MBED: Semihost`` - mbed unique ID
* ``MBED: SW Reset`` - request to the interface chip a complete reset

##Contributing

To contribute your new target to the official mbed SDK:

* Open a [pull request](https://help.github.com/articles/using-pull-requests) to the [official mbed SDK repository](https://github.com/mbedmicro/mbed), containing:
	* all the changes to the C/C++ libraries and the Python tools.
	* information about the reference target board
* logged in with your mbed.org account, sign our [Apache Contribution Agreement](http://developer.mbed.org/contributor_agreement/) and [send us a Private Message](http://developer.mbed.org/users/emilmont/) with the URL of the pull request.