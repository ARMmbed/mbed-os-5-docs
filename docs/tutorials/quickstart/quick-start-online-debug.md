### Debug

#### Desktop IDE

To debug using a desktop IDE such as Keil uVision, IAR or Eclipse, click the `Export` button under `Program Details`. Select your export platform and IDE, and click `Export`. Your browser downloads a `.zip` file with the project files.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/export_online_compiler.png)
</span>

#### Printf

Another way to do basic debugging is to use the `printf` command in your code and then read the output using a serial terminal, such as [PuTTY](http://www.putty.org/) or [CoolTerm](http://freeware.the-meiers.org/). For example, add `printf("Hello World!\n\r");` to the top of your main function, and then recompile the program and flash it to your device.

Unless otherwise specified, `printf` defaults to a baud rate of `9600` on Mbed OS.

<span class="notes">**Note:** The `mbed-os-quick-start-blinky` example runs at a baud rate of `115200`. You can view the [configuration options page](../reference/configuration.html) to learn more about how to configure OS level options.</span>

To determine which communication port your board connects to, follow the instructions for your operating system:

##### Windows

Open the Device Manager by pressing `Windows key + R`. Type `devmgmt.msc`, and click `OK`. Under `Ports (COM & LPT)`, your Mbed board is listed as a `USB Serial Device` next to its COM port.

##### Linux

Run `dmesg | grep tty` from your command-line.

##### macOS

Run `ls /dev/tty.*` from your command-line.

### Further reading

More examples:

- [Mbed OS examples](https://os.mbed.com/teams/mbed-os-examples/code/) - list of Mbed OS 5 example repositories.

- Documentation
    - [Mbed OS APIs](../apis/index.html) - list of all APIs available in Mbed OS.
    - [Peripheral drivers](../apis/drivers.html) - IO driver APIs (I2C, SPI, UART and so on).

- Tutorials
    - [Advanced debugging](debugging.html).
    - [Serial communications](../tutorials/serial-communication.html).
    - [Optimizing binary size](optimizing.html).

- Other resources
    - [Components database](https://os.mbed.com/components/) - libraries and example code for various hardware and software components.
    - [Mbed OS forum](https://os.mbed.com/forum/) - a resource of questions and answers and an active user community. Ask your questions here first.
    - [Youtube channel](http://youtube.com/armmbed) - videos and workshop content.
