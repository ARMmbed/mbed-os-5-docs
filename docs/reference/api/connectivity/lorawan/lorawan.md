<h2 id="lorawan-api">LoRaWAN</h2>

LoRaWAN is a technology designed for low-power battery powered devices. These devices operate in an unlicensed spectrum, creating high desnity wide-area networks.

Arm Mbed OS provides a native network stack for LoRaWAN, which can run on any Mbed Enabled device with a LoRa radio onboard. 

The [LoRaWANInterface](https://github.com/ARMmbed/mbed-os/blob/feature-lorawan/features/lorawan/LoRaWANInterface.h) provides a C++ API for connecting to the internet over a LoRa network.

## LoRaWANInterface class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/class_l_o_r_a_w_a_n_interface.html)

## Usage

To bring up the Mbed LoRaWAN stack, consider the following progression: 

1) An [EventQueue](https://os.mbed.com/docs/v5.8/reference/eventqueue.html) object. 

```cpp
// construct an event queue 
EventQueue ev_queue(NUM_EVENTS * EVENTS_EVENT_SIZE);
```
2) A [LoRaRadio](https://os.mbed.com/docs/v5.8/reference/loraradio.html) object

```CPP
// construct a LoRadio object
SX1272_LoRaRadio radio(PIN_NAMES ... );
```

3) Instantiate `LoRaWANInterface` and pass `LoRaRadio` object

```CPP
LoRaWANInterface lorawan(radio) ;
``` 

4) Initialize mac layer and pass `EventQueue` object

```CPP
lorawan.initialize(&ev_queue);
```

5) Setup the event callback.

```cpp
lorawan_app_callbacks_t callbacks
callbacks.events = mbed::callback(YOUR_EVENT_HANDLER);
lorawan.add_app_callbacks(&callbacks);
```

6) Add network credentials (security keys) and any configurations.

```CPP
lorawan_connect_t connection;

connection.connect_type = LORAWAN_CONNECTION_OTAA;
connection.connection_u.otaa.app_eui = YOUR_APP_EUI_KEY;
connection.connection_u.otaa.dev_eui = YOUR_DEV_EUI_KEY;
connection.connection_u.otaa.app_key = YOUR_APP_KEY;
connection.connection_u.otaa.nb_trials = MBED_CONF_LORA_NB_TRIALS;

lorawan.connect(connection);
``` 

### LoRaWAN example

Please visit our [github example repository](https://github.com/ARMmbed/mbed-os-example-lorawan) and follow the instructions in the `README.md`.

### Related content

- End-to-end [LoRa on Arm Mbed tutorial](https://docs.mbed.com/docs/lora-with-mbed/en/latest/).
