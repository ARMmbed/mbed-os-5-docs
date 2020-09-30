# Machine learning with TensorFlow and Mbed OS
<!--https://github.com/COTASPAR/K66F/blob/master/README.md-->
As an IoT developer, you might think of machine learning as a server-side technology: sensors on your device capture data and send it to the cloud, where Machine Learning (ML) models on hefty machines make sense of it. A network connection is obligatory, and you are going to expect some latency, not to mention hosting costs.

But with the launch of [TensorFlow Lite for Microcontrollers](https://www.tensorflow.org/lite/microcontrollers), you can run machine learning inference on extremely low-powered devices, like the Cortex-M microcontroller series. You can deploy your ML models to the IoT devices themselves, bring ML closer to your sensors, remove your reliance on a network connection, and skip the round trip to the server for lower latency.

This is especially exciting for IoT, because lower network use means lower power consumption. You can also better guarantee the security and privacy of your users, since you do not need to send data back to the cloud unless you know for sure that it is relevant.

In this guide, you will learn how to perform machine learning inference on an Arm Cortex-M microcontroller with TensorFlow Lite for Microcontrollers. You will deploy a sample application we wrote that uses the microphone on the K66F and a TensorFlow machine learning model to detect the words “yes” and “no”.

The guide has step by step instructions for installing and running the application, followed by information about how TensorFlow and the application work. Finally, it shows you how to retrain the ML model with new words.

## Using the example application

<!--this needs to move-->
**Important:** We recommend running the following commands from inside the Mbed CLI terminal that gets launched with the Mbed CLI Application. This is because it will be much quicker to set up, because it resolves all your environment dependencies automatically.

### Prerequisites

Here is what you will need to complete the guide:

* Ubuntu 20.04 LTS. If you are using a Windows machine, install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)<!--originally you said 6.0 - that version's support ended in July. Can they install the latest version, or do they need 6.0 specifically?--> and then [Install Ubunto on it](https://www.virtualbox.org/wiki/Linux_Downloads).

* [Mbed CLI (version 1.10.4)](../build-tools/install-and-set-up.html).

* The [GNU Arm Embedded](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads) toolchain [that Mbed CLI supports](../build-tools/index.html).<!--Mbed OS supports ARMC 6.14, and many users rely on it. Can they use it?--> For Windows users, if you have already set up the Linux virtual environment, install the toolchain there.

    Configure Mbed CLI to find your GNU installation:

    ```    
    mbed config -G GCC_ARM_PATH <path_to_your_arm_toolchain>/bin
    ```

* Make 3.82 or newer (if you are using an older version, see the troubleshooting section for instructions).

    <span class="notes">**Note**: On a Mac, you might have to use gmake instead of make.</span>

