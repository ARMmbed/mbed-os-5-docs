# USB device

The HAL USBPhy API provides physical access to the USB bus in the role of a USB device. Implementing this API enables the use of any supported class driver, such as CDC, HID and MSD.

## Assumptions

### Defined behavior

- You can use any endpoint configurations that fit in the parameters of the table returned by `USBPhy::endpoint_table`.
- You can use all endpoints in any valid endpoint configuration concurrently.
- The device supports use of at least one control, bulk, interrupt and isochronous in each direction at the same time - at least 8 endpoints.
- USBPhy supports all standard endpoint sizes (wMaxPacketSize).
- USBPhy can handle an interrupt latency of at least 100ms if the host PC is not performing a reset or setting the device's address.
- USBPhy only sends USBPhyEvents when it is in the initialized state.
- When unpowered, USBPhy only sends the `USBPhyEvents::power` event.
- On USB reset, all endpoints are removed except for endpoint 0.
- A call to `USBPhy::ep0_write` results in the call of `USBPhyEvents::in` when the PC reads the data unless a power loss, reset or a call to `USBPhy::disconnect` occurs first.
- A call to `USBPhy::endpoint_write` results in the call of `USBPhyEvents::in` when the PC reads the data unless a power loss, reset or a call to `USBPhy::endpoint_abort` occurs first.
- A call to `USBPhy::endpoint_read` results in the call of `USBPhyEvents::out` when the PC sends data unless a power loss, reset or a call to `USBPhy::endpoint_abort` occurs first.
- Endpoint 0 naks all transactions aside from setup packets until higher-level code calls one of `USBPhy::ep0_read`, `USBPhy::ep0_write` or `USBPhy::ep0_stall`.
- Endpoint 0 stall automatically clears on reception of a setup packet.

### Undefined behavior

- Calling `USBPhy::endpoint_add` or `USBPhy::endpoint_remove` outside of the control requests SetInterface or SetConfiguration.
- Calling `USBPhy::endpoint_remove` on an endpoint that has an ongoing read or write operation. To avoid undefined behavior, you must abort ongoing operations with `USBPhy::endpoint_abort`.
- Devices behavior is undefined if latency is greater than 2ms when address is being set - see USB spec 9.2.6.3.
- Devices behavior is undefined if latency is greater than 10ms when a reset occurs - see USB spec 7.1.7.5.
- Calling any of the USBPhy::endpoint_* functions on endpoint 0.

### Notes

- Make sure USBPhy sends USBPhyEvents in the correct order when multiple packets are present. USBPhy must send IN endpoint events before OUT endpoint events if both are pending.
- A host PC may resend setup packets to a USB device if there is noise on the USB line. The USBPhy should be able to handle this scenario and respond to the setup packet with an ACK.
- Bidirectional protocols making use of alternating IN and OUT phases should not rely on the last ACK an IN transfer to indicate that the OUT phase should start. Instead, the OUT phase should be started at the same time the last IN transfer is started. This is because the ACK to the last in transfer may be dropped if there is noise on the USB line. If dropped, it will only be resent on the next IN phase. You can find more information on this in section 8.5.3.3 of the USB specification.

## Implementing USB

You can find the HAL API and specification for USB in the following module:

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/group__drivers___u_s_b_device.html)

To enable the HAL USBPhy API in Mbed OS, add the `USBDEVICE` label in the `device_has` option of the target's section in the `targets.json` file.

## Testing

The Mbed OS HAL provides a set of conformance tests for the HAL USBPhy API. You can use these tests to validate the correctness of your implementation. To run the HAL USBPhy API tests, use the following command:

```
mbed test -t <toolchain> -m <target> -n mbed-os-tests-usb_device-*
```

For **setup instructions**, known issues and more information about USB tests, please see the [README](https://github.com/ARMmbed/mbed-os/blob/master/TESTS/usb_device/README.md).
