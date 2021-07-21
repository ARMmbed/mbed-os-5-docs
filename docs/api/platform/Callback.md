# Callback

A callback is a user provided function that a user may pass to an API. The callback allows the API to execute the user’s code in its own context.

This is the technical reference for callbacks. You should read the [Callbacks](../apis/platform-concepts.html#callbacks) section of the [Platform Overview](../apis/platform-concepts.html) first for deeper insight into their use.

## Calling callbacks

Callbacks overload the function call operator, so you can call a Callback like you would a normal function:

```c++
void run_timer_event(Callback<void(float)> on_timer) {
    on_timer(1.0f);
}
```

The only thing to watch out for is that the Callback type has an empty Callback, just like a null function pointer. Default initialized callbacks are empty and assert if you call them. If a callback may be empty, you need to check if it is empty before calling it.

``` c++
void run_timer_event(Callback<void(float)> on_timer) {
    if (on_timer) {
        on_timer(1.0f);
    }
}
```

You can reset Callbacks to empty by assigning `nullptr`.

The Callback class is what’s known in C++ as a “Concrete Type”. That is, the Callback class is lightweight enough to be passed around like an int, pointer or other primitive type.

## Configuration

Two system configuration options permit trade-offs between image size and flexibility of the Callback class.

* `platform.callback-nontrivial` controls whether Callbacks can store non-trivially-copyable function objects. Having this setting off saves significant code size, as it makes Callback itself trivially-copyable, so all Callback assignments and copies are simpler. Almost all users use Callback only with function pointers, member function pointers or lambdas with trivial captures, so this setting can almost always be set to false. A compile-time error will indicate that this setting needs to be set to true if any code attempts to assign a non-trivially-copyable object to a Callback.

* `platform.callback-comparable` controls whether two Callbacks can be compared to each other. The ability to support this comparison increases code size whenever a Callback is assigned, whether or not any such comparison occurs. Turning the option off removes the comparison operator and saves a little image size.

<span class="tips">**Tip:** See the documentation of the [Arm Mbed configuration system](../program-setup/advanced-configuration.html) for more details about `mbed_app.json`. </span>

## Callback class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.13/mbed-os-api-doxy/classmbed_1_1_callback.html)

## Serial passthrough example with callbacks
[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Callback_SerialPassthrough/tree/v6.13)](https://github.com/ARMmbed/mbed-os-snippet-Callback_SerialPassthrough/blobl/v6.13/main.cpp)

## Thread example with callbacks

The Callback API provides a convenient way to pass arguments to spawned threads. This example uses a C function pointer in the Callback.

 [![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Threading_with_callback/tree/v6.13)](https://github.com/ARMmbed/mbed-os-snippet-Threading_with_callback/blobl/v6.13/main.cpp)

## Sonar example

Here is an example that uses everything discussed in the [introduction to callbacks](../apis/platform-concepts.html#callbacks) document in the form of a minimal Sonar class. This example uses a C++ class and method in the Callback.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Sonar/tree/v6.13)](https://github.com/ARMmbed/mbed-os-snippet-Sonar/blobl/v6.13/main.cpp)
