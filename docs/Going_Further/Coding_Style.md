#Coding Style

This page describes mbed coding style. Our goal is the files written in mbed SDK conform this standard (exceptions are there, for instance 3rd libraries supplied by partners). 

Be consistent.

The mbed SDK code follows [K&R style](http://en.wikipedia.org/wiki/Indent_style#K.26R_style) with at least two exceptions that can be found in the list below the code snippet.

```c
	
	static const PinMap PinMap_ADC[] = {
		{PTC2, ADC0_SE4b, 0},
		{NC  , NC       , 0}
	};

	uint32_t adc_function(analogin_t *obj, uint32_t options)
	{
		uint32_t instance = obj->adc >> ADC_INSTANCE_SHIFT;
		switch (options) {
			case 1:
				timeout = 6;
				break;
			default:
				timeout = 10;
				break;
		}

		while (!adc_hal_is_conversion_completed(instance, 0)) {
			if (timeout == 0) {
				break;
			} else {
				timeout--;
			}
		}

		if (obj->adc == ADC_CHANNEL0) {
			adc_measure_channel(instance);
			adc_stop_channel(instance);
		} else {
			error("channel not available");
		}

	#if DEBUG
		for (uint32_t i = 0; i < 10; i++) {
			printf("Loop : %d", i);
		}
	#endif
		return adc_hal_get_conversion_value(instance, 0);
	}
```

##Rules

* Indentation - 4 spaces. Please do not use tabs.
* Braces - K&R, except for functions where the opening brace is on the new line.
* 1 TBS - use braces for statements if, else, while, for [exception from K&R](http://en.wikipedia.org/wiki/Indent_style#Variant:_1TBS)
* One line per statement
* Preprocessor macro starts at the beginning of a new line, the code inside is indented accordingly the code above it
* Cases within switch are indented (exception from K&R)
* Space after statements if, while, for, switch, same applies to binary and ternary operators
* Each line has preferably at most 120 characters
* For pointers, '*' is adjacent to a name (analogin_t *obj)
* Don't leave trailing spaces at the end of lines
* Empty lines should have no trailing spaces
* Unix line endings are default option for files
* Use capital letters for macros
* A file should have an empty line at the end

##Naming convention

Classes 

* Begins with a capital letter, and each word in it begins also with a capital letter (AnalogIn, BusInOut). 
* Methods contain small letters, distinct words separated by underscore. 
* Private members starts with an underscore.

User defined types (typedef)

* Structures - suffix _t - to denote it is user defined type
* Enumeration - the type name and values name  - same naming convention as classes (e.g MyNewEnum)

Functions

* contain lower case letters (as methods within classes)
* distinct words separated by underscore (wait_ms, read_u16)

```c

	#define ADC_INSTANCE_SHIFT 8

	class AnalogIn {
	public:
		/** Create an AnalogIn, connected to the specified pin
		*
		* @param pin AnalogIn pin to connect to
		* @param name (optional) A string to identify the object
		*/
		AnalogIn(PinName pin) {
			analogin_init(&_adc, pin);
		}

		/** Read the input voltage, represented as a float in the range [0.0, 1.0]
		*
		* @returns
		*    A floating-point value representing the current input voltage, measured as a percentage
		*/
		uint32_t read() {
			return analogin_read(&_adc, operation);
		}

	protected:
		analogin_t _adc;
	};

	typedef enum {
		ADC0_SE0 = (0 << ADC_INSTANCE_SHIFT) | 0,
	} ADCName;

	struct analogin_s {
		ADCName adc;
	};

	typedef struct analogin_s analogin_t;
```

##Doxygen documentation

All functions/methods should contain a documentation using doxygen javadoc in a header file. More information regarding writing API Documentation, follow the [link](/Going_Further/Docu/).

```c
	
	#ifndef ADC_H
	#define ADC_H

	#ifdef __cplusplus
	extern "C" {
	#endif

	/** ADC Measurement method
	*
	*  @param obj Pointer to the analogin object.
	*  @param options Options to be enabled by ADC peripheral.
	*
	*  @returns
	*    Measurement value on defined ADC channel.
	*/
	uint32_t adc_function(analogin_t *obj, uint32_t options) 

	#ifdef __cplusplus
	}
	#endif

	#endif
```

##Source code indenter

In Mbed project you can use AStyle ([Artistic Style](http://astyle.sourceforge.net/)) source code indenter to help you auto format your source code. It will for sure not correct all your coding styles but for sure will eliminate most of them.
You can download AStyle from this [location](http://sourceforge.net/projects/astyle/files/).

Official Mbed SDK styles include below AStyle styles (defined by command line switched):

``--style=kr --indent=spaces=4 --indent-switches``

To format your file you can execute below command. Just replace **$(FULL_CURRENT_PATH)** with path to your source file.

``astyle.exe --style=kr --indent=spaces=4 --indent-switches $(FULL_CURRENT_PATH)``