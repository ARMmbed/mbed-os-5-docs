# CircularBuffer

The CircularBuffer class provides APIs to `push` and `pop` data from a buffer. You should check if the buffer is `full` before pushing the data because a full buffer overwrites the data. The `empty` API is available to check contents in buffer before performing the pop operation.

CircularBuffer class is interrupt safe; all data operations are performed inside the critical section.

CircularBuffer is a templated class supporting different datatypes. The declaration of the CircularBuffer class must specify datatype and buffer size.

### Declaration example

This is an example of `BUF_SIZE` long integer CircularBuffer:

```
CircularBuffer<int, BUF_SIZE> buf;
```

## CircularBuffer class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_circular_buffer.html)

## CircularBuffer example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/mbed-os-example-circular-buffer/)](https://os.mbed.com/teams/mbed_example/code/mbed-os-example-circular-buffer/file/6c43979d0645/main.cpp)
