### Instrumented Trace Macrocell

For targets with Arm CoreSight (for example, Cortex-M3 and Cortex-M4), the Instrumented Trace Macrocell provides a lightweight, nonintrusive way to collect debug trace output. 

#### Assumptions

##### Defined behavior

- When initialized, writing data to the ITM stimulus registers will result in the data being transmitted over the SWO line.

##### Undefined behavior

- The debug clock frequency is left undefined because the most optimal frequency varies from target to target. It is up to each target's owner to choose a frequency that doesn't interfere with normal operation and that the owner's preferred debug monitor supports. 
- If another peripheral tries to take control of the SWO pin it is undefined whether that operation should succeed or not.

##### Notes

- Some SWO viewers do not allow for an arbitrary frequency to be set. Make sure that the chosen frequency is supported by the development tools you expect your users to use.

#### Dependencies

- The target supports Arm CoreSight.
- The target has SWO connected either to a compatible interface chip or exposed as a debug pin.

#### Implementing the ITM API

- You must implement the function `itm_init`. When the function is called:
  - The debug clock for the ITM must be initialized.
  - The SWO pin must be configured for debug output.
- You must add `ITM` to the `device_has` section in `target.json`.

It should not be necessary to mofify any of the ITM registers in `itm_init`, except for the one related to the clock prescaling, `TPI->ACPR`. The helper function `mbed_itm_init` is responsible for calling `itm_init` and initializing the generic ITM registers. `mbed_itm_init` will only call the function `itm_init` exactly once making it unnecessary to protect `itm_init` against multiple initializations.

#### Testing

You can use the `SerialWireOutput` to send `stdout` to the SWO stimulus port on the ITM by including this override function:

```
#include "SerialWireOutput.h"

FileHandle* mbed::mbed_override_console(int fd)
{
    static SerialWireOutput swo;
    return &swo;
}
```

You can place the function in any C++ compilation unit, including `main.cpp`.
