# Debug

Mbed OS provides a set of debug functions that you can use to output debug messages to `STDIO` at runtime. `mbed_debug.h` declares these functions, which are available only in debug builds.

The `debug` function is a printf-style function that takes a format string followed by arguments. Below are some sample usages.

```CPP TODO
void *operator new(std::size_t count) {
    void *buffer = malloc(count);
    if (NULL == buffer) {
        error("Operator new out of memory\r\n");
    } else {
        debug("Operator new succeded");
    }
    return buffer;
}
```

The `debug_if` function is similar to the `debug` function except that it takes an additional argument as its first parameter. The message prints to `STDIO` only if the first paramater evaluates to `true`.

```C TODO
void *operator new(std::size_t count) {
    debug_if( count == 0, "\nnew called with 0 size");
    ...
}
```

## Debug functions reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/mbed__debug_8h_source.html)

## Debug example

[![View Example](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/mbed-os-example-platform-utils/file/92b97ba04fd3/main.cpp/)](https://os.mbed.com/teams/mbed_example/code/mbed-os-example-platform-utils/file/92b97ba04fd3/main.cpp)
