
### The importance of state

A callback is a user provided function that a user may pass to an API. The callback allows the API to execute the user’s code in its own context. You can find more information on how to use callbacks in the [technical callback documentation](callbacks.md).

#### Why not function pointers?

Callbacks have two important pieces of information, the code to execute and the state associated with the callback.

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

This API is sufficient for simple applications but falls apart when there are multiple ADC modules available. This problem becomes especially noticeable when a user tries to reuse the same procedure for multiple callbacks.

For example, consider applying a low-pass filter to two different ADC modules

``` c++
// Here is a small running-average low-pass filter.
float low_pass_result;
void low_pass_step(float data) {
     low_pass_result = low_pass_result*0.99 + data*0.01;
}

// Our two adc modules
ADC adc1;
ADC adc2;

// Here we can register the low-pass filter on both ADC modules
int main() {
    // Register one low pass filter
    adc1.attach(low_pass_step);

    // Register a second low pass filter
    // Problem! Now both low pass filters are sharing the same state!
    adc2.attach(low_pass_step);
}
```

Without state, callbacks offer very limited composability. In C, you can fix this by adding an additional “state” argument to the function pointer, which allows you to pass in the opaque “state” when you register the callback.

Here’s the low-pass example using an additional argument for state.

```c++
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

// Here we can register the low-pass filter on both ADC modules
int main() {
    // Register one low pass filter
    adc1.attach(low_pass_step, &low_pass_result1);

    // Register a second low pass filter, no more issues!
    adc2.attach(low_pass_step, &low_pass_result1);
}
```

One of the core features of C++ is the encapsulation of this “state” in classes, with operations that modify the state being represented as member functions in the class. Unfortunately, member function pointers are not compatible with standard function pointers, but you can rewrite the low-pass example to use member function pointers, allowing you to pass in state as a C++ object.

Here’s the low-pass example rewritten to use member function pointers.

```c++
class ADC {
public:
    // Here, the adc_callback_t type is a function that takes in data
    template <typename T>
    typedef void (T::*adc_callback_t)(float data);


    // In this example, the ADC read function calls the user-provided callback
    // when data is available.
    template <typename T>
    void attach(T *obj, adc_callback_t<T> cb);
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

// Here we can register the low-pass filter on both ADC modules
int main() {
    // Register one low pass filter
    adc1.attach(&low_pass1, &LowPass::step);
    adc2.attach(&low_pass2, &LowPass::step);
}
```

#### Why should you use Callbacks?

Unfortunately, supporting all of the standard C++ function types is difficult.

- State is important, so need to support either C-style function pointers with state, or C++ member function pointers.

- Stateless callbacks are just as common, but passing a stateless callback as a member function function requires writing a lot of boilerplate code and instantiating an empty class. So we need to also support a standard function pointer.

- Another design pattern you may see is the function object, a class that overrides the function call operator. We can expect the user to pass function objects as C++ member function pointers if needed.

- A useful C++ feature is the enforcement of const-correctness, but this becomes unfortunately complicated with the state associated with callbacks. A C++ API needs to support both the const and non-const versions of member function pointers.

- Another C++ feature is volatile-correctness in case the underlying state must be volatile, but if necessary we can probably expect the user to hide volatile members inside of a non-volatile class.

C++ requires a large set of overloads to support all of the standard function types. It is unreasonable to expect a new library author to add all of these overloads to every function that could take in a callback.

C++ provides the tools to delegate this problem to a single class. This class is the Callback class. The Callback class should be familiar to users of the std::function class that C++11 introduced but is available for older versions of C++.

**An overly-simplified description of the Callback class is that is contains all of this madness so you don’t have to.**

Here’s the low-pass filter example rewritten to use the callback class:

``` c++
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

// Here we can register the low-pass filter on both ADC modules
int main() {
    // Register one low pass filter
    adc1.attach(callback(&low_pass1, &LowPass::step));
    adc2.attach(callback(&low_pass2, &LowPass::step));
}
```
