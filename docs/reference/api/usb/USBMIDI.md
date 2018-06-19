## USBMIDI

<span class="images">![](https://os.mbed.com/docs/v5.9/feature-hal-spec-usb-device-doxy/class_u_s_b_m_i_d_i.png)<span>USBMIDI class hierarchy</span></span>

The USBMIDI interface can be used to send and receive MIDI messages over USB using the standard USB-MIDI protocol.

Using this library, you can do things like send MIDI messages to a computer (such as to record in a sequencer, or trigger a software synthesiser) and receive messages from a computer (such as actuate things based on MIDI events)

### USBMIDI class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/v5.9/feature-hal-spec-usb-device-doxy/class_u_s_b_m_i_d_i.html)

### USBMIDI example

```C++
#include "mbed.h"
#include "USBMIDI.h"

USBMIDI midi;

int main() {             
    while (1) {    
        for(int i=48; i<83; i++) {     // send some messages!
            midi.write(MIDIMessage::NoteOn(i));
            wait(0.25);
            midi.write(MIDIMessage::NoteOff(i));
            wait(0.5);
        }
    }
}
```
