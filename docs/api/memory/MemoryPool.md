# MemoryPool

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classrtos_1_1_memory_pool.png)<span>MemoryPool class hierarchy</span></span>

You can use the MemoryPool class to define and manage fixed-size memory pools. You can allocate memory blocks of fixed size from the pool using the `alloc` or `calloc` method, which returns a pointer to the block of memory or NULL if there is no space available in the pool. It's the user's responsibility to initialize the objects placed in blocks. The `calloc` function sets the block of memory to zeros before returning the pointer of the block to the caller.

## MemoryPool class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classrtos_1_1_memory_pool.html)

## MemoryPool example

```
MemoryPool<message_t, 16> mpool;

message_t *message = mpool.alloc();

mpool.free(message);
```

## Queue and MemoryPool example

This example shows [Queue](queue.html) and MemoryPool managing measurements.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/rtos_queue/)](https://os.mbed.com/teams/mbed_example/code/rtos_queue/file/bbbae4aa4768/main.cpp)

## Related content

- [Queue](queue.html) API reference.
