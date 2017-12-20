## Runtime memory tracing

Running out of memory is a common problem with resource constrained systems such as the MCUs on which Arm Mbed OS runs. When faced with an out of memory error, you often need to understand how your software uses dynamic memory. The runtime memory tracer in Mbed OS 5 is the tool that shows the runtime memory allocation patterns of your software: which parts of the code allocate and free memory and how much memory they need.

### Using the memory tracer

The memory tracer is not enabled by default. To enable it, you need to define the **`MBED_MEM_TRACING_ENABLED`** macro. The recommended way to define this macro is to add it to the list of macros defined in your `mbed_app.json`:

```
{
    "macros": ["MBED_MEM_TRACING_ENABLED"]
}
```

<span class="tips">**Tip:** See the documentation of the [Arm Mbed configuration system](/docs/v5.7/tools/configuring-tools.html) for more details about `mbed_app.json`. </span>

After it is enabled, the memory tracer intercepts the calls to the standard allocation functions (`malloc`, `realloc`, `calloc` and `free`). It invokes a user supplied callback each time one of these functions is called. To let the tracer know which callback it needs to invoke, call `mbed_mem_trace_set_callback(callback_function_name)` as early as possible (preferably at the beginning of your `main` function). You can find the full documentation of the callback function in the [memory tracer header file](https://github.com/ARMmbed/mbed-os/blob/master/platform/mbed_mem_trace.h#L42). The tracer supplies a default callback function (`mbed_mem_trace_default_callback`) that outputs trace data on the Mbed console (using `printf`). For each memory operation, the callback outputs a line that begins with `#<op>:<0xresult>;<0xcaller>-`:

- **op** identifies the memory operation (`m` for `malloc`, `r` for `realloc`, `c` for `calloc` and `f` for `free`).
- **result** (base 16) is the result returned by the memory operation. This is always 0 for `free` because `free` doesn't return anything.
- **caller** (base 16) is the address in the code where the memory operation was called.

The rest of the output depends on the operation being traced:

- For `malloc`: `size`, where `size` is the original argument to `malloc`.
- For `realloc`: `0xptr;size`, where `ptr` (base 16) and `size` are the original arguments to `realloc`.
- For `calloc`: `nmemb;size`, where `nmemb` and `size` are the original arguments to `calloc`.
- For `free`: `0xptr`, where `ptr` (base 16) is the original argument to `free`.

Examples:

- `#m:0x20003240;0x600d-50` encodes a `malloc` that returned 0x20003240. It was called by the instruction at 0x600D with the `size` argument equal to 50.
- `#f:0x0;0x602f-0x20003240` encodes a `free` that was called by the instruction at 0x602f with the `ptr` argument equal to 0x20003240.

Find the source of the default callback [here](https://github.com/ARMmbed/mbed-os/blob/master/platform/mbed_mem_trace.c#L81). Besides being useful in itself, it can also serve as a template for user defined callback functions.

<span class="tips">**Tip:** Find the full documentation of the callback function in the [memory tracer header file](https://github.com/ARMmbed/mbed-os/blob/master/platform/mbed_mem_trace.h#L42). </span>

### Example

A simple code example that uses the memory tracer on a K64F board:

```
#include <stdlib.h>
#include "mbed.h"
#include "mbed_mem_trace.h"


int main() {
    mbed_mem_trace_set_callback(mbed_mem_trace_default_callback);
    while (true) {
        void *p = malloc(50);
        wait(0.5);
        free(p);
    }
}
```

It outputs the following trace:

```
#m:0x20003080;0x182f-50
#f:0x0;0x183f-0x20003080
#m:0x20003080;0x182f-50
#f:0x0;0x183f-0x20003080
#m:0x20003080;0x182f-50
#f:0x0;0x183f-0x20003080
...
```

### Limitations

- The tracer doesn't handle nested calls of the memory functions. For example, if you call `realloc` and the implementation of `realloc` calls `malloc` internally, the call to `malloc` is not traced.
- The **caller** argument of the callback function isn't always reliable. It doesn't work at all on some toolchains, and it might output erroneous data on others.
