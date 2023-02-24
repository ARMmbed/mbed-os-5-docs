# USBMIDI

<span class="images">![](https://os.mbed.com/docs/mbed-os/v6.16/mbed-os-api-doxy/class_u_s_b_m_i_d_i.png)<span>USBMIDI class hierarchy</span></span>

You can use the USBMIDI interface to send and receive MIDI messages over USB using the standard USB-MIDI protocol.

Examples of tasks you can perform using this library include sending MIDI messages to a computer (such as to record in a sequencer, or trigger a software synthesiser) and receiving messages from a computer (such as actuating things based on MIDI events).

## USBMIDI class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.16/mbed-os-api-doxy/class_u_s_b_m_i_d_i.html)

The two examples below use a program called "Anvil Studio 32-bit" to play MIDI notes from an Mbed board through the host PC. You can play back the MIDI notes through headphones or speakers by following the steps below:

1. Flash the board, and ensure the target's USB is plugged into the PC.
2. Open Anvil Studio.
3. Click **View > Synthesizers, MIDI + Audio Devices**.
4. Uncheck **Synth is too slow to echo incoming events**.
5. Click **View > Composer (Staff Editor)** to see notes from the board being mapped to the sheet music.

## USBMIDI example  

Below is an example to send a series of MIDI notes to the host PC:    

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-USBMIDI/tree/v6.7)](https://github.com/ARMmbed/mbed-os-snippet-USBMIDI/blob/v6.7/main.cpp)

## Play "Take Me Out to the Ball Game" example

You can use USBMIDI to play an entire song, not just a series of notes. "Take Me Out to the Ball Game" is a popular song in the public domain. To play "Take Me Out to the Ball Game" (public domain) using MIDI over USB on the host PC:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-USBMIDI_Take_Me_Out/tree/v6.7)](https://github.com/ARMmbed/mbed-os-snippet-USBMIDI_Take_Me_Out/blob/v6.7/main.cpp)
