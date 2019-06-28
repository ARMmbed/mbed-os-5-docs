# USBAudio

<span class="images">![](https://os.mbed.com/docs/v5.10/feature-hal-spec-usb-device-doxy/class_u_s_b_audio.png)<span>USBAudio class hierarchy</span></span>

You can use the USBAudio interface to send and receive audio across USB. By selecting a USBAudio device as your PC's speaker output, you can send audio data. You can also use it as your PC's microphone and receive sound sent by USBAudio.

## USBAudio class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os.mbed.com/docs/v5.10/feature-hal-spec-usb-device-doxy/class_u_s_b_audio.html)

## USBAudio example

```C++
#include "mbed.h"
#include "USBAudio.h"

// Audio loopback example use:
// 1. Select "Mbed Audio" as your sound device
// 2. Play a song or audio file
// 3. Record the output using a program such as Audacity

int main() {

    USBAudio audio(true, 44100, 2, 44100, 2);

    printf("Looping audio\r\n");
    static uint8_t buf[128];
    while (true) {
        if (!audio.read(buf, sizeof(buf))) {
            memset(buf, 0, sizeof(buf));
        }
        audio.write(buf, sizeof(buf));
    }
}
```
