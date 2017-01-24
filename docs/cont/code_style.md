# Code contributions: GitHub pull requests and code style guide

The mbed OS code base is hosted on GitHub, and you can submit new features or bug fixes. Please follow the [guidelines for GitHub pull requests](#guidelines-for-github-pull-requests) and the [coding style guide](#coding-style) in your submissions.

<span class="tips">**Tip:** Please also read the section [Creating and publishing your own libraries and contributing to mbed OS](contributing.md) for a review of the process and legal requirements.</span>

## Guidelines for GitHub pull requests

Pull requests on GitHub have to meet a number of requirements in order to keep the code and commit history clean:

* Commits should always contain a proper description of their content. Start with a concise and sensible one-line description, then elaborate on reasoning of the choices taken, descriptions for reviewers and other information that might otherwise  be lost.
* Commits should always be written to allow publication, so they can never contain confidential information, reference private documents, links to intranet locations, or rude language.
* Each commit should be the minimum self-contained commit for a change. A commit should always result in a new state that is again in a compilable state. Large changes should (if possible) be split up into logical smaller commits that help reviewers follow the reasoning behind the full change.
* Commits should follow [Chris Beam’s seven rules of great commit messages](http://chris.beams.io/posts/git-commit#seven-rules):
	1. Separate subject from body with a blank line.
	1. Limit the subject line to 72 characters (note that this is a deviation from Beam's standard).
	1. Capitalize the subject line.
	1. Do not end the subject line with a period.
	1. Use the imperative mood in the subject line.
	1. Wrap the body at 72 characters.
	1. Use the body to explain _what_ and _why_ vs _how_.
* Since we use GitHub and explicit CLAs, special commit tags that other projects might use, like “Reviewed-by”, or “Signed-off-by”, are redundant and should be omitted. GitHub keeps track of who reviewed what and when, and our stack of signed CLAs shows us who has agreed to our development contribution agreement.
* Prefixing your commit message with a domain is acceptable and recommended where it makes sense to do so. However, prefixing one's domain with the name of the repo is not useful. For example, making a commit entitled "mbed-drivers: Fix doppelwidget frobulation" to the mbed-drivers repo would not be acceptable, as it is already understood that the commit applies to "mbed-drivers". Renaming the commit to "doppelwidget: Fix frobulation" would be better, if we presume that "doppelwidget" is a meaningful domain for changes, as it communicates that the change applies to the doppelwidget area of mbed-drivers.

## Code acceptance

[After the CLA](contributing.md) is in place and the code has gone through automated testing, developers will take a look and comment on the pull request. If all is well and acceptable, your code will be ready for merging into the central development branch.

## Coding style

Whether you're writing new code or fixing bugs in existing code, please follow the mbed OS coding style. 

mbed OS follows the [K&R style](https://en.wikipedia.org/wiki/Indent_style#K.26R_style), with at least two exceptions (which can be found in the list below the code sample).

#### Code sample

```c
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
#### Rules

* Indentation - four spaces. Please do not use tabs.

* Braces - K&R style

* One true brace style (1TBS) - use braces for statements of type `if`, `else`, `while` and `for` (exception [from K&R](http://en.wikipedia.org/wiki/Indent_style#Variant:_1TBS)). 

* One line per statement

* Preprocessor macro starts at the beginning of a new line, the code inside is indented according to the code above it.

* Cases within `switch` are indented (exception from K&R).

* Space after statements of type `if`, `while`, `for`, `switch`. The same applies to binary operators (like, `+` and `*`) and the ternary operator (`?` and `:`).

* Each line preferably has at most 120 characters.

* Comments should use proper spelling and grammar.

* For pointers, `*` is adjacent to a name (analogin_t *obj).

* Don't leave trailing spaces at the end of lines.

* Empty lines should have no trailing spaces.

* Unix line endings are default option for files.

* Use capital letters for macros.

* A file should have an empty line at the end.

#### Naming conventions

__Classes__

* Begins with a capital letter, and each word in it also begins with a capital letter (AnalogIn, BusInOut).

* Methods contain small letters, with words separated by underscore.

* Private members starts with an underscore: ``__User defined types (typedef)))``.

* Structures - suffix _t - to denote it is a user defined type.

* Enumeration - the type name and values name - same naming convention as classes (for example MyNewEnum).

__Functions__

* Contain lower case letters (as methods within classes)

* Words separated by underscore (wait_ms, read_u16)

As an example:

```c
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

#### Doxygen documentation

All functions and methods should contain documentation using Doxgyen.

<span class="tips">**Tip:** You can publish your documentation on docs.mbed.com. See our [publishing guide](https://docs.mbed.com/docs/writing-and-publishing-guides/en/latest/publishing_guide/) for more details.</span>

You can use [Artistic Style (AStyle)](http://sourceforge.net/projects/astyle/files/) to format your code. Use the command-line switch to select the correct style and point to the file you want to edit:

```
astyle.exe --style=kr --indent=spaces=4 --indents-switches $(full_path_to_file)
```

