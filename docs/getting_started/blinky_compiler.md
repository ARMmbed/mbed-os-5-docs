# Blinky on the mbed Online Compiler

<span class="tips">Please create a [developer account](https://developer.mbed.org/account/signup/). It's free, and we don't spam.</span>
 
## Importing Blinky

To get Blinky into the mbed Online Compiler, click the **Import into mbed IDE** button below:

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-blinky/)](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-blinky/file/tip/main.cpp)

<span class="images">![](images/import_dialog.png)<span>Importing Blinky</span></span>

The import mechanism offers a default name, but you're free to change it. When you're done, click **Import**.

## Viewing Blinky

The imported Blinky has two interesting parts:

* ``main.cpp``, where the Blinky-specific code is. You can double-click the file in the navigation pane on the left to view the code.
* ``mbed-os``, where the mbed OS codebase is.

Later we'll compile the code; this will take both of these parts and create a single application file from them.

<span class="images">![](images/main_cpp.png)<span>Viewing the code in main.cpp</span></span>

## Selecting a target board

The mbed Online Compiler can build your application to match any mbed Enabled board. However, you have to select the target before compiling.

### Adding a board to your list

To add a board to your list, go to the board's page on mbed.com, and click the **Add to your mbed Compiler** button:

<span class="images">![](../dev_tools/Images/add_board.png)<span>Adding a board to the mbed Online Compiler's board list</span></span>

### Selecting a board

The compiler shows the current build board's name on the upper right corner:

<span class="images">![](../dev_tools/Images/show_board.png)<span>Opening the list of boards</span></span>

Click the name to change your board as needed:

<span class="images">![](../dev_tools/Images/select_board.png)<span>Selecting a board</span></span>

## Compile and install

The mbed Online Compiler builds a ``.bin`` file that you can install on your board.

1. Click **Compile**.

	<span class="images">![](images/compile.png)<span>The Compile menu; choose Compile to build and download your application</span></span>

1. The program compiles:

	<span class="images">![](images/compiling.png)<span><span>Compilation progress</span></span></span>

1. When the compiled file is ready, it's downloaded to your default download location (or opens a Download dialog box). The file format is ``.bin``, and the file  name is the same as your program name.

1. Connect your board to your computer over USB. mbed boards are shown as "removable storage".

	<span class="images">![](images/DeviceOnMac.png)<span>The device is listed as "MBED", and its type is removable storage</span></span>

1. Drag and drop your program to the board. 

1. The board installs the program and then runs it. You should see the LED blink.

