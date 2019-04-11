# Queue

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classrtos_1_1_queue.png)<span>Queue class hierarchy</span></span>

A Queue allows you to queue pointers to data from producer threads to consumer threads.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/queue.png)</span>

## Queue class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classrtos_1_1_queue.html)

## Queue example

```
Queue<message_t, 32> queue;

message_t *message;

queue.put(message);

osEvent evt = queue.get();
if (evt.status == osEventMessage) {
    message_t *message = (message_t*)evt.value.p;
```

## Queue and MemoryPool example

This example shows `Queue` and [MemoryPool](memorypool.html) managing measurements.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/rtos_queue/)](https://os.mbed.com/teams/mbed_example/code/rtos_queue/file/bbbae4aa4768/main.cpp)

## Related content

- [MemoryPool](memorypool.html) API reference.
