## Serial Audio Interface (SAI)

The Serial Audio Interface (SAI) provides a class to communicate with audio devices. SAI is a broader feature that encompasses audio interfaces such as I2S.

SAI uses a four wire serial protocol consisting of:
  * Master Clock Pin  (mclk)
  * Data Pin          (sd)
  * Bit Clock pin     (bclk)
  * Word Clock Pin    (wclk)

The master clock is used to optionally synchronize the device's IO lines. When using SAI to communicate in loopback or with an on-target audio codec, there may be an internally shared master clock and this pin is not required. The `mclk_source` field in the format object that may be optionally passed into the SAI constructor can be set to internal, external or sibling.

The bit clock fires on each bit of data transmitted across the data lines, and its frequency is determined by the sampling rate, number of bits per channel and number of channels. The sampling rate is highly device-dependent and needs to be configured for each target (typically found in the target's device.h file).

The word clock runs at the frequency as the sample rate. It is used to select which active audio channel is being transmitted.

The SAI constructor requires the above pins as well as direction of data transfer (transmitter or receiver). Optionally the SAITransmitter and SAIReceiver classes can be used requiring only the pins.

Note for full duplex two objects will need to be instantiated.

### Frame Formats
| Data Type | Field | Description |
|-----------|-------|-------------|
| bool      | bclk_polarity | true for Active high                                                     |
| bool      | wclk_polarity | true for Active high                                                     |
| bool      | ws_delay      | true to toggle ws one bit earlier than the frame                         |
| uint8_t   | ws_length     | ws assertion length from 1bclk to word length                            |
| uint8_t   | frame_length  | Frame length in word count [1: 32]                                       |
| uint32_t  | word_mask     | Mask on frame for used word (bitfield)                                   |
| uint8_t   | word_length   | Word length in bits [1: 32]                                              |
| uint8_t   | data_length   | Data length within the word. This must less than or equal to word_length |
| bool      | lsb_first     | true to send LSB first                                                   |
| bool      | aligned_left  | true to align Left                                                       |
| uint8_t   | bit_shift     | sample bit shift distance from its alignment point                       |

### Errors

 * `sai_init()` returns `SAI_RESULT_INVALID_PARAM`  if at least one of the given parameters is undefined (NULL)
 * `sai_init()` returns `SAI_RESULT_ALREADY_INITIALIZED` if SAI is already initialized
 * `sai_init()` returns `SAI_RESULT_CONFIG_UNSUPPORTED` if the device can never support this configuration
 * `sai_init()` returns `SAI_RESULT_CONFIG_MISMATCH` if the device is not able to support this configuration at this point time because of other 'live' constraints
 (such as a shared format/clock configuration with a sibling)
 * `sai_free()` does nothing if passed a NULL pointer
 * `sai_free()` de-initialized & un-clock unused part of the device a device/block can be reinitialized via `sai_init()` after being `sai_free()`d.

### SAI class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_sai.html)

### SAI hello, world

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/SAI_HelloWorld/)](https://os.mbed.com/teams/mbed_example/code/SAI_HelloWorld/file/fa13d56ff9ff/main.cpp)
