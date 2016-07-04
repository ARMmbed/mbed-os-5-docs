# USBMouse

<span class="images">[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/1lSjP6E7RV4/0.jpg)](http://www.youtube.com/watch?v=1lSjP6E7RV4)</span>

The USBMouse interface is used to emulate a mouse over the USB port. You can choose relative or absolute co-ordinates, and send clicks, button state and scroll wheel movements.

The USB connector should be attached to 

* **p31 (D+), p32 (D-) and GND** for the **LPC1768 and the LPC11U24**
* The on-board USB connector of the **FRDM-KL25Z**

## Hello World

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/samux/code/USBMouse_HelloWorld/)](https://developer.mbed.org/users/samux/code/USBMouse_HelloWorld/file/tip/main.cpp) 

## API

[![View code](https://www.mbed.com/embed/?url=<http://mbed.org/users/mbed_official/code/USBDevice/)](http://mbed.org/users/mbed_official/code/USBDevice/file/6d85e04fb59f/main.cpp>) 

## Details

You can choose either a relative mouse or an absolute mouse. By default, a USBMouse is a relative mouse. For instance, you can use an absolute mouse to draw a circle:

```
 #include "mbed.h"
 #include "USBMouse.h"

 USBMouse mouse(ABS_MOUSE);

 #include 

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
