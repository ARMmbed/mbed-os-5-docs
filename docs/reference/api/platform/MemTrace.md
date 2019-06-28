# Memory tracing

Mbed OS provides a set of functions that you can use to study the runtime memory allocation pattern of your software: which sections of the code allocate and free memory and how much memory they need.

You must define the `MBED_MEM_TRACING_ENABLED` macro to enable memory tracing.

You can use the `mbed_mem_trace_set_callback` API to set the callback for memory tracing. The callback is invoked every time you call standard allocation functions, such as `malloc`, `realloc`, `calloc` and `free`.

For a step-by-step guide about how to use optimize memory using runtime memory tracing, please see our [runtime memory tracing tutorial](/docs/v5.9/tutorials/optimizing.html#runtime-memory-tracing).

## Memory tracing function reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/v5.9/mbed-os-api-doxy/mbed__mem__trace_8h_source.html)

## Memory tracing example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/memory_tracing_example/)](https://os.mbed.com/teams/mbed_example/code/memory_tracing_example/file/168ab14e6694/main.cpp)

## Related content

- [Runtime memory tracing tutorial](/docs/v5.9/tutorials/optimizing.html#runtime-memory-tracing).
