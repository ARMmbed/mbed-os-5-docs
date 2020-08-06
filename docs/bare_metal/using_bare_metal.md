# Using the bare metal profile

This guide shows how to create a bare metal profile application, or move an existing Mbed 2 application to Mbed OS 6 bare metal:

1. By default, the build tool uses the full profile for all application builds. To use the bare metal profile, set up your application to override this default behaviour.
1. The bare metal profile uses a minimal set of default APIs. You can add additional ones [from the list of supported APIs](../bare-metal/index.html#features) if your application needs them.

Here is a code snippet that can work for both Mbed OS profiles; it prints text at regular intervals using the `EventQueue` class. You will create an application that uses this code, set it to use the bare metal profile, and add the non-default `EventQueue` class.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-EventQueue_ex_2/tree/v6.0)](https://github.com/ARMmbed/mbed-os-snippet-EventQueue_ex_2/blob/v6.0/main.cpp)

<span class="notes">**Note:** To be compatible with Arm microlib, a bare metal application should not return from `main()`. In this example, the `queue.dispatch_forever()` call never returns. For more details, see [Non-returning main()](../bare-metal/using-small-c-libraries.html).</span>

## 1. Creating a bare metal application

To create the application using Mbed CLI:

1. Create a new Mbed OS application and navigate to its directory:

    ```
    mbed new example_app && cd example_app
    ```

    The directory contains the full Mbed OS library (`mbed-os/`) and no application files.

1. Create a `main.cpp` file.

1. Copy the code snippet above into `main.cpp`.

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

    The `mbed_app.json` file specifies which **profile** to use (`"requires": ["bare-metal"]`) and which **C library** to use (`"target.c_lib": "small"`).

    This example uses `"target.c_lib": "small"` (small C library). This means your application will use an optimised version of the C library with lower memory footprint. For more details, see [Using small C libraries in Mbed OS bare metal](../bare-metal/using-small-c-libraries.html).

## 2. Adding APIs

Your application is set to use the bare metal profile with the default APIs. However, this example uses APIs that are not part of the default bare metal profile. You need to manually add support for those APIs to the application (for a list of default and supported APIs, [please see our full API list](../apis/index.html)).

To add API support, add the library name to the same `requires` array you used to set the bare metal profile. The following example shows how to find the library name, and how to add it to the array.

This example depends on the `EventQueue` class, and adds the library that contains that class to the `mbed_app.json` file:

1. In `mbed-os/`, locate the API and the library in which it is declared.

1. In the library folder, open `mbed_lib.json` and find the library's name. You will need it for the next step.

    For example: `mbed-os/events/mbed_lib.json`:

    ```
    {
        "name": "events",
        "config": {
            "present": 1,
            ...
        }
    }
    ```

1. Go back to the application's root directory.

1. Open `mbed_app.json` again, and add the library to the `"requires"` array:

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

The application is now ready to compile, and will include the events library (which has no dependencies).

<span class="notes">**Note:** Including a library does not automatically include all of its dependencies. Review compilation errors to find missing dependencies.</notes>

## 3. Compiling and running the application

Connect a supported board to your computer, and compile and run your application:

```
mbed compile -t <TOOLCHAIN> -m <TARGET> --flash --sterm
```

When the example is flashed to the board, a serial terminal opens (because of `--sterm`). The output is:

```
called immediately
called every 1 seconds
called in 2 seconds
called every 1 seconds
called every 1 seconds
called every 1 seconds
```

To exit the serial terminal, press <kbd>Ctrl</kbd> + <kbd>C</kbd>.
