# SPISlave

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_s_p_i_slave.png)<span>SPISlave class hierarchy</span></span>

Use the SPISlave class to communicate with a SPI master device.

The default format is set to 8 bits, mode 0 and a clock frequency of 1MHz. Synchronization level: not protected.

## SPISlave class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/classmbed_1_1_s_p_i_slave.html)

## SPISlave example

Reply to a SPI master as slave:

```c++
#include "mbed.h"

SPISlave device(D9, D11, D12, D13); // mosi, miso, sclk, ssel

int main() {
   device.reply(0x00);              // Prime SPI with first reply
   while(1) {
       if(device.receive()) {
           int v = device.read();   // Read byte from master
           v = (v + 1) % 0x100;     // Add one to it, modulo 256
           device.reply(v);         // Make this the next reply
       }
   }
}
```
