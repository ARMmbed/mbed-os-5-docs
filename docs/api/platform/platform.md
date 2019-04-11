# Platform overview

The role of the platform modules is to provide general purpose MCU management infrastructure, a few common data structures and  a consistent user experience on top of different standard libraries and toolchains. This page contains reference material about these subjects.

## General MCU Management Infrastructure

Mbed OS eases MCU management through the use of several scoped locks and several global APIs.

The locks, `DeepSleepLock` and `CriticalSectionLock`, use RAII to create a scope within which the appropriate lock is held; These locks acquire operation is their constructor and their release operation is their destructor. This uses core C++ language features, object lifetime and deconstruction on scope exit, to eliminate most resource leaks and reduce program complexity. The `DeepSleepLock` prevents the MCU from deep sleeping while it's alive and the `CriticalSectionLock` prevents preemption while it's alive. As these acquisition of a critical section or a deep sleep lock cannot fail, both of these classes do not raise exceptions.

Mbed OS also provides global APIs for the sleep and preemption global resources. The `PowerManagement` module includes a function to go to sleep now and the `Wait` module include a function to preempt now.
- [Wait](wait.html): An API that provides simple wait capabilities. These wait capabilities are integrated with the RTOS to schedule another thread if the current thread is blocked. If all threads are blocked, the idle thread will save power by putting the MCU to sleep.
- [CriticalSectionLock](criticalsectionlock.html): An object that establishes the beginning of a critical section and uses RAII to disable and restore interrupt state when the current scope exits.
- [Power management](power-management.html): An API to control sleep modes. A user of this API configures the sleep states that the MCU enters on idle, when everything is blocked.
- [DeepSleepLock](deepsleeplock.html): A class that prevents sleep within a scope. For instance, Use this class to prevent the configured sleep mode from interfering with a fast or low latency communication channel.

## Common data structures

Mbed OS provides the CircularBuffer and ATCmdParser as these are commonly used utilities in embedded systems.

- [CircularBuffer](circularbuffer.html): The class that provides APIs to push and pop data from a buffer in an interrupt safe fashion.
- [ATCmdParser](atcmdparser.html): An Mbed OS compatible AT command parser and serializer.

## C++ ergonomics extensions

Mbed OS includes a few convenience classes that are tailored for embedded systems development. These are the `Callback`, `Error` and `NonCopyable` classes.

- [Callback](callback.html): An API that executes the user’s code in its own context. Many other Mbed OS APIs build on the Callback API by taking a callback to execute.
- [Time](time.html): A group of functions in the standard library of the C programming language implementing date and time manipulation operations.
- [Error](../apis/error-handling.html): A functions that generates a fatal runtime error.
- [NonCopyable](noncopyable.html): An API that tags a class as not supporting copy operations. It creates a compile-time error if you copy the object.
- [Span](span.html): A nonowning view to a sequence of contiguous elements. It can replace the traditional pair of pointer and size arguments passed as array definitions in function calls.

### Callbacks

A callback is a user provided function that a user may pass to an API. The callback allows the API to execute the user’s code in its own context.

For example, the following code allows a user to provide a customized response whenever the serial line receives data:

```c++
// Create a serial object
Serial serial(USBTX, USBRX);

// A function that echoes any received data back
 void echo() {
    while (serial.readable()) {
         serial.putc(serial.getc());
    }
 }

 int main(void) {
     // Call our function echo whenever the serial line receives data
     serial.attach(&echo, Serial::RxIrq);
 }
```

The Callback class manages C/C++ function pointers so you don't have to. If you are asking yourself why you should use the Callback class, you should read the [Importance of State](platform.html#the-importance-of-state) section.

#### Why should you use Callbacks?

Supporting all of the standard C++ function types is difficult for an API developer. An API developer must consider state, C++ Function objects, const correctness and volatile correctness.

State is important, so an API developer must support either C-style function pointers with state, or C++ member function pointers. Stateless callbacks are just as common, but passing a stateless callback as a member function requires writing a lot of boilerplate code and instantiating an empty class. Further, an API developer also must support a standard function pointer.

