## Icetea testing applications

### Using tests

#### Test code structure

Icetea tests are composed of two parts. One is the C++-application running on the Device Under Test (DUT). The other part is the Python script running on your computer. The provided C++ applications running on the DUT are actually command-line interface (CLI) applications that you can run on their own and give commands to the DUT over a serial console. The test cases are provided as Python scripts, and each Python script is tied to a specific C++ application.

You can find the Icetea test applications and test cases under the `TEST_APPS` folder in `mbed-os`. `TEST_APPS/device` lists all of the C++ test applications. `TEST_APPS/icetea_plugins` contains plugins for the test cases. These are mainly parsers that provide a functionality for the test scripts to parse the DUT provided output from the serial console. `TEST_APPS/testcases` lists all the tests and any possible utility scripts the tests need.

##### Test discovery

When using Icetea under the `mbed-os repository`, the `TEST_APPS folder` stores the CLI applications and the test cases. The `TEST_APPS` folder is located in the root of the `mbed-os` repository. If you are using Icetea somewhere else, you need to provide Icetea the information where the tests reside. You can do this with the `--tcdir <directory>` option.

##### Test names

Test names are defined in the Python scripts themselves. For example, the `SOCKET_BIND_PORT.py` contains two test cases; `TCPSOCKET_BIND_PORT` and `UDPSOCKET_BIND_PORT` are both defined in the Python file.

#### Building tests

You can build tests through Arm Mbed CLI. For information on using Mbed CLI, please see the [CLI documentation](/docs/development/tools/arm-mbed-cli.html).

When you build tests for a target and a toolchain, the script first discovers the available tests, then the C++ applications linked to the tests and then builds the C++ applications in parallel.

##### Building process

The `test.py` script (not to be confused with `tests.py`) located under the `tools` directory handles the process for building tests. This handles the discovery and building of all test cases for a target and toolchain.

The full build process is:

1. Build the nontest code (all code not under a `TESTS` folder), but do not link it. The resulting object files are placed in the build directory.
1. Find all tests that match the given target and toolchain.
1. Find all the C++ applications that are defined in the tests.
1. For each discovered C++ application, build all of its source files and link it with the nontest code that was built in step 1.
1. If specified, create a test specification file and place it in the given directory for use by testing tools. This is placed in the build directory by default when using Mbed CLI.

#### Running tests

You can run automated tests through Mbed CLI with the `--icetea` option. You can find more information about this in the [Mbed CLI test documentation] (/docs/tools/offline/cli-test-debug.md).

The testing process requires tests to be built and that a test specification JSON file exist that describes these available tests. See the [test specification format](https://github.com/ARMmbed/greentea#test-specification-json-formatted-input).

The test specification JSON is similar for the Greentea and Icetea tests.

The Icetea tool handles the actual testing process. To read more about this tool, please visit its [GitHub repository](https://github.com/ARMmbed/icetea).

#### Writing tests

##### Writing test cases

For writing your own Python test scripts, you can read further information from [Icetea Test Case API](https://github.com/ARMmbed/icetea/blob/master/doc/tc_api.md).

##### Writing CLI applications

To be able to run the commands given to the DUT, you need to provide a CLI application that runs on the DUT. There is a library that you can use to create your own CLI application; it is called [mbed-client-cli](https://github.com/ARMmbed/mbed-client-cli). You can also find example Mbed CLI applications from the `mbed-os` repository [test applications](https://github.com/ARMmbed/mbed-os/tree/master/TEST_APPS/device).

### Debugging tests

Debugging tests is a crucial part of the development and porting process. This section covers exporting the test, then driving the test with the test tools while the target is attached to a debugger.

#### Exporting tests

The most straightforward way to export a test is to copy the test application's source code from its test directory to your project's root. This way, the tools treat it like a normal application.

You can find the path to the test application you wish to export by running the following command:

```
mbed test --compile-list -n <test name> --icetea
```

Once you've copied all of the test's source files to your project root, export your project:

```
mbed export -i <IDE name>
```

You can find your exported project in the root project directory.

#### Running a test while debugging

After you export your test to your IDE, build the project, and load it onto your target using your debugger.

Bring the target out of reset, and run the program. Your target waits for a command over serial line.

You can now use Icetea commands to run the test:

```
icetea -m <target> -t <toolchain> --tc <path to testcase>
```

This detects your attached target and drives the test. If you need to rerun the test, reset the device with your debugger, run the program and run the same command.

For an explanation of the arguments used in this command, please run `icetea --help`.

Note that instead of running the test you can also open a serial connection to the target and give the Mbed CLI commands manually.
