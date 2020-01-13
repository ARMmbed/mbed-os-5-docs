# Style

The Arm Mbed OS codebase is hosted on GitHub, and you can submit new features or bug fixes. Please follow the [guidelines for GitHub pull requests](../contributing/workflow.html#guidelines-for-github-pull-requests) and the [coding style guide](#coding-style) in your submissions.

<span class="tips">**Tip:** Please also read the [workflow](../contributing/workflow.html) section for a review of the process and legal requirements.</span>

## Code acceptance

After the code has gone through automated testing, developers will take a look and comment on the pull request. If all is well and acceptable, your code will be ready for merging into the central development branch.

## Coding style

Whether you're writing new code or fixing bugs in existing code, please follow the Mbed OS coding style.

Mbed OS follows the [K&R style](https://en.wikipedia.org/wiki/Indent_style#K.26R_style), with at least two exceptions (see [Rules](#rules)).

The only exception to this coding style involves third-party code. Third-party code should be added to the `.astyleignore` file located in the Mbed OS root directory.

You can use [Artistic Style (AStyle)](http://sourceforge.net/projects/astyle/files/) to format your code. Use the command-line switch to select the correct style and point to the file you want to edit:

```
astyle -n --options=.astylerc $(full_path_to_file)
```

File `.astylerc` defines Mbed OS code style and it's in the Mbed OS root directory.

### Code sample

```c TODO
static const PinMap PinMap_ADC[] = {
    {PTC2, ADC0_SE4b, 0},
    {NC , NC , 0}
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

### Rules

- Indentation - four spaces. Please do not use tabs.
- Braces - K&R style.
- One true brace style (1TBS) - use braces for statements of type `if`, `else`, `while` and `for` (exception [from K&R](http://en.wikipedia.org/wiki/Indent_style#Variant:_1TBS)).
- One line per statement.
- Preprocessor macro starts at the beginning of a new line; the code inside is indented according to the code above it.
- Cases within `switch` are indented (exception from K&R).
- Space after statements of type `if`, `while`, `for`, `switch`. The same applies to binary operators (like, `+` and `*`) and the ternary operator (`?` and `:`).
- Each line preferably has at most 120 characters.
- Comments should use proper spelling and grammar.
- For pointers or references, the symbols `*` or `&` are adjacent to a name (`analogin_t *obj`. `analogin_t &obj`). If you omit the name, place the space between the type and `*` (such as `int *` or `int &`).
- For function return pointers or references, the symbols `*` or `&` are adjacent to a function name (`int *func()` or `int &func()`).
- Don't leave trailing spaces at the end of lines.
- Empty lines should have no trailing spaces.
- Unix line endings are default option for files.
- Use capital letters for macros.
- A file should have an empty line at the end.

### Naming conventions

#### Classes

- Begin with a capital letter, and each word within a class also begins with a capital letter (AnalogIn, BusInOut).
- Methods contain small letters, with words separated by underscore.
- Private members start with an underscore: ``__User defined types (typedef)))``.
- Structures - `suffix _t` - to denote it is a user-defined type.
- Enumeration - the type name and values name - same naming convention as classes (for example MyNewEnum).

#### Functions

- Contain lower case letters (as methods within classes).
- Words separated by underscore (wait_ms, read_u16).

An example:

```cPP TODO
#define ADC_INSTANCE_SHIFT 8

class AnalogIn {
public:
    /** Create an AnalogIn connected to the specified pin.
     *
     * @param pin AnalogIn pin to connect to
     * @param name (optional) A string to identify the object
     */
    AnalogIn(PinName pin)
    {
        analogin_init(&_adc, pin);
    }

    /** Read the input voltage, represented as a float in the range [0.0, 1.0].
     *
     * @returns
     * 	A floating-point value representing the current input voltage, measured as a percentage
     */
    uint32_t read()
    {
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

#### Namespaces

Namespaces used to group subsystems are lower case, such as `rtos` and `event`. If not in a specific subsystem, C++ APIs are in namespace `mbed`. A few APIs remain in the global namespace for backward compatibility.

Occasionally, namespaces are used to act as-if "static singleton" objects. One example is namespace `ThisThread` in `rtos` (which was modeled after C++11 `std::this_thread`). These namespaces follow the class naming convention, so calls to their functions look like calls to static class methods. 

Below is an example of typical namespace use in a source file:

```
    using namespace rtos;
    
    ThisThread::sleep_for(1000);
    
```

### Doxygen documentation

All functions and methods should contain documentation using Doxygen.

## Compiler settings

All C and C++ code submitted to Mbed OS must compile with GCC Arm Embedded, Arm Compiler 6 and IAR EWARM. Mbed OS:

- Uses the GNU11 standard for C.
- Uses the GNU++14 standard for C++.
- Sets the `char` type to unsigned.
- Disables C++ exceptions.
- Disables C++ runtime type information.
- Disables variable length arrays (C++ only).
