# USBMIDI

<span class="images">![](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_m_i_d_i.png)<span>USBMIDI class hierarchy</span></span>

You can use the USBMIDI interface to send and receive MIDI messages over USB using the standard USB-MIDI protocol.

Examples of tasks you can perform using this library include sending MIDI messages to a computer (such as to record in a sequencer, or trigger a software synthesiser) and receiving messages from a computer (such as actuating things based on MIDI events).

## USBMIDI class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/class_u_s_b_m_i_d_i.html)

The two examples below use a program called "Anvil Studio 32-bit" to play MIDI notes from an Mbed board through the host PC. You can play back the MIDI notes through headphones or speakers by following the steps below:

1. Flash the board, and ensure the target's USB is plugged into the PC.
2. Open Anvil Studio.
3. Click **View > Synthesizers, MIDI + Audio Devices**.
4. Uncheck **Synth is too slow to echo incoming events**.
5. Click **View > Composer (Staff Editor)** to see notes from the board being mapped to the sheet music.

## USBMIDI example  

Below is an example to send a series of MIDI notes to the host PC:    

```C++ TODO
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

## Play "Take Me Out to the Ball Game" example

You can use USBMIDI to play an entire song, not just a series of notes. "Take Me Out to the Ball Game" is a popular song in the public domain. To play "Take Me Out to the Ball Game" (public domain) using MIDI over USB on the host PC:

```C++ TODO
#include "mbed.h"
#include "USBMIDI.h"

#define REST -1
#define C  0
#define Cs 1
#define D  2
#define Ds 3
#define E  4
#define F  5
#define Fs 6
#define G  7
#define Gs 8
#define A  9
#define As 10
#define B  11

#define OCTAVE0  0
#define OCTAVE1  12
#define OCTAVE2  24
#define OCTAVE3  36
#define OCTAVE4  48
#define OCTAVE5  60
#define OCTAVE6  72
#define OCTAVE7  84

#define WHOLE_NOTE     1.15
#define HALF_NOTE      (WHOLE_NOTE / 2)
#define QUARTER_NOTE   (WHOLE_NOTE / 4)
#define EIGHTH_NOTE    (WHOLE_NOTE / 8)
#define SIXTEENTH_NOTE (WHOLE_NOTE / 16)

#define THREE_EIGHTHS_NOTE   (EIGHTH_NOTE * 3)
#define THREE_FORTHS_NOTE   (QUARTER_NOTE * 3)

USBMIDI midi;

void PlayNote(int note, int octave, float duration){
    if(note == REST){
        wait(duration);
    }
    else{
        midi.write(MIDIMessage::NoteOn(note + octave));
        wait(duration);
        midi.write(MIDIMessage::NoteOff(note + octave));
    }    
}

