## Memory tracing

Mbed OS provides a set of functions that you can use to study the runtime memory allocation pattern of your software: which sections of the code allocate and free memory and how much memory they need.
You must define the MBED_MEM_TRACING_ENABLED macro, to enable memory tracing.

You can use `mbed_mem_trace_set_callback` API, to set the callback for memory tracing. Callback will be invoked every time standard allocation functions (malloc, realloc, calloc and free) are called.

### Memory tracing functions reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/mbed__mem__trace_8h_source.html)

### Memory tracing example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/memory_tracing_example/)](https://os.mbed.com/teams/mbed_example/code/memory_tracing_example/file/168ab14e6694/main.cpp/)
