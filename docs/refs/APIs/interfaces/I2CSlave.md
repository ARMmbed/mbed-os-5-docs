### I2CSlave

Use I2C Slave to communicate with I2C Master.

Synchronization level: not protected.

#### API

[![View code](https://www.mbed.com/embed/?type=library)](https://docs.mbed.com/docs/mbed-os-api/en/mbed-os-5.5/api/I2CSlave_8h_source.html)

#### Example

Try this example to see how an I2C responder works.

```c++
#include <mbed.h>

I2CSlave slave(p9, p10);

int main() {
   char buf[10];
   char msg[] = "Slave!";

   slave.address(0xA0);
   while (1) {
       int i = slave.receive();
       switch (i) {
           case I2CSlave::ReadAddressed:
               slave.write(msg, strlen(msg) + 1); // Includes null char
               break;
           case I2CSlave::WriteGeneral:
               slave.read(buf, 10);
               printf("Read G: %s\n", buf);
               break;
           case I2CSlave::WriteAddressed:
               slave.read(buf, 10);
               printf("Read A: %s\n", buf);
               break;
       }
       for(int i = 0; i < 10; i++) buf[i] = 0;    // Clear buffer
   }
}
```
