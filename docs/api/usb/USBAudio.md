# USBAudio

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_audio.png)<span>USBAudio class hierarchy</span></span>

You can use the USBAudio interface to send and receive audio data over USB. Once a USB program is loaded onto the Mbed board, you can send audio data to your PC by selecting **Mbed Audio** as your PC's microphone input. Your Mbed Enabled board can receive audio data from your PC if you select **Mbed Audio** as your PC's speaker output.

## USBAudio class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_audio.html)

## USBAudio square wave example

This example outputs an audio square wave over USB.

```C++ TODO
// This example simply generates a square wave. 
// Use a program like Audacity to record and hear the square wave, or route microphone input to output device.
#include "mbed.h"
#include "USBAudio.h"
#include <math.h>

int16_t square_wave(uint32_t freq_hz, uint16_t amplitude, float time_s)
{
    float period = (float)1 / freq_hz;
    if (fmod(time_s, period) > period / 2) {
        return amplitude / 2;
    } else {
        return -(amplitude / 2);
    }
}

int main() {
    uint32_t tx_freq = 16000;
    USBAudio audio(true, 8000, 2, tx_freq, 1, 10, 0x7bb8, 0x1112, 0x0100);
    float cur_time = 0;
    while (true) {
        uint16_t samples[64];
        for (int i = 0; i < 64; i++) {
            samples[i] = square_wave(100, 5000, cur_time);
            cur_time += 1.0 / tx_freq;
        }
        if (!audio.write((uint8_t *)&samples, sizeof(samples))) {
            audio.write_wait_ready();
        }
    }
}

```

## USBAudio loopback example

This example loops input audio to the Mbed board back to the host PC, so that you may record the audio or listen to it through headphones or speakers.

```C++ TODO
// Audio loopback example use:
// 1. Select "Mbed Audio" as your PC's default speaker and microphone devices.
// 2. Play some sound (YouTube, audio file, etc.) on your PC with Mbed board connected to your PC via the target's USB.
// 3. Record using a program such as Audacity with the Mbed board connected and with the audio on your PC playing.
// 4. The audio that is playing on your PC will be recorded by Audacity via USB loopback.
#include "mbed.h"
#include "USBAudio.h"

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

## USBAudio play sound data example

This example loads raw audio data to your board's flash. That data then plays on the host PC over USB. We have tested this example with the NXP FRDM-K64F, which has 1 MB of flash memory. If you are using a board that has less than 1 MB of flash memory, delete data from the end of the `data` array, and set `NUM_ELEMENTS` accordingly until the program size is small enough to flash without exceeding storage. Follow the link below, and click Ctrl + s to save the raw code view for `main.cpp`.   

#### [main.cpp](https://raw.githubusercontent.com/mrcoulter45/mbed-os-5-docs/USBAudio.md_additions/docs/reference/api/usb/Audio_Play_Sound_Data.cpp)
