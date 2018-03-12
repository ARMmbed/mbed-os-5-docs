### SAI : Serial Audio Interface

Implementing SAI enables Mbed OS to emit and/or receive an audio data stream.

#### Assumptions

##### Defined behavior

 - Supports a subset of the possible configuration space - verified by ::sai_
 - Reports a failure (returns false) upon any invocation to an unsupported feature/parameter - verified by ::sai_
 - Is able to indicate the currently processed word - verified by ::sai_

###### (optional) Defined behavior if feature supported
 - Is able to change receiver format without interrupting transmitter format - verified by ::sai_
 - Is able to change transmitter format without interrupting receiver format - verified by ::sai_
 - Is able to change transmitter and receiver format without interrupting the current frame - verified by ::sai_

##### Undefined behavior

 - Calling any function other than `sai_init` before the initialization of the SAI.

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
