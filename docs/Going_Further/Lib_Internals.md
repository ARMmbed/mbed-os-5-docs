#mbed Library Internals

This document describes the internals of the mbed library. It should be helpful for:
* Porting the mbed library to a new microcontroller
* Adding a driver for a new peripheral
* Providing support for a new toolchain

This document assumes that you are familiar with the C Programming Language, but it does not assume a deep knowledge of microcontrollers.

##Design Overview

The mbed library provides abstractions for the microcontroller (MCU) hardware (in particular drivers for the MCU peripherals) and it is divided in the following software layers and APIs:

<span style="text-align:center; display:block;">
![](/Going_Further/Images/Lib_Intern/Layers.png)
</span>

To port the mbed library to a new microcontroller you will have to provide the two software layers marked as "MCU dependent" in the above diagram.

To present the role of each of these layers in a peripheral driver, we will show how the driver for the General Purpose Input/Output (GPIO) for the LPC1768 is structured, from the bottom up. For each layer we will also provide an implementation of the same simple example application: the toggling of an LED ("blinky").

###mbed library sources in the online IDE

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
If you need to edit the mbed library, you can delete the binary build of the mbed library from your project and [import its sources](http://developer.mbed.org/users/mbed_official/code/mbed-src/).
</span>

###Directory Structure

In the image below you can see the directory structure of the sources constituting the mbed library as they are published on the official [mbed github repository](https://github.com/mbedmicro/mbed).

Three target independent directories:

* ``mbed/api``: The headers defining the actual mbed library API

* ``mbed/common``: mbed common sources

* ``mbed/hal``: The HAL API to be implemented by every target

Two target dependent directories:

* ``mbed/targets/hal``: The HAL implementations

* ``mbed/targets/cmsis``: CMSIS-CORE sources

<span style="text-align:center; display:block;">
![](/Going_Further/Images/Lib_Intern/Direct.png)
</span>

##MCU Registers

###Peripherals

If you come from a software background and you want to understand the behaviour of a microcontroller peripheral using a software analogy, you can think of a peripheral like a software thread being executed by a separate core. You have only one communication channel with this thread: a shared area of memory. Each single addressable byte of this area of memory, used to communicate with the hardware, is called: register.  You communicate with the peripherals writing and reading these registers.

###LPC17xx GPIO

Silicon Vendors, like NXP, provide detailed user manuals describing the registers of each peripheral.

This is a page from the [|LPC17xx user manual](http://www.nxp.com/documents/user_manual/UM10360.pdf describing the registers of the GPIO peripheral:

<span style="text-align:center; display:block;">
![](/Going_Further/Images/Lib_Intern/GPIO_R.png)
</span>

###Blinky example poking registers

Let's see how to blink an LED on our LPC1768 mbed simply poking these registers: 

<span style="text-align:center; display:block;">
![](/Going_Further/Images/Lib_Intern/Blinky1.png)
</span>

<span style="text-align:center; display:block; padding:20px;">
![](/Going_Further/Images/Lib_Intern/Blinky2.png)
</span>

```c

	#include "mbed.h"

	// Reuse initialization code from the mbed library
	DigitalOut led1(LED1); // P1_18

	int main() {
		unsigned int mask_pin18 = 1 << 18;
		
		volatile unsigned int *port1_set = (unsigned int *)0x2009C038;
		volatile unsigned int *port1_clr = (unsigned int *)0x2009C03C;

		while (true) {
			*port1_set |= mask_pin18;
			wait(0.5);

			*port1_clr |= mask_pin18;
			wait(0.5);
		}
	}
```
 

##CMSIS-CORE

The [CMSIS-CORE](http://www.arm.com/products/processors/cortex-m/cortex-microcontroller-software-interface-standard.php) headers provide you a suitable data structure to access these low level registers:

```c

	typedef struct {
		__IO uint32_t FIODIR;
		uint32_t RESERVED0[3];
		__IO uint32_t FIOMASK;
		__IO uint32_t FIOPIN;
		__IO uint32_t FIOSET;	
		__O  uint32_t FIOCLR;
		} LPC_GPIO_TypeDef;

	#define LPC_GPIO_BASE   (0x2009C000UL)

	#define LPC_GPIO0       ((LPC_GPIO_TypeDef *) (LPC_GPIO_BASE + 0x00000))
	#define LPC_GPIO1       ((LPC_GPIO_TypeDef *) (LPC_GPIO_BASE + 0x00020))
	#define LPC_GPIO2       ((LPC_GPIO_TypeDef *) (LPC_GPIO_BASE + 0x00040))
	#define LPC_GPIO3       ((LPC_GPIO_TypeDef *) (LPC_GPIO_BASE + 0x00060))
	#define LPC_GPIO4       ((LPC_GPIO_TypeDef *) (LPC_GPIO_BASE + 0x00080))
```

As you can see the ``LPC_GPIO_TypeDef`` structure is a one to one map of its related GPIO port 32 bytes registers:

```c

	FIODIR   :  4 bytes
	RESERVED0: 12 bytes
	FIOMASK  :  4 bytes
	FIOPIN   :  4 bytes
	FIOSET   :  4 bytes
	FIOCLR   :  4 bytes	
	tot      : 32 bytes = 0x20 bytes
```

For example, in the GPIO documentation you can read that the address of the FIOPIN register of port 1 is: ``0x2009C034``.

We can point the content of that location using the  ``LPC_GPIO_TypeDef`` like that:

```c

	#include "mbed.h"

	int main() {
		printf("LPC_GPIO1->FIOSET: %p\n", &LPC_GPIO1->FIOSET);
	}
```

The above program will print:

```c

	LPC_GPIO1->FIOSET: 2009c038
```

###Blinky example using CMSIS-CORE

Let's see how to blink an LED on our LPC1768 mbed using the CMSIS-CORE API:

```c

	#include "mbed.h"

	// Reuse initialization code from the mbed library
	DigitalOut led1(LED1); // P1_18

	int main() {
		unsigned int mask_pin18 = 1 << 18;

		while (true) {
			LPC_GPIO1->FIOSET |= mask_pin18;
			wait(0.5);

			LPC_GPIO1->FIOCLR |= mask_pin18;
			wait(0.5);
		}
	}

```

###mbed additions to CMSIS-CORE

The mbed library provides certain additions to the CMSIS-CORE layer:

* startup file for each of the [Supported Toolchains](/Going_Further/Export/)

* linker file and support functions to define the [Memory Map](/Going_Further/Mem_Mo/)

* functions to set and get Interrupt Service Routines (ISR) addresses from the [Nested Vectored Interrupt Controller (NVIC)](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0552a/BABEDCBC.html) and to  program [Vector Table Offset Register (VTOR)](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0552a/Ciheijba.html).

##mbed HAL API

###Target independent API

The target independent HAL API is our foundation for the mbed target independent library. This is the GPIO HAL API:

```c

	typedef struct gpio_s gpio_t;
	
	void gpio_init (gpio_t *obj, PinName pin, PinDirection direction);

	void gpio_mode (gpio_t *obj, PinMode mode);
	void gpio_dir  (gpio_t *obj, PinDirection direction);

	void gpio_write(gpio_t *obj, int value);
	int  gpio_read (gpio_t *obj);
```

<span style="background-color:lightyellow; color:black; display:block; height:100%; padding:10px">
**Warning:** The HAL API is an internal interface used to help porting the mbed library to a new target and it is subject to change. If you want to "future proof" your application avoid using this API and use the mbed API instead. 
</span>

###Target dependent implementation

The implementation of the mbed HAL API should encapsulate all the required target dependent code.

There are multiple ways to implement such API, with different trade-offs. In our implementation for the LPC family of processors (LPC2368, LPC1768, LPC11U24) we decided to keep all the differences among these processors in the GPIO object initialization keeping all the GPIO "methods" small, fast and target independent. Additionally, for speed optimization, we allow the GPIO functions to be completely inlined by the compiler.

In this document, to have a clear presentation of the code, we are removing the preprocessor directives for target conditional code and we are grouping together function definitions from multiple sources (``.c`` and ``.h``):

```c

	struct gpio_s {
		PinName  pin;
		uint32_t mask;

		__IO uint32_t *reg_dir;
		__IO uint32_t *reg_set;
		__IO uint32_t *reg_clr;
		__I  uint32_t *reg_in;
	};

	void gpio_init(gpio_t *obj, PinName pin, PinDirection direction) {
		if(pin == NC) return;

		obj->pin = pin;
		obj->mask = gpio_set(pin);

		LPC_GPIO_TypeDef *port_reg = (LPC_GPIO_TypeDef *) ((int)pin & ~0x1F);

		obj->reg_set = &port_reg->FIOSET;
		obj->reg_clr = &port_reg->FIOCLR;
		obj->reg_in  = &port_reg->FIOPIN;
		obj->reg_dir = &port_reg->FIODIR;

		gpio_dir(obj, direction);
		switch (direction) {
			case PIN_OUTPUT: pin_mode(pin, PullNone); break;
			case PIN_INPUT : pin_mode(pin, PullDown); break;
		}
	}

	void gpio_mode(gpio_t *obj, PinMode mode)
		pin_mode(obj->pin, mode);
	}

	void gpio_dir(gpio_t *obj, PinDirection direction) {
		switch (direction) {
			case PIN_INPUT : *obj->reg_dir &= ~obj->mask; break;
			case PIN_OUTPUT: *obj->reg_dir |=  obj->mask; break;
		}
	}

	void gpio_write(gpio_t *obj, int value) {
		if (value)
			*obj->reg_set = obj->mask;
		else
			*obj->reg_clr = obj->mask;
	}

	int gpio_read(gpio_t *obj) {
		return ((*obj->reg_in & obj->mask) ? 1 : 0);
	}
```

###mbed internal conventions

As a practical convention, the ``PinName`` enum definition for each target contains information for both the ``port`` and the ``pin number``. How this information is stored can be target dependent.

For example, in the LPC1768 a ``PinName`` entry is the ``port address`` plus the ``pin number`` stored in the rightmost 5 bits. To extract the port address from an LPC1768 ``PinName`` we simply have to create a mask ignoring the rightmost 5 bits:

```c

	LPC_GPIO_TypeDef *port_reg = (LPC_GPIO_TypeDef *) ((int)pin & ~0x1F);
```

##mbed API

The mbed API is providing the actual friendly, object oriented API to the final user. This is the API used by the majority of the programs developed on the mbed platform.

We also define basic operators to provide intuitive casting to primitive types and assignments:


```c

	class DigitalInOut {

	public:
		DigitalInOut(PinName pin) {
			gpio_init(&gpio, pin, PIN_INPUT);
		}
	
		void write(int value) {
			gpio_write(&gpio, value);
		}

		int read() {
			return gpio_read(&gpio);
		}

		void output() {
			gpio_dir(&gpio, PIN_OUTPUT);
		}

		void input() {
			gpio_dir(&gpio, PIN_INPUT);
		}

		void mode(PinMode pull) {
			gpio_mode(&gpio, pull);
		}

		DigitalInOut& operator= (int value) {
			write(value);
			return *this;
		}

		DigitalInOut& operator= (DigitalInOut& rhs) {
			write(rhs.read());
			return *this;
		}

		operator int() {
			return read();
		}

	protected:
		gpio_t gpio;
	};
```

###Blinky example using the mbed API

This is the final, microcontroller independent, GPIO abstraction provided by the mbed library:

```c

	#include "mbed.h"

	DigitalOut led1(LED1);

	int main() {
		while (true) {
			led1 = 1;
			wait(0.5);

			led1 = 0;
			wait(0.5);
		}
	}
```

##C library retargeting

The C standard library stdio module provides many functions for file input and output.

The C standard library implementations provided by the various toolchains give the possibility to customise how these input/output are named and redirected. This customization is often called "C library retargeting".

The mbed library defines this C library retargeting in this file: ``mbed/src/common/stdio.cpp``.

This is an excerpt of the retargeting of (stdout, stdin and stderr) to an UART: 

```c

	#if DEVICE_SERIAL
	extern int stdio_uart_inited;
	extern serial_t stdio_uart;
	#endif

	static void init_serial() {
	#if DEVICE_SERIAL
		if (stdio_uart_inited) return;
		serial_init(&stdio_uart, STDIO_UART_TX, STDIO_UART_RX);
		serial_format(&stdio_uart, 8, ParityNone, 1);
		serial_baud(&stdio_uart, 9600);
	#endif
	}

	extern "C" FILEHANDLE PREFIX(_open)(const char* name, int openmode) {
		/* Use the posix convention that stdin,out,err are filehandles 0,1,2.
		*/
		if (std::strcmp(name, __stdin_name) == 0) {
			init_serial();
			return 0;
		} else if (std::strcmp(name, __stdout_name) == 0) {
			init_serial();
			return 1;
		} else if (std::strcmp(name,__stderr_name) == 0) {
			init_serial();
			return 2;
		}
	[...]
		
	#if defined(__ICCARM__)
	extern "C" size_t    __write (int        fh, const unsigned char *buffer, size_t length) {
	#else
	extern "C" int PREFIX(_write)(FILEHANDLE fh, const unsigned char *buffer, unsigned int length, int mode) {
	#endif
		int n; // n is the number of bytes written
		if (fh < 3) {
	#if DEVICE_SERIAL
		if (!stdio_uart_inited) init_serial();
        for (unsigned int i = 0; i < length; i++) {
            serial_putc(&stdio_uart, buffer[i]);
        }
	#endif
			n = length;
		} else {
	[...]

	#if defined(__ICCARM__)
	extern "C" size_t    __read (int        fh, unsigned char *buffer, size_t       length) {
	#else
	extern "C" int PREFIX(_read)(FILEHANDLE fh, unsigned char *buffer, unsigned int length, int mode) {	
	#endif
		int n; // n is the number of bytes read
		if (fh < 3) {
			// only read a character at a time from stdin
	#if DEVICE_SERIAL
			*buffer = serial_getc(&stdio_uart);
	#endif
			n = 1;
		} else {
	[...]
```
