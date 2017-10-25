## Debug

Mbed-OS provides a set of debug functions which can be used to output debug messages to STDIO at runtime. These macros are defined in mbed_debug.h and are available only in debug builds.

### Debug functions reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/group__platform__debug.html)

### Debug example

The debug function is a printf-style function which takes a format string followed by arguments, as the example shown below.

void *operator new(std::size_t count)
{
    void *buffer = malloc(count);
    if (NULL == buffer) {
        error("Operator new out of memory\r\n");
    } else {
        debug("Operator new succeded");
    }
    return buffer;
}

The debug_if function is similar to debug function except that it takes an additional argument
as its first parameter. The message is printed out to STDIO only if the first paramater evaluates to "true".

void *operator new(std::size_t count)
{
    debug_if( count == 0, "\nnew called with 0 size");
    ...
} 
