## Blinky on the Arm Mbed Online Compiler

<span class="tips">Please create a [developer account](https://os.mbed.com/account/signup/). It's free, and we don't spam.</span>

### Importing Blinky

To get Blinky into the Mbed Online Compiler, click the **`Import into Mbed IDE`** button below:

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-blinky/)](https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-blinky/file/tip/main.cpp)

You're taken to the online IDE, and the **Import Program** dialog box opens:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/import_dialog.png)<span>Importing Blinky</span></span>

The import mechanism offers a default name, but you're free to change it. When you're done, click **Import**.

### Viewing Blinky

The imported Blinky has two interesting parts:

* ``main.cpp``, where the Blinky-specific code is. You can double-click the file in the navigation pane on the left to view the code.
* ``mbed-os``, where the Arm Mbed OS codebase is.

Later we'll compile the code; this will take both of these parts and create a single application file from them.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/maincpp.png)<span>Viewing the code in main.cpp</span></span>

### Selecting a target board

The Mbed Online Compiler can build your application to match any Arm Mbed Enabled board. However, you have to select the target board before compiling.

#### Adding a board to your list

To add a board to your list, go to [the board's page on `os.mbed.com`](https://os.mbed.com/platforms/), and click the **`Add to your Mbed Compiler`** button:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/add_board.png)<span>Adding a board to the Mbed Online Compiler's board list</span></span>

#### Selecting a board

The compiler shows the current build board's name on the upper right corner:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/show_board.png)<span>Opening the list of boards</span></span>

Click the name to change your board as needed:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/select_board.png)<span>Selecting a board</span></span>

### Compile and install

The Mbed Online Compiler builds your program as a `.bin` file that you can install on your board.

1. Click **Compile**.

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/compileandinstall.png)<span>The Compile menu; choose Compile to build and download your application</span></span>

1. The program compiles:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-imagese/compiling.png)<span><span>Compilation progress</span></span></span>

1. When the compiled file is ready, it's downloaded to your default download location (or opens a Download dialog box). The file format is `.bin`, and the file  name is the same as your program name.

1. Connect your board to your computer over USB. Mbed boards are shown as "removable storage".

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/DeviceOnWindows.png)<span>The device is listed as `MBED` or `DAPLINK`, and its type is removable storage</span></span>

1. Drag and drop your program to the board. The board installs the program.

1. Reset the board, and see the LED blink.
