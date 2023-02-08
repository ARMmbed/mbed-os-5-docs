<h1 id="debugging">Debugging with third party tools</h1>

There are extensive instructions on debugging Arm Mbed OS applications with [Keil uVision 5](../debug-test/keil-uvision.html), [Eclipse](../debug-test/eclipse.html) and [Visual Studio Code](../debug-test/visual-studio-code.html), but you can use any IDE that supports GDB to debug Mbed OS applications. This document gives advice on how to configure these IDEs. Before starting, first [configure your local debug toolchain](setting-up-a-local-debug-toolchain.html).

## Exporting your project with Mbed CLI

You can use Mbed CLI to generate Makefiles. Almost any C/C++ IDE can use Makefiles to build a project.

In your project folder, run:

```
## alternatively, use -i make_armc5 for ARMCC, or -i make_iar for IAR
## replace K64F with your target board

$ mbed export -i make_gcc_arm -m K64F
```

## Building your project

You can now configure your IDE to build this project by setting the build command to:

```
make -j
```

The resulting binary will end up at `BUILD\projectname.elf`.

## Debugging your project

To debug your project, you first need to start a [debug server](setting-up-a-local-debug-toolchain.html#running-a-debug-server). This is often exposed as a setting in your IDE under 'Remote debugging' or 'Debug server'.

- When using pyOCD, set the full path to the `pyocd-gdbserver` binary, and do not set arguments.
- When using OpenOCD, set the full path to the `openocd` binary, and set the arguments for your development board. (See [the instructions](setting-up-a-local-debug-toolchain.html#openocd).)

Next, you need to configure GDB.

- Set the program to be debugged to the location of the `.elf` file.
- Set the remote target to `localhost:3333`.
- Set the following options as 'set up commands' (to execute right after the connection to GDB):

    ```
    -target-select remote localhost:3333
    -file-exec-and-symbols YOUR_PROJECT_ROOT\BUILD\projectname.elf"
    -interpreter-exec console "monitor reset"
    -interpreter-exec console "monitor halt"
    -interpreter-exec console "monitor arm semihosting enable"
    -target-download
    ```

   Make sure to update the path on line 2 to your `.elf` file.

This starts a debug server, attaches GDB to your development board, flashes the binary using GDB and starts a debug session.
