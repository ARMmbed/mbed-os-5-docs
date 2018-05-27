## USBKeyboard

The USBKeyboard class provides the functionality of a keyboard. You can send key presses, check the status of control keys and send a key press sequences though a stream interface. If you need mouse or keyboard and mouse functionality see the classes [USBMouse](USBMouse.md) and [USBMouseKeyboard](USBMouseKeyboard.md).

### USBKeyboard class reference

TODO

### USBKeyboard example

```C++
#include "mbed.h"
#include "USBKeyboard.h"

USBKeyboard key;

int main(void)
{
  while (1) {
      key.printf("Hello World\r\n");
      wait(1);
  }
}
```

### Related content

- [USBMouse](USBMouse.md)
- [USBMouseKeyboard](USBMouseKeyboard.md)
