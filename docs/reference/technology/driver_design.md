## Driver Design

### Background and requirements

Terms used in this document
- Service: driver or library which provides functionality to a user application
- Event: A callback in interrupt or thread context to indicate that something occurred
- Synchronous API: API which does not generate any events
- Asynchronous API: API which can generate events

Rules for mbed-os drivers
- All drivers must work both with (mbed 5) and without (mbed 2) an RTOS
- Drivers must maximize portability and run on even constrained devices

Application design patterns / use cases
- Single thread running entire system on an event queue or super loop. None of the system services can block indefinitely
- Limited number of threads which run services in different priority groups.
- Thread per service

### HAL API design

HAL APIs can be broken into two main categories - Synchronous and Asynchronous. Asynchronous APIs typically provide the attach function to send events, while Synchronous APIs do not send events.

Requirements:
- No RTOS primitives can be used
 - This implies that the HAL cannot suspend execution during a call


Assertions:
1. Some peripherals require an Async API for reasonable use
2. On hardware without DMA some peripherals require a Synchronous API for reasonable use
3. The right Async API allows for efficient DMA transparently in the HAL


#### 1. Some peripherals require an Async API for reasonable use

Peripherals which can block indefinitely waiting on a condition can't be reasonably used at the HAL layer with a blocking API with or without an RTOS. This is because the condition needs to be polled by the CPU which causes impractically high power consumption. Because of this the HAL API for these peripherals must be an Asynchronous API and cannot be Synchronous.

[Show example of Serial here]

#### 2. On hardware without DMA some peripherals require a Synchronous API for reasonable use

Some peripherals expect high data transfer rates which require the CPU to quickly send data to the peripheral. When the time between successive data requests from the peripheral is far shorter then the time it takes for the CPU to service a data interrupt the peripheral performance is degraded by having an Async API. A Synchronous API allows the data to be sent in a tight loop, without the added overhead of servicing an interrupt. In some cases the performance difference is so great that it is not feasible to use an Async API. Because of this the HAL API for these peripherals must be Synchronous and cannot be Asynchronous.

[Add case study of SPI Sync vs Async here]

#### 3. The right Async API allows for efficient DMA transparently in the HAL

Peripherals which support DMA can use DMA to perform transfers that would otherwise require heavy CPU intervention as in 2. This allows an Async API to work efficient where it otherwise couldn't, as the CPU is only used when the entire transfer is complete.

### Driver API design

Requirements
- Drivers which can be backed by a Synchonous HAL should have only a Synchronous API
- Drivers backed by an Asynchronous HAL must have both a Synchronous and Asynchronous API
 - The Synchronous Driver API must expose all events through blocking calls

### Driver + HAL API design considerations

Design questions:
- Are the user facing operations abortable or have a timeout?
 - If yes then async + isr state machine desing is simpler
- Does any single call to the HAL take more than 20us?
 - If yes then sync + thread
- Are all events user initiated
 - If yes then sync + thread or isr

### HAL Synconization types

| Module            | Sync Type  |
|:-----------------:|:-----------|
| AnalogIn          | Sync*      |
| AnalogOut         | Sync*      |
| BusIn             | Sync       |
| BusInOut          | Sync       |
| BusOut            | Sync       |
| CAN               | Async      |
| DigitalIn         | Sync       |
| DigitalInOut      | Sync       |
| DigitalOut        | Sync       |
| FlashIAP          | Sync       |
| I2C               | Sync*      |
| I2CSlave          | Async      |
| InterruptIn       | Async      |
| LowPowerTicker    | Async      |
| LowPowerTimeout   | Async      |
| LowPowerTimer     | Sync       |
| MbedCRC           | Sync       |
| PortIn            | Sync       |
| PortInOut         | Sync       |
| PortOut           | Sync       |
| PwmOut            | Sync       |
| RawSerial         | Async      |
| Serial            | Async      |
| SerialBase        | Async      |
| SPI               | Sync       |
| SPISlave          | Async      |
| TableCRC          | Sync       |
| Ticker            | Async      |
| Timeout           | Async      |
| Timer             | Sync       |
| TimerEvent        | Async      |
| UARTSerial        | Async      |
 ```*May require further investigation```

### Common driver design patterns

Design patterns for increasing complexity
- No Synchronization
- Wrap in mutex
- ISR state machine

|                   | No Events         | Events            |
|:-----------------:|:-----------------:|:-----------------:|
| One thread        |No Synchronization |ISR state machine  |
| Many Threads      |Wrap in mutex      |ISR state machine  |

#### No Synchronization

The intended use case of this service is by a single thread so no special protection or design considerations are needed.


#### Wrap in mutex

This service could be used by multiple threads but does not block or generate any events. A mutex or critical section is required to serialize access.

#### ISR State machine

This service generate one or more events internally and can have one or more threads accessing it at the same time. Wrapping this service in a mutex is insufficient, as this prevents multiple threads from blocking on different events at the same time. Using a condition variable partially alleviates this, but the design does not scale well when more events can occur.

[add psuedo code example here]
