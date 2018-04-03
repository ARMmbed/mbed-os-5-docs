## Callback

A callback is a user provided function that a user may pass to an API. The callback allows the API to execute the user’s code in its own context.

This is the technical reference for callbacks. You should read the [Callbacks](/docs/development/reference/platform.html#callbacks) section of the [Platform Overview](/docs/development/reference/platform.html) first for deeper insight into their use.

### Callback class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_callback_3_01_r_07_a0_00_01_a1_00_01_a2_00_01_a3_00_01_a4_08_4.html)

### Serial passthrough example with callbacks
[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/rtos_threading_with_callback/)](https://os.mbed.com/users/mbedAustin/code/SerialPassthrough/file/96cb82af9996/main.cpp)

### Thread example with callbacks

The Callback API provides a convenient way to pass arguments to spawned threads.

 [![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/rtos_threading_with_callback/)](https://os.mbed.com/teams/mbed_example/code/rtos_threading_with_callback/file/d4b2a035ffe3/main.cpp)

### Sonar example

Here is an example that uses everything discussed in the [introduction to callbacks](/docs/development/reference/platform.html#callbacks) document in the form of a minimal Sonar class.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/callback-sonar-example/)](https://os.mbed.com/teams/mbed_example/code/callback-sonar-example/file/1713cdc51510/main.cpp)

### Related content

- [Platform overview](/docs/development/reference/platform.html).
- [Introduction to callbacks](/docs/development/reference/platform.html#callbacks).

#### Create callbacks

First, you need to understand the syntax of the Callback type. The Callback type is a templated type parameterized by a C++ function declaration:

``` c++
// Callback</*return type*/(/*parameters*/)> cb;
Callback<int(float)> cb;          // A callback that takes in a float and returns an int
Callback<void(float)> cb;         // A callback that takes in a float and returns nothing
Callback<int()> cb;               // A callback that takes in nothing and returns an int
Callback<void(float, float)> cb;  // A callback that takes in two floats and returns nothing
```

You can create a Callback directly from a C function or function pointer with the same type:

``` c++
void dosomething(int) {
    // do something
}

Callback<void(int)> cb(dosomething);
```

If an API provides a function that takes in a callback, you can pass in a C function or function pointer with the same type:

``` c++
class ADC {
    // ADC can pass an analog value to the callback
    void attach(Callback<void(float)> cb);
};

void dosomething(float f) {
    // do something
}

ADC adc;
adc.attach(dosomething);
```

But what about state? The Callback type also supports passing a state pointer for a function. This state can be either a pointer to an object that is passed to a member function, or a pointer passed to a C-style function.

Because this form of creating Callbacks requires two arguments, you need to create the Callback explicitly using the Callback constructor. The Callback also comes with the lowercase callback function, which creates callbacks based on the arguments type and avoids the need to repeat the template type.

You can create a callback with a member function.

``` c++
class Thing {
    int state;
    void catinthehat(int i) {
        state = // do something
    }
}

// We can create a Callback with the Callback constructor
Thing thing1;
adc.attach(Callback<void(int)>(&thing1, &Thing::catinthehat));

// Or we can create a Callback with the callback function to avoid repeating ourselves
Thing thing2;
adc.attach(callback(&thing2, &Thing::catinthehat));
```

Or you can pass the state to a C-style function.

``` c++
struct thing_t {
    int state;
}

void catinthehat(thing_t *thing, float f) {
    thing->state = // do something
}

// We can create a Callback with the Callback constructor
thing_t thing1;
adc.attach(Callback<void(int)>(catinthehat, &thing1));

// Or we can create a Callback with the callback function to avoid repeating ourselves
thing_t thing2;
adc.attach(callback(catinthehat, &thing2));
```

<span class="notes">**Note:** This state is restricted to a single pointer. This means you can’t bind both an object and argument to a callback.</span>

``` c++
 // Does not work
adc.attach(callback(&thing, &Thing::dosomething, &arg));
```

If you need to pass multiple arguments to a callback and you can’t store the arguments in the class, you can create a struct that contains all of the arguments and pass a pointer to that. However, you need to handle the memory allocation yourself.

``` c++
// Create a struct that contains all of the state needed for “dosomething”
struct dosomething_arguments {
    Thing *thing;
    int arg1;
    int arg2;
};

// Create a function that calls “dosomething” with the arguments
void dosomething_with_arguments(struct dosomething_arguments *args) {
    args->thing->dosomething(args->arg1, args->arg2);
}


// Allocate arguments and pass to callback
struct dosomething_arguments args = { &thing, arg1, arg2 };
adc.attach(callback(dosomething_with_arguments, &args)); // yes
```

#### Call callbacks

Callbacks overload the function call operator, so you can call a Callback like you would a normal function:

```c++
void callme(Callback<void(float)> cb) {
    cb(1.0f);
}
```

The only thing to watch out for is that the Callback type has a null Callback, just like a null function pointer. Uninitialized callbacks are null and assert if you call them. If you want a call to always succeed, you need to check if it is null first.

``` c++
void callmemaybe(Callback<void(float)> cb) {
    if (cb) {
        cb(1.0f);
    }
}
```

The Callback class is what’s known in C++ as a “Concrete Type”. That is, the Callback class is lightweight enough to be passed around like an int, pointer or other primitive type.

```c++
class Thing {
private:
    Callback<void(int)> _cb;

public:
    void attach(Callback<void(int)> cb) {
         _cb = cb
    }

    void dothething(int arg) {
        If (_cb) {
            _cb(arg);
        }
    }
}
```

<h4 id="the-importance-of-state">The importance of state</h4>

A callback is a user provided function that a user may pass to an API. The callback allows the API to execute the user’s code in its own context. You can find more information on how to use callbacks in the [technical callback documentation](/docs/development/reference/callback.html).
