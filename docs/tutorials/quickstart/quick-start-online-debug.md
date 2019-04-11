<h1 id="debug-ide-qs">Debugging the quick start</h1>

## Using printf

The easiest way to do basic debugging is to use the `printf` command in your code, then read the output using a serial terminal, such as [PuTTY](http://www.putty.org/) or [CoolTerm](http://freeware.the-meiers.org/).

For example, add `printf("Hello World!\n\r");` to the top of your main function, and then recompile the program and flash it to your device.

<span class="notes">**Note:** Unless otherwise specified, `printf` defaults to a baud rate of `9600` on Mbed OS. You can modify this value in the `mbed_app.json` file. To configure your terminal client to this baud rate, change the speed option when selecting the port. You can view the [configuration options page](../reference/configuration.html) to learn more about how to configure OS-level options.</span>

To determine which communication port your board connects to:

1. **On Windows**:

    1. Open the Device Manager by pressing <kbr>Windows key</kbr> + <kbr>R</kbr>.
    1. Enter `devmgmt.msc`.
    1. Click **OK**.
    1. Under **Ports (COM & LPT)**: your Mbed board is listed as a `USB Serial Device` next to its COM port.

1. **On Linux**: Run `dmesg | grep tty` from your command-line.

1. **On macOS**: Run `ls /dev/tty.*` from your command-line.

## Exporting to a desktop IDE

To debug using a desktop IDE such as Keil uVision, IAR or Eclipse:

1. Under **Program Details**, click the **Export** button.
1. Select your export platform and IDE.
1. Click **Export**.
1. Your browser downloads a `.zip` file with the project files.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/export_online_compiler.png)</span>
