# CircularBuffer

The CircularBuffer class provides APIs to `push` and `pop` data from a buffer. You should check if the buffer is `full` before pushing the data because a full buffer overwrites the data. The `empty` API is available to check contents in buffer before performing the pop operation.

CircularBuffer class is interrupt safe; all data operations are performed inside the critical section.

CircularBuffer is a templated class supporting different datatypes. The declaration of the CircularBuffer class must specify datatype and buffer size.

## Memory considerations

The actual data buffer is allocated as part of the CircularBuffer object memory.

## Declaration example

This is an example of `BUF_SIZE` long integer CircularBuffer:

```
CircularBuffer<int, BUF_SIZE> buf;
```

## CircularBuffer class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.13/mbed-os-api-doxy/classmbed_1_1_circular_buffer.html)

## CircularBuffer example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-CircularBuffer_ex_1/tree/v6.13)](https://github.com/ARMmbed/mbed-os-snippet-CircularBuffer_ex_1/blob/v6.13/main.cpp)
