# Arm Mbed tutorials

The Arm Mbed ecosystem is expansive and offers many opportunities. In contrast to other sections of the documentation, which provide background reference material, this section provides instructions for specific tasks you may wish to perform. This section contains two formats of documentation: tutorials and examples. Tutorials include step-by-step guidance, and examples are code snippets you can use as a starting point for your application or as a reference on how to use a particular API.

## Getting started

<td><a href="../quick-start/index.html">Mbed OS quick start tutorial</a></td>

## Using the APIs

These tutorials and examples show you how to perform specific tasks that use the Arm Mbed APIs:

### Using platform APIs

| API | Examples |
| --- | --- |
| Wait | [Wait example](../apis/wait.html#example) |
| callback | [Serial passthrough example](../apis/callback.html#serial-passthrough-example-with-callbacks)<br> [Thread example](../apis/callback.html#thread-example-with-callbacks)<br> [Sonar example](../apis/callback.html#sonar-example) |
| DeepSleepLock | [DeepSleepLock example](../apis/deepsleeplock.html#example) |
| PowerManagement | [PowerManagement example](../apis/power-management-sleep.html#example) |
| IdleLoop | [IdleLoop example](../apis/idle-loop.html#example) |
| CriticalSectionLock | [CriticalSectionLock example](../apis/criticalsectionlock.html#criticalsectionlock-example) |
| Time | [Time example](../apis/time.html#time-example) |
| RTC | [RTC example](../apis/rtc.html#rtc-time-example) |
| Debug | [Debug example](../apis/debug.html#debug-example) |
| Memory tracing | [Memory tracing example](../apis/memory-tracing.html#memory-tracing-example) |
| Error handling | [Error handling example](../apis/error-handling.html#error-handling-example)<br> [Crash reporting example](../apis/error-handling.html#crash-reporting-example) |
| Assert | [Assert example](../apis/assert.html#assert-example) |
| NonCopyable | [NonCopyable example](../apis/noncopyable.html#noncopyable-example) |
| SharedPtr | [Shared pointer example](../apis/shared-pointer.html#shared-pointer-example) |
| Span | [Span example](../apis/span.html#span-example) |
| FileHandle | [C library example](../apis/filehandle.html#filehandle-using-c-library-example)<br> [Sigio example](../apis/filehandle.html#filehandle-sigio-example) |
| Poll | [Poll example](../apis/poll.html#poll-example) |
| PlatformMutex | [PlatformMutex example](../apis/platformmutex.html#platformmutex-example) |
| CircularBuffer | [CircularBuffer example](../apis/circularbuffer.html#circularbuffer-example) |
| ATCmdParser | [ATCmdParser example](../apis/atcmdparser.html#atcmdparser-examples) |
| Mbed statistics | [CPU usage example](../apis/mbed-statistics.html#cpu-usage-example)<br> [Memory statistics example](../apis/mbed-statistics.html#memory-statistics-example) <br> [Thread statistics example](../apis/mbed-statistics.html#thread-statistics-example) <br> [System information example](../apis/mbed-statistics.html#system-information-example) <br> [CPU statistics example](../apis/mbed-statistics.html#cpu-statistics-example)|
| MPU management | [MPU management example](../apis/mpu-management.html#example) |
| ScopedRamExecutionLock | [ScopedRamExecutionLock](../apis/scopedramexecutionlock.html#example) |
| ScopedRomWriteLock | [ScopedRomWriteLock example](../apis/scopedromwritelock.html#scopedromwritelock-class-reference) |

### Using drivers APIs

| API | Examples  | Hello, World |
| --- | ---  | --- |
| AnalogIn | [AnalogIn example](../apis/analogin.html#analogin-examples) | [AnalogIn Hello, World](../apis/analogin.html#analogin-hello-world)|
| AnalogOut | [AnalogOut example](../apis/analogout.html#analogout-example) | [AnalogIn Hello, World](../apis/analogout.html#analogout-hello-world) |
| DigitalIn | [DigitalIn exanple](../apis/digitalin.html#digitalin-example) | [DigitlaIn Hellw, World](../apis/digitalin.html#digitalin-hello-world) |
| DigitalOut | | [DigitalOut Hello, World](../apis/digitalout.html#digitalout-hello-world) |
| DigitalInOut | | [DigitalInOut Hello, World](../apis/digitalinout.html#digitalinout-hello-world) |
| BusIn | | [BusIn Hello, World](../apis/busin.html#busin-hello-world) |
| BusOut | | [BusOut Hello, World](../apis/busout.html#busout-hello-world) |
| BusInOut | | [BusInOut Hello, World](../apis/businout.html#businout-hello-world) |
| PortIn | | [PortIn Hello, World](../apis/portin.html#portin-hello-world) |
| PortOut | | [PortOut Hello, World](../apis/portout.html#portout-hello-world) |
| PortInOut | | [PortInOut Hello, World](../apis/portinout.html#portinout-hello-world) |
| PwmOut | [PwmOut example](../apis/pwmout.html#pwmout-code-examples) | [PwmOut Hello, World](../apis/pwmout.html#pwmout-hello-world) |
| InterruptIn | [InterruptIn example](../apis/interruptin.html#interruptin-example) | [InterruptIn Hello, World](../apis/interruptin.html#interruptin-hello-world) |
| Ticker | [Ticker example](../apis/ticker.html#ticker-examples) | [Ticker Hello, World](../apis/ticker.html#ticker-hello-world) |
| Timeout | [Timeout example](../apis/timeout.html#timeout-example) | [Timeout Hello, World](../apis/timeout.html#timeout-hello-world) |
| Timer | | [Timer Hello, World](../apis/timer.html#timer-hello-world) |
| LowPowerTicker | [LowPowerTicker example](../apis/lowpowerticker.html#lowpowerticker-example) | |
| LowPowerTimeout | [LowPowerTimeout example](../apis/lowpowertimeout.html#lowpowertimeout-example) | |
| LowPowerTimer | [LowPowerTimer example](../apis/lowpowertimer.html#lowpowertimer-example) | |
| Flash IAP | [Flash IAP example](../apis/flash-iap.html#flash-iap-example) | |
| RawSerial | [RawSerial example](../apis/rawserial.html#rawserial-examples) | [RawSerial Hello, World](../apis/rawserial.html#rawserial-hello-world) |
| Serial | [Serial example](../apis/serial.html#serial-examples) | [Serial Hello, World](../apis/serial.html#serial-hello-world) |
| SPI | | [SPI Hello, World](../apis/spi.html#spi-hello-world) |
| SPISlave | [SPISlave example](/apis/spislave.html#spislave-example) | |
| QuadSPI (QSPI) | [QuadSPI example](../apis/quadspi-qspi.html#quadspi-example) | |
| I2C | | [I2C Hello, World](../apis/i2c.html#i2c-hello-world) |
| I2CSlave | [I2CSlave example](../apis/i2cslave.html#i2cslave-example) | [I2C Hello, World](../apis/i2c.html#i2c-hello-world) |
| CAN | | [CAN Hello, World](../apis/can.html#can-hello-world) |
| MbedCRC | [MbedCRC example](../apis/mbedcrc.html#mbedcrc-examples) |

And the following tutorials:

- [Application flow control](../tutorials/application-flow-control.html)
- [Alarm](../tutorials/alarm-tutorial.html)

### Using RTOS APIs

| API | Examples | Tutorials |
| --- | --- | --- |
| EventQueue | [Chaining events from more than one queue](../apis/eventqueue.html#eventqueue-example-chaining-events-from-more-than-one-queue)<br> [Deferring from interrupt context](../apis/eventqueue.html#eventqueue-example-deferring-from-interrupt-contextl) <br> [Posting events to the queue](../apis/eventqueue.html#eventqueue-example-posting-events-to-the-queue) <br> [Shared event: deferring from interrupt context](../apis/eventqueue.html#shared-event-example-running-the-shared-queue-from-main)<br>  [Shared event: running the shared queue from main](../apis/eventqueue.html#shared-event-example-running-the-shared-queue-from-main)<br> [Static event queue example](../apis/eventqueue.html#static-eventqueue-example-posting-user-allocated-events-to-the-static-queue) | [EventQueue tutorial](the-eventqueue-api.html)|
| UserAllocatedEvent | [Static event queue example](../apis/userallocatedevent.html#static-eventqueue-example-posting-user-allocated-events-to-the-queue) | |
| Mutex | [Mutex example](../apis/mutex.html#mutex-example) | |
| MemoryPool | [MemoryPool example](../apis/memorypool.html#memorypool-example) | |
| Kernel | [Example: get_ms_count()](../apis/kernel-interface-functions.html#get-ms-count-example)<br> [Example: hooks](../apis/kernel-interface-functions.html#kernel-hooks-example) | |
| Thread | [Thread example](../apis/thread.html#thread-example)<br> [Thread example with callbacks](../apis/thread.html#thread-example-with-callbacks)<br> | |
| ThisThread | [ThisThread example](../apis/thisthread.html#thisthread-example) | |
| Semaphore  | [Semaphore example](../apis/semaphore.html#semaphore-example) | |
| Mail | [Mail example](../apis/mail.html#mail-example) | |
| EventFlags | [EventFlags example](../apis/eventflags.html#eventflags-example) | |
| ConditionVariable | [ConditionVariable example](../apis/conditionvariable.html#conditionvariable-example) | |
| Queue | [Queue example](../apis/queue.html#queue-example) <br> [Queue and MemoryPool](../apis/queue.html#queue-and-memorypool-example)| |

### Using USB APIs

| API | Examples | Tutorials |
| --- | --- | --- |
| USBSerial | [USBSerial example](../apis/usbserial.html#usbserial-example) | |
| USBAudio | [Sound data example](../apis/usbaudio.html#usbaudio-play-sound-data-example) <br> [Square wave example](../apis/usbaudio.html#usbaudio-square-wave-exampl) <br> [Loopback example](../apis/usbaudio.html#usbaudio-loopback-example) | [Audio player tutorial](../tutorials/mbed-usb-wav-audio-player.html) |
| USBHID | [USBHID example](../apis/usbhid.html#usbhid-example) | |
| USBCDC | [USBCDC example](../apis/usbcdc.html#usbcdc-example) | |
| USBMSD | [USBMSD example](../apis/usbmsd.html#usbmsd-example) | |
| USBMIDI | [USBMIDI example](../apis/usbmidi.html#usbmidi-example) <br> ["Take Me Out to the Ball Game" example](../apis/usbmidi.html#play-take-me-out-to-the-ball-game-example) | |
| USBMouse | [USBMouse example](../apis/usbmouse.html#usbmouse-example) <br> [Joystick example](../apis/usbmouse.html#usbmouse-joystick-example) | |
| USBKeyboard | [USBKeyboard example](../apis/usbkeyboard.html#usbkeyboard-example) | |
| USBMouseKeyboard | [USBMouseKeyboard](../apis/usbmousekeyboard.html#usbmousekeyboard-example) | |

### Using network socket APIs

| API | Examples | Tutorials |
| --- | --- | --- |
| Socket | [Socket example](../apis/socket.html#socket-example) | |
| UDPSocket | [UDPSocket example](../apis/udpsocket.html#udpsocket-example) | |
| TCPSocket | [TCPSocket example](../apis/tcpsocket.html#tcpsocket-example) | |
| SocketAddress | [SocketAddress example](../apis/socketaddress.html#socketaddress-example) | |
| Non-IP cellular socket | [Non-IP cellular socket example](../apis/non-ip-cellular-socket.html#cellularnonipsocket-example) | |
| DNS Resolver | [DNS Resolver example](../apis/dns-resolver.html#dns-resolver-example) | |
| TLSSocket | [TLSSocket example](../apis/tlssocket.html#tlssocket-example) | [Secure communication tutorial](../tutorials/tls-tutorial.html) |
| DTLSSocket | [DTLSSocket example](../apis/dtlssocket.html#dtlssocket-example) | |
| SocketStats | [SocketStats example](../apis/socketstats.html#socketstats-example) | |

### Using network interfaces APIs

| API | Examples | Tutorials |
| --- | --- | --- |
| EthInterface | [EthInterface example](../apis/ethernet.html#ethinterface-example) | |
| Wi-Fi | [Wi-Fi example](../apis/wi-fi.html#wi-fi-example) | |
| Cellular | [Cellular example](../apis/cellular-api.html#cellular-example-connection-establishment) | |
| Mesh | | [Mesh tutorial](../tutorials/mesh-tutorial.html) <br>  [Light control tutorial](../tutorials/light-control.html) |
| Network status | [Network status example](../apis/network-status.html#example) | |


### Using bluetooth APIs

| API | Examples | Tutorials |
| --- | --- | --- |
| BLE | [Beacon example](../apis/ble.html#example-ble-beacon) <br> [Heart rate example](../apis/ble.html#example-ble-heart-rate-monitor)| [BLE tutorial](../tutorials/ble-tutorial.html) <br> [BLE service templates](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-Button/) |
| GAP | [GAP example](../apis/gap.html#gap-example) <br> [Button count example](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-GAPButton)| |
| GattClient | [GattClient example](../apis/gattclient.html#gattclient-example) | [LED](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-LED/) and [LED blinker](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-LEDBlinker) <br> [Thermometer](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-ble-Thermometer)|
| GattServer | [GattServer example](../apis/gattserver.html#gattserver-example) | |
| SecurityManager | [SecurityManager example](../apis/securitymanager.html#securitymanager-example) | |
| BatteryService | [Battery level example](../apis/batteryservice.html#batteryservice-example) | |
| HeartRateService | [Heart rate service example](../apis/heartrateservice.html#heartrateservice-example) | |
| ibeacon | [ibeacon example](../apis/ibeacon.html#ibeacon-example) | |


### Using LoRa APIs

A [private network tutorial](../tutorials/LoRa-tutorial.html) and [an example for the API](../apis/lorawan-api.html#lorawan-example).

### Using NFC APIs

| API | Examples |
| --- | --- |
| NFCController | [NFCController example](../apis/nfccontroller.html#nfccontroller-example) |
| NFCEEPROM | [NFCEEPROM example](../apis/nfc-eeprom.html#nfceeprom-example) |
| MessageParser | [MessageParser example](../apis/messageparser.html#messageparser-example) |
| SimpleMessageParser | [SimpleMessageParser example](../apis/simplemessageparser.html#simplemessageparser-example) |
| MessageBuilder | [MessageBuilder example](../apis/messagebuilder.html#messagebuilder-example) |

### Using security APIs

| API | Examples |
| --- | --- |
| TLS | [Benchmark example](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-tls-benchmark) <br> [Hashing example](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-tls-hashing) <br> [Client example](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-tls-tls-client) <br> [Authenticated encryption example](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-tls-authcrypt) |
| DeviceKey | [DeviceKey example](../apis/devicekey.html#devicekey-example) |


### Using storage APIs

| API | Examples |
| --- | --- |
| KVStore | [KVStore example](../apis/kvstore.html#kvstore-example) |
| FileSystem | [FileSystem example](../apis/filesystem.html#file-system-example) |
| BlockDevice | [BlockDevice example](../apis/blockdevice.html#blockdevice-example) |
| HeapBlockDevice | [HeapBlockDevice example](../apis/heapblockdevice.html#heapblockdevice-example) |
| MBRBlockDevice | [MBRBlockDevice example](../apis/mbrblockdevice.html#mbrblockdevice-example) |
| ChainingBlockDevice | [ChainingBlockDevice example](../apis/chainingblockdevice.html#chainingblockdevice-example) |
| SlicingBlockDevice | [SlicingBlockDevice](../apis/slicingblockdevice.html#slicingblockdevice-example) |
| ProfilingBlockDevice | [ProfilingBlockDevice example](../apis/profilingblockdevice.html#profilingblockdevice-example) |
| BufferedBlockDevice | [BufferedBlockDevice example](../apis/bufferedblockdevice.html#bufferedblockdevice-example) |
| FlashSimBlockDevice | [FlashSimBlockDevice example](../apis/flashsimblockdevice.html#flashsimblockdevice-example) |
| DataFlashBlockDevice | [DataFlashBlockDevice example](../apis/dataflashblockdevice.html#dataflashblockdevice-example) |
| FlashIAPBlockDevice | [FlashIAPBlockDevice example](../apis/flashiapblockdevice.html#flashiapblockdevice-example) |
| SDBlockDevice | [SDBlockDevice example](../apis/sdblockdevice.html#sdblockdevice-example-application) |
| SPIFBlockDevice | [SPIFBlockDevice example](../apis/spi-flash-block-device.html#spifblockdevice-example) |
| QSPIFBlockDevice | [QSPIFBlockDevice example](../apis/qspifblockdevice.html#qspifblockdevice-example) |
| NVStore | [NVStore](../apis/nvstore.html#nvstore-example) |

## Serial communication

These tutorials teach you to communicate with your development board, an essential part of programming and debugging:

- [Windows serial driver tutorial](../tutorials/windows-serial-driver.html)
- [Board to PC communication over USB tutorial](../tutorials/serial-comm.html)
- [Low memory serial printf example](../tutorials/serial-comm.html#minimal-printf)

## Debugging

These tutorials show you how to install, export a project to and start a debugging session with different IDEs.

### Tools

- [Eclipse](../tutorials/eclipse.html).
- [Keil uVision](../tutorials/keil-uvision.html).
- [Visual Studio](../tutorials/visual-studio-code.html).
- [BBC micro:bit, pyOCD and GDB debugging tutorial](../tutorials/debug-microbit.html).

### Methods

- [Troubleshooting common issues](../tutorials/debugging.html).
- [Analyzing Mbed OS crash dump tutorial](../tutorials/analyzing-mbed-os-crash-dump.html).
- [Compile time errors tutorial](../tutorials/compile-time-errors.html).
- [Debugging using `printf` statements](../tutorials/debugging-using-printf-statements.html).
- [Error handling API example](../apis/error-handling.html#error-handling-example)

## Bootloader

A [tutorial for creating and using a bootloader](../tutorials/bootloader.html), and [an example bootloader](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-bootloader).

## Optimizing

<table>
<tbody>
<tr>
<td><a href="optimizing.html">Memory optimizations tutorial</a></td>
<td><a href="../apis/mbed-statistics.html#thread-statistics-example">Thread statistics example</a></td>
<td><a href="../apis/mbed-statistics.html#cpu-usage-example">CPU usage example</a></td>
<td><a href="power-optimization.html">Power optimization tutorial</a></td>
</tr>
<tr>
<td><a href="../apis/mbed-statistics.html#system-information-example">System information example</a></td>
<td><a href="../apis/mbed-statistics.html#cpu-statistics-example">CPU statistics example</a></td>
<td><a href="../reference/bare-metal-example-application.html">Blinky bare metal example</a></td>
</tr>
</tbody>
</table>

## Migrating to Mbed OS 5

[Mbed OS 2 to 5 migration tutorial](../tutorials/migrating-to-mbed-os-5.html)
