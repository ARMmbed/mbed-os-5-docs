# Thread safety and porting

The [thread safety documentation is available in our Reference section](../reference/thread-safety.html).

## Considerations when porting

Porting new platforms to Mbed OS 5 is nearly the same as it is in Mbed 2. In general, drivers that operate below the C HAL layer don't need synchronization mechanisms because this is already provided at a higher level. The only exceptions to this are the functions `port_read`, `port_write`, `gpio_read` and `gpio_write`, which are expected to use processor-specific `set` and `clear` registers rather than performing a read-modify-write sequence. For more information, see the [example](https://github.com/mbedmicro/mbed/blob/52e93aebd083b679a8fe7b0e47039f138fa8c224/hal/targets/hal/TARGET_Freescale/TARGET_KSDK2_MCUS/TARGET_K64F/drivers/fsl_gpio.h#L135).

## HAL C API

The HAL C API is the porting layer of Mbed OS 5 and is not thread safe. Developers should not typically use this API directly, instead using the higher-level drivers and libraries. If you program directly to the HAL C API, it is your responsibility to synchronize operations with an appropriate mechanism, such as a mutex.
