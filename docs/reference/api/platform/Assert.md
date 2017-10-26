## Assert

Mbed OS provides a set of macros that evaluates an expression and prints an error message if the expression evaluates to false. There are two types of macros, one for evaluating the expression during runtime and one for compile-time evaluation. `mbed_assert.h` defines these macros.

### Assert macros reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/group__platform__Assert.html)

### Assert usage example

You can use the `MBED_ASSERT` macro for runtime evaluation of expressions. If the evaluation fails, an error message prints to bash in the below format. Note that the `MBED_ASSERT` macro is available in the debug and develop build profiles but not in the release build profile. 

mbed assertation failed: <EVALUATED EXPRESSION>, file: <FILE NAME>, line <LINE NUMBER IN FILE>

The below function uses `MBED_ASSERT` to validate a pointer to `serial_t` object.

```C
uint8_t serial_tx_active(serial_t *obj) {
    MBED_ASSERT(obj);
    ...
}
```

You can use the `MBED_STATIC_ASSERT` macro for compile-time evaluation of expressions. If the evaluation fails, the passed in error message prints, and the compilation fails.

The below function uses `MBED_ASSERT_STATIC` to validate the size of the `equeue_timer` structure.

```C
void equeue_tick_init() {
    MBED_STATIC_ASSERT(sizeof(equeue_timer) >= sizeof(Timer),"The equeue_timer buffer must fit the class Timer");
    ...
}
```