* Python 2.7. We recommend [using pyenv to manage Python versions](https://pypi.org/project/pyenv/).<!--The install page for Mbed CLI now requires 3.7. Why are we asking for 2.7?-->

* Git.

* xxd.<!--unless is exists by default on all Linux computers?-->

* A development board that can run [TensorFlow Lite for Microcontrollers](https://www.tensorflow.org/lite/microcontrollers#supported_platforms). We tested on the [NXP FRDM-K66F](https://os.mbed.com/platforms/FRDM-K66F/) development board.

* A mini-USB cable.

<!--MarkDown doesn't support embedded YouTube players, which is one reason I removed the videos. Another is that it's better practice to link to official sites, not to videos uploaded by "unofficial" users who may remove them without warning and may, for all we know, be in legal disputes with the companies who created those products (I admit that isn't very likely with "how to install" videos). Also, not sure these videos will work in all countries.-->
### Download, build and install the application

1. Navigate to the directory where you keep code projects.
1. Download the TensorFlow Lite source code:

    ```
    git clone https://github.com/tensorflow/tensorflow.git
    ```

1. Navigate into the project directory and build it:

    ```
    cd tensorflow

    make -f tensorflow/lite/micro/tools/make/Makefile TARGET=mbed TAGS="nxp_k66f" generate_micro_speech_mbed_project
    ```
    <!--I got a "no such file or directory error". I think it's because there was already `cd tensorflow` and then the path in the command also has `tensorflow`. Removing `tensorflow` from the path removed the error-->

    This creates a folder in `tensorflow/lite/micro/tools/make/gen/mbed_cortex-m4/prj/micro_speech/mbed` that contains the source and header files for the example application, Mbed OS driver files, and a README.

1. Navigate into the `mbed` folder:

    ```
    cd tensorflow/lite/micro/tools/make/gen/mbed_cortex-m4/prj/micro_speech/mbed
    ```

1. Execute the following (on an environment that runs Python 2.7):

    ```
    mbed config root .

    mbed deploy

    mbed compile -m K66F -t GCC_ARM
    ```

    <!--The install page for Mbed CLI now requires 3.7. Why are we asking for 2.7?-->
    <!--need to explain what `config root .` and `deploy` do and why we need them - neither one is part of a standard workflow where you use Mbed CLI to import an application, so this is a special case-->
    <!--and why are we compiling here? We compile again two steps down, with the flash parameter-->

    For some compilers<!--we only support two, and you specifically asked for GNU, so in what case will this happen?-->, you may get a compilation error in `mbed_rtc_time.cpp`. Go to  `mbed-os/platform/mbed_rtc_time.h`  and comment out line 32 and line 37:

    ```
    //#if !defined(__GNUC__) || defined(__CC_ARM) || defined(__clang__) struct timeval {
    time_t  tv_sec; int32_t tv_usec;
    };
    //#endif
    ```

1. Connect your board to your computer over USB. On your board, when the Ethernet port is facing you, the micro USB port is to its left.

    Your board appears as storage on your computer. If your system does not recognize the board with the `mbed detect` command, follow the instructions for setting up [DAPLink](https://armmbed.github.io/DAPLink/?board=FRDM-K66F).

1. Flash the application to the board:
    <!--I compiled two steps ago - that probably needs to be removed-->
    ```
    mbed compile -m K66F -t GCC_ARM –flash
    ```
1. Deploy the example to your K66F<!--but we flshed already. What are we doing here?-->

    Copy the binary file that we built earlier to the USB storage.

    Note: if you have skipped the previous steps<!--which ones?-->, download the [binary file]() to proceed.

    The file is at:

    ```
    cp ./BUILD/K66F/GCC_ARM/mbed.bin /Volumes/K66F/
    ```

    Depending on your operating system <!--aren't we making everyone use Linux?-->, the exact copy command and paths may vary.

    When you have copied the file, the LEDs on the board start flashing, and the board will eventually reboot with the sample program running.<!--this contradicts your request to disconnect USB and connect power to cycle the app-->

1. Disconnect the board from USB to power it down.
1. Connect the board's power cable to start running the model.
1. To view output, connect your board to a serial port. The baud rate is 9600.

    For example, if you're on Linux and the serial device is `/dev/ttyACM0`, run:

    ```
    sudo screen /dev/ttyACM0 9600
    ```

1. Speak into the board's microphone: Saying "Yes" will print "Yes" and "No" will print "No" on the serial port:

    ```
    Heard yes (208) @116448ms  
    Heard unknown (241) @117984ms  
    Heard no (201) @124992ms
    ```

Congratulations! You are now running a machine learning model that can recognise keywords on an Arm Cortex-M4 microcontroller, directly on your K66F.

It is easy to change the behavior of our program, but is it difficult to modify the machine learning model itself? The answer is no, and the section [Retrain the machine learning model](https://developer.arm.com/solutions/machine-learning-on-arm/developer-material/how-to-guides/build-arm-cortex-m-voice-assistant-with-google-tensorflow-lite/retrain-the-machine-learning-model) will show you how. First, let's review what the application is doing - and how.

## How TensorFlow and the application work

Let’s explore the project files on [for the speech example](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/micro/examples/micro_speech) and learn how this TensorFlow Lite for Microcontrollers example works.

The application samples audio from the microphone on the K66F. The audio is run through a Fast Fourier transform to create a spectrogram. The spectrogram is then fed into a pre-trained machine learning model. The model uses a [convolutional neural network](https://developers.google.com/machine-learning/practica/image-classification/convolutional-neural-networks) to identify whether the sample represents “yes”, “no”, an unknown input or silence. We will explore how this works in more detail later in the guide.

Here are descriptions of some interesting source files:

-   [nxp_k66f/audio_provider.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/nxp_k66f/audio_provider.cc): Captures audio from the microphone on the board.

-   [micro_features/micro_features_generator.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/micro_features/micro_features_generator.cc): Uses a Fast Fourier transform to create a spectrogram from audio.

-   [micro_features/model.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/micro_features/model.cc): This file is the machine learning model itself, represented by a large array of unsigned char values.

-   [command_responder.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/command_responder.cc): Called every time a potential command has been identified.

-   [main.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/main.cc): The entry point for the Mbed OS program, which runs the machine learning model using TensorFlow Lite for Microcontrollers.

### Convolutional neural networks

Convolutional networks are a type of deep neural network. These networks are designed to identify features in multidimensional vectors. The information in these vectors is contained in the relationships between groups of adjacent values.

These networks are usually used to analyse images. An image is a good example of the multidimensional vectors described above, in which a group of adjacent pixels might represent a shape, a pattern, or a texture. During training, a convolutional network can identify these features and learn what they represent. The network can learn how simple image features, like lines or edges, fit together into more complex features, like an eye or an ear. The network can also learn how those features are combined to form an input image, like a photo of a human face. This means that a convolutional network can learn to distinguish between different classes of input image, for example a photo of a person and a photo of a dog.

While they are often applied to images, which are 2D grids of pixels, a convolutional network can be used with any multidimensional vector input. In the example in this guide, a convolutional network has been trained on a spectrogram that represents 1 second of audio bucketed into multiple frequencies.

The following image is a visual representation of the audio. The network in our sample has learned which features in this image come together to represent a "yes", and which come together to represent a "no".

<span class="images">![Spectrogram of "yes" and "no"](https://raw.githubusercontent.com/COTASPAR/K66F/master/images/spectogram2.jpeg?auto=compress,format&w=680&h=510&fit=max)</span>

To generate this spectrogram, we use an interesting technique that is described in the next section.

### Feature generation with Fast Fourier transform

In our code, each spectrogram is represented as a 2D array, with 43 columns and 49 rows. Each row represents a 30ms sample of audio that is split into 43 frequency buckets.

To create each row, we run a 30ms slice of audio input through a Fast Fourier transform. Fast Fourier transform analyses the frequency distribution of audio in the sample and creates an array of 256 frequency buckets, each with a value from 0 to 255. These buckets are averaged together into groups of 6, leaving us with 43 buckets. The code in the file [micro_features/micro_features_generator.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/micro_features/micro_features_generator.cc) performs this action.

To build the entire 2D array, we combine the results of running the Fast Fourier transform on 49 consecutive 30ms slices of audio, with each slice overlapping the last by 10ms, as illustrated below:

<span class="images">![Diagram of audio sampling](https://raw.githubusercontent.com/COTASPAR/K66F/master/images/fft.jpeg?auto=compress,format&w=680&h=510&fit=max)</span>

You can see how the 30ms sample window is moved forward by 20ms each time until it has covered the full one-second sample. The resulting spectrogram is passed into the convolutional model.

### Recognition and windowing

The process of capturing one second of audio and converting it into a spectrogram leaves us with something that our ML model can interpret. The model outputs a probability score for each category it understands (yes, no, unknown, and silence). The probability score indicates whether the audio is likely to belong to that category.

The model was trained on the one-second samples of audio we saw above. In the training data, the word “yes” or “no” is spoken at the start of the sample, and the entire word is contained within that one-second. However, when the application is running, there is no guarantee that a user will begin speaking at the very beginning of our one-second sample. If the user starts saying “yes” at the end of the sample instead of the beginning, the model might not be able to understand the word. This is because the model uses the position of the features within the sample to help predict which word was spoken.

To solve this problem, our code runs inference as often as it can<!--here you lost me, probably because I don't deal with ML - is this in the training again? where is it getting new samples?-->, depending on the speed of the device, and averages all of the results within a rolling 1000ms window. The code in the file [recognize_commands.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/recognize_commands.cc) performs this action. When the average for a given category in a set of predictions goes above the threshold<!--lost me here too - are we talking about training or recognising actual users?-->, as defined in [recognize_commands.h](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/recognize_commands.h), we can assume a valid result.

### Interpreting the results

The RespondToCommand method in [command_responder.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/micro_speech/command_responder.cc) is called when a command a user speals has been recognised. Currently, this results in a line being printed to the serial port. Later in this guide, we will modify the code to display the result on the screen.

## Retrain the machine learning model

The model that we are using for speech recognition was trained on a dataset of one-second spoken commands called the [Speech Commands Dataset](https://ai.googleblog.com/2017/08/launching-speech-commands-dataset.html). The dataset contains examples of ten words: yes, no, up, down, left, right, on, off, stop, go.

While the model in this sample was originally trained to recognise “yes” and “no”, the TensorFlow Lite for Microcontrollers source contains scripts that make it easy to retrain the model to classify any other combination of these words.

We are going to use another pre-trained model to recognise “up” and “down”:

1. Look at how the TensorFlow model gets converted to the TensorFlow Lite format.
1. Download a model that has been trained and frozen using TensorFlow.
1. Convert the TensorFlow Lite model into a C source file.
1. Modify the code and deploy to the board.

<span class="tips">**Tip:** Building TensorFlow and training the model will each take a couple of hours on an average computer. We will not perform this at this stage. If you are interested in the full flow, including the training of the model, refer to the [Supplementary information: model training](https://developer.arm.com/solutions/machine-learning-on-arm/developer-material/how-to-guides/build-arm-cortex-m-voice-assistant-with-google-tensorflow-lite/supplementary-information-model-training) guide.</span>

## Background: Converting the trained model

To get a converted model that can run on the controller itself from the trained model, we need to run a conversion script: the [TensorFlow Lite converter](https://www.tensorflow.org/lite/convert). This tool makes our model as small and efficient as possible, and converts it to a TensorFlow Lite FlatBuffer. To reduce the size of the model, we used a technique called [quantization](https://www.tensorflow.org/lite/performance/post_training_quantization). All weights and activations in the model get converted from 32-bit floating point format to an 8-bit and fixed-point format, as you can see in the following command:

<span class="images">![Convert the model to the TensorFlow Lite format code](https://raw.githubusercontent.com/COTASPAR/K66F/master/images/convert_model.png)</span>

This conversion will not only reduce the size of the network traffic, but will also avoid the more computationally expensive floating points.

To save time, in this guide we skip the conversion step and instead download a converted model.

## Downloading the model and creating a C file

1. Download the [tiny_conv.tflite file](https://developer.arm.com/-/media/Files/downloads/Machine%20learning%20how-to%20guides/tiny_conv.tflite?revision=495eb362-4325-49b8-b3ba-3141df0c9b95&la=en&hash=0F37BA2C5DE95A1561979CDD18973171767A47C3).
1. Convert this model into a C file that works with Mbed OS projects.

    Use a tool called xxd to generate a file called `model.cc`:

    ```
    xxd -i  tiny_conv.tflite > ../micro_features/model.cc
    ```

1. Update `model.cc` so that it is compatible with our code:

    1. Open the file. The top two lines should look similar to the following code, although the exact variable name and hex values may be different:

        ```
        const  unsigned  char  g_model[] DATA_ALIGN_ATTRIBUTE = {  
        0x18, 0x00, 0x00, 0x00, 0x54, 0x46, 0x4c, 0x33, 0x00, 0x00, 0x0e, 0x00,
        ```

    1. Add the `include` from the following snippet and change the variable declaration without changing the hex values:

        ```
        #include "tensorflow/lite/micro/examples/micro_speech/micro_features/model.h"  
        const unsigned char g_tiny_conv_micro_features_model_data[] = {  
        0x18, 0x00, 0x00, 0x00, 0x54, 0x46, 0x4c, 0x33, 0x00, 0x00, 0x0e, 0x00,
        ```

    1. Go to the bottom of the file and find the unsigned int variable:

        ```
        unsigned int tiny_conv_tflite_len = 18216;
        ```

    1. Change the declaration to the following code, but do not change the number assigned to it, even if your number is different from the one in this guide:

        ```
        const int g_tiny_conv_micro_features_model_data_len = 18216;
        ```

    1. Save the file.

1. Copy the `tiny_conv_micro_features_model_data.cc` <!--where is this file? it's not the one I was just editing-->file into the `tensorflow/tensorflow/lite/micro/tools/make/gen/mbed_cortex-m4/prj/micro_speech/mbed/tensorflow/lite/micro/examples/micro_speech/micro_features` directory.

## Modify the application code

If you build and run your code now, your ML model knows the words “up” and “down”, but your application assumes that the words are “yes” and “no”. Let’s update the references and the user interface so that the appropriate words are printed.

1. Navigate to the `tensorflow/lite/micro/examples/micro_speech/` directory and open the file `micro_features/micro_model_settings.cc`.

    You see the following category labels:

    ```
    const char* kCategoryLabels[kCategoryCount] = {  
    "silence",  
    "unknown",  
    "yes",  
    "no",  
    };
    ```

    The code uses this array to map the output of the model to the correct value. Because we specified our wanted_words<!--is that underscore correct?--> as “up, down” in the training script, we should update this array to reflect these words in the same order.

1. Edit the code so that "up" replaces "yes" and "down" replaces "no":

    ```
    const char* kCategoryLabels[kCategoryCount] = {  
    "silence",  
    "unknown",  
    "up",  
    "down",  
    };
    ```

1. Update the code in `command_responder.cc` to reflect these new labels, modifying the if statements and the DisplayStringAt call:

    ```
    void RespondToCommand(tflite::ErrorReporter* error_reporter,  
    int32_t current_time, const char* found_command,  
    uint8_t score, bool is_new_command) {  
        if (is_new_command) {  
            error_reporter->Report("Heard %s (%d) @%dms", found_command, score,  
            current_time);  
        if(strcmp(found_command, "up") == 0) {  
            lcd. Clear(0xFF0F9D58);  
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
<!--I added indents - I assumed their lack was a result of copy/paste destroying something, not a decision-->

1. Navigate back to the mbed directory:

    ```
    cd <path_to_tensorflow>/tensorflow/lite/micro/tools/make/gen/mbed_cortex-m4/prj/micro_speech/mbed
    ```

1. Rebuilt the project:

    ```
    mbed compile -m K66F -t GCC_ARM
    ```

1. Copy the binary to the USB storage of the device<!--why aren't we using flash?-->, using the same method that you used earlier.

You can now say “up” and “down” to update the display.

## Troubleshooting

We have found some common errors that users face and have listed them here to help you get started with your application as quickly as possible.

- If you encounter:

    ```
    Mbed CLI issues or Error: collect2: error: ld returned 1 exit status
    ```

    Purge the cache with the following command:

    ```
    mbed cache purge
    ```

    You probably also have a stale BUILD folder. Clean up your directory and try again:

    ```
    rm -rf BUILD
    ```

- If your terminal is wrapping your text as show here:

    <span class="images">![Error prompt wrapping around line](https://raw.githubusercontent.com/COTASPAR/K66F/master/images/troubleshooting.png)</span>

    In your terminal, type:

    ```
    export PS1='\u@\h: '
    ```

    For a more minimalist type:

    ```
    export PS1='> '
    ```

- Error: `Requires make version 3.82 or later (current is 3.81)`

    If you encounter this error, install Brew and Make:

    ```
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

    brew install make
    ```
- Error: `-bash: mbed: command not found`

    Your Mbed CLI installation isn't working properly. We recommend [using the installers](../build-tools/install-and-set-up.html).

    If you installed manually, make sure to follow the [instructions for configuring the compiler location](../build-tools/install-and-set-up.html).
