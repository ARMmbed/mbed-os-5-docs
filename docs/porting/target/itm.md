<h1 id="itm-port">Instrumentation Trace Macrocell</h1>

For targets with Arm [CoreSight](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.ddi0314h/) (for example, Cortex-M3 and Cortex-M4), the Instrumentation Trace Macrocell (ITM) provides a lightweight, nonintrusive way to collect debug trace output.

## Assumptions

### Defined behavior

When the ITM has been initialized (by the SerialWireOutput class or other application), writing data to the ITM stimulus registers results in the ITM transmitting the data over the SWO line.

### Undefined behavior

- The debug clock frequency is left undefined because the most optimal frequency varies by target. It is up to each target's owner to choose a frequency that doesn't interfere with normal operation and that the owner's preferred debug monitor supports.
- If another peripheral tries to take control of the SWO pin, it is undefined whether that operation succeeds.

### Note

Some SWO viewers do not allow an arbitrary frequency to be set. Make sure that the development tools you expect your users to use support the chosen frequency.

## Dependencies

- The target supports Arm CoreSight.
- The target has SWO connected either to a compatible interface chip or exposed as a debug pin.

## Implementing the ITM API

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/group__itm__hal.html)

- You must implement the function `itm_init`. When the function is called:
  - The function must initialize the debug clock for the ITM.
  - The function must configure the SWO pin for debug output.
- You must add `ITM` to the `device_has` section in `target.json`.

It is not necessary to modify any of the ITM registers in `itm_init`, except for the one related to the clock prescaling, `TPI->ACPR`. The helper function `mbed_itm_init` is responsible for calling `itm_init` and initializing the generic ITM registers. `mbed_itm_init` only calls the function `itm_init` once, making it unnecessary to protect `itm_init` against multiple initializations.

## Testing

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
