# Compiling the code

1. When Mbed CLI is installed, get the code for the Mbed OS full profile or bare metal profile.

    Open a command-line shell.

    For the full profile, enter:

    ```console
    $ mbed import https://github.com/ARMmbed/mbed-os-example-blinky
    $ cd mbed-os-example-blinky
    ```

    For the bare metal profile, enter:

    ```console
    $ mbed import https://github.com/ARMmbed/mbed-os-example-blinky-baremetal
    $ cd mbed-os-example-blinky-baremetal
    ```

    The rest of the workflow is identical for both profiles.

1. Compile and program your board:

   Invoke `mbed compile`, and specify the name of your build target and your installed toolchain (`GCC_ARM`, `ARM`, `IAR`). For example, for the K64F board and ARM toolchain:

    ```console
    $ mbed compile --target K64F --toolchain ARM --flash
    ```

   The `--flash` argument automatically flashes the compiled program onto your board if it is connected to your computer.

   <span class="tips">**Tip:** You can get the name of the board plugged into your computer by running `mbed detect`, and you can get a full list of supported toolchains and targets by running the `mbed compile --supported` command.</span>

1. Press the board's reset button. The LED blinks.
