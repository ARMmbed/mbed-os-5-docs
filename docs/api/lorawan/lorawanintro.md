# LoRaWAN overview

LoRaWAN is a technology designed for low-power battery powered devices. These devices operate in an unlicensed spectrum, creating high density wide-area networks.

Arm Mbed OS provides a native network stack for LoRaWAN, which can run on any Mbed Enabled device with a LoRa radio onboard.

The [LoRaWANInterface](lorawan-api.html) provides a C++ API for connecting to the internet over a LoRa network.

## Usage

To bring up the Mbed LoRaWAN stack, consider the following progression:

1) An [EventQueue](eventqueue.html) object:

```cpp TODO
// construct an event queue
EventQueue ev_queue(NUM_EVENTS * EVENTS_EVENT_SIZE);
```

2) A [LoRaRadio](lorawan-api.html) object:

```CPP TODO
// construct a LoRadio object
SX1272_LoRaRadio radio(PIN_NAMES ... );
```

3) Instantiate `LoRaWANInterface`, and pass `LoRaRadio` object:

```CPP TODO
LoRaWANInterface lorawan(radio) ;
```

4) Initialize mac layer and pass `EventQueue` object:

```CPP TODO
lorawan.initialize(&ev_queue);
```

5) Set up the event callback:

```cpp TODO
lorawan_app_callbacks_t callbacks
callbacks.events = mbed::callback(YOUR_EVENT_HANDLER);
lorawan.add_app_callbacks(&callbacks);
```

6) Add network credentials (security keys) and any configurations:

```CPP TODO
lorawan_connect_t connection;

connection.connect_type = LORAWAN_CONNECTION_OTAA;
connection.connection_u.otaa.app_eui = YOUR_APP_EUI_KEY;
connection.connection_u.otaa.dev_eui = YOUR_DEV_EUI_KEY;
connection.connection_u.otaa.app_key = YOUR_APP_KEY;
connection.connection_u.otaa.nb_trials = MBED_CONF_LORA_NB_TRIALS;

lorawan.connect(connection);
```

Owing to the fact that most of the LoRaWAN devices are simple telemetry devices, the stack and its operation need to be as simple as possible. That's why the Mbed LoRaWAN stack is event driven.

### Network events and callbacks

Here is the list of possible events that you can post from the stack to the application:

| Event    | Description
| --------------- | ------------- |
| `CONNECTED` | When the connection is complete |
| `DISCONNECTED` | When the protocol is shut down in response to disconnect() |
| `TX_DONE` | When a packet is transmitted |
| `TX_TIMEOUT` | When the stack is unable to send packet in TX window |
| `TX_ERROR` | A general TX error |
| `TX_CRYPTO_ERROR` | If MIC fails, or any other crypto related error |
| `TX_SCHEDULING_ERROR` | When the stack is unable to schedule a packet |
| `TX_TIMEOUT` | When the stack is unable to send a packet in TX window  |
| `RX_DONE` | When a packet is received |
| `RX_ERROR` | A general RX error |

The application must attach an event handler to the stack. The `LoRaWANInterface` provides an API to attach various callbacks to the stacks. One such callback is the event handler callback.

### Application callbacks

The Mbed LoRaWAN stack currently maps 3 different callbacks:

| Callback type   | Description
| --------------- | ------------- |
| `Event callback` | Mandatory, Direction: from stack to application |
| `Link check response callback` |Optional, Direction: from stack to application |
| `Battery level callabck` | Optional, Direction: from application to stack |

#### Event handler

An example of attaching your event handler to the stack:

```CPP TODO

void your_event_handler(lorawan_event_t event)
{
    switch (event) {
        case CONNECTED:
        //do something
            break;
        case DISCONNECTED:
            break;
	....
	....
    }
}
lorawan_app_callbacks_t callbacks;

callbacks.events = mbed::callback(your_event_handler);
//lorawan is the LoRaWANInterface object
lorawan.add_app_callbacks(&callbacks);
```

