### USB Device

The HAL USBPhy API provides physical access to the USB bus in the role of a USB Device. Implementing this API enables the use of any supported class driver, such as CDC, HID and MSD.

#### Assumptions

##### Defined behavior

- Any endpoint configurations which fit in the parameters of the table returned by USBPhy::endpoint_table can be used.
- All endpoints in any valid endpoint configuration can be used concurrently
- Device supports use of at least one control, bulk, interrupt and isochronous in each direction at the same time - at least 8 endpoints.
- Device supports all standard endpoint sizes (wMaxPacketSize)
- Device can handle an interrupt latency of at least 100ms if reset is not being performed and address is not being set
- USBPhyEvents events are only sent when USBPhy is in the initialized state
- When unpowered only the USBPhyEvents::power event can be sent
- On USB reset all endpoints are removed except for endpoint 0
- USBPhyEvents::out and USBPhyEvents::in events only occur for endpoints which have been added
- A call to USBPhy::ep0_write results in USBPhyEvents::in getting called if not interrupted by a power loss or reset
- A call to endpoint_read followed by endpoint_read_result results in USBPhyEvents::out getting called if not interrupted by a power loss or reset
- Endpoint 0 naks all transactions aside from setup packets until one of ep0_read, ep0_write or ep0_stall has been called
- Endpoint 0 stall is automatically cleared on reception of a setup packet

##### Undefined behavior

- Calling USBPhy::endpoint_add or USBPhy::endpoint_remove outside of the control requests SetInterface or SetConfiguration
- Devices behavior is undefined if latency is greater than 2ms when address is being set - see USB spec 9.2.6.3
- Devices behavior is undefined if latency is greater than 10ms when a reset occurs - see USB spec 7.1.7.5
- Calling any of the USBPhy::endpoint_* functions on endpoint 0

##### Notes

- Make sure USB packets are processed in the correct order when multiple packets are present. Typically IN endpoints should be handled before OUT endpoints if both are pending.
- Setup packets may be resent if there is noise on the USB line. The USBPhy should be able to gracefully handle this scenario and respond to the setup packet with an ACK.
- Bi-directional protocols making use of alternating IN and OUT phases should not rely on the last ACK an IN transfer to indicate that the OUT phase should start. Instead, the OUT phase should be started at the same time the last IN transfer is started. This is because the ACK to the last in transfer may be dropped if there is noise on the USB line. If dropped it will only get re-sent on the next IN phase. More info on this can be found in section 8.5.3.3 of the USB spec.

#### Implementing USB

To add support for the HAL USBPhy API you need to implement this API and submit pull request against feature-hal-spec-usb-device branch. You can find the API and specification for the HAL USBPhy API here:

TODO

To enable the HAL USBPhy API in Mbed OS, add the `USBDEVICE` label in the `device_has` option of the target's section in the `targets.json` file.

#### Testing

The Mbed OS HAL provides a set of conformance tests for the HAL USBPhy API. You can use these tests to validate the correctness of your implementation. To run the HAL USBPhy API tests, use the following command:
```
mbed test -t <toolchain> -m <target> -n mbed-os-tests-usb_device-*
```
