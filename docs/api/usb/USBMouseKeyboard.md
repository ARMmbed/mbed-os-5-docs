# USBMouseKeyboard

<span class="images">![](https://os.mbed.com/docs/v5.10/feature-hal-spec-usb-device-doxy/class_u_s_b_mouse_keyboard.png)<span>USBMouseKeyboard class hierarchy</span></span>

You can use the USBMouseKeyboard interface to emulate a mouse and a keyboard at the same time over the USB port. You can send both presses and mouse movements with this class.

## USBMouseKeyboard class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/v5.10/feature-hal-spec-usb-device-doxy/class_u_s_b_mouse_keyboard.html)

## USBMouseKeyboard example

```C++
#include "mbed.h"
#include "USBMouseKeyboard.h"

//LED1: NUM_LOCK
//LED2: CAPS_LOCK
//LED3: SCROLL_LOCK
BusOut leds(LED1, LED2, LED3);

//USBMouseKeyboard
USBMouseKeyboard key_mouse;

int main(void) {
    while (1) {
        key_mouse.media_control(KEY_VOLUME_DOWN);
        key_mouse.printf("Hello World from Mbed\r\n");
        key_mouse.key_code('s', KEY_CTRL);
        key_mouse.move(20, 0);
        key_mouse.key_code(KEY_SCROLL_LOCK);
        wait(1);
        leds = key_mouse.lock_status();
    }
}
```

## Related content

- [USBMouse](USBMouse.html).
- [USBKeyboard](USBKeyboard.html).
