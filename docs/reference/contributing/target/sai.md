### SAI : Serial Audio Interface

Implementing SAI enables Mbed OS to emit and/or receive an audio data stream.

#### Assumptions

##### Defined behavior

- `sai_init()` returns `SAI_RESULT_INVALID_PARAM`  if at least one of the given parameters is undefined (NULL) ;
- `sai_init()` returns `SAI_RESULT_ALREADY_INITIALIZED` if SAI is already initialized ;
- `sai_init()` returns `SAI_RESULT_CONFIG_UNSUPPORTED` if the device can never support this configuration ;
- `sai_init()` returns `SAI_RESULT_CONFIG_MISMATCH` if the device is not able to support this configuration at this point time because of other 'live' constraints (such as a shared format/clock configuration with a sibling) ;
- `sai_free()` does nothing if passed a NULL pointer ;
- `sai_free()` de-initialized & un-clock unused part of the device ;
- a device/block can be reinitialized via `sai_init()` after being `sai_free()`d.

If the device is a *receiver* :
- `sai_xfer()` returns false if the `sai_t` object is NULL ;
- `sai_xfer()` returns false if there's no sample in the FiFo ;
- `sai_xfer()` if `psample` is NULL : it pops 1 sample from the FiFo and returns true ;
- `sai_xfer()` if `psample` is not NULL : it pops 1 sample from the FiFo, stores it to the address pointed by `psample`,  and returns true.

If the device is a *transmitter* :
- `sai_xfer()` returns false if the `sai_t` object is NULL ;
- `sai_xfer()` returns false if the fifo is full and `*psample` could not be pushed ;
- `sai_xfer()` if `psample` is NULL : it pushes one '0' sample to the FiFo and returns true ;
- `sai_xfer()` if `psample` is not NULL : it pushes the pointed sample to the FiFo and returns true.

##### Undefined behaviours

- Calling any function other than `sai_init()` before the initialization of the SAI ;
- Calling any function other than `sai_init()` after calling `sai_free()`.

##### other requirements

A target must also define these elements to allow tests to be run.
- `#define SAI_DEFAULT_SAMPLE_RATE (xxxxxU)` ;
- Pins for 2 SAI/I²S interface including MCLK, BCLK, WCLK and SD named respectively
  - SAI_A_MCLK, SAI_A_BCLK, SAI_A_WCLK and SAI_A_SD ;
  - SAI_B_MCLK, SAI_B_BCLK, SAI_B_WCLK and SAI_B_SD.

##### Notes

Watch out for these common trouble areas when implementing this API:

 - A transceiver supporting async rx/tx should be considered as 2 different peripherals :
   - one read-only
   - one write-only
   The first allocated channel may or may not limit the second one's feature.
   eg:
   In a peripheral that supports async rx/tx but requires format to be the same, the first allocated instance will set the format and tie the second one to this format.

#### Dependencies

Hardware SAI/I²S capabilities.

#### Implementing the RTC API

You can find the API and specification for the SAI API in the following header file:

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/feature-hal-spec-sai/group__hal__sai.html)

To enable SAI support in Mbed OS, add the `SAI` label in the `device_has` option of the target's section in the `targets.json` file.

#### Testing

The Mbed OS HAL provides a set of conformance tests for SAI. You can use these tests to validate the correctness of your implementation. To run the SAI HAL tests, use the following command:

```
mbed test -t <toolchain> -m <target> -n "tests-mbed_hal-sai*"
```

You can read more about the test cases:

 [![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/feature-hal-spec-sai/group__hal__sai__tests.html)
