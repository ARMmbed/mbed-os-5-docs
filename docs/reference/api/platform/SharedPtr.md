## Shared Pointer

A shared pointer is a "smart" pointer that retains ownership of an object using
reference counting accross all smart pointers referencing that object.

It is similar to the `std::shared_ptr` class introduced in C++11,
however this is not a compatible implementation (no weak pointer, no make_shared, no custom deleters, etc.)

Usage: `SharedPtr<Class> ptr(new Class())`

When `ptr` is passed around by value the copy constructor and
destructor manages the reference count of the raw pointer.
If the counter reaches zero, `delete` is called on the raw pointer.

To avoid loops, "weak" references should be used by calling the original
pointer directly through `ptr.get()`.


### SharedPtr class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/class_shared_ptr.html)

### Shared pointer example

```cpp
#include "platform/SharedPtr.h"
  
void test() {
    struct MyStruct { int a; };

    // Create shared pointer
    SharedPtr<MyStruct> ptr( new MyStruct );

    // Increase reference count
    SharedPtr<MyStruct> ptr2( ptr );

    ptr = NULL; // Reference to the struct instance is still held by ptr2

    ptr2 = NULL; // The raw pointer is freed
}
```
