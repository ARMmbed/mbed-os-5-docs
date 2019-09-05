# Full API list

## Platform APIs

[Platform APIs](platform.html) provide general purpose MCU management infrastructure, common data structures and a consistent user experience on top of different standard libraries and toolchains.

<table>
<tbody>
<tr>
<td><a href="wait.html">Wait</a></td>
<td><a href="time.html">Time</a></td>
<td><a href="noncopyable.html">NonCopyable</a></td>
<td><a href="circularbuffer.html">CircularBuffer</a></td>
</tr>
<tr>
<td><a href="callback.html">Callback</a></td>
<td><a href="rtc.html">RTC</a></td>
<td><a href="shared-pointer.html">Shared pointer</a></td>
<td><a href="atcmdparser.html">ATCmdParser</a></td>
</tr>
<tr>
<td><a href="deepsleeplock.html">DeepSleepLock</a></td>
<td><a href="debug.html">Debug</a></td>
<td><a href="span.html">Span</a></td>
<td><a href="mbed-statistics.html">Mbed statistics</a></td>
</tr>
<tr>
<td><a href="power-management-sleep.html">Power management (sleep)</a></td>
<td><a href="memory-tracing.html">Memory tracing</a></td>
<td><a href="filehandle.html">FileHandle</a></td>
<td><a href="mpu-management.html">MPU management</a></td>
</tr>
<tr>
<td><a href="idle-loop.html">Idle loop</a></td>
<td><a href="error-handling.html">Error handling</a></td>
<td><a href="poll.html">Poll</a></td>
<td><a href="scopedramexecutionlock.html">ScopedRamExecutionLock</a></td>
</tr>
<tr>
<td><a href="criticalsectionlock.html">CriticalSectionLock</a></td>
<td><a href="assert.html">Assert</a></td>
<td><a href="platformmutex.html">PlatformMutex</a></td>
<td><a href="scopedromwritelock.html">ScopedRomWriteLock</a></td>
</tr>
</tbody>
</table>

## Drivers APIs

[Driver APIs](drivers.html) include analog and digital inputs and outputs on development boards, as well as digital interfaces, which allow your board to interface with a computer or external devices.

<table>
<tbody>
<tr>
<td><a href="analogin.html">AnalogIn</a></td>
<td><a href="businout.html">BusInOut</a></td>
<td><a href="timeout.html">Timeout</a></td>
<td><a href="flash-iap.html">Flash IAP</a></td>
<td><a href="i2cslave.html">I2CSlave</a></td>
</tr>
<tr>
<td><a href="analogout.html">AnalogOut</a></td>
<td><a href="portin.html">PortIn</a></td>
<td><a href="timer.html">Timer</a></td>
<td><a href="rawserial.html">RawSerial</a></td>
<td><a href="can.html">CAN</a></td>
</tr>
<tr>
<td><a href="digitalin.html">DigitalIn</a></td>
<td><a href="portout.html">PortOut</a></td>
<td><a href="lowpowerticker.html">LowPowerTicker</a></td>
<td><a href="serial.html">Serial</a></td>
<td><a href="mbedcrc.html">MbedCRC</a></td>
</tr>
<tr>
<td><a href="digitalout.html">DigitalOut</a></td>
<td><a href="portinout.html">PortInOut</a></td>
<td><a href="lowpowertimeout.html">LowPowerTimeout</a></td>
<td><a href="spi.html">SPI</a></td>
</tr>
<tr>
<td><a href="digitalinout.html">DigitalInOut</a></td>
<td><a href="pwmout.html">PwmOut</a></td>
<td><a href="lowpowertimer.html">LowPowerTimer</a></td>
<td><a href="spislave.html">SPISlave</a></td>
</tr>
<tr>
<td><a href="busin.html">BusIn</a></td>
<td><a href="interruptin.html">InterruptIn</a></td>
<td><a href="watchdog.html">Watchdog</a></td>
<td><a href="quadspi-qspi.html">QuadSPI (QSPI)</a></td>
</tr>
<tr>
<td><a href="busout.html">BusOut</a></td>
<td><a href="ticker.html">Ticker</a></td>
<td><a href="resetreason.html">ResetReason</a></td>
<td><a href="i2c.html">I2C</a></td>
</tr>
</tbody>
</table>

