## Error

Mbed OS provides an error function to output messages to `STDIO` at runtime when the system encounters a fatal error and the Application calling the error function will be terminated. Note that the error function outputs the error message in <a href="/docs/v5.6/tools/build-profiles.html" target="_blank">debug and develop builds</a> only. In release builds, the error function does not generate any `STDIO` output, but the application is still terminated. `mbed_error.h` declares the error function.

### Error function reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/mbed__error_8h_source.html)

### Error example

The code below uses an error function to print a fatal error indicating an out-of-memory condition.

```C
void *operator new(std::size_t count) {
    void *buffer = malloc(count);
    if (NULL == buffer) {
        error("Operator new out of memory\r\n");
    }
    return buffer;
}
```

### Related content

- Debug and develop <a href="/docs/v5.6/tools/build-profiles.html" target="_blank">build profiles</a>.
