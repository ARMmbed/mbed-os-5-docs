# Compiling the code

1. Get the code

   After the installation of Mbed CLI is complete, import the example by opening a command-line shell and entering:

   ```console
   $ mbed import https://github.com/ARMmbed/mbed-os-example-blinky
   $ cd mbed-os-example-blinky
   ```

1. Compile and program your board:

   Invoke `mbed compile`, and specify the name of your platform and your installed toolchain (`GCC_ARM`, `ARM`, `IAR`). For example, for the K64F platform and Arm Compiler 5 toolchain:

    ```console
    $ mbed compile --target K64F --toolchain ARM --flash
    ```

   The `--flash` argument automatically flashes the compiled program onto your board if it is connected to your computer.

   <span class="tips">**Tip:** You can get the name of the board plugged into your computer by running `mbed detect`, and you can get a full list of supported toolchains and targets by running the `mbed compile --supported` command.</span>

   <span class="notes">**Note:** To build with the Mbed OS bare metal profile, add `"requires": ["bare-metal"]` to the `mbed_app.json` file:</span>
   ```NOCI
      {
          "requires": ["bare-metal"],
          "target_overrides": {
              "*": {
   ```

1. Press the board's reset button. The LED blinks.
