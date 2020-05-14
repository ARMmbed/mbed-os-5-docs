# Using the bare metal profile

This guide shows how to create a bare metal profile application:

1. Set the profile: By default, the build tool uses the full profile for all application builds. To use the bare metal profile, set up your application to override this default behaviour.
1. By default, the bare metal profile uses a minimal set of APIs. You can add additional ones [from the list of supported APIs](../bare-metal/index.html#features) if your application needs them.

To demonstrate how to create a bare metal application, here is an example that prints text at regular intervals using the `EventQueue` class:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_RTOS/EventQueue_ex_2/)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_RTOS/EventQueue_ex_2/main.cpp)

## Creating a bare metal application

To create the application:

1. Create a new Mbed OS application and navigate to its directory:

    ```
    mbed new example_app && cd example_app
    ```

    The directory contains the full Mbed OS library (`mbed-os/`) and no application files.

1. Create a `main.cpp` file containing the `EventQueue` code snippet above.

1. Open `mbed_app.json` (in the root of the application) and replace it with the following content:

    ```json
    {
        "requires": ["bare-metal"],
        "target_overrides": {
            "*": {
                "target.c_lib": "small"
            }
        }
    }
    ```

    The file specifies which profile to use (`"requires": ["bare-metal"]`) and which C library to use (`"target.c_lib": "small"`).
    
    In this example, we're using `"target.c_lib": "small"` (small C library). This means your application will use an optimised version of the C library with lower memory footprint. For more details, see [Using small C libraries in Mbed OS bare metal](../bare-metal/using-small-c-libraries.html).

You now have application code and a bare metal profile with the default APIs. However, this example uses APIs that are not part of the default bare metal profile - you need to manually add support for those APIs to the application.

## Adding APIs

Bare metal has a minimal set of default APIs - those that are always available to a bare metal application. You can add other supported APIs if you need the features they enable.

For a list of default and supported APIs, [please see our full API list](../apis/index.html).

This example depends on the `EventQueue` class, so you need to add the library that contains that class:

1. In `mbed-os/`, locate the API and the library in which it is declared.
1. In the library folder, open `mbed_lib.json` and find the library's name. You will need it for the next step.

    For example: `mbed-os/events/mbed_lib.json`:
    ```json
    {
        "name": "events",
        "config": {
            "present": 1,
            ...
        }
    }
    ```
    To continue, go back to the application's root directory.

1. Open `mbed_app.json` again, and add the library to the `"requires"` field:

    ```json
    {
        "requires": ["bare-metal", "events"],
        "target_overrides": {
            "*": {
                "target.c_lib": "small"
            }
        }
    }
    ```

## Compiling and Running the Application

Connect a supported board to your computer, and compile and run your application:

```
mbed compile -t <TOOLCHAIN> -m <TARGET> --flash --sterm
```

When the example is flashed, a serial terminal opens (because of `--sterm`). The outputis:

```
called immediately
called every 1 seconds
called in 2 seconds
called every 1 seconds
called every 1 seconds
called every 1 seconds
```

To exit the serial terminal, press <kbd>Ctrl</kbd> + <kbd>C</kbd>.
