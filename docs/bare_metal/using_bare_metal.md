# Using the bare metal profile

This guide shows how to create a bare metal profile application:
1. By default, when you build an application binary, the build tool uses the full profile. To use the bare metal profile, you need to set up your application to override this default behaviour.
1. Bare metal has a [minimal set of APIs](bare_metal_api.md). You can add additional ones [from the list of supported API](../../api/api.md).

## Creating a bare metal application

1. Create a new Mbed application and enter its directory:

    ```
    mbed new example_app && cd example_app
    ```

    This contains an empty application with Mbed OS (`mbed-os/`) pre-fetched.

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

    For a list of default and supported APIs, [please see our full API list](../../api/api.md).

1. To add an API - in this example, the `EventQueue` class:

    1. Locate the library you want to use in `mbed-os/`.
    1. In the library folder, find the library's name in `mbed_lib.json`. You will need it for the next step.

        For example: `events/mbed_lib.json`:
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
            "requires": [
                "bare-metal",
                "events"
            ]
        }
        ```

1. Write the application using the libraries you added.

    [![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/mbed-os-example-baremetal-eventqueue-blinky/)](https://github.com/ARMmbed/mbed-os-example-baremetal-eventqueue-blinky/blob/master/main.cpp)

1. With a supported board connected to your computer, compile and flash your application:
    ```
    mbed compile -t <TOOLCHAIN> -m <TARGET> --flash
    ```

    In the example above, the on-board LED keeps blinking.
