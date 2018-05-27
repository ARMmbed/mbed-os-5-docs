## USBMouseKeyboard

The USBMouseKeyboard interface is used to emulate a mouse and a keyboard at the same time over the USB port. Both presses and mouse movements can be sent with this class.

### USBMouseKeyboard class reference

TODO

### USBMouseKeyboard example

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

### Related content

- [USBMouse](USBMouse.md)
- [USBKeyboard](USBKeyboard.md)
