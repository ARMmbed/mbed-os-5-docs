# USBMouse

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_mouse.png)<span>USBMouse class hierarchy</span></span>

You can use the USBMouse interface to emulate a mouse over the USB port. You can choose relative or absolute coordinates and send clicks, button state and scroll wheel movements. If you need keyboard or keyboard and mouse functionality, please see the [USBKeyboard](../apis/usbkeyboard.html) and [USBMouseKeyboard](../apis/usbmousekeyboard.html) classes.

## USBMouse class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_mouse.html)

## USBMouse example

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_USB/USBMouse_relative_pos)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_USB/USBMouse_relative_pos/main.cpp)

You can choose either a relative mouse or an absolute mouse. With a relative mouse, the USBMouse move function will move the mouse x, y pixels away from its previous position on the screen. For an absolute mouse, the USBMouse move function will move the mouse to coordinates x, y on the screen. By default, a USBMouse is a relative mouse. For example, you can use an absolute mouse to draw a circle:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_USB/USBMouse_absolute_pos)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_USB/USBMouse_absolute_pos/main.cpp)

## USBMouse Joystick example  

This example uses a Grove - Thumb Joystick to act as a mouse. Use the joystick to move the mouse around the screen and click the joystick down to do a mouse left click.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_USB/USBMouse_joystick)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_USB/USBMouse_joystick/main.cpp)

## Related content

- [USBKeyboard](../apis/usbkeyboard.html).
- [USBMouseKeyboard](../apis/usbmousekeyboard.html).
