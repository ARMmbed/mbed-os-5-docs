# Full API list

<!--add a few words about full v bare-->
This is the full list of APIs Mbed OS offers. The ticks indicate which of the APIs the [bare metal profile](../bare-metal/index.html) supports. For consistency, we also show the full profile's API support, although that is - and is expected to remain - all APIs.

<!--This list does not include the internal APIs, which are not intended for use by application code.-->

## RTOS and event handling

The Mbed OS RTOS capabilities include managing objects such as threads, synchronization objects and timers. It also provides interfaces for attaching an application-specific idle hook function, reads the OS tick count and implements functionality to report RTOS errors.

| API | Full profile | Bare metal profile |
| - | - | - |
| [Thread](../apis/rtos-apis.html) | &#10004; | |
| [ThisThread](../apis/thisthread.html) | &#10004; | &#10004; |
| [Mutex](../apis/mutex.html) | &#10004; | Partial |
| [Semaphore](../apis/semaphore.html) | &#10004; | &#10004;|
| [Queue](../apis/queue.html) | &#10004; | |
| [EventQueue](../apis/eventqueue.html) | &#10004; | &#10004; |
| [UserAllocatedEvent](../apis/userallocatedevent.html) | &#10004; | &#10004; |
| [Mail](../apis/mail.html) | &#10004; | |
| [EventFlags](../apis/eventflags.html) | &#10004; | &#10004; |
| [Event](../apis/event.html) | &#10004; | &#10004; |
| [Conditionvariable](../apis/conditionvariable.html) | &#10004; | |
| [Kernel interface functions](../apis/kernel-interface-functions.html) | &#10004; | Partial |

## Drivers

The drivers are digital interfaces that allow your board to interface with a computer or external devices.

| API | Full profile | Bare metal profile |
| - | - | - |
| [Ticker](../apis/driver-apis.html) | &#10004; | &#10004; |
| [Timeout](../apis/timeout.html) | &#10004; | &#10004; |
| [Timer](../apis/timer.html) | &#10004; | &#10004; |
| [Watchdog](../apis/watchdog.html) | &#10004; | &#10004;|
| [ResetReason](../apis/resetreason.html) | &#10004; | &#10004; |
| [Flash IAP](../apis/flash-iap.html) | &#10004; | &#10004; |
| [BufferedSerial](../apis/bufferedserial.html) | &#10004; | &#10004; |
| [UnbufferedSerial](../apis/unbufferedserial.html) | &#10004; | &#10004; |
| [SPI](../apis/spi.html) | &#10004; | &#10004; |
| [SPISlave](../apis/spislave.html) | &#10004; | &#10004; |
| [QuadSPI (QSPI)](../apis/quadspi-qspi.html) | &#10004; | &#10004; |
| [I2C](../apis/i2c.html) | &#10004; | &#10004; |
| [I2CSlave](../apis/i2cslave.html) | &#10004; | &#10004; |
| [CAN](../apis/can.html)| &#10004; | &#10004; |
| [MbedCRC](../apis/mbedcrc.html) | &#10004; | &#10004; |

## Input/Output

Input/Output APIs include analog and digital inputs and outputs on development boards, as well as digital interfaces, which allow your board to interface with a computer or external devices.

| API | Full profile | Bare metal profile |
| - | - | - |
| [AnalogIn](../apis/i-o-apis.html) | &#10004; | &#10004; |
| [AnalogOut](../apis/analogout.html) | &#10004; | &#10004; |
| [DigitalIn](../apis/digitalin.html) | &#10004; | &#10004; |
| [DigitalOut](../apis/digitalout.html) | &#10004; | &#10004;|
| [DigitalInOut](../apis/digitalinout.html) | &#10004; | &#10004; |
| [BusIn](../apis/busin.html) | &#10004; | &#10004; |
| [BusOut](../apis/busout.html) | &#10004; | &#10004; |
| [BusInOut](../apis/businout.html) | &#10004; | &#10004; |
| [PortIn](../apis/portin.html) | &#10004; | &#10004; |
| [PortOut](../apis/portout.html) | &#10004; | &#10004; |
| [PortInOut](../apis/portinout.html) | &#10004; | &#10004; |
| [PwmOut](../apis/pwmout.html) | &#10004; | &#10004; |
| [InterruptIn](../apis/interruptin.html) | &#10004; | &#10004; |

## Data storage

The data storage APIs include file system APIs, for file system operations, and block devices, which provide the raw storage for the file systems.


