# Overview
<!--https://github.com/COTASPAR/K66F/blob/master/README.md-->
As an IoT developer, you might think of machine learning as a server-side technology. In the traditional view, sensors on your device capture data and send it to the cloud, where Machine Learning (ML) models on hefty machines make sense of it. A network connection is obligatory, and you are going to expect some latency, not to mention hosting costs.

But more and more, developers want to deploy their ML models to the edge, on IoT devices themselves. If you bring ML closer to your sensors, you remove your reliance on a network connection, and you can achieve much lower latency without a round trip to the server.

This is especially exciting for IoT, because less network utilization means lower power consumption. Also, you can better guarantee the security and privacy of your users, since you do not need to send data back to the cloud unless you know for sure that it is relevant.

In the following guide, you will learn how you can perform machine learning inference on an Arm Cortex-M microcontroller with TensorFlow Lite for Microcontrollers.

**About TensorFlow Lite**

TensorFlow Lite is a set of tools for running machine learning models on-device. TensorFlow Lite powers billions of mobile app installs, including Google Photos, Gmail, and devices made by Nest and Google Home.

With the launch of TensorFlow Lite for Microcontrollers, developers can run machine learning inference on extremely low-powered devices, like the Cortex-M microcontroller series. Watch the video to learn more about the announcement:

