#### EventQueue memory pool

[TO-DO: A document about the fragmentation of the memory pool of the EventQueue. This documentation should include how it works, use cases and behaviors. Start by rewriting the information from https://github.com/ARMmbed/mbed-os/issues/3873.]

The [EventQueue API](events.md) memory is a fixed size. This fixed size is what makes the EventQueue's allocation of events interrupt safe. Allocating from the general purpose heap is not IRQ safe. Although the EventQueue memory sized is fixed, the Eventqueue supports events of are variable size. 

Variable-sized events introduce fragmentation to the memory region. This fragmentation makes it difficult to determine how many more events the EventQueue can dispatch. The EventQueue may be able to dispatch many small events, but fragmentation may prevent it from allocating one large event. 

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

The following example would fail because of fragmentation: [NOTE: EXAMPLE GIVEN BY OTHERS. REPLACE.]

```
EventQueue queue(8*sizeof(int)); // 8 words of storage
queue.call(func, 1);       // requires 2 words of storage
queue.call(func, 1);       // requires 2 words of storage
queue.call(func, 1);       // requires 2 words of storage
queue.call(func, 1);       // requires 2 words of storage
// after this we have 0 words of storage left

queue.dispatch();  // free all pending events
// now all memory should be free again (8 words)?

queue.call(func, 1, 2, 3); // requires 4 words of storage --> Would this fail now?
```

Four words of storage are free but only for allocations fewer than than two words.

The EventQueue has two allocators. One is a simple slab of memory that feeds a set of fixed size allocators. The slab is maintained by a single pointer into the buffer that indicates how much unallocated space is left. In theory, the slab could support deallocation but only from the front.

It's possible to coalesce with two extra words in each chunk, but these could only be returned to the slab if they border it. As soon as you allocate a chunk near the end of the buffer, the free chunks in front could never be returned. A more sophisticated allocator that could recover chunks for the slab may have to traverse the entire buffer, which would be too costly for interrupt contexts.

Because recovering chunks isn't reliable and coalescing requires two additional words, coalescing was dropped.

This isn't that bad of a thing. Coalescing is less important for event queues than general-purpose memory allocators. Event queues don't change "modes" often, so previously allocated chunks are likely to be reused. The bigger risk in event queues is when multiple aperiodic events end up occuring at the same time. Coalescing chunks could end up hiding a problem that doesn't show itself until later in the life of the application.
