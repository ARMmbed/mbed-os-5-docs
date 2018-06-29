## Import, Compile, Flash

To run code on your board you will need to import the code from a URL (either git or mercurial), then compile the code using the compiler you installed, and then flash the code onto the board. 

### Online

#### Import

To import code into the online compiler you will need the URL of the git or mercurial repository. Once you have it open the [Online Compiler](http://os.mbed.com/compiler), click the **Import** button on the online compiler, then click the link to **Import from URL**, paste the URL intot he box and click **import**. 

![](images/import_online.gif) 

#### Compile

To compile your code make sure your target is selected in the top right corner of the online compiler, then click **Compile**. If the compile is successful then you will be prompted to save a file to your computer. Save it to your `Downloads` folder. 

![](images/compile_online.gif)

#### Flash

To program the board you simply drag and drop the binary to the board, like moving a file onto a flash drive. The board will accept the binary and then program itself. Thats it! Super simple!

![](images/flash_online.gif)


### Offline

#### Import

To import code using Mbed CLI use the `mbed import <URL>` command, where the `<URL>` is a valid git or mercurial repository.

For example: `mbed import http://github.com/armmbed/mbed-os-example-blinky`

This will clone the repository and all sub dependencies to your machine. 

#### Compile

To compile your code you can either do it the verbose way, or the easy way. 

The verbose way involves specifying your target and compiler toolchain every time. This command looks like this `mbed compile --target <target> --toolchain <TOOLCHAIN>`. To find your `<target>` name and `<TOOLCHAIN>` name you can run `mbed compile --supported` to get a full list of supported targets and toolchains, or you can run `mbed detect` to find the target name of the board connected to your computer. For example `mbed compile --target K64F --toolchain GCC_ARM`. 

The easy way involves setting your toolchain and target globally, for all projects. 

`mbed config -G toolchain GCC_ARM` - set your compiler toolchain for all projects you compile
`mbed config -G target auto` - set the target to be whatever is connected to your computer and detected by the `mbed detect` command. 
`mbed compile` - compile the program, the two configuration commands you


#### Flash

To flash your code to the board you can either open up the `BUILD` directory in your project and find the compiled binary, then drag and drop it to the board, or you can simply add the `--flash` command to your compile command to automatically flash the board. 

For example: `mbed compile --flash`, with both compile the binary and then flash the binary to your board. 

#### Other useful commands

Some other useful commands to know about:
- `mbed config --list` - check your configuration options
- `mbed sterm` - open serial terminal connected to the board
- `mbed compile --flash --sterm` - compile, flash and open serial terminal to board
- `mbed cache on` - turn on caching of the mbed-os library so you dont have to download it for every project. This helps when offline or in an area with slow internet


