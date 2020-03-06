# Memory tracing

Mbed OS provides a set of functions that you can use to study the runtime memory allocation pattern of your software: which sections of the code allocate and free memory and how much memory they need.

You must enable the `memory-tracing-enabled` setting in the Mbed OS platform configuration options to enable memory tracing. We recommend doing this by adding it to your `mbed_app.json`:

```
{
    "target_overrides": {
        "*": {
            "platform.memory-tracing-enabled": true
        }
    }
}
```

You can use the `mbed_mem_trace_set_callback` API to set the callback for memory tracing. The callback is invoked every time you call standard allocation functions, such as `malloc`, `realloc`, `calloc` and `free`.

For a step-by-step guide about how to use optimize memory using runtime memory tracing, please see our [runtime memory tracing tutorial](../tutorials/optimizing.html#runtime-memory-tracing).

## Memory tracing functions reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/6.0.0-preview/mbed-os-api-doxy/mbed__mem__trace_8h_source.html)

## Memory tracing example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_Platform/Memory_tracing_ex_1/)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_Platform/Memory_tracing_ex_1/main.cpp)

## Related content

- [Runtime memory tracing tutorial](../tutorials/optimizing.html#runtime-memory-tracing).