| API | Full profile | Bare metal profile |
| - | - | - |
| [KVStore](../apis/data-apis) | &#10004; | &#10004; |
| [Static Global API](../apis/static-global-api.html) | &#10004; | &#10004; |
| [FileSystem](../apis/filesystem.html) | &#10004; | &#10004; |
| [Dir](../apis/dir.html) | &#10004; | &#10004;|
| [File](../apis/file.html) | &#10004; | &#10004; |
| [LittleFileSystem](../apis/littlefilesystem.html) | &#10004; | &#10004; |
| [FATFileSystem](../apis/fatfilesystem.html) | &#10004; | &#10004; |
| [BlockDevice](../apis/blockdevice.html) | &#10004; | &#10004; |
| [HeapBlockDevice](../apis/heapblockdevice.html) | &#10004; | &#10004; |
| [MBRBlockDevice](../apis/mbrblockdevice.html) | &#10004; | &#10004; |
| [ChainingBlockDevice](../apis/chainingblockdevice.html) | &#10004; | &#10004; |
| [SlicingBlockDevice](../apis/slicingblockdevice.html) | &#10004; | &#10004; |
| [ProfilingBlockDevice](../apis/profilingblockdevice.htm) | &#10004; | &#10004; |
| [BufferedBlockDevice](../apis/bufferedblockdevice.html) | &#10004; | &#10004; |
| [FlashSimBlockDevice](../apis/flashsimblockdevice.html) | &#10004; | &#10004; |
| [DataFlashBlockDevice](../apis/dataflashblockdevice.html) | &#10004; | &#10004; |
| [FlashIAPBlockDevice](../apis/flashiapblockdevice.html) | &#10004; | &#10004; |
| [SDBlockDevice](../apis/sdblockdevice.html) | &#10004; | &#10004; |
| [SPI Flash block device](../apis/spi-flash-block-device.html)| &#10004; | &#10004; |
| [QSPIFBlockDevice](../apis/qspifblockdevice.html) | &#10004; | &#10004; |
| [PSA internal storage](../apis/psa-internal-storage.html) | &#10004; |  |
| [PSA protected storage](../apis/psa-protected-storage.html) | &#10004; |  |

## Connectivity

### Network interface

Network interfaces are the application level APIs where users choose the driver, connectivity method and IP stack. These include ethernet, Wi-Fi, cellular and mesh interfaces.

| API | Full profile | Bare metal profile |
| - | - | - |
| [Ethernet](../apis/ethernet.html) | &#10004; | |
| [Wi-Fi](../apis/wi-fi.html) | &#10004; | |
| [Cellular](../apis/cellular-api.html) | &#10004; | |
| [Mesh](../apis/mesh-api.htm) | &#10004; | |
| [Network status](../apis/network-status.html) | &#10004; | |
| [MessageParser](../apis/messageparser.html) | &#10004; | |
| [SimpleMessageParser](../apis/simplemessageparser.html) | &#10004; | |
| [MessageBuilder](../apis/messagebuilder.html) | &#10004; | |

### Socket

Socket APIs include the application programming interface for IP networking. In Mbed OS, this API supports both TCP and UDP protocols.

| API | Full profile | Bare metal profile |
| - | - | - |
| [Socket](../apis/socket.html) | &#10004; | |
| [UDPSocket](../apis/udpsocket.html) | &#10004; |  |
| [TCPSocket](../apis/tcpsocket.html) | &#10004; |  |
| [SocketAddress](../apis/socketaddress.html) | &#10004; | |
| [Non-IP cellular socket](../apis/non-ip-cellular-socket.html) | &#10004; | |
| [SocketStats](../apis/socketstats.html) | &#10004; | |

### Secure socket

| API | Full profile | Bare metal profile |
| - | - | - |
| [TLSSocket](../apis/secure-socket-apis.html) | &#10004; | |
| [DTLSSocket](../apis/dtlssocket.html) | &#10004; |  |

### DNS

| API | Full profile | Bare metal profile |
| - | - | - |
| [DNS Resolver](../apis/dns-apis.html) | &#10004; | |

### BLE

Bluetooth low energy (BLE) is a low power wireless technology standard for building personal area networks. Typical applications of BLE are health care, fitness trackers, beacons, smart home, security, entertainment, proximity sensors, industrial and automotive.

| API | Full profile | Bare metal profile |
| - | - | - |
| [BLE](../apis/ble.html) | &#10004; | &#10004; |
| [GAP](../apis/gap.html) | &#10004; | &#10004; |
| [GattClient](../apis/gattclient.html) | &#10004; | &#10004; |
| [GattServer](../apis/gattserver.html) | &#10004; | &#10004;|
| [SecurityManager](../apis/SecurityManager.html) | &#10004; | &#10004; |
| [BatteryService](../apis/batteryservice.html) | &#10004; | &#10004; |
| [HeartRateService](../apis/heartrateservice.html) | &#10004; | &#10004; |

### NFC

You can use Near-Field Communication (NFC), a short-range radio technology, for use cases such as contactless payments, access control and device pairing.

| API | Full profile | Bare metal profile |
| - | - | - |
| [NFCController](../apis/nfccontroller.html) | &#10004; | &#10004; |
| [NFC EEPROM](../apis/nfc-eeprom.html) | &#10004; | &#10004; |

### LoRaWAN

Arm Mbed OS provides a native network stack for LoRaWAN. LoRaWAN is a technology designed for low-power battery-powered devices. These devices operate in an unlicensed spectrum, creating high density wide-area networks.