#### Link check response handler

Link check request is a MAC command defined by the LoRaWAN specification. To receive the response of this MAC command, set the `link_check_resp` callback.

```CPP TODO
void your_link_check_response(uint8_t demod_margin, uint8_t num_gw)
{
	//demod_margin is the demodulation margin
	// num_gw represents the number of gateways involved in the path
}

callbacks.link_check_resp = mbed::callback(your_link_check_response);
lorawan.add_app_callbacks(&callbacks);

```

#### Battery level handler

The battery level callback is different from others. The direction of this callback is from the application to the stack. In other words, it provides information to the stack. The application is reponsible for letting the stack know about the current battery level.

```CPP TODO
uint8_t your_battery_level()
{
	return battery_level;
}

callbacks.battery_level = mbed::callback(your_battery_level);
lorawan.add_app_callbacks(&callbacks);
```

#### Error codes

All operations on `LoRaWANInterface` return an error code `lorawan_status_t` that reflects success or failure of the operation.

Below is the list of error codes and their description.

| Error code    | Value | Description |
| --------------- | ------------- | ----------|
| `LORAWAN_STATUS_OK`| 0 | Service done successfully |
| `LORAWAN_STATUS_BUSY`| -1000|  Stack busy |
|`LORAWAN_STATUS_WOULD_BLOCK`| -1001 | Stack cannot send at the moment or have nothing to read |
| `LORAWAN_STATUS_SERVICE_UNKNOWN`| -1002 | Unknown service request |
| `LORAWAN_STATUS_PARAMETER_INVALID`| -1003 | Invalid parameter  |
| `LORAWAN_STATUS_FREQUENCY_INVALID`| -1004| Invalid frequency  |
| `LORAWAN_STATUS_DATARATE_INVALID` | -1005| Invalid frequency and datarate  |
| `LORAWAN_STATUS_FREQ_AND_DR_INVALID`| -1006| When stack was unable to send packet in TX window  |
|`LORAWAN_STATUS_NO_NETWORK_JOINED`| -1009 | Device is not part of a network yet (Applicable only for OTAA) |
|`LORAWAN_STATUS_LENGTH_ERROR`| -1010 | Payload length error |
| `LORAWAN_STATUS_DEVICE_OFF`| -1011 | The device is off, in other words, disconnected state |
| `LORAWAN_STATUS_NOT_INITIALIZED`| -1012| Stack not initialized  |
| `LORAWAN_STATUS_UNSUPPORTED`| -1013| Unsupported service |
| `LORAWAN_STATUS_CRYPTO_FAIL`| -1014| Crypto failure  |
|`LORAWAN_STATUS_PORT_INVALID`| -1015 | Invalid port |
|`LORAWAN_STATUS_CONNECT_IN_PROGRESS`| -1016 | Connection in progress (application should wait for CONNECT event) |
|`LORAWAN_STATUS_NO_ACTIVE_SESSIONS`| -1017 | No active session in progress |
|`LORAWAN_STATUS_IDLE`| -1018 | Stack idle at the moment |
|`LORAWAN_STATUS_DUTYCYCLE_RESTRICTED`| -1020 | Transmission will be delayed because of duty cycling |
|`LORAWAN_STATUS_NO_CHANNEL_FOUND`| -1021 | No channel is enabled at the moment |
|`LORAWAN_STATUS_NO_FREE_CHANNEL_FOUND`| -1022 | All channels marked used, cannot find a free channel at the moment |
|`LORAWAN_STATUS_METADATA_NOT_AVAILABLE`| -1023 | Metadata is stale, cannot be made available as its not relevant |

You can find the API documentation for the LoRaWANInterface and LoRaRadio classes below:

- [LoRaWANInterface API docs](lorawan.html): The class that provides APIs for LoRaWAN network stack.
- [LoRaRadio API docs](loraradio-api.html): The class that provides pure virtual APIs to implement a LoRa radio driver.
