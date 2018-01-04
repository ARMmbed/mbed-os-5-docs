## Arm Mbed Online Compiler

### Setup

#### Create an Arm Mbed developer account

Go to [os.mbed.com](os.mbed.com), and [create an account](https://os.mbed.com/account/signup/F).

#### Setup environment

- Plug your Mbed board into your computer, and open its USB device folder.
- Double click on the `MBED.HTM` file. (This adds your Mbed platform to the Online Compiler.)

If you do not have an Mbed board, go to [os.mbed.com/platforms](http://os.mbed.com/platforms), select a board and click the “Add to your Mbed Compiler” button.
<span class="images">![](https://sarahmarshy.github.io/img/add-to-compiler.png)
</span>

### Code

#### Import 

Visit the Mbed OS [blinky example repository](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-blinky/), and click the "Import into Compiler" button.
 
<span class="images">![](https://sarahmarshy.github.io/img/import-compiler.png)
</span>

#### Compile

Click on the "Compile" button. Your browser downloads the program as an executable file.

<span class="images">![](https://sarahmarshy.github.io/img/compile.png)
</span>

#### Program

Open the folder where the executable file was downloaded, and then click and drag (or copy and paste) the file to your Mbed board's USB device folder.

Once you have flashed the file to the board, press the board's reset button. The LED blinks.

### Debug

#### Desktop IDE

To debug using a desktop IDE such as Keil uVision, IAR or Eclipse, click the `Export` button under `Program Details`. Select your export platform and IDE, and click `Export`. Your browser downloads a `.zip` file with the project files.

<span class="images">![](https://sarahmarshy.github.io/img/export.png)
</span>

#### Printf

Another way to do basic debugging is to use the `printf` command in your code and then read the output using a serial terminal, such as [PuTTY](http://www.putty.org/) or [CoolTerm](http://freeware.the-meiers.org/). For example, add `printf("Hello World!\n\r");` to the top of your main function, and then recompile the program and flash it to your device.

Unless otherwise specified, `printf` defaults to a baud rate of `9600` on Mbed OS. To determine which communication port your board connects to, follow the instructions for your operating system:

##### Windows

Open the Device Manager by pressing `Windows key + R`. Type `devmgmt.msc`, and click `OK`. Under `Ports (COM & LPT)`, your Mbed board is listed as a `USB Serial Device` next to its COM port.

##### Linux

Run `dmesg | grep tty` from your command-line. 

##### Mac

Run `ls /dev/tty.*` from your command-line. 

### Further reading

- Documentation
	- [Mbed OS APIs](https://os.mbed.com/docs/latest/reference/apis.html) - list of all APIs available in Mbed OS.
	- [Peripheral drivers](https://os.mbed.com/docs/latest/reference/drivers.html) - IO driver APIs (I2C, SPI, UART and so on).

- Tutorials
	- [Advanced debugging](https://os.mbed.com/docs/latest/tutorials/debugging.html).
	- [Serial communications](https://os.mbed.com/docs/latest/tutorials/serial-communication.html).
	- [Optimizing binary size](https://os.mbed.com/docs/latest/tutorials/optimizing.html).

- Other resources 
	- [Components database](https://os.mbed.com/components/) - libraries and example code for various hardware and software components.
	- [Mbed OS forum](https://os.mbed.com/forum/) - a resource of questions and answers and an active user community. Ask your questions here first.
	- [Youtube channel](http://youtube.com/armmbed) - videos and workshop content.
