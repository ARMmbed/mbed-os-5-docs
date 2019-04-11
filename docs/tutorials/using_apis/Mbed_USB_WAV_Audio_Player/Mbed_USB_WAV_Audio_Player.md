# Mbed USB WAV audio player

This tutorial explains how to put together a USB WAV audio player with Mbed. You will load a WAV file onto an SD card connected to an Mbed board. You can then play the WAV file from the board on a host computer over USB. Once connected, the Mbed board acts as a USB microphone. The sound that the microphone is "recording" is actually sound data read from the SD card and sent to the host computer. This allows the sound to be played on speakers or headphones or recorded with a program, such as Audacity.

## Libraries

This tutorial uses several Mbed libraries:

- USB (part of Mbed OS).
- [sd-driver](https://github.com/ARMmbed/sd-driver) (external library).
- [AudioPlayer](https://github.com/c1728p9/AudioPlayer) (external library).

This tutorial uses the USBAudio class of the USB library to send audio data from the Mbed board to the host PC. It uses the SDBlockDevice and FATFileSystem classes of the `sd-driver` library, so you can store the WAV files on an SD card and the Mbed board can access them. Lastly, it uses the AudioPlayer and WaveAudioStream classes of the AudioPlayer library to access the audio data from the WAV file on the SD card.

## What you need

- Mbed Enabled board.
- SD card.
- SD card shield (if board does not already have an SD card port).
- USB cable.

## Setup

The following steps demonstrate the setup and use of the Mbed WAV audio player:

1. Create a new Mbed project:
   
   `mbed new <project name>`
   
1. Add the [sd-driver](https://github.com/ARMmbed/sd-driver) and [AudioPlayer](https://github.com/c1728p9/AudioPlayer) libraries into the new Mbed project directory: 
   
   `mbed add https://github.com/ARMmbed/sd-driver`    
   `mbed add https://github.com/c1728p9/AudioPlayer`
   
1. Copy and paste the below example code into `main.cpp`.
1. Make sure the SPI pins for the SDBlockDevice object are updated and correct for your board. For example, in the example below, line 10 sets up SPI for the SDBlockDevice for the NXP K64F Mbed board.
1. Load WAV file(s) onto SD card. The example below uses a public domain WAV file called "Bach-minuet-in-g.wav" (attached below for download) that is inside a "songs" directory on the SD card. It is important that the WAV file be PCM signed 16-bit little endian, or else it will not play becaues USBAudio does not support any other WAV formats. The WAV file can have any sampling rate and can have any number of channels. You can use [Online-convert](https://audio.online-convert.com/convert-to-wav) to achieve WAV files with different formats from any source audio file. The file "Bach-minuet-in-g.wav" is already in the correct format.
   
   ![Convert audio to WAV](https://raw.githubusercontent.com/ARMmbed/mbed-os-5-docs/development/docs/images/Mbed_USB_WAV_Audio_Player_img1.png)
   
1. Compile the program and flash the binary.
1. Ensuring that the target's USB is connected to the host computer, select `Mbed Audio` as the host PC's default audio input device. On Windows, in Control Panel, set `View by` to `Category` in the top right corner. Then, navigate to `Hardware` and `Sound` > `Sound`, and in the recording tab, right click on `Microphone Mbed Audio` > `Properties` > `Listen`. Check the `Listen to this Device` box, and click `Apply`. The audio from the WAV file is now audible through whichever output device is selected for the host PC's audio output. If `View by` is not set to `Category`, audio will be under Sound in Control Panel:
   
   ![Sound](https://raw.githubusercontent.com/ARMmbed/mbed-os-5-docs/development/docs/images/Mbed_USB_WAV_Audio_Player_img2.PNG)
   
   ![Microphone properties](https://raw.githubusercontent.com/ARMmbed/mbed-os-5-docs/development/docs/images/Mbed_USB_WAV_Audio_Player_img3.PNG)
   
1. See [Troubleshooting](#troubleshooting) if issues persist.
 
## main.cpp

```c++ NOCI
// Mbed WAV Audio Player
#include "mbed.h"
#include "USBAudio.h"
#include "SDBlockDevice.h"
#include "FATFileSystem.h"
#include "AudioPlayer.h"
#include "WaveAudioStream.h"

// Connection for SD card
SDBlockDevice sd(PTE3, PTE1, PTE2, PTE4);//MOSI, MISO, SCLK, CS
FATFileSystem fs("sd", &sd);

int main() {
    // Set the maximum speed so it can keep up with audio
    sd.frequency(25000000);
    // Load WAV file from SD card
    // WAV file must be PCM signed 16-bit little endian
    File file;
    if (file.open(&fs, "songs/Bach-minuet-in-g.wav") != 0) {
        error("Could not open 'songs/Bach-minuet-in-g.wav'\r\n");
    }
    WaveAudioStream song(&file);//"song" is the audio data object
    // Check to see if file is a valid WAV file
    if(song.get_valid() == 0){
        error("ERROR: not valid WAV file\r\n");
    }
    // WAV file must be 16-bit
    if(song.get_bytes_per_sample() != 2){
        error("ERROR: WAV file not 2 bytes per sample (16-bit)\r\n");
    }
    USBAudio audio(true, 8000, song.get_channels(), song.get_sample_rate(), song.get_channels());
    uint8_t buffer[1500];
    int num_bytes_read;
    printf("Playing Audio\r\n");
    // Reads and plays data from WAV file over USB until song is over
    while(1){
        num_bytes_read = song.read(buffer, 1500);
        if(num_bytes_read == -1){
            printf("Song Over\r\n");
            break;
        }
        audio.write(buffer, num_bytes_read);
    }
    song.close();//Close the WAV file
}
```

## Example WAV file  

[Bach-minuet-in-g.wav](https://github.com/mrcoulter45/mbed-os-5-docs/raw/Mbed_USB_WAV_Audio_Player_Tutorial/docs/tutorials/using_apis/Mbed_USB_WAV_Audio_Player/Bach-minuet-in-g.wav)

## Troubleshooting   

If USB properties of the Mbed USB WAV Audio Player are altered, such as the sample rate or number of channels, the Mbed board will need to be deleted and re-installed in the host PC's installed device list. In Device Manager, click View > Devices by Connection. Find "Mbed Audio" and uninstall the device. Reset the board and repeat Setup step 6. If problems still persist, be sure to format the WAV file correctly, as is denoted in Setup step 4.   

![Device manager](https://raw.githubusercontent.com/ARMmbed/mbed-os-5-docs/development/docs/images/Mbed_USB_WAV_Audio_Player_img4.png)
