## NonCopyable

The NonCopyable class prevents objects of a class from supporting copy operations. You can easily identify it from its class declaration. It creates a compile-time error if you copy the object. Inheriting from this class results in autogeneration of private copy construction and assignment operations, which are not accessible in derived classes.

### NonCopyable class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_non_copyable.html)

### NonCopyable example

Copying objects of classes used for locking, network encapsulation, hardware bus and so on should not occur. Mbed OS has noncopyable classes, such as [Mutex](/docs/v5.6/reference/mutex.html), [EventFlags](/docs/v5.6/reference/eventflags.html), [BusOut](/docs/v5.6/reference/busout.html), [InterruptIn](/docs/v5.6/reference/interruptin.html), [I2C](/docs/v5.6/reference/i2c.html).
