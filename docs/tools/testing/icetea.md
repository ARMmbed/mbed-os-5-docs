# Command-line test framework

*Icetea* is an [Arm Mbed](www.mbed.com) test framework written
with python 2.7. It is generally used to verify the Arm Mbed
IoT Device Platform, which provides the operating system and cloud services.

When testing [`Mbed OS`](https://www.mbed.com/en/platform/mbed-os/)
*Icetea* allows you to execute commands remotely via
the command line interface in the Device Under Test (`DUT`).
The `DUT` is running an Mbed application that can connect to the test framework.
The test framework itself runs on your computer.
The interface between the test framework and `DUT` can be
for example UART, a network socket or stdio.
Icetea related applications provided within the `Mbed OS` are using buffered stdio as the interface between the test framework and the `DUT`.

A more detailed description of the *Icetea* concept is
available [here](https://github.com/ARMmbed/icetea/blob/master/doc/README.md).

## Installation

We recommend users to create a separate Python virtual environment for this purpose.
To be able to run the test cases written with Icetea test environment, the Icetea needs to be installed in the system.

### Required dependencies:

* In case you want to use **local mbed devices**
  * [mbed-ls](https://github.com/armmbed/mbed-ls)
    * To enumerate connected boards
  * [mbed-flasher](https://github.com/ARMmbed/mbed-flasher)
    * to flash devices automatically
  * Both of these should be installed automatically by
  Icetea installation.

**OS specific:**

Linux:
* python-dev and python-lxml
`sudo apt-get install python-dev python-lxml`
* For documentation install sphinx:
`apt-get install python-sphinx`

OS X:
* [XCode developer tools](http://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/)
* lxml as described
[here](http://lxml.de/installation.html#installation):
`STATIC_DEPS=true sudo pip install lxml`
* For documentation install sphinx:
`sudo port install py27-sphinx`, `sudo port select --set python python27`,
`sudo port select --set sphinx py27-sphinx`

Windows:
* python-lxml installation is problematic on Windows since
it usually requires build tools. It can however be installed
from pre-built binaries.
    * Download binary for you system from the internet.
    * Navigate to the directory where you downloaded the
    binary and install it with `pip install <insert_file_name>`
* For documentation install sphinx with pip:
`pip install sphinx`

### Optional dependencies

* If you wish to decorate your console log with all kinds of colors,
install the coloredlogs module using pip. `pip install coloredlogs`
    * There have been issues with coloredlogs installation on Windows.
     We might switch to a different module at some point to enable
     colored logging on Windows as well.
* [valgrind](http://valgrind.org)
* [gdb](https://www.gnu.org/software/gdb/)


### Installation step-by-step

```
git clone https://github.com/ARMmbed/icetea.git
cd icetea
python setup.py install
```

**Linux**

In order to run test cases with hardware in Linux without sudo rights:

```
sudo usermod -a -G dialout username
Log out & log in back to Linux
```

This command will add the user 'username' to the 'dialout' group and
grant the required permissions to the USB ports.

## Usage

To print the help page:

`icetea --help`

All cli parameters are described in [icetea.md](https://github.com/ARMmbed/icetea/blob/master/doc/Icetea.md)

To list all local testcases from the `./testcases` subfolder:

`icetea --list`

## Test Case API

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

## Documentation
HTML documentation for Icetea can be built using sphinx. The source
for the documentation is located in [doc-source](https://github.com/ARMmbed/icetea/tree/master/doc-source).
For installation of sphinx see [installation](#installation).

A build script for the documentation is included in build_docs.py.
It's a simple python scripts that also generates autodoc api documentation.
Run the script with:

`python build_docs.py`

Currently similar documentation is available in markdown format in
[doc](doc). This documentation will be phased out and is not maintained
as well as the sphinx documentation.

## Examples

**Note:** Following examples uses [`dummyDut`](https://github.com/ARMmbed/icetea/blob/master/test/dut/dummyDut.c)
application. It works in unix systems.
To run following examples please compile `dummyDut` first using make:
`> make -C test/dut`.

To print available parameters:

`> icetea --help`

To run a single test case with the process dut:

`> icetea --tc test_cmdline --tcdir examples --type process --bin ./test/dut/dummyDut`

To run all existing test cases from the `examples` folder:

`> icetea --tc all --tcdir examples --type process --bin ./test/dut/dummyDut`

To debug dut locally with [GDB](https://www.gnu.org/software/gdb/):

**Note:** You have to install [gdb](https://www.gnu.org/software/gdb/) first (`apt-get install gdb`)

```
> icetea --tc test_cmdline --tcdir examples --type process --gdb 1 --bin ./test/dut/dummyDut
> sudo gdb ./CliNode 3460
```

To debug dut remotely with GDB server:

```
> icetea --tc test_cmdline --tcdir examples --type process --gdbs 1 --bin  ./test/dut/dummyDut
> gdb  ./test/dut/dummyDut --eval-command="target remote localhost:2345"
```

To analyse memory leaks with valgrind:

**Note:** You have to install [valgrind](http://valgrind.org) first (`apt-get install valgrind`)
```
> icetea --tc test_cmdline --tcdir examples --type process --valgrind --valgrind_tool memcheck --bin  ./test/dut/dummyDut
```

## Running unit tests with *Icetea*

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

To generate a coverage reports for plugin unit tests run:

```
> coverage html --include "icetea_lib/Plugin/plugins/*" --omit "icetea_lib/Plugin/plugins/plugin_tests/*"
```

### Dependencies

Unit tests depend on mock, coverage and netifaces.

```
> pip install mock
> pip install netifaces
> pip install coverage
```

## License

See the [license](https://github.com/ARMmbed/icetea/blob/master/LICENSE) agreement.
