<h2 id="debug-cli-qs">Debugging the quick start</h2>


### Using printf

The easiest way to do basic debugging is to use the `printf` command in your code, then read the output using a serial terminal, such as [PuTTY](http://www.putty.org/) or [CoolTerm](http://freeware.the-meiers.org/).

For example, add `printf("Hello World!\n\r");` to the top of your main function, and then recompile the program and flash it to your device.

<span class="notes">**Note:** Unless otherwise specified, `printf` defaults to a baud rate of `9600` on Mbed OS. The `mbed-os-example-blinky` example runs at a baud rate of `115200`. You can view the [configuration options page](../reference/configuration.html) to learn more about how to configure OS-level options.</span><!--but the thing I should really do now is set a new baud rate in my terminal, right?-->

### Exporting to a desktop IDE

To debug using a desktop IDE such as Keil uVision, IAR or Eclipse, use the `mbed export` command to generate project files.

For example, for a K64F and Keil uVision:

```console
$ mbed export --ide uvision --target K64F
```  

<span class="notes">**Note:** For a full list of supported exporters, run the `mbed export --supported` command.</span>
