## NonCopyable

By default, C++ objects are copyable. Unfortunately some type of objects like resources or polymorphic types are not meant to be copied as they have unique identities. 

To prevent copy to happen, a common practices has been to declare the copy constructor and copy assignment operator of non copyable types privates. This pattern has the disadvantage of not being semantically explicit. Therefore it can be hard to find out if a type is copyable or not.

The `NonCopyable` class is here to solves these issue. Simply inherit privately from it and you're done. 

```c++ NOCI
class Resource : NonCopyable<Resource> { /* resource code */ };

Resource r1, r2;

// Copy construction generates a compile time error.
Resource r3 = r1;

// Copy assignment generates a compile time error.
r1 = r2;
```

The non copyable properties also transfer to classes that derives from a non copyable class as well as classes that owns a non copyable instance: 

```c++ NOCI
class DerivedResouce : public Resource { /* DerivedResource code */ };

DerivedResouce r1, r2;

// Copy construction generates a compile time error.
DerivedResouce r3 = r1;

// Copy assignment generates a compile time error.
r1 = r2;

class ResourceOwner { 
    /* code */
    Resource r;
};

ResourceOwner o1, o2;

// Copy construction generates a compile time error.
ResourceOwner o3 = o1;

// Copy assignment generates a compile time error.
r1 = r2;
```

We recommend inheriting from the `NonCopyable` class whenever a class is a resource or owns a resource (lock/hardware/file) that should or could not be copied.

### NonCopyable class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_non_copyable.html)

### NonCopyable example

Copying objects of classes used for locking, network encapsulation, hardware bus and so on should not occur. Mbed OS has noncopyable classes, such as [Mutex](mutex.html), [EventFlags](eventflags.html), [BusOut](busout.html), [InterruptIn](interruptin.html) and [I2C](i2c.html).

### Related content

- [Mutex](mutex.html) API reference.
- [EventFlags](eventflags.html) API reference.
- [BusOut](busout.html) API reference.
- [InterruptIn](interruptin.html) API reference.
- [I2C](i2c.html) API reference.
