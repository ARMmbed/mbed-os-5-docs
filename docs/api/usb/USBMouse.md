# USBMouse

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_mouse.png)<span>USBMouse class hierarchy</span></span>

You can use the USBMouse interface to emulate a mouse over the USB port. You can choose relative or absolute coordinates and send clicks, button state and scroll wheel movements. If you need keyboard or keyboard and mouse functionality, please see the [USBKeyboard](../apis/usbkeyboard.html) and [USBMouseKeyboard](../apis/usbmousekeyboard.html) classes.

## USBMouse class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_mouse.html)

## USBMouse example

```C++ TODO
#include "mbed.h"
#include "USBMouse.h"

//create mouse object
USBMouse mouse;

int main() {
    int16_t x = 0;
    int16_t y = 0;
    int32_t radius = 10;
    int32_t angle = 0;

    while (1) {
        //will cause mouse to move in a circle
        x = cos((double)angle*3.14/180.0)*radius;
        y = sin((double)angle*3.14/180.0)*radius;

        //will move mouse x, y away from its previous position on the screen
        mouse.move(x, y);
        angle += 3;
        wait(0.001);
    }
}
```

You can choose either a relative mouse or an absolute mouse. With a relative mouse, the USBMouse move function will move the mouse x, y pixels away from its previous position on the screen. For an absolute mouse, the USBMouse move function will move the mouse to coordinates x, y on the screen. By default, a USBMouse is a relative mouse. For example, you can use an absolute mouse to draw a circle:

```C++ TODO
#include "mbed.h"
#include "USBMouse.h"

//setup mouse to be absolute
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

      //x_screen, y_screen will be the mouse's position on the screen
      mouse.move(x_screen, y_screen);
      angle += 3;
      wait(0.01);
  }
}
```

## USBMouse Joystick example  

This example uses a Grove - Thumb Joystick to act as a mouse. Use the joystick to move the mouse around the screen and click the joystick down to do a mouse left click.

```C++ TODO
//Grove - Thumb Joystick mouse
//Constructor is blocking, so main will not run if the target's USB is not connected
#include "mbed.h"
#include "USBMouse.h"

USBMouse mouse;
// x and y axis of the joystick
AnalogIn   ainx(A0);
AnalogIn   ainy(A1);
int16_t a_inx;
int16_t a_iny;

int main() {
    int16_t x = 0;
    int16_t y = 0;

    while (1) {
        // reads x and y values from the joystick
        a_inx = (int16_t)(ainy.read() * 100.0);
        a_iny = (int16_t)(ainx.read() * 100.0);

        // prints x and y values to serial monitor
        printf("X: %u\r\n", a_inx);
        printf("Y: %u\r\n", a_iny);

        // move position of mouse right
        if(a_inx > 52){
            x = (x - (50 - a_inx)) / 3;
        }
        // move position of mouse left
        else if(a_inx < 47){
            x = (a_inx - 50) / 2;
        }
        // keeps mouse stationary in x-axis
        else{
            x = 0;
        }
        // move position of mouse down
        if(a_iny > 52 && a_iny != 99){
            y = (y - (50 - a_iny)) / 3;
        }
        // move position of mouse up
        else if(a_iny < 47){
            y = (a_iny - 50) / 2;
        }
        // keeps mouse stationary in y-axis
        else{
            y = 0;
        }
        // if button is pressed, a_iny will be 99
        // performs mouse left click
        if(a_iny == 99){
            //click
            mouse.click(MOUSE_LEFT);
            wait(0.4);
        }
        // moves mouse to specified x, y coordinates on screen
        mouse.move(x, y);
        wait(0.001);
    }
}

```

## Related content

- [USBKeyboard](../apis/usbkeyboard.html).
- [USBMouseKeyboard](../apis/usbmousekeyboard.html).