## RTOS APIs

The [Mbed OS RTOS](rtos.html) capabilities include managing objects such as threads, synchronization objects and timers. It also provides interfaces for attaching an application-specific idle hook function, reads the OS tick count and implements functionality to report RTOS errors.

<table>
<tbody>
<tr>
<td><a href="thread.html">Thread</a></td>
<td><a href="semaphore.html">Semaphore</a></td>
<td><a href="userallocatedevent.html">UserAllocatedEvent</a></td>
<td><a href="eventflags.html">EventFlags</a></td>
<td><a href="kernel-interface-functions.html">Kernel interface functions</a></td>
</tr>
<tr>
<td><a href="thisthread.html">ThisThread</a></td>
<td><a href="queue.html">Queue</a></td>
<td><a href="memorypool.html">MemoryPool</a></td>
<td><a href="event.html">Event</a></td>
</tr>
<tr>
<td><a href="mutex.html">Mutex</a></td>
<td><a href="eventqueue.html">EventQueue</a></td>
<td><a href="mail.html">Mail</a></td>
<td><a href="conditionvariable.html">ConditionVariable</a></td>
</tr>
</tbody>
</table>

## USB APIs

The Mbed OS classes providing USB peripheral functionality, also known as [USB components](../apis/usb.html), inherit from USBDevice and provide specific USB peripherial functionality.

<table>
<tbody>
<tr>
<td><a href="usbserial.html">USBSerial</a></td>
<td><a href="usbhid.html">USBHID</a></td>
<td><a href="usbcdc-ecm.html">USBCDC_ECM</a></td>
<td><a href="usbmidi.html">USBMIDI</a></td>
<td><a href="usbkeyboard.html">USBKeyboard</a></td>
</tr>
<tr>
<td><a href="usbaudio.html">USBAudio</a></td>
<td><a href="usbcdc.html">USBCDC</a></td>
<td><a href="usbmsd.html">USBMSD</a></td>
<td><a href="usbmouse.html">USBMouse</a></td>
<td><a href="usbmousekeyboard.html">USBMouseKeyboard</a></td>
</tr>
</tbody>
</table>

## Network socket APIs

[Network socket APIs](network-socket.html) include the application programming interface for IP networking. In Mbed OS, this API supports both TCP and UDP protocols.

<table>
<tbody>
<tr>
<td><a href="socket.html">Socket</a></td>
<td><a href="tcpsocket.html">TCPSocket</a></td>
<td><a href="non-ip-cellular-socket.html">Non-IP cellular socket</a></td>
<td><a href="tlssocket.html">TLSSocket</a></td>
<td><a href="socketstats.html">SocketStats</a></td>
</tr>
<tr>
<td><a href="udpsocket.html">UDPSocket</a></td>
<td><a href="socketaddress.html">SocketAddress</a></td>
<td><a href="dns-resolver.html">DNS resolver</a></td>
<td><a href="dtlssocket.html">DTLSSocket</a></td>
</tbody>
</table>

## Network interfaces APIs

[Network interfaces](network-interfaces.html) are the application level APIs where users choose the driver, connectivity method and IP stack. These include ethernet, Wi-Fi, cellular and mesh interfaces.

<table>
<tbody>
<tr>
<td><a href="ethernet.html">Ethernet</a></td>
<td><a href="cellular-api.html">Cellular</a></td>
<td><a href="network-status.html">Network status</a></td>
</tr>
<tr>
<td><a href="wi-fi.html">Wi-Fi</a></td>
<td><a href="mesh-api.html">Mesh</a></td>
</tr>
</tbody>
</table>

## Bluetooth Low Energy (BLE) APIs

[Bluetooth low energy (BLE)](bluetooth.html) is a low power wireless technology standard for building personal area networks. Typical applications of BLE are health care, fitness trackers, beacons, smart home, security, entertainment, proximity sensors, industrial and automotive.

