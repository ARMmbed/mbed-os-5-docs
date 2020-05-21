# Arm Mbed tutorials

The Arm Mbed ecosystem is expansive and offers many opportunities. In contrast to other sections of the documentation, which provide background reference material, this section provides instructions for specific tasks you may wish to perform. This section contains two formats of documentation: tutorials and examples. Tutorials include step-by-step guidance, and examples are code snippets you can use as a starting point for your application or as a reference on how to use a particular API.

## Getting started

Our [quick start](../quick-start/index.html) guides show how to build an example application for both the full profile and bare metal profile, on Mbed CLI, Mbed Studio and the Mbed Online Compiler.

| [Build with Mbed Studio](https://os.mbed.com/docs/mbed-studio/current/getting-started/index.html) | [Build with Mbed Online Compiler](../quick-start/build-and-debug-with-the-online-compiler.html) |  [Build with Mbed CLI](../quick-start/build-and-debug-with-mbed-cli.html) |
| --- | --- | --- |
| Download our dedicated desktop IDE, including all the necessary tools to work with Mbed OS. <br>This link will take you to the Mbed Studio documentation site. | Zero-installation web IDE to explore Mbed OS; great for rapid prototyping and education. | Command-line tool requiring manual setup of tools, but providing the greatest degree of flexibility. |

## RTOS APIs

| API | Snippets |
| --- | --- |
| ConditionVariable | [ConditionVariable snippet](../apis/rtos-apis.html#conditionvariable-example) |
| EventFlags | [EventFlags snippet](../apis/eventflags.html#eventflags-example) |
| IdleLoop | [IdleLoop snippet](../apis/idle-loop.html#example) |
| Kernel | - [get_ms_count()](../apis/kernel-interface-functions.html#get-ms-count-example)<br> - [Hooks](../apis/kernel-interface-functions.html#kernel-hooks-example) |
| Mail | [Mail snippet](../apis/mail.html#mail-example) |
| Mutex | [Mutex snippet](../apis/mutex.html#mutex-example) |
| Queue | [Queue snippet](../apis/queue.html#queue-example) <br> [Queue and MemoryPool](../apis/queue.html#queue-and-memorypool-example)|
| Semaphore  | [Semaphore snippet](../apis/semaphore.html#semaphore-example) |
| ThisThread | [ThisThread snippet](../apis/thisthread.html#thisthread-example) |
| Thread | - [Thread snippet](../apis/thread.html#thread-example)<br> - [Thread example with callbacks](../apis/thread.html#thread-example-with-callbacks)<br> |

## Event handling APIs

| API | Snippets | Tutorials |
| --- | --- | --- |
| Event | [Posting events to the queue](../apis/event-handling-apis.html) |  |
| EventQueue | - [Chaining events from more than one queue](../apis/eventqueue.html#eventqueue-example-chaining-events-from-more-than-one-queue)<br> - [Deferring from interrupt context](../apis/eventqueue.html#eventqueue-example-deferring-from-interrupt-contextl) <br> - [Posting events to the queue](../apis/eventqueue.html#eventqueue-example-posting-events-to-the-queue) <br> - [Shared event: deferring from interrupt context](../apis/eventqueue.html#shared-event-example-running-the-shared-queue-from-main)<br> - [Shared event: running the shared queue from main](../apis/eventqueue.html#shared-event-example-running-the-shared-queue-from-main)<br> - [Static event queue snippet](../apis/eventqueue.html#static-eventqueue-example-posting-user-allocated-events-to-the-static-queue) | [EventQueue tutorial](../apis/scheduling-tutorials.html)|
| UserAllocatedEvent | [Static event queue snippet](../apis/userallocatedevent.html#static-eventqueue-example-posting-user-allocated-events-to-the-queue) | |

## Serial (UART) Driver APIs

| API | Snippets  | Hello, World |
| --- | ---  | --- |
| BufferedSerial | [BufferedSerial snippet](../apis/serial-uart-apis.html#bufferedserial-examples) | |
| UnbufferedSerial | [UnbufferedSerial snippet](../apis/unbufferedserial.html#unbufferedserial-example) | |

## SPI APIs

| API | Snippets | Hello, World |
| --- | --- | --- |
| QuadSPI (QSPI) | [QuadSPI snippet](../apis/spi-apis.html#quadspi-example) | |
| SPI | | [SPI Hello, World](../apis/spi.html#spi-hello-world) |
| SPISlave | [SPISlave snippet](/apis/spislave.html#spislave-example) | |


## Input/Output (I/O) Driver APIs

| API | Snippets  | Hello, World |
| --- | ---  | --- |
| AnalogIn | [AnalogIn snippet](../apis/i-o-apis.html#analogin-examples) | [AnalogIn Hello, World](../apis/i-o-apis.html#analogin-hello-world)|
| AnalogOut | [AnalogOut snippet](../apis/analogout.html#analogout-example) | [AnalogIn Hello, World](../apis/analogout.html#analogout-hello-world) |
| BusIn | | [BusIn Hello, World](../apis/busin.html#busin-hello-world) |
| BusOut | | [BusOut Hello, World](../apis/busout.html#busout-hello-world) |
| BusInOut | | [BusInOut Hello, World](../apis/businout.html#businout-hello-world) |
| DigitalIn | [DigitalIn exanple](../apis/digitalin.html#digitalin-example) | [DigitlaIn Hellw, World](../apis/digitalin.html#digitalin-hello-world) |
| DigitalOut | | [DigitalOut Hello, World](../apis/digitalout.html#digitalout-hello-world) |
| DigitalInOut | | [DigitalInOut Hello, World](../apis/digitalinout.html#digitalinout-hello-world) |
| InterruptIn | [InterruptIn snippet](../apis/interruptin.html#interruptin-example) | [InterruptIn Hello, World](../apis/interruptin.html#interruptin-hello-world) |
| PortIn | | [PortIn Hello, World](../apis/portin.html#portin-hello-world) |
| PortOut | | [PortOut Hello, World](../apis/portout.html#portout-hello-world) |
| PortInOut | | [PortInOut Hello, World](../apis/portinout.html#portinout-hello-world) |
| PwmOut | [PwmOut snippet](../apis/pwmout.html#pwmout-code-examples) | [PwmOut Hello, World](../apis/pwmout.html#pwmout-hello-world) |

## USB Driver APIs

| API | Snippets | Tutorials |
| --- | --- | --- |
| USBAudio | - [Sound data snippet](../apis/usb-apis.html#usbaudio-play-sound-data-example) <br> - [Square wave snippet](../apis/usb-apis.html#usbaudio-square-wave-exampl) <br> - [Loopback snippet](../apis/usb-apis.html#usbaudio-loopback-example) | [Audio player tutorial](../apis/usb-wav-audio-player.html) |
| USBCDC | [USBCDC snippet](../apis/usbcdc.html#usbcdc-example) | |
| USBCDC_ECM | [USBCDC_ECM snippet](../apis/usbcdc-ecm.html) | |
| USBHID | [USBHID snippet](../apis/usbhid.html#usbhid-example) | |
| USBKeyboard | [USBKeyboard snippet](../apis/usbkeyboard.html#usbkeyboard-example) | |
| USBMIDI | - [USBMIDI snippet](../apis/usbmidi.html#usbmidi-example) <br> - ["Take Me Out to the Ball Game" snippet](../apis/usbmidi.html#play-take-me-out-to-the-ball-game-example) | |
| USBMouse | - [USBMouse snippet](../apis/usbmouse.html#usbmouse-example) <br> - [Joystick snippet](../apis/usbmouse.html#usbmouse-joystick-example) | |
| USBMouseKeyboard | [USBMouseKeyboard](../apis/usbmousekeyboard.html#usbmousekeyboard-example) | |
| USBMSD | [USBMSD snippet](../apis/usbmsd.html#usbmsd-example) | |
| USBSerial | [USBSerial snippet](../apis/usbserial.html#usbserial-example) | |

## Other Driver APIs

| API | Snippets | Tutorials |
| --- | --- | --- |
| CAN | | [CAN Hello, World](../apis/other-driver-apis.html#can-hello-world) |
| Flash IAP | [Flash IAP snippet](../apis/flash-iap.html#flash-iap-example) | |
| I2C | | [I2C Hello, World](../apis/i2c.html#i2c-hello-world) |
| I2CSlave | [I2CSlave snippet](../apis/i2cslave.html#i2cslave-example) | [I2C Hello, World](../apis/i2c.html#i2c-hello-world) |
| MbedCRC | [MbedCRC snippet](../apis/mbedcrc.html#mbedcrc-examples) | |
| ResetReason | [ResetReason snippet](../apis/resetreason.html) | |
| Watchdog | [Watchdog snippet](../apis/watchdog.html) | |

And the following tutorial:

- [Alarm](../apis/drivers-tutorials.html)

## Time Platform APIs

| API | Snippets |
| --- | --- |
| RTC | [RTC snippet](../apis/time-apis.html#rtc-time-example) |
| Ticker | [Ticker snippet](../apis/ticker.html#ticker-examples) | [Ticker Hello, World](../apis/ticker.html#ticker-hello-world) |
| Time | [Time snippet](../apis/time.html#time-example) |
| Timeout | [Timeout snippet](../apis/timeout.html#timeout-example) | [Timeout Hello, World](../apis/timeout.html#timeout-hello-world) |
| Timer | | [Timer Hello, World](../apis/timer.html#timer-hello-world) |

And the following tutorial:

- [Application flow control](../apis/platform-tutorials.html)

## Power Platform APIs

| API | Snippets |
| --- | --- |
| DeepSleepLock | [DeepSleepLock snippet](../apis/power-apis.html#example) |
| LowPowerTicker | [LowPowerTicker snippet](../apis/lowpowerticker.html#lowpowerticker-example) | |
| LowPowerTimeout | [LowPowerTimeout snippet](../apis/lowpowertimeout.html#lowpowertimeout-example) | |
| LowPowerTimer | [LowPowerTimer snippet](../apis/lowpowertimer.html#lowpowertimer-example) | |
| PowerManagement | [PowerManagement snippet](../apis/power-management-sleep.html#example) |

## Memory Platform APIs

| API | Snippets | Tutorials | Official examples |
| --- | --- | --- | --- |
| Memory tracing (mbed_mem_trace) | [Memory tracing snippet](../apis/memory-apis.html#memory-tracing-example) | [Runtime memory tracing](../apis/runtime-memory-tracing.html) | |
| MPU management (mpug_mgmt) | [MPU management snippet](../apis/mpu-management.html#example) | | |
| MemoryPool | [MemoryPool snippet](../apis/memorypool.html#memorypool-example) | | |
| Mbed statistics  (mbed_stats)| - [Memory statistics snippet](../apis/mbed-statistics.html#memory-statistics-example) <br> - [Thread statistics snippet](../apis/mbed-statistics.html#thread-statistics-example) <br> - [System information snippet](../apis/mbed-statistics.html#system-information-example) <br> - [CPU statistics snippet](../apis/mbed-statistics.html#cpu-statistics-example)|  | - [CPU statistics official example](https://github.com/ARMmbed/mbed-os-example-cpu-stats) </br> - [CPU usage official example](https://github.com/ARMmbed/mbed-os-example-cpu-usage) </br> - [Thread statistics official example](https://github.com/ARMmbed/mbed-os-example-thread-statistics)|

And the following tutorial:

- [Power optimization](../apis/power-optimization.html)

## Other Platform APIs

| API | Snippets | Official examples |
| --- | --- | --- |
| Assert | [Assert snippet](../apis/other-platform-apis.html#assert-example) | |
| ATCmdParser | [ATCmdParser snippet](../apis/atcmdparser.html#atcmdparser-examples) | |
| Callback | [Serial passthrough snippet](../apis/callback.html#serial-passthrough-example-with-callbacks)<br> [Thread snippet](../apis/callback.html#thread-example-with-callbacks)<br> [Sonar snippet](../apis/callback.html#sonar-example) | |
| CircularBuffer | [CircularBuffer snippet](../apis/circularbuffer.html#circularbuffer-example) | |
| CriticalSectionLock | [CriticalSectionLock snippet](../apis/criticalsectionlock.html#criticalsectionlock-example) | |
| Debug | [Debug snippet](../apis/debug.html#debug-example) | |
| Error handling | [Error handling snippet](../apis/error-handling.html#error-handling-example)<br> [Crash reporting snippet](../apis/error-handling.html#crash-reporting-example) | [Error handling official example](https://github.com/ARMmbed/mbed-os-example-error-handling) |
| FileHandle | [C library snippet](../apis/filehandle.html#filehandle-using-c-library-example)<br> [Sigio snippet](../apis/filehandle.html#filehandle-sigio-example) | |
| NonCopyable | [NonCopyable snippet](../apis/noncopyable.html#noncopyable-example) | |
| PlatformMutex | [PlatformMutex snippet](../apis/platformmutex.html#platformmutex-example) | |
| Poll | [Poll snippet](../apis/poll.html#poll-example) |
| ScopedRamExecutionLock | [ScopedRamExecutionLock](../apis/scopedramexecutionlock.html#example) | |
| ScopedRomWriteLock | [ScopedRomWriteLock snippet](../apis/scopedromwritelock.html#scopedromwritelock-class-reference) |
| SharedPtr | [Shared pointer snippet](../apis/shared-pointer.html#shared-pointer-example) | |
| Span | [Span snippet](../apis/span.html#span-example) | |

## File system APIs

| API | Snippets | Official examples |
| --- | --- | --- |
| FileSystem | [FileSystem snippet](../apis/filesystem.html#file-system-example) | [FileSystem official example](https://github.com/ARMmbed/mbed-os-example-filesystem) |
| KVStore | [KVStore snippet](../apis/kvstore.html#kvstore-example) | [KVStore official example](https://github.com/ARMmbed/mbed-os-example-kvstore) |

## BlockDevice APIs

| API | Snippets | Official examples |
| --- | --- | --- |
| BlockDevice | [BlockDevice snippet](../apis/blockdevice-apis.html#blockdevice-example) | [BlockDevice official example](https://github.com/ARMmbed/mbed-os-example-blockdevice) |
| BufferedBlockDevice | [BufferedBlockDevice snippet](../apis/bufferedblockdevice.html#bufferedblockdevice-example) | |
| ChainingBlockDevice | [ChainingBlockDevice snippet](../apis/chainingblockdevice.html#chainingblockdevice-example) | |
| DataFlashBlockDevice | [DataFlashBlockDevice snippet](../apis/dataflashblockdevice.html#dataflashblockdevice-example) | |
| FlashIAPBlockDevice | [FlashIAPBlockDevice snippet](../apis/flashiapblockdevice.html#flashiapblockdevice-example) | |
| FlashSimBlockDevice | [FlashSimBlockDevice snippet](../apis/flashsimblockdevice.html#flashsimblockdevice-example) | |
| HeapBlockDevice | [HeapBlockDevice snippet](../apis/heapblockdevice.html#heapblockdevice-example) | |
| MBRBlockDevice | [MBRBlockDevice snippet](../apis/mbrblockdevice.html#mbrblockdevice-example) | |
| ProfilingBlockDevice | [ProfilingBlockDevice snippet](../apis/profilingblockdevice.html#profilingblockdevice-example) | |
| QSPIFBlockDevice | [QSPIFBlockDevice snippet](../apis/qspifblockdevice.html#qspifblockdevice-example) | |
| SDBlockDevice | [SDBlockDevice snippet](../apis/sdblockdevice.html#sdblockdevice-example-application) | [SD driver official example](https://github.com/ARMmbed/mbed-os-example-sd-driver) |
| SlicingBlockDevice | [SlicingBlockDevice](../apis/slicingblockdevice.html#slicingblockdevice-example) | |
| SPIFBlockDevice | [SPIFBlockDevice snippet](../apis/spi-flash-block-device.html#spifblockdevice-example) | |

## Network socket APIs

| API | Snippets | Tutorials | Official examples |
| --- | --- | --- | --- |
| Non-IP cellular socket | [Non-IP cellular socket snippet](../apis/network-socket-apis.html#cellularnonipsocket-example) | | |
| Socket | [Socket snippet](../apis/socket.html#socket-example) | |[Sockets official example](https://github.com/ARMmbed/mbed-os-example-sockets) |
| SocketAddress | [SocketAddress snippet](../apis/socketaddress.html#socketaddress-example) | | |
| SocketStats | [SocketStats snippet](../apis/socketstats.html#socketstats-example) | | [Socket statistics official example](https://github.com/ARMmbed/mbed-os-example-socket-stats) |
| TCPSocket | [TCPSocket snippet](../apis/tcpsocket.html#tcpsocket-example) | | |
| UDPSocket | [UDPSocket snippet](../apis/udpsocket.html#udpsocket-example) | | |

## Network interfaces APIs

| API | Snippets | Tutorials | Official examples |
| --- | --- | --- | --- |
| Cellular | [Cellular snippet](../apis/network-interface-apis.html#cellular-example-connection-establishment) | | [Cellular official example](https://github.com/ARMmbed/mbed-os-example-cellular) |
| EthInterface | [EthInterface snippet](../apis/ethernet.html#ethinterface-example) | | |
| LoRaWAN | | - [LoRaWAN usage](../apis/lorawan-usage.html)</br> - [Building a private loRa network](../apis/LoRa-tutorial.html) </br> - [Nanostack border router](https://github.com/ARMmbed/nanostack-border-router)| [LoRaWAN official example](https://github.com/ARMmbed/mbed-os-example-lorawan) (also available in the tutorials) |
| Mesh | | [Mesh tutorial](./apis/connectivity-tutorials.html) | [Mesh minimal official example](https://github.com/ARMmbed/mbed-os-example-mesh-minimal) (also available in the [light control tutorial](../apis/light-control.html)) |
| Network status | [Network status snippet](../apis/network-status.html#example) | | |
| Wi-Fi | [Wi-Fi snippet](../apis/wi-fi.html#wi-fi-example) | | [Wi-Fi official example](https://github.com/ARMmbed/mbed-os-example-wifi) |

## Secure socket APIs

| API | Snippets | Tutorials | Official examples |
| --- | --- | --- | --- |
| DTLSSocket | [DTLSSocket snippet](../apis/secure-socket-apis.html#dtlssocket-example) | | |
| TLSSocket | [TLSSocket snippet](../apis/tlssocket.html#tlssocket-example) | [Secure communication tutorial](../apis/tls-tutorial.html) | [TLS socket official example](https://github.com/ARMmbed/mbed-os-example-tls-socket) |

## DNS API

| API | Snippets | Tutorials |
| --- | --- | --- |
| DNS Resolver | [DNS Resolver snippet](../apis/dns-apis.html#dns-resolver-example) | |

## Bluetooth (BLE) APIs

We have placed all of our official BLE examples in a single [GitHub repository](https://github.com/ARMmbed/mbed-os-example-ble).

## NFC APIs

| API | Snippets |
| --- | --- |
| MessageBuilder | [MessageBuilder snippet](../apis/nfc-apis.html#messagebuilder-example) |
| MessageParser | [MessageParser snippet](../apis/messageparser.html#messageparser-example) || Mesh | | [Mesh tutorial](../apis/connectivity-tutorials.html) <br>  [Light control tutorial](../apis/light-control.html) |
| NFCController | [NFCController snippet](../apis/nfccontroller.html#nfccontroller-example) |
| NFCEEPROM | [NFCEEPROM snippet](../apis/nfc-eeprom.html#nfceeprom-example) |
| SimpleMessageParser | [SimpleMessageParser snippet](../apis/simplemessageparser.html#simplemessageparser-example) |

And the [official examples repository](https://github.com/ARMmbed/mbed-os-example-nfc).

## LoRa APIs

A [private network tutorial](../apis/LoRa-tutorial.html).

## Security APIs

You can try the following examples on GitHub:

- [ATECC608A secure element](https://github.com/ARMmbed/mbed-os-example-atecc608a)

- [DeviceKey](https://github.com/ARMmbed/mbed-os-example-devicekey): Injects a dummy root of trust (ROT) if a true random number generator (TRNG) is not available. The application also invokes the derive key API in different conditions and prints the results.

- [Mbed Crypto](https://github.com/ARMmbed/mbed-os-example-mbed-crypto): A set of examples demonstrating the compilation and use of Mbed Crypto on Mbed OS.

- [Mbed TLS: Authenticated encryption](https://github.com/ARMmbed/mbed-os-example-tls/blob/master/authcrypt): Demonstrates using the Cipher API for encrypting and authenticating data with AES-CCM.

- [Mbed TLS: Benchmark](https://github.com/ARMmbed/mbed-os-example-tls/blob/master/benchmark): Measures the time taken to perform basic cryptographic functions used in the library.

- [Mbed TLS: Hashing](https://github.com/ARMmbed/mbed-os-example-tls/blob/master/hashing): Demonstrates the various APIs for computing hashes of data (also known as message digests) with SHA-256.

- [Mbed TLS: TLS client](https://github.com/ARMmbed/mbed-os-example-tls/blob/master/tls-client): Downloads a file from an HTTPS server (os.mbed.com) and looks for a specific string in that file.

- [PSA attestation](https://github.com/ARMmbed/mbed-os-example-attestation): Injects an attestation key-pair, gets the attestation token size and the token.

Each of them comes with complete usage instructions as a readme file in the repository.

- Or try [the DeviceKey snippet](../apis/security-apis.html#devicekey-example).

## Serial communication

These tutorials teach you to communicate with your development board, an essential part of programming and debugging:

- [Windows serial driver tutorial](../program-setup/windows-serial-driver.html)
- [Board to PC communication over USB tutorial](../program-setup/serial-communication.html)
- [Low memory serial printf snippet](../program-setup/serial-communication.html#minimal-printf)

## Debugging

These tutorials show you how to install, export a project to and start a debugging session with different IDEs.

### Methods

- [BBC micro:bit, pyOCD and GDB debugging tutorial](../debug-test/debug-microbit.html).
- [Troubleshooting common issues](../debug-test/troubleshooting-common-issues.html).
- [Analyzing Mbed OS crash dump tutorial](../debug-test/analyzing-mbed-os-crash-dump.html) and [crash reporting official example](https://github.com/ARMmbed/mbed-os-example-crash-reporting)
- [Compile time errors tutorial](../debug-test/compile-time-errors.html).
- [Debugging using `printf` statements](../debug-test/debugging-using-printf-statements.html).


### Debugging with third party tools

- [Eclipse](../debug-test/third-party-tools.html).
- [Keil uVision](../debug-test/keil-uvision.html).
- [Visual Studio](../debug-test/visual-studio-code.html).

## Bootloader

- [A tutorial for creating and using a bootloader](../program-setup/creating-and-using-a-bootloader.html).
- [An official example](https://github.com/ARMmbed/mbed-os-example-bootloader).

## Connecting to the cloud

[Pelion Device Management](https://github.com/ARMmbed/mbed-os-example-pelion)

<!--404 https://github.com/ARMmbed/mbed-os-example-aws -->

## Migrating

If you are moving from Mbed OS 5 to Mbed OS 6, please see [the list of deprecated APIs](../apis/index.html#deprecated-apis).

If you are moving from Mbed 2 to Mbed OS 6 bare metal, [please see the bare metal documentation](../bare-metal/index.html).
