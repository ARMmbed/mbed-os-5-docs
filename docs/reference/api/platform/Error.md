## Error

Mbed-OS provides an error function to output messages to STDIO at runtime when the system encounters a fatal error and causes the application to terminate. Its declared in mbed_error.h. Note that error function will output the error message in Debug and Develop builds only. On Release builds error function will not generate any output but the application will still be terminated.

### Error function reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/group__platform__error.html)

### Error usage example
The code below uses error function to print a fatal error indicating out of memory condition.

```C
void *operator new(std::size_t count) {
    void *buffer = malloc(count);
    if (NULL == buffer) {
        error("Operator new out of memory\r\n");
    }
    return buffer;
}
```