<table>
<tbody>
<tr>
<td><a href="ble.html">BLE</a></td>
<td><a href="gattclient.html">GattClient</a></td>
<td><a href="securitymanager.html">SecurityManager</a></td>
<td><a href="heartrateservice.html">HeartRateService</a></td>
</tr>
<tr>
<td><a href="gap.html">GAP</a></td>
<td><a href="gattserver.html">GattServer</a></td>
<td><a href="batteryservice.html">BatteryService</a></td>
<td><a href="ibeacon.html">iBeacon</a></td>
</tr>
</tbody>
</table>

## LoRaWAN APIs

Arm Mbed OS provides a native network stack for [LoRaWAN](lorawan.html). LoRaWAN is a technology designed for low-power battery-powered devices. These devices operate in an unlicensed spectrum, creating high density wide-area networks.

<table>
<tbody>
<tr>
<td><a href="lorawan-api.html">LoRaWANInterface</a></td>
</tr>
<tr>
<td><a href="loraradio-api.html">LoRaRadio</a></td>
</tr>
</tbody>
</table>

## NFC APIs

You can use [Near-Field Communication (NFC)](nfc.html), a short-range radio technology, to enable use cases such as contactless payments, access control and device pairing.

<table>
<tbody>
<tr>
<td><a href="nfccontroller.html">NFCController</a></td>
<td><a href="messageparser.html">MessageParser</a></td>
<td><a href="messagebuilder.html">MessageBuilder</a></td>
</tr>
<tr>
<td><a href="nfc-eeprom.html">NFC EEPROM</a></td>
<td><a href="simplemessageparser.html">SimpleMessageParser</a></td>
</tr>
</tbody>
</table>

## Security API

With [Arm Mbed TLS](security.html), a comprehensive SSL/TLS solution, you can include cryptographic and SSL/TLS capabilities in your code.

<table>
<tbody>
<tr>
<td><a href="../apis/psa-initial-attestation.html">PSA attestation</a></td>
<td><a href="../apis/psa-lifecycle.html">PSA lifecycle</a></td>
<td><a href="devicekey.html">DeviceKey</a></td>
</tr>
<tr>
<td><a href="mbed-crypto.html">Mbed Crypto</a></td>
<td><a href="tls.html">TLS</a></td>
</tr>
</tbody>
</table>

## Storage APIs

The [storage APIs](storage.html) include file system APIs, for file system operations, and block devices, which provide the raw storage for the file systems.

<table>
<tbody>
<tr>
<td><a href="kvstore.html">KVStore</a></td>
<td><a href="littlefilesystem.html">LittleFileSystem</a></td>
<td><a href="chainingblockdevice.html">ChainingBlockDevice</a></td>
<td><a href="../apis/dataflashblockdevice.html">DataFlashBlockDevice</a></td>
<td><a href="nvstore.html">NVStore</a></td>
</tr>
<tr>
<td><a href="static-global-api.html">Static Global API</a></td>
<td><a href="fatfilesystem.html">FATFileSystem</a></td>
<td><a href="slicingblockdevice.html">SlicingBlockDevice</a></td>
<td><a href="flashiapblockdevice.html">FlashIAPBlockDevice</a></td>
<td><a href="../apis/psa-internal-storage.html">PSA internal storage</a></td>
</tr>
<tr>
<td><a href="filesystem.html">FileSystem</a></td>
<td><a href="blockdevice.html">BlockDevice</a></td>
<td><a href="profilingblockdevice.html">ProfilingBlockDevice</a></td>
<td><a href="sdblockdevice.html">SDBlockDevice</a></td>
<td><a href="../apis/psa-protected-storage.html">PSA protected storage</a></td>
</tr>
<tr>
<td><a href="dir.html">Dir</a></td>
<td><a href="heapblockdevice.html">HeapBlockDevice</a></td>
<td><a href="bufferedblockdevice.html">BufferedBlockDevice</a></td>
<td><a href="spi-flash-block-device.html">SPIFlashBlockDevice</a></td>
</tr>
<tr>
<td><a href="file.html">File</a></td>
<td><a href="mbrblockdevice.html">MBRBlockDevice</a></td>
<td><a href="flashsimblockdevice.html">FlashSimBlockDevice</a></td>
<td><a href="qspifblockdevice.html">QSPIFBlockDevice</a></td>
</tr>
</tbody>
</table>
