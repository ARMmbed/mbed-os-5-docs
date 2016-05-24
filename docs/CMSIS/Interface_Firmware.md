#CMSIS-DAP Interface Firmware

The source code of the mbed HDK (tools + libraries) is available in [this repository](https://github.com/mbedmicro/CMSIS-DAP).

##What It Provides

The CMSIS-DAP Interface Firmware provides:
   
* USB Mass Storage Device for drag and drop programming of the target chip
* USB Communications Device Class for Serial Communication with the target chip
* USB HID CMSIS-DAP for debugging
* USB bootloader for updating the interface firmware itself

##Hardware Interfaces

The following image shows how an Onboard Interface running the CMSIS-DAP Interface Firmware might be used to build an evaluation board:

<span style="text-align:center; display:block;">
![](/Development/Images/EvaluationBoard.png)
</span>

When the Onboard Interface is plugged to an host PC it enumerates as a composite device with the following interfaces:

* MSD, mass storage device class
* CDC, communications device class
* HID, human interface device class

It is connected to the following pins of the target microcontroller:

* SWD + Reset
* UART
* Sleep and Wake (Not currently implemented, reserved for future use)

<span style="text-align:center; display:block;">
![](/Development/Images/CMSISDAPInterface.png)
</span>

##Shared Code

The Bootloader and CMSIS-DAP Interface Firmware for every target share common middleware and components in the folder ***shared***:
   
* ``shared\cmsis``: The CMSIS-CORE software layer
* ``shared\rtos``: The RTX operating system
* ``shared\USBStack``: The USB Device middleware

 ##Bootloader

The bootloader allows a firmware update of the interface chip.

Currently, this project support only the !LPC11U35, its project file is located in: ``bootloader\mdk\lpc11u35\lpc11u35_bootloader.uvproj``

At startup it checks the state of a given pin, default high by pull-up resistor:

* If the pin is high: it simply relocates the vector table to point to the interrupt handlers of the CMSIS-DAP Interface Firmware and then it jumps to its start address.
* If the pin is low: it enumerates as a mass storage device, waiting for a new firmware image to be flashed using In Application Programming (IAP)

<span style="text-align:center; display:block;">
![](/Development/Images/CMSIS_Bootloader.png)
</span>

###Porting to a New Chip

When you are porting to a new chip, you should first be sure to have the correspondent CMSIS-CORE files in the ``shared\cmsis`` folder.

To simplify the effort of porting this bootloader to a new target chip, we have kept together the majority of the target dependent code in the directory ``bootloader\hal``:

* ``flash.c``: functions to provide In Application Programming (IAP)
* ``gpio.c``: functions to init the on board led/reset button interrupt
* ``read_uid.c``: Read of the chip unique ID
* ``usbd_XXX.c``: low-level driver for the USB device controller.  This file contains all the low level functions used by the MDK USB device stack to access the USB controller
* ``vector_table.c``: Relocation of the interrupt vector table

The current implementations are:
   
* **LPC11U35**: ``bootloader\hal\TARGET_NXP\TARGET_LPC11U35``

##Flash Algorithms

The CMSIS-DAP Interface Firmware, to be able to flash a new image on the target microcontroller, needs to have a flash algorithm (a sequence of binary instructions) to be loaded on the RAM of the target itself.

The flash algorithm is developed as a small application compiled as *position independent* code and stored in the interface code as a "binary blob".

We provide two such MDK projects for generating the flash algorithms for two family of microcontrollers:
   
* ``interface\flash_algo_mdk\LPC_IAP\LPC_IAP.uvproj``: flash algorithm for NXP LPC family
* ``interface\flash_algo_mdk\MKXXX\MKXX.uvproj``: flash algorithm for Freescale MK family

These projects have multiple configurations for the different sizes of the flash memory within the supported family of microcontrollers.

Once you have generated the position independent flash algorithm, we provide scripts for generating the code to be included in the interface project for your target.

Copy the output elf binary ".axf" to ``tools\tmp\flash_algo.axf`` and run:

```python

	tools> python flash_algo_gen.py
```

This will generate a text file named ``**tools\tmp\flash_algo.txt**`` that will look like this:

```python

	const uint32_t flash_algo_blob[] = {
		0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,

		/*0x020*/ 0x28100b00, 0x210ed302, 0xd0eb01, 0x494f4770, 0x607af44f, 0x60084449, 0x2100484d, 0x21aa7001,
		/*0x040*/ 0x21557301, 0x21017301, 0x1c40f800, 0x47702000, 0x47702000, 0x41f0e92d, 0x20324c46, 0x2500444c,
		/*0x060*/ 0xe884261dL, 0xf1040061L, 0x4f430114, 0x46204688, 0x696047b8, 0x2034b960, 0x61e884, 0x4641483b,
		/*0x080*/ 0x68004448, 0x462060e0, 0x696047b8, 0xd0002800L, 0xe8bd2001L, 0xe92d81f0L, 0xf7ff41f0L, 0x4d35ffc1,
		/*0x0A0*/ 0x444d4604, 0xe9c52032L, 0xf1050400L, 0x4e320114, 0x4628460f, 0x47b060ac, 0xb9686968L, 0xe9c52034L,
		/*0x0C0*/ 0x482a0400, 0x444860ac, 0x68004639, 0x462860e8, 0x696847b0, 0xd0dc2800L, 0xe7da2001L, 0x41f0e92d,
		/*0x0E0*/ 0x64614, 0x4825d11d, 0x12fcf8d4, 0xd03a4281L, 0x42814823, 0x4823d037, 0xd0344281L, 0x4030ea4f,
		/*0x100*/ 0xd0304281L, 0x100e9d4, 0xe9d44408L, 0x44111202, 0x69214408, 0x69614408, 0x69a14408, 0x42404408,
		/*0x120*/ 0x463061e0, 0xff7cf7ffL, 0x21324d12, 0x4f12444d, 0x1000e9c5, 0x114f105, 0x468860a8, 0x47b84628,
		/*0x140*/ 0xb9806968L, 0xe9c52033L, 0xf44f0600L, 0xe9c57000L, 0x48064002, 0x44484641, 0x61286800, 0x47b84628,
		/*0x160*/ 0x28006968, 0x2001d095, 0xe793, 0x4, 0x400fc080, 0x8, 0x1fff1ff1, 0x4e697370,
		/*0x180*/ 0x12345678, 0x87654321L, 0x0, 0x0,
	};
	
	static const TARGET_FLASH flash = {
		0x1000002F, // Init
		0x10000051, // UnInit
		0x10000055, // EraseChip
		0x10000097, // EraseSector
		0x100000DD, // ProgramPage
```

##Interface

Currently, two microcontrollers are supported:
   
* **LPC11U35**: ``interface\mdk\lpc11u35\lpc11u35_interface.uvproj``
* **KL25Z**: ``interface\mdk\kl25z\kl25z_interface.uvproj``

Each of these projects provides multiple configurations, to:
   
* Support different targets: providing a different flash algorithm and reset/unlock sequences
* Standalone build at address ``0x0`` (useful during development for better debugging) / Bootloader build at address ``0x5000`` ready to be loaded by the bootloader.

###Supporting a new target

We keep the target dependent code in two files:
   
* ``target_flash.h``: Implements an API to load a new binary into the flash of the target, largely generated from the above Flash Algorithm project
* ``target_reset.c``: provides function in order to unlock/set the target in a specific state

The current target implementations are:
   
* **LPC812**: ``interface\target\hal\DBG_NXP\DBG_LPC812``
* **LPC1768**: ``interface\target\hal\DBG_NXP\DBG_LPC1768``
* **KL25Z**: ``interface\target\hal\DBG_Freescale\DBG_KL25Z``
* **KL46Z**: ``interface\target\hal\DBG_Freescale\DBG_KL46Z``
* **KL05Z**: ``interface\target\hal\DBG_Freescale\DBG_KL05Z``

###Porting to a New Interface Chip

When you are porting the CMSIS-DAP Interface Firmware to a new chip, you should first be sure to have the correspondent CMSIS-CORE files in the ``shared\cmsis`` folder.

To simplify the effort of porting the bootloader to a new interface chip, we have kept together the majority of the target dependent code in the directory ``interface\hal``:
   
* ``DAP_config.h``: implements gpio driver to drive the SWD lines of the target chip.
* ``gpio.c``: functions to init the on board led/reset button interrupt.
* ``read_uid.c``: Read of the chip unique ID.
* ``usbd_XXX.c``: low-level driver for the USB device controller.  This file contains all the low level functions used by the MDK USB device stack to access the USB controller.
* ``uart.c``: provides low level driver to access the uart for the usb <-> uart pipe.
* ``usb_buf.h``: declares the usb_buffer array. This is interface dependent because the developer may want to put this array into a specific location in memory.

The current implementations are:
   
* **LPC11U35**: ``interface\interface\hal\TARGET_NXP\TARGET_LPC11U35``
* **MK20DX**: ``interface\interface\hal\TARGET_Freescale\TARGET_MK20DX``

##Concatenated Production Image

The final production image will be a single binary containing the bootloader code at address ``0x0`` and the interface firmware at address ``0x5000``. We do provide a simple script for concatenating these two images that is knowledgeable of the path conventions for the generate elf file of the different projects. It takes as input option the name of the interface and target microcontrollers. For example, for generating the image for an LPC11U35 interface targeting a LPC1768, you can use the following command line:

```python

	tools> python concat.py -i LPC11U35 -t LPC1768
```

This will generate the file: ``tools\tmp\if_lpc11u35_target_lpc1768.bin``