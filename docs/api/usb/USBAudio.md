# USBAudio

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_audio.png)<span>USBAudio class hierarchy</span></span>

You can use the USBAudio interface to send and receive audio data over USB. Once a USB program is loaded onto the Mbed board, you can send audio data to your PC by selecting **Mbed Audio** as your PC's microphone input. Your Mbed Enabled board can receive audio data from your PC if you select **Mbed Audio** as your PC's speaker output.

## USBAudio class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_audio.html)

## USBAudio square wave example

This example outputs an audio square wave over USB.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_USB/USBAudio_square_wave)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_USB/USBAudio_square_wave/main.cpp)

## USBAudio loopback example

This example loops input audio to the Mbed board back to the host PC, so that you may record the audio or listen to it through headphones or speakers.

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_USB/USBAudio_loopback_example)](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_USB/USBAudio_loopback_example/main.cpp)

## USBAudio play sound data example

This example loads raw audio data to your board's flash. That data then plays on the host PC over USB. We have tested this example with the NXP FRDM-K64F, which has 1 MB of flash memory. If you are using a board that has less than 1 MB of flash memory, delete data from the end of the `data` array, and set `NUM_ELEMENTS` accordingly until the program size is small enough to flash without exceeding storage. Follow the link below, and click Ctrl + s to save the raw code view for `main.cpp`.   

#### [main.cpp](https://github.com/ARMmbed/mbed-os-examples-docs_only/blob/master/APIs_USB/USBAudio_play_sound/main.cpp)
