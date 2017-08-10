#### EventQueue memory pool

[TO-DO: A document about the fragmentation of the memory pool of the EventQueue. This documentation should include how it works, use cases and behaviors. Start by rewriting the information from https://github.com/ARMmbed/mbed-os/issues/3873.]

It is not possible to know how many events are in an eventqueue, and it is not possible to have the current and maxium number of events present in an [eventqueue](https://github.com/ARMmbed/mbed-os/tree/master/events). You cannot tailor the EventQueue size to the actual maximum number of events that need to be handled in the queue at the same time. The event queue supports dynamically sized contexts, which makes determining how many more events can be dispatched complicated. By this, we mean the events are variable size, but the memory the event queue operates out of is not. This is required to allocate events in interrupt context safely (allocations from the general purpose heap is not irq safe).

Variable sized events introduce fragmentation in this memory region, which makes it difficult to know exactly how many more events can be allocated. Even if you can dispatch many small events, fragmentation may prevent you from allocating a single larger event. If you are only using fix-sized events, you can just keep a counter tracking how many events have been dispatched.

Adding this sort of statistics is a good idea, though we don't have any hooks in place currently. There is an internal variable that holds how much space is untouched (EventQueue._equeue.slab.size), but this may change from version to version, and a different implementation of the event queue may not have access to this information at all.

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

The event queue does have some strong garuntees on fragmentation. Once an allocation has been successful, that unit of memory will never be fragmented further (this is important for periodic systems). You could calculate how many events are available for a specific size of event, but this is also complicated by untouched space, which can service any event that fits.

The following case would fail because of fragmentation: [NOTE: EXAMPLE GIVEN BY OTHERS. REPLACE.]

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

Four words of storage are free but only for allocations less than 2 words.

The event queue has two separate allocators. One is a simple slab of memory that feeds a set of fixed size allocators. The slab is maintained by a single pointer into the buffer that indicates how much unallocated space is left. In theory, the slab could support deallocation, but only from the front.

It's possible to coalesce with two extra words in each chunk, but these could only be returned to the slab if they border it. As soon as you allocate a chunk near the end of the buffer, the free chunks in front could never be returned. A more sophisticated allocator that could recover chunks for the slab may have to traverse the entire buffer, which would be too costly for interrupt contexts.

Because recovering chunks isn't reliable and coalescing requires two additional words, coalescing was dropped.

This isn't that bad of a thing. Coalescing is less important for event queues than general-purpose memory allocators. Event queues don't change "modes" often, so previously allocated chunks are likely to be reused. The bigger risk in event queues is when multiple aperiodic events end up occuring at the same time. Coalescing chunks could end up hiding a problem that doesn't show itself until later in the life of the application.