| API | Full profile | Bare metal profile |
| - | - | - |
| [LoRaWANInterface](../apis/lorawaninterface.html) | &#10004; | &#10004; |
| [LoRaRadio](../apis/nfc-loraradio.html) | &#10004; | &#10004; |

## USB

The Mbed OS classes providing USB peripheral functionality, also known as USB components, inherit from USBDevice and provide specific USB peripherial functionality.

| API | Full profile | Bare metal profile |
| - | - | - |
| [USBSerial](../apis/usb-apis.html) | &#10004; | &#10004; |
| [USBAudio](../apis/usbaudio.html) | &#10004; | &#10004; |
| [USBHID](../apis/ubshid.html) | &#10004; | &#10004; |
| [USBCDC](../apis/usbcdc.html) | &#10004; | &#10004; |
| [USBCDC_ECM](../apis/usbcdc-ecm.html) | &#10004; | |
| [USBMSD](../apis/usbmsd.html) | &#10004; | &#10004; |
| [USBMIDI](../apis/usbmidi.html) | &#10004; | &#10004; |
| [USBMouse](../apis/usbmouse.html) | &#10004; | &#10004; |
| [USBKeyboard](../apis/usbkeyboard.html) | &#10004; | &#10004; |
| [USBMouseKeyboard](../apis/usbmousekeyboard.html) | &#10004; | &#10004; |

## Security

With [Arm Mbed TLS](security.html), a comprehensive SSL/TLS solution, you can include cryptographic and SSL/TLS capabilities in your code.


| API | Full profile | Bare metal profile |
| - | - | - |
| [PSA initial attestation](../apis/security-apis.html) | &#10004; | |
| [PSA lifecycle](../apis/psa-lifecycle.html) | &#10004; |  |
| [Mbed Crypto](../apis/mbed-crypto.html) | &#10004; | &#10004; |
| [TLS](../apis/tls.html) | &#10004; | &#10004; |
| [DeviceKey](../apis/devicekey.html) | &#10004; | &#10004; |

## Power

<!--needs intro-->

| API | Full profile | Bare metal profile |
| - | - | - |
| [Power management (sleep)](../apis/power-apis.html) | &#10004; | &#10004; |
| [DeepSleepLock](../apis/deepsleeplock.html) | &#10004; | &#10004;  |
| [Idle loop](../apis/idle-loop.html) | &#10004; | |
| [LowPowerTicker](../apis/lowpowerticker.html) | &#10004; | &#10004; |
| [LowPowerTimeout](../apis/lowpowertimeout.html) | &#10004; | &#10004; |
| [LowPowerTimer](../apis/lowpowertimer.html) | &#10004; | &#10004; |

## Memory

<!--needs intro-->

| API | Full profile | Bare metal profile |
| - | - | - |
| [mbed_stats (Mbed statistics)](../apis/mbed-statistics.html) | &#10004; | &#10004; |
| [mpug_mgmt (MPU management)](../apis/mpu-management.html) | &#10004; | &#10004;  |
| [mbed_mem_trace (Memory tracing)](../apis/memory-tracing.html) | &#10004; | &#10004; |
| [MemoryPool](../apis/memorypool.html) | &#10004; | |

## Utilities

<!--needs intro-->

| API | Full profile | Bare metal profile |
| - | - | - |
| [Callback](../apis/util-apis.html) | &#10004; | &#10004; |
| [CriticalSectionLock](../apis/criticalsectionlock.html) | &#10004; | &#10004; |
| [Time](../apis/time.html) | &#10004; | &#10004; |
| [RTC](../apis/rtc.html) | &#10004; | &#10004; |
| [Debug](../apis/debug.html) | &#10004; | &#10004; |
| [Error handling](../apis/error-handling.html) | &#10004; | &#10004; |
| [Assert](../apis/assert.html) | &#10004; | &#10004; |
| [NonCopyable](../apis/noncopyable.html) | &#10004; | &#10004; |
| [SharedPtr (Shared pointer](../apis/shared-pointer.html) | &#10004; | &#10004; |
| [Span](../apis/span.html) | &#10004; | &#10004; |
| [FileHandle](../apis/filehandle.html) | &#10004; | &#10004; |
| [Poll](../apis/poll.html) | &#10004; | &#10004; |
| [PlatformMutex](../apis/platformmutex.html) | &#10004; | &#10004; |
| [CircularBuffer](../apis/circularbuffer.html) | &#10004; | &#10004; |
| [ATCmdParser](../apis/atcmdparser.html) | &#10004; | &#10004; |
| [ScopedRamExecutionLock](../apis/scopedramexecutionlock.html) | &#10004; | &#10004; |
| [ScopedRomWriteLock](../apis/scopedromwritelock.html) | &#10004; | &#10004; |

## Deprecated APIs: moving from Mbed OS 5 to 6

If you're moving your program from Mbed OS 5 to 6, you will need to replace deprecated APIs:

| Deprecated API | Replaced by |
| - | - |
| Serial | [BufferedSerial](../apis/bufferedserial.html), [UnbufferedSerial](../apis/unbufferedserial.html) |
