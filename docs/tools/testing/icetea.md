## Command-line test framework

*Icetea* is an Arm Mbed test framework written with Python 2.7. You can use it to verify the Arm Mbed IoT Device Platform, which provides the operating system and cloud services.

When testing Mbed OS, *Icetea* allows you to execute commands remotely using the command-line interface in the Device Under Test (`DUT`). The `DUT` runs an Mbed application that can connect to the test framework. The test framework itself runs on your computer. The interface between the test framework and `DUT` can be, for example, UART, a network socket or stdio. Icetea-related applications provided within Mbed OS use buffered stdio as the interface between the test framework and the `DUT`.

### Installation

We recommend creating a separate Python virtual environment for this purpose. To be able to run the test cases written with the Icetea test environment, you need to install Icetea in the system.

#### Required dependencies:

- To use **local Mbed devices**
  - [mbed-ls](https://github.com/armmbed/mbed-ls).
    - To enumerate connected boards.
  - [mbed-flasher](https://github.com/ARMmbed/mbed-flasher).
    - To flash devices automatically.
  - Icetea installation installs both of these automatically.
  
**OS specific:**

Linux:

- `python-dev` and `python-lxml`
`sudo apt-get install python-dev python-lxml`
- For documentation, install sphinx:
`apt-get install python-sphinx`

OS X:

- [XCode developer tools](http://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/).
- [lxml](http://lxml.de/installation.html#installation):
`STATIC_DEPS=true sudo pip install lxml`
- For documentation, install sphinx:
`sudo port install py27-sphinx`, `sudo port select --set python python27`, `sudo port select --set sphinx py27-sphinx`

Windows:

- `python-lxml` installation usually requires build tools. You can, however, install it from prebuilt binaries.
    - Download the binary for your system from the internet.
    - Navigate to the directory where you downloaded the binary, and install it with `pip install <insert_file_name>`.
- For documentation, install sphinx with pip:
`pip install sphinx`

#### Optional dependencies

- To decorate your console log with colors, install the coloredlogs module using pip:
`pip install coloredlogs`
    - Windows does not support the coloredlogs module.
- [valgrind](http://valgrind.org).
- [gdb](https://www.gnu.org/software/gdb/).

#### Installation instructions

```
git clone https://github.com/ARMmbed/icetea.git
cd icetea
python setup.py install
```

**Linux**

To run test cases with hardware in Linux without sudo rights:

```
sudo usermod -a -G dialout username
Log out & log in back to Linux
```

This command adds the user `username` to the `dialout` group and grants the required permissions to the USB ports.

### Use

To print the help page:

`icetea --help`

All CLI parameters are described in [icetea.md](https://github.com/ARMmbed/icetea/blob/master/doc/Icetea.md)

To list all local testcases from the `./testcases` subfolder:

`icetea --list`

#### Test case API

To execute a single command line:

` execute_command(<dut>, <cmd>, (<arguments>) ) `

or alias `command(...)`


```
dut[number]             #dut index (1..)
dut[string]             #dut nick name, or '*' to execute command in all duts
cmd[string]             #command to be executed
arguments[dictionary]   #optional argument list
        wait = <boolean>           # whether retcode is expected before continue next command. True (default) or False
        expected_retcode = <int>    # expected return code (default=0)
        timeout=<int>              # timeout, if no retcode receive
```

### Documentation

You can build HTML documentation for Icetea using sphinx. The source for the documentation is located in [doc-source](https://github.com/ARMmbed/icetea/tree/master/doc-source). For installation of sphinx, please see the [installation instructions](#installation).

A build script for the documentation is included in `build_docs.py`. It's a Python script that also generates autodoc API documentation. Run the script with:

`python build_docs.py`

### Examples

**Note:** The following examples use the [`dummyDut`](https://github.com/ARMmbed/icetea/blob/master/test/dut/dummyDut.c) application. It works in unix systems. To run the following examples, please compile `dummyDut` using Make:

`> make -C test/dut`.

To print available parameters:

`> icetea --help`

To run a single test case with the process DUT:

`> icetea --tc test_cmdline --tcdir examples --type process --bin ./test/dut/dummyDut`

To run all existing test cases from the `examples` folder:

`> icetea --tc all --tcdir examples --type process --bin ./test/dut/dummyDut`

To debug DUT locally with [GDB](https://www.gnu.org/software/gdb/):

**Note:** You have to install [GDB](https://www.gnu.org/software/gdb/) first (`apt-get install gdb`).

```
> icetea --tc test_cmdline --tcdir examples --type process --gdb 1 --bin ./test/dut/dummyDut
> sudo gdb ./CliNode 3460
```

To debug DUT remotely with the GDB server:

```
> icetea --tc test_cmdline --tcdir examples --type process --gdbs 1 --bin  ./test/dut/dummyDut
> gdb  ./test/dut/dummyDut --eval-command="target remote localhost:2345"
```

To analyze memory leaks with valgrind:

**Note:** You have to install [valgrind](http://valgrind.org) first (`apt-get install valgrind`):

```
> icetea --tc test_cmdline --tcdir examples --type process --valgrind --valgrind_tool memcheck --bin  ./test/dut/dummyDut
```

### Running unit tests with *Icetea*

To build a test application for DUT and execute the test:

```
> make
> coverage run -m unittest discover -s test
```

To generate a coverage report (excluding plugins):

```
> coverage html --include "icetea_lib/*" --omit "icetea_lib/Plugin/plugins/*"
```

To run unit tests for plugins that ship with Icetea:

```
> coverage run -m unittest discover -s icetea_lib/Plugin/plugins/plugin_tests
```

To generate a coverage reports for plugin unit tests, run:

```
> coverage html --include "icetea_lib/Plugin/plugins/*" --omit "icetea_lib/Plugin/plugins/plugin_tests/*"
```

#### Dependencies

Unit tests depend on mock, coverage and netifaces.

```
> pip install mock
> pip install netifaces
> pip install coverage
```

### License

See the [license](https://github.com/ARMmbed/icetea/blob/master/LICENSE) agreement.
