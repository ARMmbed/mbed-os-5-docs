## Blinky on Arm Mbed CLI

This tutorial builds Blinky using the Arm Mbed CLI, which allows you to build Mbed OS applications on your own machine. You will need to install Mbed CLI and a toolchain before you can work with Blinky.

<span class="tips">Please create a <a href="https://os.mbed.com/account/signup/" target="_blank">developer account</a>. It's free, and we don't spam.</span>

### Blinky's code

Blinky's code is a simple `while` loop inside the `main()` function:

```
#include "mbed.h"
#include "rtos.h"

DigitalOut led1(LED1);

// main() runs in its own thread in the OS
// (note the calls to wait below for delays)
int main() {
    while (true) {
        led1 = !led1;
        wait(0.5);
    }
}
```

### Quick start video

This video shows how to use Mbed CLI to import and build Blinky. Note that it assumes you have already installed Mbed CLI (see next section):

<span class="images">[![Video tutorial](http://img.youtube.com/vi/PI1Kq9RSN_Y/0.jpg)](https://www.youtube.com/watch?v=PI1Kq9RSN_Y)<span>Watch how to create your first application on Arm Mbed CLI</span></span>

### Installing Mbed CLI and a toolchain

Mbed CLI is an offline tool, meaning you'll have to install it before you can work. You will also need to install a toolchain. Please follow the installation instructions on the <a href="/docs/v5.6/tools/setup.html" target="_blank">Mbed CLI setup page</a>, and come back here when you're done.

### Setting context

Whenever you work with Mbed CLI, you need to navigate your command-line terminal to the directory in which you want to work. For example, if your program is in a folder called `my_program`:

```
cd my_program
```

You can then start running Mbed CLI commands, and they will run in the correct context.

### Getting Blinky

Mbed CLI can import Blinky, along with the Arm Mbed OS codebase. The import process creates a new directory as a subdirectory of your current context (as explained above).

To import Blinky, from the command-line:

1. Navigate to a directory of your choice. We're navigating to our development directory:

  ```
  cd dev_directory
  ```

2. Import the example:

  ```
  mbed import mbed-os-example-blinky
  cd mbed-os-example-blinky
  ```

<span class="tips">**Tip:** `import` requires a full URL to Mercurial or GitHub. If you don't enter a full URL, Mbed CLI prefixes your snippet with `https://github.com/ARMmbed/`. We took advantage of this feature in our example; `import mbed-os-example-blinky` is interpreted as `https://github.com/ARMmbed/mbed-os-example-blinky`.</span>

Blinky is now under `dev_directory` > `mbed-os-example-blinky`. You can look at `main.cpp` to familiarize yourself with the code.

### Compiling

Invoke `mbed compile`, specifying:

* Your board: `-m <board_name>`.
* Your toolchain: `-t <GCC_ARM, ARM, ARMC6 or IAR>`.

For example, for the board K64F and the Arm Compiler 5:

```
mbed compile -m K64F -t ARM
```

If you don't know the name of your target board, there are several ways to tell.

- Invoke `mbed detect`, and the Mbed CLI tool displays an output similar to below, where 'K64F' is the name of your target platform and COM3 is the name of the serial port that the platform connects to:

```
[mbed] Detected "K64F" connected to "D:" and using com port "COM3"
```

- Check the board information page on the list of <a href="https://developer.mbed.org/platforms/" target="_blank">Mbed Enabled boards</a>. The right side of each information page lists the name of the target.

- If you only have one Mbed Enabled board connected, Mbed CLI can automatically detect the target by specifing `-m detect`.

Your PC may take a few minutes to compile your code. At the end you should get the following result:

```
[snip]
+----------------------------+-------+-------+------+
| Module                     | .text | .data | .bss |
+----------------------------+-------+-------+------+
| Misc                       | 13939 |    24 | 1372 |
| core/hal                   | 16993 |    96 |  296 |
| core/rtos                  |  7384 |    92 | 4204 |
| features/FEATURE_IPV4      |    80 |     0 |  176 |
| frameworks/greentea-client |  1830 |    60 |   44 |
| frameworks/utest           |  2392 |   512 |  292 |
| Subtotals                  | 42618 |   784 | 6384 |
+----------------------------+-------+-------+------+
Allocated Heap: unknown
Allocated Stack: unknown
Total Static RAM memory (data + bss): 7168 bytes
Total RAM memory (data + bss + heap + stack): 7168 bytes
Total Flash memory (text + data + misc): 43402 bytes
Image: .\.build\K64F\ARM\mbed-os-example-blinky.bin             
```

The program file, `mbed-os-example-blinky.bin`, is under your `mbed-os-example-blinky\build\K64F\ARM\` folder.

### Programming your board

Arm Mbed Enabled boards are programmable by drag and drop over a USB connection:

1. Connect your mbed board to the computer over USB.
1. Copy the binary file to the board. In the example above, the file is `mbed-os-example-blinky.bin`, and it's under the `mbed-os-example-blinky\build\K64F\ARM\` folder.
1. Press the reset button to start the program.

You should see the LED of your board turning on and off.
