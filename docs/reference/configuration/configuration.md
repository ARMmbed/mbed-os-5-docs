## The configuration system

The Arm Mbed OS configuration system, a part of the Arm Mbed OS build tools, customizes compile time configuration parameters. Each library may define a number of configuration parameters in its `mbed_lib.json`. `mbed_app.json` may override the values of these configuration parameters. Configuration is defined using [JSON](http://www.json.org/). Some examples of configuration parameters:

- The sampling period for a data acquisition application.
- The default stack size for a newly created OS thread.
- The receive buffer size of a serial communication library.
- The flash and RAM memory size of an Mbed target.

The Arm Mbed OS configuration system gathers and interprets the configuration defined in the target in its [target configuration](../reference/adding-and-configuring-targets.html), all `mbed_lib.json` files and the `mbed_app.json` file. The configuration system creates a single header file, `mbed_config.h`, that contains all of the defined configuration parameters converted into C preprocessor macros. `mbed compile` places `mbed_config.h` in the build directory, and `mbed export` places it in the application root. `mbed compile` runs the Mbed configuration system before invoking the compiler, and `mbed export` runs the configuration system before creating project files.

<span class="notes">**Note:** Throughout this document, "library" means any reusable piece of code within its own directory.</span>

<span class="notes">**Note:** In prior releases, the configuration system provided a method for adding custom targets. The Mbed OS tools now look for custom targets in a file named `custom_targets.json` in the root of an application and treat custom targets the same as [Mbed targets](../reference/adding-and-configuring-targets.html).</span>

<span class="notes">**Note:** This document only deals with passing macros to part of the toolchain suite. For documentation about how to control other flags to the compiler see the [build profiles documentation](../tools/build-profiles.html).</span>

### Examining available configuration parameters

Mbed CLI includes a command for listing and explaining the compile time configuration, `mbed compile --config`. This command prints a summary of configuration parameters, such as:

```
Configuration parameters
------------------------
cellular.random_max_start_delay = 0 (macro name: "MBED_CONF_CELLULAR_RANDOM_MAX_START_DELAY")
cellular.use-apn-lookup = 1 (macro name: "MBED_CONF_CELLULAR_USE_APN_LOOKUP")
configuration-store.storage_disable = 0 (macro name: "CFSTORE_STORAGE_DISABLE")
drivers.uart-serial-rxbuf-size = 256 (macro name: "MBED_CONF_DRIVERS_UART_SERIAL_RXBUF_SIZE")
drivers.uart-serial-txbuf-size = 256 (macro name: "MBED_CONF_DRIVERS_UART_SERIAL_TXBUF_SIZE")
events.present = 1 (macro name: "MBED_CONF_EVENTS_PRESENT")
events.shared-dispatch-from-application = 0 (macro name: "MBED_CONF_EVENTS_SHARED_DISPATCH_FROM_APPLICATION")
events.shared-eventsize = 256 (macro name: "MBED_CONF_EVENTS_SHARED_EVENTSIZE")
events.shared-highprio-eventsize = 256 (macro name: "MBED_CONF_EVENTS_SHARED_HIGHPRIO_EVENTSIZE")
events.shared-highprio-stacksize = 1024 (macro name: "MBED_CONF_EVENTS_SHARED_HIGHPRIO_STACKSIZE")
events.shared-stacksize = 1024 (macro name: "MBED_CONF_EVENTS_SHARED_STACKSIZE")
<output truncated for brevity>
```

Use the `-v` switch to include the help text defined with the configuration parameter, where the value of the configuration parameter is defined, and other details. The command `mbed compile --config -v` in the same application as above prints:

```
Configuration parameters
------------------------
Name: cellular.random_max_start_delay
    Description: Maximum random delay value used in start-up sequence in milliseconds
    Defined by: library:cellular
    No value set
Name: cellular.use-apn-lookup
    Description: Use APN database lookup
    Defined by: library:cellular
    Macro name: MBED_CONF_CELLULAR_USE_APN_LOOKUP
    Value: 1 (set by library:cellular)
Name: configuration-store.storage_disable
    Description: Configuration parameter to disable flash storage if present. Default = 0, implying that by default flash storage is used if present.
    Defined by: library:configuration-store
    No value set
<output truncated for brevity>
```

### Using configuration data in code

When compiling or exporting, the configuration system generates C preprocessor macro definitions of the configuration parameters. The configuration system writes these definitions in a file named `mbed_config.h` located in the build directory. When compiling the same example as the prior section for target `K64F`, the `mbed_config.h` file includes this snippet (note that the order of the definitions may be different):

```C NOCI
// Automatically generated configuration file.
// DO NOT EDIT, content will be overwritten.

#ifndef __MBED_CONFIG_DATA__
#define __MBED_CONFIG_DATA__

// Configuration parameters
#define MBED_CONF_CELLULAR_RANDOM_MAX_START_DELAY         0 // set by library:cellular
#define MBED_CONF_CELLULAR_USE_APN_LOOKUP                 1 // set by library:cellular
<file truncated for brevity>
```

The name of the macro for a configuration parameter is either a prefixed name or explicitly specified by `macro_name`. The configuration system constructs a prefixed name from the prefix `MBED_CONF_`, followed by the name of the library or `APP`, followed by the name of the parameter. The configuration system then capitalizes the prefixed name and converts it to a valid C macro name. For example, the configuration system converts the `random_max_start_delay` configuration parameter in the library `cellular` to `MBED_CONF_CELLULAR_RANDOM_MAX_START_DELAY`.

The Mbed OS build tools instruct the compiler to process the file `mbed_config.h` as if it were the first include of any C or C++ source file, so you do not have to include `mbed_config.h` manually.

Do not edit `mbed_config.h` manually. It may be overwritten the next time you compile or export your application, and you will lose all your changes.

### Configuration parameters in `mbed_app.json`, `mbed_lib.json`

An application may have one `mbed_app.json` in the root of the application and many `mbed_lib.json` files throughout the application. When present, `mbed_app.json` may override configuration parameters defined in libraries and the target and define new configuration parameters.

#### Overriding configuration parameters

The configuration system allows a user to override any defined configuration parameter with a JSON object named `"target_overrides"`.

The keys in the `"target_overrides"` section are the names of a target that the overrides apply to, or the special wildcard `*` that applies to all targets. The values within the `"target_overrides"` section are objects that map configuration parameters, as printed by `mbed compile --config`, to new values. See the example `"target_overrides"` section below.

```JSON
"target_overrides": {
    "*": {
        "cellular.random_max_start_delay": "100"
    },
    "K64F": {
        "cellular.use-apn-lookup": false
    }
}
```

Examining the configuration for the target `LPC1768` with `mbed compile --config -m LPC1768` results in the following configuration:

```
Configuration parameters
------------------------
cellular.random_max_start_delay = 100 (macro name: "MBED_CONF_CELLULAR_RANDOM_MAX_START_DELAY")
cellular.use-apn-lookup = 1 (macro name: "MBED_CONF_CELLULAR_USE_APN_LOOKUP")
<output truncated for brevity>
```

Examining the configuration for the target `K64F` with `mbed compile --config -m K64F` results in the following configuration:

```
Configuration parameters
------------------------
cellular.random_max_start_delay = 100 (macro name: "MBED_CONF_CELLULAR_RANDOM_MAX_START_DELAY")
cellular.use-apn-lookup = 0 (macro name: "MBED_CONF_CELLULAR_USE_APN_LOOKUP")
<output truncated for brevity>
```

The order in which overrides are considered is:

 1. Libraries override target configuration with `mbed_lib.json`.
 2. The application overrides target and library configuration with `mbed_app.json`

#### Defining configuration parameters

The configuration system understands configuration parameters that targets, libraries and applications define using a JSON object called "config".

For example:

```JSON
{
    "config": {
        "param1": {
            "help": "The first configuration parameter",
            "macro_name": "CUSTOM_MACRO_NAME",
            "value": 0
        },
        "param2": {
            "help": "The second configuration parameter",
            "required": true
        },
        "param3": {
            "help": "The third configuration parameter",
            "value_min": 0,
            "value_max": 10,
            "value": 5
        },
        "param4": {
            "help": "The fourth configuration parameter",
            "accepted_values": ["test1", "test2", "0x1000"],
            "value": "test2"
        },
        "param5": {
            "help": "The fifth configuration parameter",
            "value": null
        },
        "param6": 10
    }
}
```

You define a configuration parameter by specifying its name as the key and specifying its value either with a description object or by value. Leaving the value field undefined or setting the value field to `null` will allow the parameter to be stored as a configuration option and appear with the `mbed compile --config` command; however, the key will not be defined in `mbed_config.h` and will not affect the application or OS unless it is overridden. See `param2` and `param5` for examples of this. The JSON fragment above defines six configuration parameters named `param1`, `param2`, `param3`, `param4`, `param5` and `param6`.

Above, the configuration parameters `param1` through `param5` are defined using a description object. The description object supports the following keys:

  - `help`: an optional help message that describes the purpose of the parameter.
  - `value`: an optional field that defines the value of the parameter.
  - `value_min`: an optional field that defines the minimum acceptable value of the parameter.
  - `value_max`: an optional field that defines the maximum acceptable value of the parameter.
  - `accepted_values`: an optional field that defines a list of acceptable values for the parameter.
  - `required`: an optional key that specifies whether the parameter must have a value before compiling the code (`false` by default). It's not possible to compile a source tree with one or more required parameters that don't have a value. Generally, setting `required` to true is only useful when `value` is not set.
  - `macro_name`: an optional name for the macro defined at compile time for this configuration parameter. The configuration system automatically figures out the corresponding macro name for a configuration parameter, but the user can override this automatically computed name by specifying `macro_name`.

You define a macro by value by using an integer or string instead of the description object, such as `param3` above.  Defining a parameter by value is equivalent to a configuration parameter defined with a description object with the key `value` set to the value in place of the description object, the key `help` unset, the key `macro_name` unset, and the key `required` set to `false`.

<span class="notes">**Note:** The name of a parameter in `config` can't contain a dot (`.`) character.</span>

The configuration system appends a prefix to the name of each parameter, so a parameter with the same name in a library does not conflict with parameters of the same name in targets or other libraries. The prefix is:

| Location | Prefix |
| -------- | ------ |
| Target | `target.` |
| Any library | The name of the library, as found in the `name` section of `mbed_lib.json`, followed by a dot (.) |
| Application | `app.` |

### `mbed_lib.json` format specification

`mbed_lib.json` is a JSON formatted document that contains a root JSON Object. The keys within this object are sections. See the allowed sections and their meanings below:

| Section | Required | Meaning |
| ------- | -------- | ------- |
| `name`  | Yes      | Name of the library. Must be unique. May not be `app` or `target`.|
| `macros` | No | List of macros to define in `mbed_config.h`. |
| `config` | No | Configuration parameters defined for use in this library. |
| `target_overrides` | No | Overrides for target configuration parameters and configuration parameters of the current library. |

The following is an example library, `mylib`.

```JSON
{
    "name": "mylib",
    "config": {
        "buffer_size": 1024,
        "timer_period": {
            "help": "The timer period (in us)",
            "macro_name": "INTERNAL_GPTMR_PERIOD",
            "required": true
        },
        "queue_size": {
            "help": "Size of event queue (entries)",
            "value": 10
        }
    },
    "macros": ["MYMOD_MACRO1", "MYMOD_MACRO2=\"TEST\""],
    "target_overrides": {
        "K64F": {
             "timer_period": 100,
             "queue_size": 40
        },
        "NXP": {
             "queue_size": 20,
             "buffer_size": 128,
             "target.features_add": ["IPV4"]
        }
    }
}
```

In this JSON file:

- `name` is the name of the library. **This is a required field.**
- `config` defines the configuration parameters of the library, as the section about [defining configuration parameters](#defining-configuration-parameters) explains.
- `macros` is a list of extra C preprocessor macros that are defined when compiling an application that includes this library.
- `target_overrides` is a dictionary with target-specific values for the configuration parameters.

All configuration parameters defined in `mylib` have a `mylib.` prefix. In `mbed_app.json`, `buffer_size` is accessible using the name `mylib.buffer_size`.

Use `target_overrides` to override the values of the parameters, depending on the current compilation target. The configuration system matches keys in `target_overrides` against target labels. (You can find a description of Mbed targets in our documentation about [adding and configuring targets](../reference/adding-and-configuring-targets.html).) If a key inside `target_overrides` matches one of the target labels, the parameter values change according to the value of the key.

It is an error for `mbed_lib.json` to override an undefined configuration parameter.

#### Overriding target attributes

Target configurations contain a set of attributes that you may manipulate with configuration. You may override these attributes as if they were a normal configuration parameter. Attributes may be cumulative, in which case they are a list of items. You may add to a cumulative attribute by overriding a configuration parameter with the name of the cumulative attribute suffixed with `_add` and remove from a cumulative attribute with the suffix `_remove`. When you override, add to or subtract from a cumulative attribute, the value must be a list of items to replace the definition with, add or remove. For example, add the value `IPV4` to a target's features list with the syntax:

```JSON
"target.features_add": ["IPV4"]
```

It is an error to both add and subtract the same value from a cumulative attribute. For a list of the attributes that you may overwrite, please see our documentation about [adding and configuring targets](../reference/adding-and-configuring-targets.html).

### `mbed_app.json` Specification

`mbed_app.json` may be present at the root of your application or specified as the argument of the `--app-config` parameter to `mbed compile` and `mbed export`. The configuration system interprets only one `mbed_app.json` during `mbed compile` or `mbed export`, unlike library configuration. Like `mbed_lib.json`, `mbed_app.json` is a JSON formatted document that contains a root JSON Object. The keys within this object are sections. The allowed sections and their meanings are below:

| Section | Required | Meaning |
| ------- | -------- | ------- |
| `artifact_name`  | No      | The name for the executable to generate. Defaults to the name of the containing directory. |
| `macros` | No | List of macros to define in `mbed_config.h`. |
| `config` | No | Configuration parameters defined for use in this library. |
| `target_overrides` | No | Overrides for target, library and application configuration parameters. |

The application can freely override the configuration of any of the libraries it depends on, as well as the configuration data in targets, so it has complete control over the configuration of the whole build. For example, an `mbed_app.json` from an application that depends on `mylib` above may look like this:

```JSON
{
    "artifact_name": "my-application",
    "config": {
        "welcome_string": {
            "help": "The string printed on the display on start-up",
            "value": "\"Hello!\""
        }
    },
    "target_overrides": {
        "*": {
            "mylib.timer_period": 100
        },
        "NCS36510": {
            "target.mac_addr_high": "0x11223344"
        }
    }
}
```

The application may override any configuration parameter by specifying the configuration parameters including their prefix (such as `mylib.timer_period`). If an overridden parameter doesn't have a prefix, it overrides a parameter in its own `config` section.

The `mbed_app.json` above defines its own configuration parameter (`welcome_string`) and overrides the configuration in both the target (`target.mac_addr_high`) and its `mylib` dependency (`mylib.timer_period`):

- When compiling for `NCS36510`, `app.welcome_string` is `"Hello!"`, `target.mac_addr_high` is `"0x11223344"` (from the `NCS36510` override) and `mylib.timer_period` is 100 (from the `*` override).
- When compiling for `LPC1768`, `app.welcome_string` is `"Hello!"` and `mylib.timer_period` is 100 (also from the `*` override).
- The final artifact (binary) is named `my-application.bin`, as specified by the `artifact_name` section.

It is an error for the application configuration to override an undefined configuration parameter.
