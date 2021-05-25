# Wait

<span class="notes">**Note:** The function `wait` is deprecated in favor of explicit sleep functions. To sleep, replace `wait` with `ThisThread::sleep_for` (C++) or `thread_sleep_for` (C). To wait (without sleeping), call `wait_us`. `wait_us` is safe to call from ISR context.</span>

The wait_us and wait_ns functions provide precise wait capabilities. These functions spin the CPU to produce a small delay so they should only be used for short delays. Any delay larger than a millisecond will affect power and multithread performance, and block the platform deep sleep for the entire duration. Therefore, spinning for millisecond wait is not recommended, and ThisThread::sleep_for should be used instead.

## Wait function reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v6.11/mbed-os-api-doxy/mbed__wait__api_8h_source.html)

## Example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/wait_ex_1/)](https://os.mbed.com/teams/mbed_example/code/wait_ex_1/file/4f0543415053/main.cpp)

## Related content

- [RTOS](../apis/scheduling-concepts.html) overview.
- [Application flow control tutorial](../apis/platform-tutorials.html).
