## Online Compiler

### Setup

#### Create an Mbed developer account
Go to os.mbed.com and [create an account](https://developer.mbed.org/account/signup/?next=%2F)

#### Setup Environment
- Plug your mbed board into your computer and open its USB device folder
- Double click on the MBED.HTM file (this will add your mbed platform to the online compiler)

If you do not have an Mbed board, go to [os.mbed.org/platforms](http://os.mbed.org/platforms), select a board and click the “Add to your mbed Compiler” button.
<span class="images">![](https://sarahmarshy.github.io/img/add-to-compiler.png)
</span>

### Code

#### Import 
Visit the mbed-os [blinky example repository](https://developer.mbed.org/teams/mbed-os-examples/code/mbed-os-example-blinky/) and click the "Import into Compiler" button.
 
<span class="images">![](https://sarahmarshy.github.io/img/import-compiler.png)
</span>

#### Compile
Click on the "Compile" button, your browser will then download the program as a `.bin` file.

<span class="images">![](https://sarahmarshy.github.io/img/compile.png)
</span>

#### Program
Open the folder where the `.bin` file was downloaded, then click and drag (or copy and paste) the file to your mbed board's USB device folder.

Once the file has been flashed to the board, press the board's "reset" button and you should now see the LED blinking.


### Debug

#### Desktop IDE

To debug using a desktop IDE such as Keil uVision, IAR, or Eclipse, click the "Export" button under "Program Details", select your export platform and IDE and click "Export". Your browser will then download a zip file with the project files.

<span class="images">![](https://sarahmarshy.github.io/img/export.png)
</span>

#### Printf

Another way to do basic debugging is to use the `printf` command in your code, then read the output using a serial terminal such as [PuTTY](http://www.putty.org/) or [CoolTerm](http://freeware.the-meiers.org/). For example, add `printf("Hello World!\n\r");` to the top of your main function, then recompile the program and flash it to your device.

Unless otherwise specified, `printf` defaults to a baud rate/speed of `9600` on mbed OS. To determine which communication port your board is connected to, follow the instructions for your operating system below:

##### Windows

Open the Device Manager by pressing `Windows key + R`, type `devmgmt.msc` and click "OK." Under "Ports (COM & LPT)" your mbed board will be listed as a "USB Serial Device" next to its COM port.

##### Linux

Run `dmesg | grep tty` from your command line. 

##### Mac

Run `ls /dev/tty.*` from your command line. 



### Further Reading

- Documentation
	- [Mbed OS API's](https://os.mbed.com/docs/v5.6/reference/apis.html) - List of all API's available in Mbed OS
	- [Peripheral Drivers](https://os.mbed.com/docs/v5.6/reference/drivers.html) - Traditional Driver API's (I2C, SPI, UART, ... etc)

- Tutorials
	- [Advanced Debugging](https://os.mbed.com/docs/v5.6/tutorials/debugging.html)
	- [Serial Communications](https://os.mbed.com/docs/v5.6/tutorials/serial-communication.html)
	- [Optimizing binary size](https://os.mbed.com/docs/v5.6/tutorials/optimizing.html)

- Other Resources 
	- [Components Database](https://os.mbed.com/components/) - libraries and example code for various hardware and software components
	- [Mbed OS Forum](https://os.mbed.com/forum/) - great resource full of knowledge and active user community. Ask your questions here first!
	- [Youtube Channel](http://youtube.com/armmbed) - videos and workshop content


