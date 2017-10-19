## NonCopyable
The NonCopyable class prevents ojects of a class from supporting copy operations. It is easily identified from class declaration and creates a compile-time error if you copy the object. Inheriting from this class results in autogeneration of private copy construction & assignement operations which are not accessible in derived class.

### NonCopyable class reference
[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.6/mbed-os-api-doxy/classmbed_1_1_non_copyable.html)

### Example
Copying objects of classes used for locking, network encapsulation, hardware bus etc should be prevented. Mbed OS has [Mutex](/docs/v5.6/reference/mutex.html), [EventFlags](/docs/v5.6/reference/eventflags.html), [BusOut](/docs/v5.6/reference/busout.html), [InterruptIn](/docs/v5.6/reference/interruptin.html), [I2C](/docs/v5.6/reference/i2c.html) and various other classes as noncopyable.
