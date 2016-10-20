# Runtime Statistics

Mbed 5.0 provides various runtime statistics to help characterize resource usage. This allows potential problems, such as a stack close to overflowing, to be easily identified. The metrics currently supported are available for the heap and the stack.

## Heap stats

Heap statistics provide exact information about the number of bytes dynamically allocated by a program. It does not take into account heap fragmentation or allocation overhead. This allows allocation size reported to remain consistent regardless of order of allocation (fragmentation) or allocation algorithm used (overhead).

To enable heap stats add the command line flag ```-DMBED_HEAP_STATS_ENABLED=1``` . A snapshot of heap stats can then be taken with the function **mbed_stats_heap_get()**. Note - this function is available even when the heap stats are not enabled, but always returns zero for all fields.

### Example use cases
* Getting worst case memory usage, ```max_size```, so MCU ram can be properly sized 
* Detecting program memory leaks by the current size allocated ```current_size``` and or number of allocations in use ```alloc_cnt```.
* Check if allocations have been failing and if so how many with ```alloc_fail_cnt```.

### Example program using heap statistics
```
#include "mbed.h"
#include "mbed_stats.h"

int main(void)
{
    mbed_stats_heap_t heap_stats;

    printf("Starting heap stats example\r\n");

    void *allocation = malloc(1000);
    printf("Freeing 1000 bytes\r\n");

    mbed_stats_heap_get(&heap_stats);
    printf("Current heap: %lu\r\n", heap_stats.current_size);
    printf("Max heap size: %lu\r\n", heap_stats.max_size);

    free(allocation);

    mbed_stats_heap_get(&heap_stats);
    printf("Current heap after: %lu\r\n", heap_stats.current_size);
    printf("Max heap size after: %lu\r\n", heap_stats.max_size);
}
```

### Side effects of enabling heap stats
* An additional 8 bytes of overhead for each memory allocation
* The function ```realloc``` will always never reuse the buffer it is resizing
* Memory allocation is slightly slower due to the added book keeping


## Stack stats

Stack stats provide information on the allocated stack size of a thread and the wost case stack usage. Any thread on the system can be queried for stack information. To enable heap stats add the command line flag ```-DMBED_STACK_STATS_ENABLED=1```.

### Example program using stack statistics

```
#include "mbed.h"
#include "cmsis_os.h"

int main(void)
{
    printf("Starting stack stats example\r\n");

    osThreadId main_id = osThreadGetId();

    osEvent info;
    info = _osThreadGetInfo(main_id, osThreadInfoStackSize);
    if (info.status != osOK) {
        error("Could not get stack size");
    }
    uint32_t stack_size = (uint32_t)info.value.v;
    info = _osThreadGetInfo(main_id, osThreadInfoStackMax);
    if (info.status != osOK) {
        error("Could not get max stack");
    }
    uint32_t max_stack = (uint32_t)info.value.v;

    printf("Stack used %li of %li bytes\r\n", max_stack, stack_size);
}
```
*The stack statistics API is experimental and will change in the future

