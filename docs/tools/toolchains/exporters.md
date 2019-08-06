# About the exporters

Use the Arm Mbed exporters to export your code to various third party tools and IDEs. Each exporter implements a `generate` function that produces an IDE specific project file. Exporters benefit from Mbed build tools. However, instead of using your source and [config data](../tools/compile.html) to create an executable, we use that information to populate an IDE project file that will be configured to build, flash and debug your code.

## Arm Mbed CLI command

```
usage: mbed export [-h] [-i IDE] [-m TARGET] [--source SOURCE] [-c] [-S] [-v]
                   [-vv]

Generate IDE project files for the current program.

optional arguments:
  -h, --help            show this help message and exit
  -i IDE, --ide IDE     IDE to create project files for. Example: UVISION4,
                        UVISION5, GCC_ARM, GNUARMECLIPSE, IAR, COIDE
  -m TARGET, --target TARGET
                        Export for target MCU. Example: K64F, NUCLEO_F401RE,
                        NRF51822...
  --source SOURCE       Source directory. Default: . (current dir)
  -c, --clean           Clean the build directory before compiling
  -S, --supported       Shows supported matrix of targets and toolchains
  -v, --verbose         Verbose diagnostic output
  -vv, --very_verbose   Very verbose diagnostic output
```
