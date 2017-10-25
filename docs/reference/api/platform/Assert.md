## Assert

Mbed-OS provides a set of macros which evaluates an expression and prints an error message if the expression evaluates to false. There are two types of macros, one for evaluating the expression during runtime and other can be used for compile-time evaluation. These macros are defined in mbed_assert.h.

### Assert macros reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/group__platform__Assert.html)

### Assert usage example

MBED_ASSERT macro can be used for runtime evaluation of expressions. If the evaluation fails, an error message will be printed out to bash in the below format. Note that MBED_ASSERT macro is available in Debug and Develop build profiles but not in Release builds. 

mbed assertation failed: <EVALUATED EXPRESSION>, file: <FILE NAME>, line <LINE NUMBER IN FILE>

The below function uses MBED_ASSERT to validate pointer to serial_t object.

```C
uint8_t serial_tx_active(serial_t *obj) {
    MBED_ASSERT(obj);
    ...
}
```

MBED_STATIC_ASSERT macro can be used for compile-time evaluation of expressions. If the evaluation fails, the passed in error message will be printed out and the compilation fails.

The below function uses MBED_ASSERT_STATIC to validate the size of equeue_timer struture.

```C
void equeue_tick_init() {
    MBED_STATIC_ASSERT(sizeof(equeue_timer) >= sizeof(Timer),"The equeue_timer buffer must fit the class Timer");
    ...
}
```
