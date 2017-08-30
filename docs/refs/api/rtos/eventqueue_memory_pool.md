#### EventQueue memory pool

When you create an instance of the [EventQueue](events.md), you specify a fixed size for its memory. Because allocating from the general purpose heap is not IRQ safe, the EventQueue allocates this fixed size block of memory during its creation. Although the EventQueue memory size is fixed, the Eventqueue supports various sized events.

Various sized events introduce fragmentation to the memory region. This fragmentation makes it difficult to determine how many more events the EventQueue can dispatch. The EventQueue may be able to dispatch many small events, but fragmentation may prevent it from allocating one large event.

##### Calculating the number of events

If your project only uses fix-sized events, you can use a counter that tracks the number of events the EventQueue has dispatched.

If your projects uses variable-sized events, you can calculate the number of available events of a specific size because successfully allocated memory is never fragmented further. However, untouched space can service any event that fits, which complicates such a calculation.

```
EventQueue queue(8*sizeof(int)); // 8 words of storage
queue.call(func, 1);       // requires 2 words of storage
queue.call(func, 1, 2, 3); // requires 4 words of storage
// after this we have 2 words of storage left

queue.dispatch(); // free all pending events

queue.call(func, 1, 2, 3); // requires 4 words of storage
queue.call(func, 1, 2, 3); // fails
// remaining storage has been fragmented into 2 events with 2 words 
// of storage, no space is left for a 4 word event even though 4 bytes
// exist in the memory region
```

##### Failure due to fragmentation

The following example would fail because of fragmentation:

```
EventQueue queue(4*sizeof(int)); // 4 words of storage
queue.call(func);       // requires 1 word of storage
queue.call(func);       // requires 1 word of storage
queue.call(func);       // requires 1 word of storage
queue.call(func);       // requires 1 word of storage
// 0 words of storage remain

queue.dispatch();  // free all pending events
// all memory is free again (4 words) and in one-word chunks

queue.call(func, 1, 2, 3); // requires 4 words of storage, so allocation fails
```

Four words of storage are free but only for allocations of one word or less. The solution to this failure is to increase the size of your EventQueue. Having the proper sized EventQueue prevents you from running out of space for events in the future.
