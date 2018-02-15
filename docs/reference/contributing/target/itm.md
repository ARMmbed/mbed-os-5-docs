### Instrumented Trace Macrocell

For targets with Arm CoreSight (for example, Cortex-M3 and Cortex-M4), the Instrumented Trace Macrocell provides a lightweight, nonintrusive way to collect debug trace output. 

#### Assumptions

- The target supports Arm CoreSight.
- The target has SWO connected either to a compatible interface chip or exposed as a debug pin.

##### Defined behavior

- Targets must implement the function `void itm_init(void)` and add `ITM` to the `device_has` section in `target.json`.
- When `void itm_init(void)` is called, the debug clock for the ITM must be initialized and the SWO pin configured for debug output.
- `void itm_init(void)` only has to modify the clock prescaler in the generic register `TPI->ACPR`. The helper function `mbed_itm_init` initializes the generic ITM registers. 
- `void itm_init(void)` is only called once during startup and doesn't have to be protected for multiple calls.

##### Undefined behavior

- The debug clock frequency is left undefined because the most optimal frequency varies from target to target. It is up to each target's owner to choose a frequency that doesn't interfere with normal operation and that the owner's preferred debug monitor supports. 

#### Testing

You can use the `SerialWireOutput` to send `stdout` to the SWO stimulus port on the ITM by including this override function:

```
#include "SerialWireOutput.h"

FileHandle* mbed::mbed_override_console(int fd) {
    static SerialWireOutput swo;
    return &swo;
}
```

You can place the function in any C++ compilation unit, including `main.cpp`.
