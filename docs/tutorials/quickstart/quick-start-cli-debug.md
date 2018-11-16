### Debug

#### Desktop IDE

To debug using a desktop IDE such as Keil uVision, IAR or Eclipse, use the `mbed export` command to generate project files. For example, for a K64F and Keil uVision:

```console
$ mbed export --ide uvision --target K64F
```  

<span class="notes">**Note:** For a full list of supported exporters, run the `mbed export --supported` command.</span>

#### Printf

Another way to do basic debugging is to use the `printf` command in your code and read the output using a serial terminal, such as [PuTTY](http://www.putty.org/) or [CoolTerm](http://freeware.the-meiers.org/). For example, add `printf("Hello World!\n\r");` to the top of your main function, and then recompile the program and flash it to your device.

Invoke `mbed detect` from your command-line to determine which communication port your board connects to (in other words, `COM18`, `/dev/ttyACM0` and so on). Unless otherwise specified, `printf` defaults to a baud rate of `9600` on Mbed OS.

<span class="notes">**Note:** The `mbed-os-quick-start-blinky` example runs at a baud rate of `115200`, you can view the [configuration options page](/docs/reference/configuration.html) to learn more about how to configure OS level options.</span>

### Further reading

More examples:
- [Mbed OS examples](https://os.mbed.com/teams/mbed-os-examples/code/) - list of Mbed OS 5 example repositories.

- Documentation
  - [Mbed OS APIs](/docs/development/apis/index.html) - list of all APIs available in Mbed OS.
  - [Peripheral drivers](/docs/development/apis/drivers.html) - IO driver APIs (I2C, SPI, UART and so on).

- Tutorials
  - [Advanced debugging](debugging.html).
  - [Serial communications](/docs/development/tutorials/serial-communication.html).
  - [Optimizing binary size](optimizing.html).

- Other resources
  - [Components database](https://os.mbed.com/components/) - libraries and example code for various hardware and software components.
  - [Mbed OS forum](https://os.mbed.com/forum/) - a resource of questions and answers and an active user community. Ask your questions here first.
  - [Youtube channel](http://youtube.com/armmbed) - videos and workshop content.
