# USBMouseKeyboard

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_mouse_keyboard.png)<span>USBMouseKeyboard class hierarchy</span></span>

You can use the USBMouseKeyboard interface to emulate a mouse and a keyboard at the same time over the USB port. You can send both key presses and mouse movements with this class.

## USBMouseKeyboard class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_mouse_keyboard.html)

## USBMouseKeyboard example

```C++ TODO
//Dual mouse/keyboard device example
//Example will "type" ASCII characters to the screen, move the mouse around in a circle, and assert various media and modifier keys
#include "mbed.h"
#include "USBMouseKeyboard.h"

//LED1: NUM_LOCK
//LED2: CAPS_LOCK
//LED3: SCROLL_LOCK
BusOut leds(LED1, LED2, LED3);

//USBMouseKeyboard object
USBMouseKeyboard key_mouse; 

int main(void) {
    int16_t x = 0;
    int16_t y = 0;
    int32_t radius = 70;
    int32_t angle = 0;
    while (1) {
        //moves the coordinates of the mouse around in a circle
        x = cos((double)angle*3.14/50.0)*radius;
        y = sin((double)angle*3.14/50.0)*radius;
        //example of a media key press
        key_mouse.media_control(KEY_VOLUME_DOWN);
        //example of simple keyboard output
        key_mouse.printf("Hello World from Mbed\r\n");
        //function to move the mouse to coordinates "x, y"
        key_mouse.move(x, y);
        //example of modifier key press
        key_mouse.key_code(KEY_CAPS_LOCK);
        leds = key_mouse.lock_status();
        wait(0.05);
        key_mouse.media_control(KEY_VOLUME_UP);
        key_mouse.key_code(KEY_NUM_LOCK);
        leds = key_mouse.lock_status();
        wait(0.05);
        angle += 10;
        key_mouse.key_code(KEY_SCROLL_LOCK);
        leds = key_mouse.lock_status();
        wait(0.05);
    }
}

```

## Related content

- [USBMouse](../apis/usbmouse.html).
- [USBKeyboard](../apis/usbkeyboard.html).