Another common design pattern is the function object, a class that overrides the function call operator. A user may pass function objects as C++ member function pointers and C++ requires a large set of overloads to support all of the standard function types. It is unreasonable to expect a new library author to add all of these overloads to every function that could take in a callback.

A useful C++ feature is compile time const-correctness checks, which increases API complexity when combined by callbacks with state. To allow a user to take full advantage of the const-correctness checks, a C++ API must support both the const and non-const versions of member function pointers.

Another useful C++ feature is volatile-correctness. When volatile-correctness is necessary, we expect that the user hides volatile members inside of a non-volatile class.

C++ provides the tools to delegate this complexity to a single class. This class is the Callback class. The Callback class should be familiar to users of the std::function class that C++11 introduced and is available for older versions of C++.

<h5 id="the-importance-of-state">The importance of state</h5>

Callbacks may have two important pieces of information, the code to execute and the state associated with the callback.

A common API design mistake is to use a callback type that doesn’t allow a user to attach state to a callback. The most common example of this is a simple C function pointer:

```c++
class ADC {
public:
    // Here, the adc_callback_t type is a function that takes in data
    typedef void (*adc_callback_t)(float data);


    // In this example, the ADC read function calls the user-provided callback
    // when data is available.
    void attach(adc_callback_t cb);
};
```

This API is sufficient for simple applications, but falls apart when there are multiple ADC modules available. This problem becomes especially noticeable when a user tries to reuse the same procedure for multiple callbacks.

For example, consider applying a low-pass filter to two different ADC modules:

``` c++ TODO
// Here is a small running-average low-pass filter.
float low_pass_result;
void low_pass_step(float data) {
     low_pass_result = low_pass_result*0.99 + data*0.01;
}

// Our two adc modules
ADC adc1;
ADC adc2;

int main() {
    adc1.attach(low_pass_step);

    // Problem! Now both low pass filters share the same state!
    adc2.attach(low_pass_step);
}
```

Without state, callbacks compose poorly. In C, you fix this by adding a "state" argument to the function pointer, and by passing opaque "state" when you register the callback.

Here’s the low-pass example using an additional argument for state.

```c++ TODO
class ADC {
   public:
   // Here, the adc_callback_t type is a function that takes in data, as well as a pointer for state
    template <typename T>
    typedef void (*adc_callback_t)(T *state, float data);


    // In this example, the ADC read function calls the user-provided callback
    // when data is available.
    template <typename T>
    void attach(adc_callback_t<T> cb, T *state);
};

// Here is a small running-average low-pass filter.
void low_pass_step(float *result, float data) {
     *result = *result*0.99 + data*0.01;
}

// Our two adc modules
ADC adc1;
ADC adc2;

// Our two low-pass filter results
float low_pass_result1;
float low_pass_result2;

int main() {
    adc1.attach(low_pass_step, &low_pass_result1);

    // Register a second low pass filter, no more issues!
    adc2.attach(low_pass_step, &low_pass_result2);
}
```

One of the core features of C++ is the encapsulation of this "state" in classes, with operations that modify the state being represented as member functions in the class. Member function pointers are not compatible with standard function pointers. The Callback class allows API authors to implement a single interface that accepts a Callback, and the user may provide a C function and state or C++ member function and object without special consideration by the API author.

Here’s the low-pass filter example rewritten to use the callback class:

``` c++ TODO
class ADC {
public:
    // In this example, the ADC read function calls the user-provided callback
    // when data is available.
    void attach(Callback<void(float)> cb);
};

class LowPass {
   float result;

public:
    // Move the low pass filter implementation to the ADC module
    void step(float data) {
        result = result*0.99 + data*0.01;
    }
};


// Our two adc modules
ADC adc1;
ADC adc2;

// Our two low-pass filters
LowPass low_pass1;
LowPass low_pass2;

int main() {
    adc1.attach(callback(&low_pass1, &LowPass::step));
    adc2.attach(callback(&low_pass2, &LowPass::step));
}
```
