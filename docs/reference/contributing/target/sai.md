<h2 id="sai-port">Serial Audio Interface (SAI)</h2>

Implementing SAI enables Mbed OS to emit and receive an audio data stream.

<span class="warnings">**Warning:** We are changing the SAI API in an upcoming release of Mbed OS. This page documents code that exists on a feature branch of Mbed OS. You can find details on how it may affect you in the [implementing the RTC API](#implementing-the-rtc-api) section.

### Assumptions

#### Defined behavior

- `sai_init()` returns `SAI_RESULT_INVALID_PARAM` if at least one of the given parameters is undefined (NULL).
- `sai_init()` returns `SAI_RESULT_ALREADY_INITIALIZED` if SAI is already initialized.
- `sai_init()` returns `SAI_RESULT_CONFIG_UNSUPPORTED` if the device can never support this configuration.
- `sai_init()` returns `SAI_RESULT_CONFIG_MISMATCH` if the device is not able to support this configuration now because of other 'live' constraints, such as a shared format or clock configuration with a sibling.
- `sai_free()` does nothing if passed a NULL pointer.
- `sai_free()` deinitializes and unclocks the unused part of the device.
- You can reinitialize a device or block by using `sai_init()` after you use `sai_free()` on it.

If the device is a *receiver*:

- `sai_xfer()` returns false if the `sai_t` object is NULL.
- `sai_xfer()` returns false if there's no sample in the FiFo.
- `sai_xfer()` if `psample` is NULL; it pops 1 sample from the FiFo and returns true.
- `sai_xfer()` if `psample` is not NULL; it pops 1 sample from the FiFo, stores it to the address pointed by `psample` and returns true.

If the device is a *transmitter*:

- `sai_xfer()` returns false if the `sai_t` object is NULL.
- `sai_xfer()` returns false if the FiFo is full and you can't push `*psample`.
- `sai_xfer()` if `psample` is NULL; it pushes one '0' sample to the FiFo and returns true.
- `sai_xfer()` if `psample` is not NULL; it pushes the pointed sample to the FiFo and returns true.

#### Undefined behavior

- Calling any function other than `sai_init()` before the initialization of the SAI.
- Calling any function other than `sai_init()` after calling `sai_free()`.

#### Other requirements

A target must also define these elements to allow tests to be run:

- `#define SAI_DEFAULT_SAMPLE_RATE (xxxxxU)`.
- Pins for 2 SAI orI2S interfaces, including MCLK, BCLK, WCLK and SD named:
  - SAI_A_MCLK, SAI_A_BCLK, SAI_A_WCLK and SAI_A_SD.
  - SAI_B_MCLK, SAI_B_BCLK, SAI_B_WCLK and SAI_B_SD.

#### Notes

Watch out for this common trouble area when implementing this API. You should consider a transceiver supporting asynchronous rx/tx as 2 different peripherals:

   - One read-only.
   - One write-only.
   
   The first allocated channel may or may not limit the second one's feature. For example, in a peripheral that supports asynchronous rx/tx but requires the format of both instances to be the same, the first allocated instance sets the format and ties the second one to this format.

### Dependencies

Hardware SAI/I2S capabilities.

### Implementing the RTC API

You can find the API and specification for the SAI API in the following header file:

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/feature-hal-spec-sai/group__hal__sai.html)

To enable SAI support in Mbed OS, add the `SAI` label in the `device_has` option of the target's section in the `targets.json` file.

### Testing

The Mbed OS HAL provides a set of conformance tests for SAI. You can use these tests to validate the correctness of your implementation. To run the SAI HAL tests, use the following command:

```
mbed test -t <toolchain> -m <target> -n "tests-mbed_hal-sai*"
```

You can read more about the test cases:

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/feature-hal-spec-sai/group__hal__sai__tests.html)
