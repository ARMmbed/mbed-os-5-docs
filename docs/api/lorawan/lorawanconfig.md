<h1 id="lorawan-configuration">LoRaWAN</h1>

Various parameters for Mbed LoRaWAN stack can be configured via either C++ APIs or by using the Mbed configuration system.

## Using the Mbed Configuration system

Here are the parameters that you can configure using the Mbed configuration system:

```
Configuration parameters
------------------------
Name: lora.adr-on
    Description: LoRaWAN Adaptive Data Rate, default: 1
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_ADR_ON
    Value: 1 (set by library:lora)
Name: lora.app-port
    Description: LoRaWAN application port, default: 15
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_APP_PORT
    Value: 15 (set by library:lora)
Name: lora.application-eui
    Description: Application IEEE EUI
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_APPLICATION_EUI
    Value: {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00} (set by library:lora)
Name: lora.application-key
    Description: AES encryption/decryption cipher application key
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_APPLICATION_KEY
    Value: {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00} (set by library:lora)
Name: lora.appskey
    Description: AES encryption/decryption cipher application session key
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_APPSKEY
    Value: {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00} (set by library:lora)
Name: lora.automatic-uplink-message
    Description: Stack will automatically send an uplink message when lora server requires immediate response
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_AUTOMATIC_UPLINK_MESSAGE
    Value: 1 (set by library:lora)
Name: lora.device-address
    Description: Device address on the network
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_DEVICE_ADDRESS
    Value: 0x00000000 (set by library:lora)
Name: lora.device-eui
    Description: Mote device IEEE EUI
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_DEVICE_EUI
    Value: {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00} (set by library:lora)
Name: lora.downlink-preamble-length
    Description: Number of whole preamble symbols needed to have a firm lock on the signal.
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_DOWNLINK_PREAMBLE_LENGTH
    Value: 5 (set by library:lora)
Name: lora.duty-cycle-on
    Description: Enables/disables duty cycling. NOTE: Disable only for testing. Mandatory in many regions.
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_DUTY_CYCLE_ON
    Value: 1 (set by library:lora)
Name: lora.duty-cycle-on-join
    Description: Enables/disables duty cycling for JOIN requests (disabling requires duty-cycle-on to be disabled). NOTE: Disable only for testing!
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_DUTY_CYCLE_ON_JOIN
    Value: 1 (set by library:lora)
Name: lora.fsb-mask
    Description: FSB mask for upstream [Only for US915 & AU915] Check lorawan/FSB_Usage.txt for more details
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_FSB_MASK
    Value: {0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00FF} (set by library:lora)
Name: lora.fsb-mask-china
    Description: FSB mask for upstream [CN470 PHY] Check lorawan/FSB_Usage.txt for more details
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_FSB_MASK_CHINA
    Value: {0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF} (set by library:lora)
Name: lora.lbt-on
    Description: Enables/disables LBT. NOTE: [This feature is not yet integrated].
    Defined by: library:lora
    No value set
Name: lora.max-sys-rx-error
    Description: Max. timing error fudge. The receiver will turn on in [-RxError : + RxError]
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_MAX_SYS_RX_ERROR
    Value: 5 (set by library:lora)
Name: lora.nb-trials
    Description: Indicates how many times join can be tried, default: 12
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_NB_TRIALS
    Value: 12 (set by library:lora)
Name: lora.nwkskey
    Description: AES encryption/decryption cipher network session key
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_NWKSKEY
    Value: {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00} (set by library:lora)
Name: lora.over-the-air-activation
    Description: When set to 1 the application uses the Over-the-Air activation procedure, default: true
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_OVER_THE_AIR_ACTIVATION
    Value: 1 (set by library:lora)
Name: lora.phy
    Description: LoRa PHY region: EU868, AS923, AU915, CN470, CN779, EU433, IN865, KR920, US915
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_PHY
    Value: EU868 (set by library:lora)
Name: lora.public-network
    Description: LoRaWAN will connect to a public network or private network, true = public network
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_PUBLIC_NETWORK
    Value: 1 (set by library:lora)
Name: lora.tx-max-size
    Description: User application data buffer maximum size, default: 64, MAX: 255
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_TX_MAX_SIZE
    Value: 64 (set by library:lora)
Name: lora.uplink-preamble-length
    Description: Number of preamble symbols to transmit. Default: 8
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_UPLINK_PREAMBLE_LENGTH
    Value: 8 (set by library:lora)
Name: lora.wakeup-time
    Description: Time in (ms) the platform takes to wakeup from sleep/deep sleep state. This number is platform dependent
    Defined by: library:lora
    Macro name: MBED_CONF_LORA_WAKEUP_TIME
    Value: 5 (set by library:lora)
```

For changing any of these parameters, edit the `mbed_app.json` file in the root of your application. Prefix the parameter name with `lora.`, e.g., `lora.my-parameter: value`.

```json
"target_overrides": {
    "*": {
        "lora.device-address":  "0x12345678",
        "lora.over-the-air-activation": true,
        "lora.duty-cycle-on": true
    }
}
```

## Using APIs from LoRaWANInterface

See the [API reference](../apis/lorawan.html) for information about how to use these APIs from the LoRaWANInterface.
