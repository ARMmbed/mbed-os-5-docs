<h1 id="quick-start-online">Using the Online Compiler</h1>

## Setting up

1. [Create an Mbed account](https://os.mbed.com/account/signup/).
1. If you have an Mbed Board:

    1. Plug your Mbed board into your computer, and open its USB device folder.
    1. Double click on the `MBED.HTML` file. This adds your Mbed board to the Online Compiler as a compilation target.

1. If you don't have a board but still want to follow the quick start:

    1. Go to [os.mbed.com/platforms](http://os.mbed.com/platforms).
    1. Select a board.
    1. On the board page, click **Add to your Mbed Compiler**.

## Importing the code

Click the button below to automatically import the example into the Online Compiler.

[![View Example](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-blinky)](https://github.com/ARMmbed/mbed-os-example-blinky/blob/master/main.cpp)

Alternatively, you may select the import button on the top left hand side of the Online Compiler screen and copy the [example link](https://github.com/ARMmbed/mbed-os-example-blinky) into the prompt.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/import_program.png)</span>

## Compiling and flashing (programming)

1. Click **Compile**.

    **Note:** To build with the Mbed OS bare metal profile, add `"requires": ["bare-metal"]` to the `mbed_app.json` file:

    ```NOCI
    {
        "requires": ["bare-metal"],
        "target_overrides": {
            "*": {
    ```

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/online_compile_button.png)</span>

    The Online Compiler compiles the code into an executable file, which your browser downloads.

1. Open the folder where the executable file was downloaded, and then click and drag (or copy and paste) the file to your Mbed board's USB device folder.

1. Press the board's reset button.
