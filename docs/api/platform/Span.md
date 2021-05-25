# Span

A Span is a nonowning view to a sequence of contiguous elements.

It can replace the traditional pair of pointer and size arguments passed as array definitions in function calls.

## Construction

Span objects can be constructed from a reference to a C++ array, a pointer to the sequence viewed and its size or the range of the sequence viewed:

```
const uint8_t str[] = "Hello mbed!";

Span<const uint8_t> span_from_array(str);
Span<const uint8_t> span_from_ptr_and_size(str, sizeof(str));
Span<const uint8_t> span_from_range(str, str + sizeof(str));
```

## Operations

You can copy and assign Span objects like regular value types with the help of the copy constructor or the copy assignment (=) operator.

```
const uint8_t str[] = "Hello mbed!";

Span<uint8_t> str_span(hello_mbed);
Span<uint8_t> copy_constructed_span(str_span);
Span<uint8_t> copy_assigned_span;

copy_assigned_span = str_span;
```

You can retrieve elements of the object with the subscript ([]) operator. You can access the pointer to the first element of the sequence viewed with `data()`. The function `size()` returns the number of elements in the sequence, and `empty()` informs whether there is any element in the sequence.

```
void process_unit(uint8_t);

void process(const Span<uint8_t> &data)
{
    if (data.empty()) {
        // nothing to process
        return;
    }

    for (ptrdiff_t i = 0; i < data.size(); ++i) {
        process_unit(data[i]);
    }
}
```

You can slice Span from the beginning of the sequence (`first()`), from the end of the sequence (`last()`) or from an arbitrary point in the sequence (`subspan()`).

```
const uint8_t str[] = "Hello mbed!";

Span<uint8_t> str_span(hello_mbed);

ptrdiff_t half_size = str_span.size() / 2;

Span<uint8_t> lower_half = str_span.first(half_size);
Span<uint8_t> upper_half = str_span.last(half_size);
Span<uint8_t> interquartile_range = str_span.subspan(/* offset */ half_size / 2, half_size);
```

## Size encoding

You can encode the size of the sequence in the type itself or in the value of the instance with the help of the template parameter Extent:

  - `Span<uint8_t, 6>`: Span over a sequence of 6 `uint8_t`.
  - `Span<uint8_t>`: Span over an arbitrary long sequence of `uint8_t`.

When you encode the size in the type itself, the Span view is guaranteed to be a valid sequence (not `empty()` and not NULL) - unless `Extent` equals 0. The type system also prevents automatic conversion from Span of different sizes. Finally, a single pointer internally represents the Span object.

```
Span<uint8_t> long_span;

// illegal
Span<uint8_t, 6> span_mac_address;
Span<uint8_t, 6> from_long_span(long_span);

// legal
uint8_t mac_address[6] = { };
Span<uint8_t, 6> span_mac_address(mac_address);
long_span = span_mac_address;
```

When you encode the size of the sequence viewed in the Span value, Span instances can view an empty sequence. The function `empty()` helps client code decide whether Span is viewing valid content or not.

## Span class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/structmbed_1_1_span.html)


## Span example

C++ code:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Span_cpp/tree/v6.11)](https://github.com/ARMmbed/mbed-os-snippet-Span_cpp/blob/v6.11/main.cpp)


C code:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Span_c/tree/v6.11)](https://github.com/ARMmbed/mbed-os-snippet-Span_c/blob/v6.11/main.cpp)
