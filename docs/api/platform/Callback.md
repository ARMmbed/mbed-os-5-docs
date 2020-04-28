# Callback

A callback is a user provided function that a user may pass to an API. The callback allows the API to execute the user’s code in its own context.

This is the technical reference for callbacks. You should read the [Callbacks](platform.html#callbacks) section of the [Platform Overview](platform.html) first for deeper insight into their use.

## Calling callbacks

Callbacks overload the function call operator, so you can call a Callback like you would a normal function:

```c++
void run_timer_event(Callback<void(float)> on_timer) {
    on_timer(1.0f);
}
```

The only thing to watch out for is that the Callback type has a null Callback, just like a null function pointer. Uninitialized callbacks are null and assert if you call them. If you want a call to always succeed, you need to check if it is null first.

``` c++
void run_timer_event(Callback<void(float)> on_timer) {
    if (on_timer) {
        on_timer(1.0f);
    }
}
```

The Callback class is what’s known in C++ as a “Concrete Type”. That is, the Callback class is lightweight enough to be passed around like an int, pointer or other primitive type.

## Configuration

Two system configuration options permit trade-offs between image size and flexibility of the Callback class.

* `platform.callback-nontrivial` controls whether Callbacks can store non-trivially-copyable function objects. Having this setting off saves significant code size, as it makes Callback itself trivially-copyable, so all Callback assignments and copies are simpler. Almost all users use Callback only with function pointers, member function pointers or lambdas with trivial captures, so this setting can almost always be set to false. A compile-time error will indicate that this setting needs to be set to true if any code attempts to assign a non-trivially-copyable object to a Callback.

* `platform.callback-comparable` controls whether two Callbacks can be compared to each other. The ability to support this comparison increases code size whenever a Callback is assigned, whether or not any such comparison occurs. Turning the option off removes the comparison operator and saves a little image size.

<span class="tips">**Tip:** See the documentation of the [Arm Mbed configuration system](../reference/configuration.html) for more details about `mbed_app.json`. </span>

## Callback class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classmbed_1_1_callback.html)

## Serial passthrough example with callbacks
[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/rtos_threading_with_callback/)](https://os.mbed.com/users/mbedAustin/code/SerialPassthrough/file/96cb82af9996/main.cpp)

## Thread example with callbacks

The Callback API provides a convenient way to pass arguments to spawned threads. This example uses a C function pointer in the Callback.

 [![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/rtos_threading_with_callback/)](https://os.mbed.com/teams/mbed_example/code/rtos_threading_with_callback/file/5938bdb7b0bb/main.cpp)

## Sonar example

Here is an example that uses everything discussed in the [introduction to callbacks](platform.html#callbacks) document in the form of a minimal Sonar class. This example uses a C++ class and method in the Callback.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/callback-sonar-example/)](https://os.mbed.com/teams/mbed_example/code/callback-sonar-example/file/1713cdc51510/main.cpp)
