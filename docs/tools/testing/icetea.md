## Icetea test framework

Icetea is an automated testing framework for Mbed development.
It automates the process of flashing Mbed boards, running tests
and accumulating test results into reports.
Developers use it for local development as well as for
automation in a Continuous Integration Environment.

When testing [`Mbed OS`](https://www.mbed.com/en/platform/mbed-os/)
Icetea allows you to execute commands remotely via
the command line interface (`CLI`) in a device under test (`DUT`).
The interface between the test framework and `DUT` can be
for example UART or stdio.

More detailed documentation on the tool is available
[here in rst format](https://github.com/ARMmbed/icetea/tree/master/doc-source)
and [here in markdown format](https://github.com/ARMmbed/icetea/tree/master/doc).

### Prerequisites
Icetea supports Linux (Ubuntu preferred), Windows and OS X. Our main target is Linux.
We support both Python 2.7 and 3.5 or later. Some OS specific prerequisites below:

* Linux
    * python-dev and python-lxml
        `sudo apt-get install python-dev python-lxml`
    * In order to run test cases with hardware in Linux without sudo rights:
        ```
        sudo usermod -a -G dialout username
        Log out & log in back to Linux
        ```
        This command will add the user 'username' to the 'dialout' group and
        grant the required permissions to the USB ports.
* OS X
    * [XCode developer tools](http://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/)
    * [MacPorts](https://www.macports.org/install.php)
    * [lxml](http://lxml.de/installation.html#installation):
        `STATIC_DEPS=true sudo pip install lxml`

* Windows
    * python-lxml installation is problematic on Windows since
    it usually requires build tools. It can however be installed
    from pre-built binaries.
        * Search for a binary for you system from the internet.
        * Navigate to the directory where you downloaded the
        binary and install it with `pip install <insert_file_name>`
    * You can follow instructions [here](http://lxml.de/installation.html#installation)
    instead.

#### Optional

* If you wish to decorate your console log with all kinds of colors,
install the coloredlogs module using pip. `pip install coloredlogs`
    * There have been issues with coloredlogs installation on Windows.
     We might switch to a different module at some point to enable
     colored logging on Windows as well.

### Installation

`> pip install icetea`

### Usage

To print the help page:

`icetea --help`

To list all local testcases from the examples subfolder:

`icetea --list --tcdir examples`

To print Icetea version:

`icetea --version`

#### Typical use

All of the commands described below might also need other options,
depending on the test case.

**Running test cases using the tc argument**

`> icetea --tc <test case name> --tcdir <test case search path>`

To run all existing test cases from the `examples` folder:

`> icetea --tc all --tcdir examples`

**Running an example test case with hardware**

In this example, we assume that a compatible board has been connected
to the computer and an application binary for the board is available.
The referred test case is available in [the icetea github repository](https://github.com/ARMmbed/icetea/blob/master/examples/test_cmdline.py).

`> icetea --tc test_cmdline --tcdir examples --type hardware --bin <path to a binary>`

**Using metadata filters**

To run all test cases with testtype regression in the metadata:

`> icetea --testtype regression --tcdir <test case search path>`

The following metadata filters are available:
* test type (--testtype)
* test subtype (--subtype)
* feature (--feature)
* test case name (--tc)
* tested component (--component)
* test case folder (--group)

**Running a premade suite**

Icetea supports a suite file that describes a suite of test cases
in `json` format.

`> icetea --suite <suite file name> --tcdir <test case search path> --suitedir <path to suite directory>`

**Enabling debug level logging**

Use -v or -vv arguments to control logging levels. -v increases the frameworks logging level
to debug (default is info) and the level of logging in
certain plugins and external components to info (default is warning).
--vv increases the level of logging on all Icetea loggers to debug.

**Further details**

For further details on any of the features see our documentation.

#### Creating a test case
Icetea test cases are implemented as Python classes that inherit the Bench object available in `icetea_lib.bench` module.
The test case needs to have an initialization function that defines the metadata and a case function that implements the test sequence.
There are two optional functions, setup and teardown. More information is available in our documentation.

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

### License
See the [license](https://github.com/ARMmbed/icetea/blob/master/LICENSE) agreement.
