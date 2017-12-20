## NonCopyable

The NonCopyable class prevents objects of a class from supporting copy operations. You can easily identify it from its class declaration. It creates a compile-time error if you copy the object. Inheriting from this class results in autogeneration of private copy construction and copy assignment operations, which are not accessible in derived classes.

We recommend using the NonCopyable class whenever a class owns a resource (lock/hardware/file) that should not be copied to another class.

### NonCopyable class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/v5.7/mbed-os-api-doxy/classmbed_1_1_non_copyable.html)

### NonCopyable example

Copying objects of classes used for locking, network encapsulation, hardware bus and so on should not occur. Mbed OS has noncopyable classes, such as [Mutex](/docs/v5.7/reference/mutex.html), [EventFlags](/docs/v5.7/reference/eventflags.html), [BusOut](/docs/v5.7/reference/busout.html), [InterruptIn](/docs/v5.7/reference/interruptin.html) and [I2C](/docs/v5.7/reference/i2c.html).

### Related content

- [Mutex](/docs/v5.7/reference/mutex.html) API reference.
- [EventFlags](/docs/v5.7/reference/eventflags.html) API reference.
- [BusOut](/docs/v5.7/reference/busout.html) API reference.
- [InterruptIn](/docs/v5.7/reference/interruptin.html) API reference.
- [I2C](/docs/v5.7/reference/i2c.html) API reference.
