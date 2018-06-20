## USBMouse

<span class="images">![](https://os.mbed.com/docs/v5.9/feature-hal-spec-usb-device-doxy/class_u_s_b_mouse.png)<span>USBMouse class hierarchy</span></span>

You can use the USBMouse interface to emulate a mouse over the USB port. You can choose relative or absolute coordinates and send clicks, button state and scroll wheel movements. If you need keyboard or keyboard and mouse functionality, please see the [USBKeyboard](USBKeyboard.html) and [USBMouseKeyboard](USBMouseKeyboard.html) classes.

### USBMouse class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.9/feature-hal-spec-usb-device-doxy/class_u_s_b_mouse.html)

### USBMouse example

```C++
#include "mbed.h"
#include "USBMouse.h"

USBMouse mouse;

int main() {
    int16_t x = 0;
    int16_t y = 0;
    int32_t radius = 10;
    int32_t angle = 0;

    while (1) {
        x = cos((double)angle*3.14/180.0)*radius;
        y = sin((double)angle*3.14/180.0)*radius;

        mouse.move(x, y);
        angle += 3;
        wait(0.001);
    }
}
```

You can choose either a relative mouse or an absolute mouse. By default, a USBMouse is a relative mouse. For example, you can use an absolute mouse to draw a circle:

```C++
#include "mbed.h"
#include "USBMouse.h"

USBMouse mouse(true, ABS_MOUSE);

#include <math.h>

int main(void)
{
  uint16_t x_center = (X_MAX_ABS - X_MIN_ABS)/2;
  uint16_t y_center = (Y_MAX_ABS - Y_MIN_ABS)/2;
  uint16_t x_screen = 0;
  uint16_t y_screen = 0;

  uint32_t x_origin = x_center;
  uint32_t y_origin = y_center;
  uint32_t radius = 5000;
  uint32_t angle = 0;
  printf("Booted\r\n");

  while (1)
  {
      x_screen = x_origin + cos((double)angle*3.14/180.0)*radius;
      y_screen = y_origin + sin((double)angle*3.14/180.0)*radius;

      mouse.move(x_screen, y_screen);
      angle += 3;
      wait(0.01);
  }
}
```

### Related content

- [USBMouse](USBMouse.html).
- [USBMouseKeyboard](USBMouseKeyboard.html).
