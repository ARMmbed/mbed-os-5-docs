## Error

Mbed OS provides an error function to output messages to `STDIO` at runtime when the system encounters a fatal error and causes the application to terminate. `mbed_error.h` declares this error message. Note that the error function outputs the error message in debug and develop builds only. In release builds, the error function does not generate any output, but the application is still be terminated.

### Error function reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/group__platform__error.html)

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