[![An introduction to TensorFlow Lite](http://img.youtube.com/vi/DKosV_-4pdQ/0.jpg)](http://www.youtube.com/watch?v=DKosV_-4pdQ)


## Before you begin

Here is what you will need to complete the guide:

* Computer that supports Mbed CLI (version 1.10.4)

* NXP FRDM K66F

* Mini-USB cable

* Python 2.7. Using pyenv is recommended to manage python versions.

For Windows users, install Ubuntu 20.04 LTS in a VirtualBox. Refer to the following videos to set up:

**How to install VirtalBox 6.0.10 on Windows 10**

![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/8mns5yqMfZk/0.jpg)

[Watch here](http://www.youtube.com/watch?v=8mns5yqMfZk)

**How to install Ubuntu 20.04 on VirtualBox in Windows 10**

![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/x5MhydijWmc/0.jpg)

[Watch here](http://www.youtube.com/watch?v=x5MhydijWmc)

## Getting Started

TensorFlow Lite for Microcontrollers supports several devices out of the box, and is relatively easy to extend to new devices. For this guide, we will focus on the **NXP FRDM K66F**.

![IMAGE ALT TEXT HERE](https://raw.githubusercontent.com/COTASPAR/K66F/master/images/nxp_k66f_board.jpeg)


We will deploy a sample application that uses the microphone on the K66F and a TensorFlow machine learning model to detect the words “yes” and “no”.

To do this, we will show you how to complete the following steps:

1.  Download and build the sample application


2.  Deploy the sample to your K66F


3.  Use new trained models to recognize different words

### Download and build the sample application

**Install Arm toolchain and Mbed CLI**
-   Download [Arm cross compilation](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads) toolchain. Select the correct toolchain for the OS that your computer is running. For Windows users, if you have already set up the Linux virtual environment, install the toolchain there.

-   To build and deploy the application, we will use the [Mbed CLI](https://github.com/ARMmbed/mbed-cli). We recommend that you install Mbed CLI with our installer. If you need more customization, you can perform a manual install. Although this is not recommended.  

    If you do not already have Mbed CLI installed, download the installer:  

    [Mac installer](https://github.com/ARMmbed/mbed-cli-osx-installer/releases/tag/v0.0.10)
-   After Mbed CLI is installed, tell Mbed where to find the Arm embedded toolchain.  
  ```    
 mbed config -G GCC_ARM_PATH <path_to_your_arm_toolchain>/bin
 ```

**Important:** We recommend running the following commands from inside the Mbed CLI terminal that gets launched with the Mbed CLI Application. This is because it will be much quicker to set up, because it resolves all your environment dependencies automatically.


### Build and compile micro speech example

Navigate to the directory where you keep code projects. Run the following command to download TensorFlow Lite source code.

```
git clone https://github.com/tensorflow/tensorflow.git
```

While you wait for the project to download, let’s explore the project files on [GitHub](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/micro/examples/micro_speech) and learn how this TensorFlow Lite for Microcontrollers example works.

The code samples audio from the microphone on the K66F. The audio is run through a Fast Fourier transform to create a spectrogram. The spectrogram is then fed into a pre-trained machine learning model. The model uses a [convolutional neural network](https://developers.google.com/machine-learning/practica/image-classification/convolutional-neural-networks) to identify whether the sample represents either the command “yes” or “no”, silence, or an unknown input. We will explore how this works in more detail later in the guide.

Here are descriptions of some interesting source files:

-   nxp_k66f[/audio_provider.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/nxp_k66f/audio_provider.cc) captures audio from the microphone on the device.

-   [micro_features/micro_features_generator.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/micro_features/micro_features_generator.cc): uses a Fast Fourier transform to create a spectrogram from audio.

-   [micro_features/model.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/micro_features/model.cc). This file is the machine learning model itself, represented by a large array of unsigned char values.

-   [command_responder.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/command_responder.cc) is called every time a potential command has been identified.

-   [main.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/main.cc). This file is the entry point for the Mbed program, which runs the machine learning model using TensorFlow Lite for Microcontrollers.


After the project has downloaded, you can run the following commands to navigate into the project directory and build it:

```
cd tensorflow
```


```
make -f tensorflow/lite/micro/tools/make/Makefile TARGET=mbed TAGS="nxp_k66f" generate_micro_speech_mbed_project
```

This will create a folder in ```tensorflow/lite/micro/tools/make/gen/mbed_cortex-m4/prj/micro_speech/mbed```  that contains the source and header files, Mbed driver files, and a README.

```
cd tensorflow/lite/micro/tools/make/gen/mbed_cortex-m4/prj/micro_speech/mbed
```

  Execute the following while remembering to use Python 2.7 (you can do this by using a virtual environment with pip):

```
mbed config root .

mbed deploy

mbed compile -m K66F -t GCC_ARM

```

For some Mbed compilers, you may get compile error in mbed_rtc_time.cpp. Go to  mbed-os/platform/mbed_rtc_time.h  and comment line 32 and line 37:

```
//#if !defined(__GNUC__) || defined(__CC_ARM) || defined(__clang__) struct timeval {
time_t  tv_sec; int32_t tv_usec;
};
//#endif
```

If your system does not recognize the board with the mbed detect command. Follow the instructions for setting up [DAPLink](https://armmbed.github.io/DAPLink/?board=FRDM-K66F) for the [K66F](https://os.mbed.com/platforms/FRDM-K66F/).

Connect the USB cable to the micro USB port. When the Ethernet port is facing towards you, the micro USB port is left of the Ethernet port.

Now, we are ready to flash the device:

```
mbed compile -m K66F -t GCC_ARM –flash
```

Disconnect USB cable from the device to power down the device and connect back the power cable to start running the model.

Connect to serial port with baud rate of 9600 and correct serial device to view the output from the MCU. In linux, you can run the following screen command if the serial device is  /dev/ttyACM0:

```
sudo screen /dev/ttyACM0 9600
```

Saying "Yes" will print "Yes" and "No" will print "No" on the serial port.

## Project structure
While the project builds, we can look in more detail at how it works.

### Convolutional neural networks
Convolutional networks are a type of deep neural network. These networks are designed to identify features in multidimensional vectors. The information in these vectors is contained in the relationships between groups of adjacent values.

These networks are usually used to analyze images. An image is a good example of the multidimensional vectors described above, in which a group of adjacent pixels might represent a shape, a pattern, or a texture. During training, a convolutional network can identify these features and learn what they represent. The network can learn how simple image features, like lines or edges, fit together into more complex features, like an eye, or an ear. The network can also learn, how those features are combined to form an input image, like a photo of a human face. This means that a convolutional network can learn to distinguish between different classes of input image, for example a photo of a person and a photo of a dog.

While they are often applied to images, which are 2D grids of pixels, a convolutional network can be used with any multidimensional vector input. In the example we are building in this guide, a convolutional network has been trained on a spectrogram that represents 1 second of audio bucketed into multiple frequencies.

The following image is a visual representation of the audio. The network in our sample has learned which features in this image come together to represent a "yes", and which come together to represent a "no".

![enter image description here](https://raw.githubusercontent.com/COTASPAR/K66F/master/images/spectogram2.jpeg?auto=compress,format&w=680&h=510&fit=max)

To generate this spectrogram, we use an interesting technique that is described in the next section.

## Feature generation with Fast Fourier transform
In our code, each spectrogram is represented as a 2D array, with 43 columns and 49 rows. Each row represents a 30ms sample of audio that is split into 43 frequency buckets.

To create each row, we run a 30ms slice of audio input through a Fast Fourier transform. Fast Fourier transform analyzes the frequency distribution of audio in the sample and creates an array of 256 frequency buckets, each with a value from 0 to 255. These buckets are averaged together into groups of 6, leaving us with 43 buckets. The code in the file [micro_features/micro_features_generator.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/micro_features/micro_features_generator.cc) performs this action.

To build the entire 2D array, we combine the results of running the Fast Fourier transform on 49 consecutive 30ms slices of audio, with each slice overlapping the last by 10ms. The following diagram should make this clearer:
![enter image description here](https://raw.githubusercontent.com/COTASPAR/K66F/master/images/fft.jpeg?auto=compress,format&w=680&h=510&fit=max)

You can see how the 30ms sample window is moved forward by 20ms each time until it has covered the full one-second sample. The resulting spectrogram is passed into the convolutional model.

## Recognition and windowing
The process of capturing one second of audio and converting it into a spectrogram leaves us with something that our ML model can interpret. The model outputs a probability score for each category it understands (yes, no, unknown, and silence). The probability score indicates whether the audio is likely to belong to that category.

The model was trained on one-second samples of audio. In the training data, the word “yes” or “no” is spoken at the start of the sample, and the entire word is contained within that one-second. However, when this code is running, there is no guarantee that a user will begin speaking at the very beginning of our one-second sample.

If the user starts saying “yes” at the end of the sample instead of the beginning, the model might not be able to understand the word. This is because the model uses the position of the features within the sample to help predict which word was spoken.

To solve this problem, our code runs inference as often as it can, depending on the speed of the device, and averages all of the results within a rolling 1000ms window. The code in the file [recognize_commands.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/recognize_commands.cc) performs this action. When the average for a given category in a set of predictions goes above the threshold, as defined in [recognize_commands.h](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/recognize_commands.h), we can assume a valid result.

## Interpreting the results

The RespondToCommand method in [command_responder.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/command_responder.cc) is called when a command has been recognized. Currently, this results in a line being printed to the serial port. Later in this guide, we will modify the code to display the result on the screen.

## Deploy the example to your K66F

In the previous section of this guide, we explained the build process for a keyword spotting example application.

Now that the build has completed, we will look in this section of the guide at how to deploy the binary to the K66F and test to see if it works.

First, plug in your K66F board via USB. The board should show up on your machine as a USB mass storage device. Copy the binary file that we built earlier to the USB storage.

Note: if you have skipped the previous steps, download the [binary file]() to proceed.

Use the following command:

```
cp ./BUILD/K66F/GCC_ARM/mbed.bin /Volumes/K66F/
```

Depending on your platform, the exact copy command and paths may vary. When you have copied the file, the LEDs on the board should start flashing, and the board will eventually reboot with the sample program running.

## Test keyword spotting

The program outputs recognition results to its serial port. To see the output of the program, we will need to establish a serial connection with the board at 9600 baud.

The board’s USB UART shows up as  ```/dev/tty.usbmodemXXXXXXX```.We can use ‘screen’ to access the serial console. Although, ‘screen’ is not installed on Linux by default, you can use apt-get install screen to install the package.

Run the following command in a separate terminal:

```
screen /dev/tty.usbmodemXXXXXX 9600
```

**Note**: this command may very depending on where your board is plugged.

Try saying the word “yes” several times. You should see some output like the following:

```
Heard yes (208) @116448ms  
Heard unknown (241) @117984ms  
Heard no (201) @124992ms

```

Congratulations! You are now running a machine learning model that can recognize keywords on an Arm Cortex-M4 microcontroller, directly on your K66F.

It is easy to change the behavior of our program, but is it difficult to modify the machine learning model itself? The answer is no, and the next section of this guide, [Retrain the machine learning model](https://developer.arm.com/solutions/machine-learning-on-arm/developer-material/how-to-guides/build-arm-cortex-m-voice-assistant-with-google-tensorflow-lite/retrain-the-machine-learning-model), will show you how.

## Retrain the machine learning model

The model that we are using for speech recognition was trained on a dataset of one-second spoken commands called the [Speech Commands Dataset](https://ai.googleblog.com/2017/08/launching-speech-commands-dataset.html). The dataset includes examples of the following ten different words:

yes, no, up, down, left, right, on, off, stop, go

While the model in this sample was originally trained to recognize “yes” and “no”, the TensorFlow Lite for Microcontrollers source contains scripts that make it easy to retrain the model to classify any other combination of these words.

We are going to use another pre-trained model to recognize “up” and “down”, instead. If you are interested in the full flow including the training of the model refer to the [Supplementary information: model training](https://developer.arm.com/solutions/machine-learning-on-arm/developer-material/how-to-guides/build-arm-cortex-m-voice-assistant-with-google-tensorflow-lite/supplementary-information-model-training) section of this guide.

To build our new ML application we will now follow these steps:

-   Download a pretrained model that has been trained and frozen using TensorFlow.

-   Look at how the TensorFlow model gets converted to the TensorFlow Lite format.

-   Convert the TensorFlow Lite model into a C source file.

-   Modify the code and deploy to the device.


Note: Building TensorFlow and training the model will each take a couple of hours on an average computer. We will not perform this at this stage. For a full guide on how to do this, refer to the [Supplementary information: model training](https://developer.arm.com/solutions/machine-learning-on-arm/developer-material/how-to-guides/build-arm-cortex-m-voice-assistant-with-google-tensorflow-lite/supplementary-information-model-training) section in this guide.

## Convert the model

Starting from the trained model to obtain a converted model that can run on the controller itself, we need to run a conversion script: the [TensorFlow Lite converter](https://www.tensorflow.org/lite/convert). This tool uses clever tricks to make our model as small and efficient as possible, and to convert it to a TensorFlow Lite FlatBuffer. To reduce the size of the model, we used a technique called [quantization](https://www.tensorflow.org/lite/performance/post_training_quantization). All weights and activations in the model get converted from 32-bit floating point format to an 8-bit and fixed-point format, as you can see in the following command:

![Convert the model to the TensorFlow Lite format code image](https://raw.githubusercontent.com/COTASPAR/K66F/master/images/convert_model.png)
This conversion will not only reduce the size of the network, but will avoid floating point computations that are more computationally expensive.

To save time, we will skip this step and instead download the [tiny_conv.tflite](https://developer.arm.com/-/media/Files/downloads/Machine%20learning%20how-to%20guides/tiny_conv.tflite?revision=495eb362-4325-49b8-b3ba-3141df0c9b95&la=en&hash=0F37BA2C5DE95A1561979CDD18973171767A47C3).

The final step in the process is to convert this model into a C file that we can drop into our Mbed project.

To do this conversion, we will use a tool called xxd. Issue the following command:

```
xxd -i  tiny_conv.tflite > ../micro_features/model.cc
```

Next, we need to update model.cc so that it is compatible with our code. First, open the file. The top two lines should look similar to the following code, although the exact variable name and hex values may be different:

```
const  unsigned  char  g_model[] DATA_ALIGN_ATTRIBUTE = {  
0x18, 0x00, 0x00, 0x00, 0x54, 0x46, 0x4c, 0x33, 0x00, 0x00, 0x0e, 0x00,
```

You need to add the include from the following snippet and change the variable declaration without changing the hex values:

```
#include "tensorflow/lite/micro/examples/micro_speech/micro_features/model.h"  
const unsigned char g_tiny_conv_micro_features_model_data[] = {  
0x18, 0x00, 0x00, 0x00, 0x54, 0x46, 0x4c, 0x33, 0x00, 0x00, 0x0e, 0x00,
```

Next, go to the very bottom of the file and find the unsigned int variable.

```
unsigned int tiny_conv_tflite_len = 18216;
```

Change the declaration to the following code, but do not change the number assigned to it, even if your number is different from the one in this guide.

```
const int g_tiny_conv_micro_features_model_data_len = 18216;
```

Finally, save the file, then copy the ```tiny_conv_micro_features_model_data.cc```file into the ```tensorflow/tensorflow/lite/micro/tools/make/gen/mbed_cortex-m4/prj/micro_speech/mbed/tensorflow/lite/micro/examples/micro_speech/micro_features``` directory.

## Modify the device code

If you build and run your code now, your device should respond to the words “up” and “down”. However, the code was written to assume that the words are “yes” and “no”. Let’s update the references and the user interface so that the appropriate words are printed.

First, go to the following directory:

```tensorflow/lite/micro/examples/micro_speech/```

and open the file:

```micro_features/micro_model_settings.cc```

You will see the following category labels:
```
const char* kCategoryLabels[kCategoryCount] = {  
"silence",  
"unknown",  
"yes",  
"no",  
};
```
The code uses this array to map the output of the model to the correct value. Because we specified our wanted_words as “up, down”in the training script, we should update this array to reflect these words in the same order. Edit the code so it appears as follows:
```
const char* kCategoryLabels[kCategoryCount] = {  
"silence",  
"unknown",  
"up",  
"down",  
};
```
Next, we will update the code in command_responder.cc to reflect these new labels, modifying the if statements and the DisplayStringAt call:
```
void RespondToCommand(tflite::ErrorReporter* error_reporter,  
int32_t current_time, const char* found_command,  
uint8_t score, bool is_new_command) {  
if (is_new_command) {  
error_reporter->Report("Heard %s (%d) @%dms", found_command, score,  
current_time);  
if(strcmp(found_command, "up") == 0) {  
lcd.Clear(0xFF0F9D58);  
lcd.DisplayStringAt(0, LINE(5), (uint8_t *)"Heard up", CENTER_MODE);  
} else if(strcmp(found_command, "down") == 0) {  
lcd.Clear(0xFFDB4437);  
lcd.DisplayStringAt(0, LINE(5), (uint8_t *)"Heard down", CENTER_MODE);  
} else if(strcmp(found_command, "unknown") == 0) {  
lcd.Clear(0xFFF4B400);  
lcd.DisplayStringAt(0, LINE(5), (uint8_t *)"Heard unknown", CENTER_MODE);  
} else {  
lcd.Clear(0xFF4285F4);  
lcd.DisplayStringAt(0, LINE(5), (uint8_t *)"Heard silence", CENTER_MODE);  
}  
}  
}
```

Now that we have updated the code, go back to the mbed directory:

```
cd <path_to_tensorflow>/tensorflow/lite/micro/tools/make/gen/mbed_cortex-m4/prj/micro_speech/mbed
```

and run the following command to rebuild the project:

```mbed compile -m K66F -t GCC_ARM```

Finally, copy the binary to the USB storage of the device, using the same method that you used earlier. You should now be able to say “up” and “down” to update the display.

## Troubleshooting

We have found some common errors that users face and have listed them here to help you get started with your application as quickly as possible.
If you encounter:

```Mbed CLI issues or Error: collect2: error: ld returned 1 exit status```

Purge the cache with the following command:

```mbed cache purge```

You probably also have a stale BUILD folder. Clean up your directory and try again:

```rm -rf BUILD```

Error: Prompt wrapping around line

If your terminal is wrapping your text as show here:

![Error prompt wrapping around line image](https://raw.githubusercontent.com/COTASPAR/K66F/master/images/troubleshooting.png)

In your terminal type:

```export PS1='\u@\h: '```

For a more minimalist type:

```export PS1='> '```

Error: "Requires make version 3.82 or later (current is 3.81)"

If you encounter this error, install the brew and make by typing the following code:

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

```
brew install make
```

**Note**: On a Mac, you might have to use gmake instead of make, to run your commands.

Error: -bash: mbed: command not found

If you encounter this error, try the following fixes.

For Mac:

We recommend using the [installer](https://github.com/ARMmbed/mbed-cli-osx-installer/releases/tag/v0.0.10) and running the downloaded Mbed CLI App. This app will automatically launch a shell with all the dependencies solved for you.

If installed manually, make sure to follow these [instructions](https://os.mbed.com/docs/mbed-os/v5.12/tools/macos.html).
