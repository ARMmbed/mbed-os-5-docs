# Bare metal example

By default, Mbed OS is built in full whenever you create an application binary. To build only the bare metal profile, create an `mbed_app.json` in your application with the following contents:

```
{
    "requires": ["bare-metal"]
}
```

To learn about using the bare metal profile, please see the Blinky bare metal example:

[![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/mbed-os-example-blinky-baremetal/)](https://github.com/armmbed/mbed-os-example-blinky-baremetal/blob/master/main.cpp)