void TakeMeOutToTheBallGame(){
    //https://www.bethsnotesplus.com/2012/09/take-me-out-to-ball-game.html
    PlayNote(C, OCTAVE5, HALF_NOTE);
    PlayNote(C, OCTAVE6, QUARTER_NOTE);
    
    PlayNote(A, OCTAVE5, QUARTER_NOTE);
    PlayNote(G, OCTAVE5, QUARTER_NOTE);
    PlayNote(E, OCTAVE5, QUARTER_NOTE);
    
    PlayNote(G, OCTAVE5, THREE_FORTHS_NOTE);
    
    PlayNote(D, OCTAVE5, THREE_FORTHS_NOTE);
    
    PlayNote(C, OCTAVE5, HALF_NOTE);
    PlayNote(C, OCTAVE6, QUARTER_NOTE);
    
    PlayNote(A, OCTAVE5, QUARTER_NOTE);
    PlayNote(G, OCTAVE5, QUARTER_NOTE);
    PlayNote(E, OCTAVE5, QUARTER_NOTE);
    
    PlayNote(G, OCTAVE5, THREE_FORTHS_NOTE);
    
    PlayNote(G, OCTAVE5, HALF_NOTE);
    PlayNote(REST, 0, QUARTER_NOTE);
    
    PlayNote(A, OCTAVE5, QUARTER_NOTE);
    PlayNote(Gs, OCTAVE5, QUARTER_NOTE);
    PlayNote(A, OCTAVE5, QUARTER_NOTE);
    
    PlayNote(E, OCTAVE5, QUARTER_NOTE);
    PlayNote(F, OCTAVE5, QUARTER_NOTE);
    PlayNote(G, OCTAVE5, QUARTER_NOTE);
    
    PlayNote(A, OCTAVE5, HALF_NOTE);
    PlayNote(F, OCTAVE5, QUARTER_NOTE);
    
    PlayNote(D, OCTAVE5, THREE_FORTHS_NOTE);
    
    PlayNote(A, OCTAVE5, HALF_NOTE);
    PlayNote(A, OCTAVE5, QUARTER_NOTE);
    
    PlayNote(A, OCTAVE5, QUARTER_NOTE);
    PlayNote(B, OCTAVE5, QUARTER_NOTE);
    PlayNote(C, OCTAVE6, QUARTER_NOTE);
    
    PlayNote(D, OCTAVE6, QUARTER_NOTE);
    PlayNote(B, OCTAVE5, QUARTER_NOTE);
    PlayNote(A, OCTAVE5, QUARTER_NOTE);
    
    PlayNote(G, OCTAVE5, QUARTER_NOTE);
    PlayNote(E, OCTAVE5, QUARTER_NOTE);
    PlayNote(D, OCTAVE5, QUARTER_NOTE);
    
    PlayNote(C, OCTAVE5, HALF_NOTE);
    PlayNote(C, OCTAVE6, QUARTER_NOTE);
    
    PlayNote(A, OCTAVE5, QUARTER_NOTE);
    PlayNote(G, OCTAVE5, QUARTER_NOTE);
    PlayNote(E, OCTAVE5, QUARTER_NOTE);
    
    PlayNote(G, OCTAVE5, THREE_FORTHS_NOTE);
    
    PlayNote(D, OCTAVE5, HALF_NOTE);
    PlayNote(D, OCTAVE5, QUARTER_NOTE);
    
    PlayNote(C, OCTAVE5, HALF_NOTE);
    PlayNote(D, OCTAVE5, QUARTER_NOTE);
    
    PlayNote(E, OCTAVE5, QUARTER_NOTE);
    PlayNote(F, OCTAVE5, QUARTER_NOTE);
    PlayNote(G, OCTAVE5, QUARTER_NOTE);
    
    PlayNote(A, OCTAVE5, THREE_FORTHS_NOTE);
    
    PlayNote(A, OCTAVE5, QUARTER_NOTE);
    PlayNote(A, OCTAVE5, QUARTER_NOTE);
    PlayNote(B, OCTAVE5, QUARTER_NOTE);
    
    PlayNote(C, OCTAVE6, THREE_FORTHS_NOTE);
    
    PlayNote(C, OCTAVE6, THREE_FORTHS_NOTE);
    
    PlayNote(C, OCTAVE6, QUARTER_NOTE);
    PlayNote(B, OCTAVE5, QUARTER_NOTE);
    PlayNote(A, OCTAVE5, QUARTER_NOTE);
    
    PlayNote(G, OCTAVE5, QUARTER_NOTE);
    PlayNote(Fs, OCTAVE5, QUARTER_NOTE);
    PlayNote(G, OCTAVE5, QUARTER_NOTE);
    
    PlayNote(A, OCTAVE5, THREE_FORTHS_NOTE);
    
    PlayNote(B, OCTAVE5, THREE_FORTHS_NOTE);
    
    PlayNote(C, OCTAVE6, THREE_FORTHS_NOTE);
    
    PlayNote(C, OCTAVE6, HALF_NOTE);
    PlayNote(REST, 0, QUARTER_NOTE);
}

int main() {
    while (1) {    
        TakeMeOutToTheBallGame();
    }
}

```
