<h2 id="quick-start">Arm Mbed OS Quick-Start</h2>

Learn how to leverage the Arm Mbed ecosystem to create IoT applications on hundreds of Arm platforms. This quick start will cover development workflows from selecting your target in the Arm online compiler, to creating your first application, how to flash your target, and how to interact with your device. This guide will conclude with a broad range of examples, conceptual tutorials, end to end applictions, and links to the documentation to empower you to develop on the Arm Mbed OS platform.

## Development Environment

Mbed OS support both online and offline development environments. For the online compiler, continue to the [Online Compiler](#online-compiler), otherwise continue on to [Export](#Export).

### Online Compiler

The Mbed OS online compiler allows you to dive into importing software and building binaries for your target with no installation or setup required.

#### Import

Visit the [Mbed OS Site](https://os.mbed.com/) and login with your credentials. You need to tell the Online Compiler which device you will be targeting. Please select your target from the [Mbed OS Platform Page](https://os.mbed.com/platforms/) and select `Add to your Mbed compiler` on the right hand side of the page.

Click the button below to import the example application for your device into the Online Compiler.

[![View code](https://www.mbed.com/embed/?url=https://github.com/armmbed/mbed-os-quick-start)]()

#### Building and Flashing

With the quick start example imported and your target selected, simply click on the `Compile` button. The online compiler uses the Arm 5 compiler. Once the build is complete a binary will be downloaded to your desktop.

At this step your device should be plugged into your computer over USB and will appear as a mounted flash device.

Drag and drop the downloaded binary to target's mounted drive. Reset your board and the new software will be running on the target.

#### Export

The online compiler supports exporting projects for a large number of other IDEs and toolchains to be used offline. Right click on the program in your program workspace on the left hand side of the screen and select `Export Program...`. Select your desired output format from the prompt.

### Offline Compilers
