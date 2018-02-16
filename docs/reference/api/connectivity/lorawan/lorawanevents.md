<h2 id="lorawan-events">Mbed LoRaWAN Stack events & callbacks</h2>

Owing to the fact that most of the LoRaWAN devices will be very simple telemetry drvices we need the stack and it's operation
to be as simple as possible. That's why Mbed LoRaWAN stack is event driven.

### Network events
Here is the list of possible events that can be posted from the stack to the apllication:

| Event    | Description 
| --------------- | ------------- | 
| `CONNECTED`| When the connection is complete |
| `DISCONNECTED`|When the protocol is shut down in response to disconnect() |
|`TX_DONE` | When a packet is transmitted |
| `TX_TIMEOUT` | When stack was unable to send packet in TX window  |
| `TX_ERROR` | A general TX error  |
| `TX_CRYPTO_ERROR` | f MIC fails, or any other crypto relted error  |
| `TX_SCHEDULING_ERROR` | hen stack is unable to schedule packet  |
| `TX_TIMEOUT` | When stack was unable to send packet in TX window  |
|`RX_DONE` | When a packet is received |
|`RX_ERROR` | A general RX error |

An event handler must be attached to the stack by the application. The `LoRaWANInterface` provides an API to attach various callbacks to the stacks. One of such callbacks is the event handler callback. 

### Application callbacks

Mbed LoRaWAN stack currently maps 3 different callbacks:

| Callback type    | Description 
| --------------- | ------------- | 
| `Event callback`| Mandatory, Direction: from stack to application |
| `Link check response callback`|Optional, Direction: from stack to application|
|`Battery level callabck` | Optional, Direction: from application to stack |

#### Event handler

An example of attaching your event handler to the stack can be:

```CPP

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

This callback is added when it is desired to send a link check request MAC command. 

```CPP
void your_link_check_response(uint8_t demod_margin, uint8_t num_gw) 
{
	//demod_margin is the demodulation margin 
	// num_gw represents the number of gateways involved in the path
}

callbacks.link_check_resp = mbed::callback(your_link_check_response);
lorawan.add_app_callbacks(&callbacks);

```

#### Battery level handler

Battery level callback is different from others. The direction of this callback is from application to stack, i.e., it provides information to the stack.  Application is reponsible for letting the stack know about the current battery level.

```CPP
uint8_t your_battery_level() 
{
	return battery_level;
}

callbacks.link_check_resp = mbed::callback(your_lbattery_level);
lorawan.add_app_callbacks(&callbacks);
``` 