#mbed Tools

The tools used to develop the mbed libraries are released under the permissive open source license Apache Version 2.0 in the following online code repositories:

* [GitHub/mbed](https://github.com/mbedmicro/mbed)

The tools, stored in the ``workspace_tools`` directory, are written in Python (platform independent: tested on Windows and Linux).

##Settings configuration

The mbed tools are providing sensible defaults for all the required settings in the file:

* ``workspace_tools/settings.py``

You can configure your settings changing the value of any of the settings variables in the file:

* ``workspace_tools/private_settings.py``

We configured our version control systems (ie: git) to ignore this file.

For example, if you want to change the path to your [GNU Tools for ARM Embedded Processors](https://launchpad.net/gcc-arm-embedded/4.7/4.7-2012-q4-major) to a path like ``c:/arm_gcc/bin``, you simply need to have a ``private_settings.py`` containing the following line:

```python

	GCC_ARM_PATH = "c:/arm_gcc/bin"
```

<span style="background-color:lightyellow; color:black; display:block; height:100%; padding:10px">
**Warning: Windows path in a Python string**
<br />
In a Python string ``\`` is used as an escape character to specify special characters (``\n``, ``\t``, etc). If you want to add a ``\`` in a Python string, you need to write ``{{{\\}}}``. Otherwise, as path separator you can use the forward slash: ``/`` (see above example).
</span>

##Build System

The mbed build system is composed of two scripts:

* One to build the libraries: ``workspace_tools/build.py``
* One to build and run the test projects: ``workspace_tools/make.py``

Both share a subset of options to specify the target microcontroller and the toolchain:

```python

	-m MCU -t TOOLCHAIN
```

The available target ``MCU``s are:

* ``LPC1768``
* ``LPC11U24``
* ``LPC2368``
* ``LPC812``
* ``KL25Z``

The available ``TOOLCHAIN``s are:

* ``ARM``: ARMCC toolchain with the standard C library
* ``uARM``: ARMCC toolchain with the micro C library
* ``GCC_ARM``: GCC toolchain from ARM
* ``GCC_CS``: GCC toolchain from CodeSourcery 
* ``GCC_CR``: GCC toolchain from CodeRed
* ``IAR``: IAR toolchain

###build.py

If a target and a toolchain are not specified, the build script will build the mbed library for all the available targets and toolchains.

If, for example, you want to build the mbed library for the LPC1768 mbed using the ARM GCC toolchain:

```python

	> python workspace_tools\build.py -m LPC1768 -t GCC_ARM
```

This is an example output:

```python

	>>> BUILD LIBRARY CMSIS (LPC1768, GCC_ARM)
	Copy: LPC1768.ld
	Assemble: startup_LPC17xx.s
	Compile: cmsis_nvic.c
	Compile: core_cm3.c
	[...]
	Compile: TimerEvent.cpp
	Library: libmbed.a

	Completed in: (6.31)s

	Build successes:
	* GCC_ARM::LPC1768
```

The following options are used to request the build of additional libraries:

* ``-r``: build the RTOS library
* ``-e``: build the Ethernet library
* ``-u``: build the USB device library
* ``-d``: build the DSP library

##Test System

###make.py

Make is used to build and run one of the test projects defined in the following python file: ``workspace_tools/tests.py``

Each test project is specified by a simple python dictionary of the type:


```python

	TESTS = [
		# Automated MBED tests
		{
			"id": "MBED_A1", "description": "MBED: Basic",
			"source_dir": join(TEST_DIR, "mbed", "basic"),
			"dependencies": [MBED_LIBRARIES, TEST_MBED_LIB],
			"automated": True,
		},
		{
			"id": "MBED_A2", "description": "MBED: semihost file system",
			"source_dir": join(TEST_DIR, "mbed", "file"),
			"dependencies": [MBED_LIBRARIES, TEST_MBED_LIB],
			"automated": True,
			"mcu": ["LPC1768", "LPC2368", "LPC11U24"]
		},
```

All these project specifications are contained in the ``TEST`` list. If you launch the "make" script without any option, the script will print a list of all the available tests with their correspondent number:

```python

	> python workspace_tools\make.py

		[ 0] MBED: Basic
		[ 1] MBED: semihost file system
		[ 2] MBED: C++ STL
		[ 3] MBED: I2C TMP102
		[ 4] MBED: DigitalIn DigitalOut
		[ 5] MBED: DigitalInOut
		[ 6] MBED: InterruptIn
		[ 7] MBED: Analog
		[ 8] MBED: Serial Echo at 115200
		[ 9] MBED: PortOut PortIn
		[10] MBED: PortInOut
		[11] MBED: SD File System
		[12] MBED: I2C MMA7660
		[...]
```

On top of building a test project, the "make" script can actually program and reset a target mbed and display all the output printed on the target serial port:

* ``-d``: specifies the target mbed disk (ie: ``E:\`` on Windows, or ``/media/mbed`` on Linux)
* ``-s``: specifies the target serial port (ie: ``COM4`` on Windows, or ``/dev/ttyACM0`` on Linux)

For example, to build the "Basic" test project (number: ``0``) for a ``LPC1768`` mbed using the ``ARM GCC`` toolchain, flashing the resulting binary on the disk ``E:\`` and interfacing to the serial port ``COM4``:

```python

	> python workspace_tools\make.py -m LPC1768 -t GCC_ARM -d E:\ -s COM41 -p 0
```

<span style="background-color:lightyellow; color:black; display:block; height:100%; padding:10px">
**Warning: Python Serial Port Extension**
<br />
To drive the serial port with ``make.py`` you will need to install the [pyserial package](https://pypi.python.org/pypi/pyserial)
</span>

This is an example output:


```python
	
	>>> BUILD PROJECT: BASIC (LPC1768, GCC_ARM)
	Compile: main.cpp
	Compile: test_env.cpp
	Link: basic
	Elf2Bin: basic
	Image: C:\Users\emimon01\mbed\build\test\LPC1768\GCC_ARM\MBED_A1\basic.bin
	{success}
	{end}
```

All the text appearing after the "Image:" path is actually printed through the serial port by the program running on the mbed.

If you specify a serial port with the ``-s`` option, immediately after the copy of the project binary on the mbed, the "make" script enters in a loop reading the specified serial port. To interrupt the loop simply send a keyboard interrupt (ie: ``CTRL+c``).

####Adding a test

Adding a new test project is as easy as:

* Add the sources of your project in a new directory under the ``libraries/tests`` tree.
* Add a dictionary entry to the ``workspace_tools/tests.py`` ``TEST`` list.

These are the mandatory keys of a test project dictionary:

* ``id``: A unique ID string to identify the test (used only internally by the automated test system) 
* ``description``: A human friendly description of the test displayed on the command line "help" message
* ``source_dir``: The directory containing the sources of your test project. As good practice write the path joining it with the root ``TEST_DIR`` directory.

These are the optional keys of a test project dictionary:

* ``dependencies``: A list of directory paths containing the sources of the libraries this project is depending on. (default: None)
* ``automated``: Boolean specifying if the test project can communicate automatically the result of the test without the supervision of a human using specific strings. (default: False).
* ``duration``: The maximum time taken by an automated test to complete. If the test takes longer than that to complete, it is reported as a failure. (default: (10)s)
* ``mcu``: a list of types of mbed that can run the program. (default: every mbed).
* ``peripherals``: a list of peripherals needed to run the test. (default: None).
* ``host_test``: Specific host test to be launched to verify the success of the test. (defualt: 'host_test' simply checking the special strings in curly braces ``{success}`` or ``{failure}``).
* ``extra_files``: A list of file to be copied on the mbed (for example data files to be read by the mbed program during execution).

The "automated" test projects use specific strings in curly braces to communicate to the host the result of automated tests:

* ``{success}`` and ``{failure}`` are used to communicate the result of a single check.
* ``{end}`` is used to communicate the end of the test.

##Export System

To test exporter scripts run the project.py with options for the MCU and the target compiler. This provides a handy way of checking your export scripts and testing new chips you are creating. This is the same script the online compiler will use to export projects for users to download. 

``example_Keil_uVision_project_for_FRDM-K64F_with_test_0``

```python

	$  python project.py -m K64F -i uvision -p 0
```

The script will tell you where the zip file of your project is exported to. 