# Shared Pointer

A shared pointer is a "smart" pointer that retains ownership of an object by using reference counting accross all smart pointers referencing that object.

It is similar to the `std::shared_ptr` class introduced in C++11. However, this is not a compatible implementation, as there are no weak pointers, no `make_shared`, no custom deleters, and so on.

Usage: `SharedPtr<Class> ptr(new Class())`

When `ptr` is passed around by a value, the copy constructor and destructor manage the reference count of the raw pointer. If the counter reaches zero, `delete` is called on the raw pointer.


## SharedPtr class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_shared_ptr.html)

## Shared pointer example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_Platform/Shared_pointer)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_Platform/Shared_pointer/main.cpp)
