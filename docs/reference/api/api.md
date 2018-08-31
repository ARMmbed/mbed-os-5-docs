## Full API list


### Platform

[Modules that provide consistent user experience.](platform.html)

<table>
<tbody>
<tr>
<td><a href="wait.html">Wait</a></td>
<td><a href="criticalsectionlock.html">CriticalSectionLock</a></td>
<td><a href="memory-tracing.html">Memory tracing</a></td>
<td><a href="shared-pointer.html">Shared pointer</a></td>
<td><a href="atcmdparser.html">ATCmdParser</a></td>
</tr>
<tr>
<td><a href="callback.html">Callback</a></td>
<td><a href="time.html">Time</a></td>
<td><a href="error-handling.html">Error handling</a></td>
<td><a href="span.html">Span</a></td>
<td><a href="mbed-statistics.html">Mbed statistics</a></td>
</tr>
<tr>
<td><a href="deepsleeplock.html">DeepSleepLock</a></td>
<td><a href="rtc.html">RTC</a></td>
<td><a href="assert.html">Assert</a></td>
<td><a href="platformmutex.html">PlatformMutex</a></td>
</tr>
<tr>
<td><a href="power-management.html">Power management</a></td>
<td><a href="debug.html">Debug</a></td>
<td><a href="noncopyable.html">NonCopyable</a></td>
<td><a href="circularbuffer.html">CircularBuffer</a></td>
</tr>
</tbody>
</table>

### Drivers

[Analog and digital input and outputs and digital interfaces.](drivers.html)

<table>
<tbody>
<tr>
<td><a href="analogin.html">AnalogIn</a></td>
<td><a href="portin.html">PortIn</a></td>
<td><a href="lowpowertimeout.html">LowPowerTimeout</a></td>
<td><a href="i2c.html">I2C</a></td>
</tr>
<tr>
<td><a href="analogout.html">AnalogOut</a></td>
<td><a href="portout.html">PortOut</a></td>
<td><a href="lowpowertimer.html">LowPowerTimer</a></td>
<td><a href="i2cslave.html">I2CSlave</a></td>
</tr>
<tr>
<td><a href="digitalin.html">DigitalIn</a></td>
<td><a href="portinout.html">PortInOut</a></td>
<td><a href="flash-iap.html">Flash IAP</a></td>
<td><a href="debug.html">CAN</a></td>
</tr>
<tr>
<td><a href="digitalout.html">DigitalOut</a></td>
<td><a href="pwmout.html">PwmOut</a></td>
<td><a href="rawserial.html">RawSerial</a></td>
<td><a href="mbedcrc.html">MbedCRC</a></td>
</tr>
<tr>
<td><a href="digitalinout.html">DigitalInOut</a></td>
<td><a href="interruptin.html">InterruptIn</a></td>
<td><a href="serial.html">Serial</a></td>
<td><a href="devicekey.html">DeviceKey</a></td>
</tr>
<tr>
<td><a href="busin.html">BusIn</a></td>
<td><a href="timeout.html">Timeout</a></td>
<td><a href="spi.html">SPI</a></td>
</tr>
<tr>
<td><a href="busout.html">BusOut</a></td>
<td><a href="timer.html">Timer</a></td>
<td><a href="spislave.html">SPISlave</a></td>
</tr>
<tr>
<td><a href="businout.html">BusInOut</a></td>
<td><a href="lowpowerticker.html">LowPowerTicker</a></td>
<td><a href="quadspi-qspi.html">QuadSPI (QSPI)</a></td>
</tr>
</tbody>
</table>

### RTOS

[Handling tasks and events in Mbed OS.](rtos.html)

