# I2CSlave

Use I2C Slave to communicate with I2C Master.

Synchronization level: not protected.

## I2CSlave class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_i2_c_slave.html)

## I2CSlave example

Try this example to see how an I2C responder works.

```c++ TODO
#include <mbed.h>

#if !DEVICE_I2CSLAVE
  #error [NOT_SUPPORTED] I2C Slave is not supported
#endif

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
