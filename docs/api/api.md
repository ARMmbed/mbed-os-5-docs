# Full API list
<!--these are now just the APIs - do I want to add the tutorials?-->
<!--add a few words about full v bare-->

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

<table>
<tbody>
<tr>
<td><a href="ble.html">BLE</a></td>
<td><a href="gap.html">GAP</a></td>
<td><a href="gattclient.html">GattClient</a></td>
<td><a href="gattserver.html">GattServer</a></td>
<td><a href="SecurityManager.html">SecurityManager</a></td>
</tr>
<tr>
<td><a href="batteryservice.html">BatteryService</a></td>
<td><a href="heartrateservice.html">HeartRateService</a></td>
</tr>
</tbody>
</table>

### NFC

You can use Near-Field Communication (NFC), a short-range radio technology, for use cases such as contactless payments, access control and device pairing.

<table>
<tbody>
<tr>
<td><a href="nfccontroller.html">NFCController</a></td>
<td><a href="nfc-eeprom.html">NFC EEPROM</a></td>
</tr>
</tbody>
</table>

### LoRaWAN

Arm Mbed OS provides a native network stack for LoRaWAN. LoRaWAN is a technology designed for low-power battery-powered devices. These devices operate in an unlicensed spectrum, creating high density wide-area networks.

<table>
<tbody>
<tr>
<td><a href="lorawaninterface.html">LoRaWANInterface</a></td>
<td><a href="loraradio.html">LoRaRadio</a></td>
</tr>
</tbody>
</table>

## USB

The Mbed OS classes providing USB peripheral functionality, also known as USB components, inherit from USBDevice and provide specific USB peripherial functionality.

<table>
<tbody>
<tr>
<td><a href="usb-apis.html">USBSerial</a></td>
<td><a href="usbaudio.html">USBAudio</a></td>
<td><a href="ubshid.html">USBHID</a></td>
<td><a href="usbcdc.html">USBCDC</a></td>
<td><a href="usbcdc-ecm.html">USBCDC_ECM</a></td>
</tr>
<tr>
<td><a href="usbmsd.html">USBMSD</a></td>
<td><a href="usbmidi.html">USBMIDI</a></td>
<td><a href="usbmouse.html">USBMouse</a></td>
<td><a href="usbkeyboard.html">USBKeyboard</a></td>
<td><a href="usbmousekeyboard.html">USBMouseKeyboard</a></td>
</tr>
</tbody>
</table>

## Security

With [Arm Mbed TLS](security.html), a comprehensive SSL/TLS solution, you can include cryptographic and SSL/TLS capabilities in your code.

<table>
<tbody>
<tr>
<td><a href="security-apis.html">PSA initial attestation</a></td>
<td><a href="psa-lifecycle.html">PSA lifecycle</a></td>
<td><a href="mbed-crypto.html">Mbed Crypto</a></td>
<td><a href="tls.html">TLS</a></td>
<td><a href="devicekey.html">DeviceKey</a></td>
</tr>
</tbody>
</table>

## Power

<table>
<tbody>
<tr>
<td><a href="power-apis.html">Power management (sleep)</a></td>
<td><a href="deepsleeplock.html">DeepSleepLock</a></td>
<td><a href="idle-loop.html">Idle loop</a></td>
</tr>
<tr>
<td><a href="lowpowerticker.html">LowPowerTicker</a></td>
<td><a href="lowpowertimeout.html">LowPowerTimeout</a></td>
<td><a href="lowpowertimer.html">LowPowerTimer</a></td>
</tr>
</tbody>
</table>

## Memory

<table>
<tbody>
<tr>
<td><a href="mbed-statistics.html">mbed_stats (Mbed statistics)</a></td>
<td><a href="mpu-management.html">mpug_mgmt (MPU management)</a></td>
<td><a href="memory-tracing.html">mbed_mem_trace (Memory tracing)</a></td>
<td><a href="memorypool.html">MemoryPool</a></td>
</tr>
</tbody>
</table>

## Utilities

<table>
<tbody>
<tr>
<td><a href="util-apis.html">Callback</a></td>
<td><a href="criticalsectionlock.html">CriticalSectionLock</a></td>
<td><a href="time.html">Time</a></td>
<td><a href="rtc.html">RTC</a></td>
<td><a href="debug.html">Debug</a></td>
</tr>
<tr>
<td><a href="error-handling.html">Error handling</a></td>
<td><a href="assert.html">Assert</a></td>
<td><a href="noncopyable.html">NonCopyable</a></td>
<td><a href="shared-pointer.html">SharedPtr (Shared pointer)</a></td>
<td><a href="span.html">Span</a></td>
</tr>
<tr>
<td><a href="filehandle.html">FileHandle</a></td>
<td><a href="poll.html">Poll</a></td>
<td><a href="platformmutex.html">PlatformMutex</a></td>
<td><a href="circularbuffer.html">CircularBuffer</a></td>
<td><a href="atcmdparser.html">ATCmdParser</a></td>
</tr>
<tr>
<td><a href="scopedramexecutionlock.html">ScopedRamExecutionLock</a></td>
<td><a href="scopedromwritelock.html">ScopedRomWriteLock</a></td>
</tr>
</tbody>
</table>

## Deprecated APIs: moving from Mbed OS 5 to 6

If you're moving your program from Mbed OS 5 to 6, you will need to replace deprecated APIs:

| Deprecated API | Replaced by |
| - | - |
| Serial | [BufferedSerial](../apis/bufferedserial.html), [UnbufferedSerial](../apis/unbufferedserial.html) |
