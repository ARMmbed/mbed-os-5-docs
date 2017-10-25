## Error

Mbed-OS provides an error function to output messages to STDIO at runtime when the system encounters a fatal error. Its defined in mbed_error.h. The function will output the error message when called for the first time, but will ignore subsequent calls without generating any output. 

### Error function reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/group__platform__error.html)

### Error example
The code below uses error function to print a fatal error indicating out of memory condition.

void *operator new(std::size_t count)
{
    void *buffer = malloc(count);
    if (NULL == buffer) {
        error("Operator new out of memory\r\n");
    }
    return buffer;
}

