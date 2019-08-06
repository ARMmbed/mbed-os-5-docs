# Wait

Wait functions provide simple wait capabilities. The OS scheduler puts the current thread in `waiting state`, allowing another thread to execute. Even better: If there are no other threads in `ready state`, it can put the whole microcontroller to `sleep`, saving energy.

## Avoiding OS delay

When you call wait, your board's CPU will sleep in the RTOS for the whole number of milliseconds and then spin as necessary to make up the remaining fraction of a millisecond. However, it blocks the platform deep sleep for the entire duration.

## Wait function reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/mbed__wait__api_8h_source.html)

## Example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/wait_ex_1/)](https://os.mbed.com/teams/mbed_example/code/wait_ex_1/file/4f0543415053/main.cpp)

## Related content

- [RTOS](rtos.html) overview.
- [Application flow control tutorial](../tutorials/application-flow-control.html).
