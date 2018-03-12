## NonCopyable

The NonCopyable class prevents objects of a class from supporting copy operations. You can easily identify it from its class declaration. It creates a compile-time error if you copy the object. Inheriting from this class results in autogeneration of private copy construction and copy assignment operations, which are not accessible in derived classes.

We recommend using the NonCopyable class whenever a class owns a resource (lock/hardware/file) that should not be copied to another class.

### NonCopyable class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_non_copyable.html)

### NonCopyable example

Copying objects of classes used for locking, network encapsulation, hardware bus and so on should not occur. Mbed OS has noncopyable classes, such as [Mutex](/docs/development/reference/mutex.html), [EventFlags](/docs/development/reference/eventflags.html), [BusOut](/docs/development/reference/busout.html), [InterruptIn](/docs/development/reference/interruptin.html) and [I2C](/docs/development/reference/i2c.html).

### Related content

- [Mutex](/docs/development/reference/mutex.html) API reference.
- [EventFlags](/docs/development/reference/eventflags.html) API reference.
- [BusOut](/docs/development/reference/busout.html) API reference.
- [InterruptIn](/docs/development/reference/interruptin.html) API reference.
- [I2C](/docs/development/reference/i2c.html) API reference.
