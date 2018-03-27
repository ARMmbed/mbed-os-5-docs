<h2 id="lorawan-api">LoRaWANInterface</h2>

LoRaWAN is a technology designed for low-power battery powered devices. These devices operate in an unlicensed spectrum, creating high density wide-area networks.

Arm Mbed OS provides a native network stack for LoRaWAN, which can run on any Mbed Enabled device with a LoRa radio onboard.

The [LoRaWANInterface](https://os.mbed.com/docs/v5.8/mbed-os-api-doxy/class_lo_ra_w_a_n_interface.html) provides a C++ API for connecting to the internet over a LoRa network.

### LoRaWANInterface class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.8/mbed-os-api-doxy/class_lo_ra_w_a_n_interface.html)

### Usage

To bring up the Mbed LoRaWAN stack, consider the following progression:

1) An [EventQueue](https://os.mbed.com/docs/v5.8/reference/eventqueue.html) object:

```cpp
// construct an event queue
EventQueue ev_queue(NUM_EVENTS * EVENTS_EVENT_SIZE);
```

2) A [LoRaRadio](https://os.mbed.com/docs/v5.8/reference/loraradio-api.html) object:

```CPP
// construct a LoRadio object
SX1272_LoRaRadio radio(PIN_NAMES ... );
```

3) Instantiate `LoRaWANInterface`, and pass `LoRaRadio` object:

```CPP
LoRaWANInterface lorawan(radio) ;
```

4) Initialize mac layer and pass `EventQueue` object:

```CPP
lorawan.initialize(&ev_queue);
```

5) Set up the event callback:

```cpp
lorawan_app_callbacks_t callbacks
callbacks.events = mbed::callback(YOUR_EVENT_HANDLER);
lorawan.add_app_callbacks(&callbacks);
```

6) Add network credentials (security keys) and any configurations:

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

Please visit our Arm Mbed Online Compiler example, and follow the instructions in the `README.md`.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-lorawan/)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-lorawan/file/dc95ac6d6d4e/main.cpp)

### Related content

- End-to-end [LoRa on Arm Mbed tutorial](https://docs.mbed.com/docs/lora-with-mbed/en/latest/).
