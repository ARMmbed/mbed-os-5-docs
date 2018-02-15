### Instrumented Trace Macrocell

For targets with Arm CoreSight (e.g. Cortex-M3 and Cortex-M4) the Instrumented Trace Macrocell provides a lightweight, non-intrusive way for collecting debug trace output. 

#### Assumptions

* The target supports Arm CoreSight.
* The target has SWO connected either to a compatible interface chip or exposed as a debug pin.

##### Defined behavior

* Targets must implement the function `void itm_init(void)` and add `ITM` to the `device_has` section in `target.json`.
* When `void itm_init(void)` is called, the debug clock for the ITM must be initialized and the SWO pin configured for debug output.
* `void itm_init(void)` should only have to modify the clock pre-scaler in the generic register `TPI->ACPR`. The generic ITM registers will be initialized by the helper function `mbed_itm_init`. 
* `void itm_init(void)` will only be called once during startup and doesn't have to be protected for multiple calls.

##### Undefined behavior

* The debug clock frequency is left undefined since the most optimal frequency will vary from target to target. It is up to each target's owner to pick a frequency that (a) doesn't interfere with normal operation and (b) is supported by the owner's preferred debug monitor. 

#### Testing

The `SerialWireOutput` class can be used for sending `stdout` to the SWO stimulus port on the ITM by including this override function:

```
#include "SerialWireOutput.h"

FileHandle* mbed::mbed_override_console(int fd) {
    static SerialWireOutput swo;
    return &swo;
}
```

The function can be placed in any C++ compilation unit, including `main.cpp`.
