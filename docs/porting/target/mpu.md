<h1 id="mpu-port">MPU</h1>

Implementing the MPU API enables Mbed OS to provide better security by preventing code execution and code modification where it shouldn't be allowed.

## Assumptions

### Defined behavior

- The function `mbed_mpu_init` is safe to call repeatedly.
- The function `mbed_mpu_free` disables MPU protection.
- Execution from RAM results in a fault when `execute never` is enabled. This RAM includes heap, stack, data and zero init.
- Writing to ROM results in a fault when `write never` is enabled.

### Undefined behavior

- Calling any function other than `mbed_mpu_init` before the initialization of the MPU.

## Dependency

Hardware MPU capabilities.

## Implementing the MPU API

You can find the API and specification for the MPU API in the following header file:

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/development/mbed-os-api-doxy/group__hal__mpu.html)

To enable MPU support in Mbed OS, add the `MPU` label in the `device_has` option of the target's section in the `targets.json` file.

Targets with a standard ARMv7-M or ARMv8-M MPU, indicated by `__MPU_PRESENT` being defined to 1 in the target's CMSIS header, only need the `MPU` label in the `device_has` for MPU support. This pulls in a common Mbed OS MPU driver, so you don't need a target-specific driver.

Targets with a standard ARMv7-M or ARMv8-M MPU needing to override the common Mbed OS MPU driver can do so by defining `MBED_MPU_CUSTOM`. This removes the common Mbed OS MPU driver from builds, so you can use a target-specific one, instead.

## Testing

The Mbed OS HAL provides a set of conformance tests for the MPU API. You can use these tests to validate the correctness of your implementation. To run the MPU HAL tests, use the following command:

```
mbed test -t <toolchain> -m <target> -n "tests-mbed_hal-mpu*"
```

You can read more about the test cases:

 [![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/development/mbed-os-api-doxy/group__hal__mpu__tests.html)
