# Using the bare metal profile

This guide shows how to create a bare metal profile application:
1. By default, when you build an application binary, the build tool uses the full profile. To use the bare metal profile, you need to set up your application to override this default behaviour.
1. Bare metal has a minimal set of APIs. You can add additional ones [from the list of supported API](bare_metal.md#features).

## Creating a bare metal application

To demonstrate how to create a bare metal application, we use an example that prints text in regular intervals using the `EventQueue` class:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_RTOS/EventQueue_ex_2/)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_RTOS/EventQueue_ex_2/main.cpp)

The steps are as follows:

1. Create a new Mbed application and enter its directory:

    ```
    mbed new example_app && cd example_app
    ```

    This contains an empty application with Mbed OS (`mbed-os/`) fetched.

1. Create a `main.cpp` containing the `EventQueue` example code snippet above.

1. Open `mbed_app.json` and replace it with the following content:

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
    <span class="tips">**Tip:** `"target.c_lib": "small"` enables an optimised version of the C library with lower memory footprint. For more details, see [Using small C libraries in Mbed OS bare metal](c_small_libs.md)</span>.

    Bare metal has a minimal set of default APIs - those that are always available to a bare metal application. You can add other supported APIs if you need the features they enable.

    For a list of default and supported APIs, [please see our full API list](bare_metal.md#features).

1. Add dependencies - in this example, we need to add the library that contains the `EventQueue` class:

    1. Locate the API and the library where it is declared in `mbed-os/`.
    1. In the library folder, find the library's name in `mbed_lib.json`. You will need it for the next step.

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

1. With a supported board connected to your computer, compile and run your application:
    ```
    mbed compile -t <TOOLCHAIN> -m <TARGET> --flash --sterm
    ```

    This opens a serial terminal once the example is compiled and flashed. The following output is expected:
    ```
    called immediately
    called every 1 seconds
    called in 2 seconds
    called every 1 seconds
    called every 1 seconds
    called every 1 seconds
    ```

    To exit the serial terminal, press Ctrl + C.