<table>
<tbody>
<tr>
<td><a href="thread.html">Thread</a></td>
<td><a href="queue.html">Queue</a></td>
<td><a href="mail.html">Mail</a></td>
<td><a href="event.html">Event</a></td>
</tr>
<tr>
<td><a href="mutex.html">Mutex</a></td>
<td><a href="eventqueue.html">EventQueue</a></td>
<td><a href="rtostimer.html">RtosTimer</a></td>
<td><a href="conditionvariable.html">ConditionVariable</a></td>
</tr>
<tr>
<td><a href="semaphore.html">Semaphore</a></td>
<td><a href="memorypool.html">MemoryPool</a></td>
<td><a href="eventflags.html">EventFlags</a></td>
<td><a href="kernel-interface-functions.html">Kernel interface functions</a></td>
</tr>
</tbody>
</table>

### Network socket

[Network socket API for TCP/IP.](network-socket.html)

<table>
<tbody>
<tr>
<td><a href="socket.html">Socket</a></td>
<td><a href="socketaddress.html">SocketAddress</a></td>
</tr>
<tr>
<td><a href="udpsocket.html">UDPSocket</a></td>
<td><a href="dns-resolver.html">DNS Resolver</a></td>
<tr>
<td><a href="tcpsocket.html">TCPSocket</a></td>
</tr>
</tbody>
</table>

### Network interfaces

[Network interfaces, Ethernet, Wifi, Cellular & Mesh](network-interfaces.html)

<table>
<tbody>
<tr>
<td><a href="ethernet.html">Ethernet</a></td>
<td><a href="mesh-api.html">6LoWPAN Mesh</a></td>
</tr>
<tr>
<td><a href="wi-fi.html">Wi-Fi</a></td>
<td><a href="network-status.html">Network status</a></td>
<tr>
<td><a href="cellular-api.html">Cellular</a></td>
</tr>
</tbody>
</table>

### Bluetooth Low Energy (BLE)

[Bluetooth Low Energy](bluetooth.html)

<table>
<tbody>
<tr>
<td><a href="ble.html">BLE</a></td>
<td><a href="gattserver.html">GattServer</a></td>
<td><a href="heartrateservice.html">HeartRateService</a></td>
</tr>
<tr>
<td><a href="gap.html">GAP</a></td>
<td><a href="secuirtymanager.html">SecurityManager</a></td>
<td><a href="ibeacon.html">iBeacon</a></td>
<tr>
<td><a href="gattclient.html">GattClient</a></td>
<td><a href="batteryservice.html">BatteryService</a></td>
</tr>
</tbody>
</table>

### LoRaWAN

[Low power wide area network.](lorawan.html)

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

### Security

[Working with Arm Mbed uVisor and Arm Mbed TLS in the context of Mbed OS.](security.html)

<table>
<tbody>
<tr>
<td><a href="tls.html">TLS</a></td>
</tr>
<tr>
<td><a href="uvisor.html">uVisor</a></td>
</tr>
</tbody>
</table>

### Storage

[Working with the file system.](storage.html)

<table>
<tbody>
<tr>
<td><a href="filesystem.html">FileSystem</a></td>
<td><a href="fatfilesystem.html">FATFileSystem</a></td>
<td><a href="chainingblockdevice.html">ChainingBlockDevice</a></td>
<td><a href="flashsimblockdevice.html">FlashSimBlockDevice</a></td>
</tr>
<tr>
<td><a href="dir.html">Dir</a></td>
<td><a href="blockdevice.html">BlockDevice</a></td>
<td><a href="slicingblockdevice.html">SlicingBlockDevice</a></td>
<td><a href="nvstore.html">NVStore</a></td>
</tr>
<tr>
<td><a href="file.html">File</a></td>
<td><a href="heapblockdevice.html">HeapBlockDevice</a></td>
<td><a href="profilingblockdevice.html">ProfilingBlockDevice</a></td>
</tr>
<tr>
<td><a href="littlefilesystem.html">LittleFileSystem</a></td>
<td><a href="mbrblockdevice.html">MBRBlockDevice</a></td>
<td><a href="bufferedblockdevice.html">BufferedBlockDevice</a></td>
</tr>
</tbody>
</table>
