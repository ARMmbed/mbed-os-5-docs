## Queue

A Queue allows you to queue pointers to data from producer threads to consumer threads.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/queue.png)</span>

### Queue class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/classrtos_1_1_queue.html)

### Queue example

```
Queue<message_t, 32> queue;

message_t *message;

queue.put(message);

osEvent evt = queue.get();
if (evt.status == osEventMessage) {
    message_t *message = (message_t*)evt.value.p;
```

### Queue and MemoryPool example

This example shows `Queue` and [MemoryPool](/docs/v5.8/reference/memorypool.html) managing measurements.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/rtos_queue/)](https://os.mbed.com/teams/mbed_example/code/rtos_queue/file/0cb43a362538/main.cpp)

### Related content

- [MemoryPool](/docs/v5.8/reference/memorypool.html) API reference.
