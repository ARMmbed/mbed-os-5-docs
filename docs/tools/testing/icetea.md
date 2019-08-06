<h1 id="icetea">Icetea test framework</h1>

Icetea is an automated testing framework for Mbed development. It automates the process of flashing Mbed boards, running tests and accumulating test results into reports. Developers use it for local development, as well as automation in a Continuous Integration environment.

When testing Mbed OS, Icetea allows you to execute commands remotely by using the command-line interface in a device under test (DUT). The interface between the test framework and a DUT might be, for example, UART or stdio.

More detailed documentation on the tool is available [in rst format](https://github.com/ARMmbed/icetea/tree/master/doc-source) and [in markdown format](https://github.com/ARMmbed/icetea/tree/master/doc).

## Prerequisites

Icetea supports Linux (Ubuntu preferred), Windows and OS X. Our main target is Linux.

You need `pip` to install Icetea.

Icetea supports both Python 2.7 and 3.5, or later. Some OS specific prerequisites are listed below:

- Linux.
   - python-dev and python-lxml:
      `sudo apt-get install python-dev python-lxml`
   - To run test cases with hardware in Linux, without sudo rights:
   
      ```
      sudo usermod -a -G dialout username
      Log out & log in back to Linux
      ```
   
      This command adds the user `username` to the `dialout` group and grants the required permissions to the USB ports.
      
- OS X.
   - [XCode developer tools](http://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/).
   - [MacPorts](https://www.macports.org/install.php).
   - [lxml](http://lxml.de/installation.html#installation):
      `STATIC_DEPS=true sudo pip install lxml`

- Windows
   - python-lxml installation on Windows usually requires build tools. You can, however, install it from prebuilt binaries.
      - Search the internet for a binary for your system.
      - Navigate to the directory where you downloaded the binary, and install it with `pip install <insert_file_name>`
   - You can also follow [these instructions](http://lxml.de/installation.html#installation) instead.

### Optional

If you wish to decorate your console log with colors, install the `coloredlogs` module by using pip: `pip install coloredlogs`. There have been issues with `coloredlogs` installation on Windows. There are no alternative solutions for this at the moment.

## Installation

`> pip install icetea`

## Use

To display the help page:

`icetea --help`

To list all local test cases from the examples subfolder:

`icetea --list --tcdir examples`

To print the Icetea version:

`icetea --version`

### Typical use

All of the commands described below might also require other commands, depending on the test case.

**Running test cases by using the `tc` argument**

`> icetea --tc <test case name> --tcdir <test case search path>`

To run all existing test cases from the `examples` folder:

`> icetea --tc all --tcdir examples`

**Running an example test case with hardware**

This example requires a compatible board connected to the computer and an application binary for the board. The test case below is available in [the Icetea GitHub repository](https://github.com/ARMmbed/icetea/blob/master/examples/test_cmdline.py).

`> icetea --tc test_cmdline --tcdir examples --type hardware --bin <path to a binary>`

**Using metadata filters**

To run all test cases with test-type regression in the metadata:

`> icetea --testtype regression --tcdir <test case search path>`

The following metadata filters are available:

- test type (`--testtype`).
- test subtype (`--subtype`).
- feature (`--feature`).
- test case name (`--tc`).
- tested component (`--component`).
- test case folder (`--group`).

**Running a premade suite**

Icetea supports a suite file that describes a number of test cases in `json` format:

`> icetea --suite <suite file name> --tcdir <test case search path> --suitedir <path to suite directory>`

**Enabling debug level logging**

Use `-v` or `-vv` arguments to control logging levels. `-v` increases the framework's logging level to debug (default is info), the level of logging in certain plugins and external components to info (default is warning). `--vv` increases the level of logging on all Icetea loggers to debug.

### Creating a test case

Icetea test cases are implemented as Python classes that inherit the bench object available in the `icetea_lib.bench` module. The test case needs to have an initialization function that defines the metadata and a case function that implements the test sequence. There are two optional functions: setup and teardown.

An example test case is shown below:

```
"""
Copyright 2017 ARM Limited
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from icetea_lib.bench import Bench


class Testcase(Bench):
    def __init__(self):
        Bench.__init__(self,
                       name="example_test",
                       title="Example test",
                       status="development",
                       purpose="Show example of a test",
                       component=["examples"],
                       type="smoke",
                       requirements={
                           "duts": {
                               '*': {
                                    "count": 1,
                                    "type": "hardware"
                               }
                           }
                       }
                       )

    def setup(self):
        # nothing for now
        pass


    def case(self):
        self.command(1, "echo hello world", timeout=5)
        self.command("help")

    def teardown(self):
        # nothing for now
        pass
```

## License

For licensing details, please see the [license agreement](https://github.com/ARMmbed/icetea/blob/master/LICENSE).
