# Greentea testing applications

Greentea is the automated testing tool for Arm Mbed OS development. It's a test runner that automates the process of flashing development boards, starting tests and accumulating test results into test reports. You can use it for local development, as well as for automation in a continuous integration environment.

Greentea tests run on embedded devices, but Greentea also supports `host tests`. These are Python scripts that run on a computer and can communicate back to the embedded device. You can, for example, verify that a value wrote to the cloud when the device said it did.

This document will help you start using Greentea. Please see the [`htrun` documentation](https://github.com/ARMmbed/mbed-os-tools/tree/master/packages/mbed-host-tests), the tool Greentea uses to drive tests, for the technical details of the interactions between the platform and the host machine.

## Using tests

### Test code structure

You can run tests throughout Mbed OS and for your project's code. They are located under a special directory called `TESTS`.

The fact that the code is located under this directory means that it is ignored when building applications and libraries. It is only used when building tests. This is important because all tests require a `main()` function, and building them with your application would cause multiple `main()` functions to be defined.

The macro `MBED_TEST_MODE` is defined when building tests with Mbed CLI versions 1.9.0 and later. You can wrap your application's `main()` function in a preprocessor check to prevent multiple `main()` functions from being defined:

```c++
#if !MBED_TEST_MODE
int main() {
    // Application code
}
#endif
```

In addition to being placed under a `TESTS` directory, test sources must exist under two other directories: a test group directory and a test case directory. The following is an example of this structure:

```
myproject/TESTS/test_group/test_case_1
```

In this example, `myproject` is the project root, and all the source files under the `test_case_1` directory are included in the test. The test build also includes any other source files from the OS, libraries and projects that apply to the target's configuration.

<span class="notes">**Note:** You can name both the test group and the test case directory anything you like. However, you must name the `TESTS` directory `TESTS` for the tools to detect the test cases correctly.</span>

#### Test discovery

Because test cases can exist throughout a project, the tools must find them in the project's file structure before building them.

Test discovery also obeys the same rules that are used when building your project. This means that tests that are placed under a directory with a prefix, such as `TARGET_`, `TOOLCHAIN_` or `FEATURE_`, are only discovered, built and run if your current configuration matches this prefix.

For example, if you place a test under the directory `FEATURE_BLE` with the following path:

```
myproject/mbed-os/features/FEATURE_BLE/TESTS/ble_tests/unit_test
```

This test case is only discovered if the target being tested supports the BLE feature. Otherwise, the test is ignored.

Generally, a test should not be placed under a `TARGET_` or `TOOLCHAIN_` directory because most tests should work for all target and toolchain configurations.

Tests can also be completely ignored by using the `.mbedignore` file described in the [documentation](../reference/mbed-os-build-rules.html).

#### Test names

A test case is named by its position in your project's file structure. For instance, in the above example, a test case with the path `myproject/TESTS/test_group/test_case_1` would be named `tests-test_group-test_case_1`. The name is created by joining the directories that make up the path to the test case with a dash `-` character. This is a unique name to identify the test case. You will see this name throughout the build and testing process.

### Building tests

You can build tests through Arm Mbed CLI. For information on using Mbed CLI, please see the [CLI documentation](../tools/developing-mbed-cli.html).

When you build tests for a target and a toolchain, the script first discovers the available tests and then builds them in parallel. You can also create a **test specification** file, which our testing tools can use to run automated hardware tests. For more information on the test specification file, please see the [Greentea documentation](https://github.com/ARMmbed/mbed-os-tools/tree/master/packages/mbed-greentea#test-specification-json-formatted-input).

#### Building process

The `test.py` script (not to be confused with `tests.py`), located under the `tools` directory, handles the process for building tests. It handles the discovery and building of all test cases for a target and toolchain.

The full build process is:

1. Build the non-test code (all code not under a `TESTS` folder), but do not link it. The resulting object files are placed in the build directory.
1. Find all tests that match the given target and toolchain.
1. For each discovered test, build all of its source files and link it with the non-test code that was built in step 1.
1. If specified, create a test specification file and place it in the given directory for use by the testing tools. This is placed in the build directory by default when using Mbed CLI.

#### Application configuration

When building an Mbed application, the presence of an `mbed_app.json` file allows you to set or override different configuration settings from libraries and targets. However, because the tests share a common build, this can cause issues when tests have different configurations that affect the OS.

The build system looks for an `mbed_app.json` file in your shared project files (any directory not inside of a `TESTS` folder). If the system finds it, then this configuration file is used for both the non-test code and each test case inside your project's source tree. If there is more than one `mbed_app.json` file in the source tree, then the configuration system will error.

If you need to test with multiple configurations, then you can use the `--app-config` option. This overrides the search for an `mbed_app.json` file and uses the configuration file that you specify for the build.

## Writing your first test

You can write tests for your own project or add more tests to Mbed OS. You can write tests by using the [Greentea client](https://github.com/ARMmbed/mbed-os/tree/master/features/frameworks/greentea-client) and the [UNITY](https://github.com/ARMmbed/mbed-os/tree/master/features/frameworks/unity) and [utest](https://github.com/ARMmbed/mbed-os/tree/master/features/frameworks/utest) frameworks, which are located in `/features/frameworks`.

To write your first test, use Mbed CLI to create a new project:

```
$ mbed new first-greentea-test
```

By convention, all tests live in the `TESTS/` directory. In the `first-greentea-test` folder, create a folder `TESTS/test-group/simple-test/`.

```
first-greentea-test/
└── TESTS/
    └── test-group/
        └── simple-test/
            └── main.cpp
```

*Test structure for Greentea tests*

In this folder, create a file `main.cpp`. You can use UNITY, utest and the Greentea client to write your test:

```cpp
#include "mbed.h"
#include "utest/utest.h"
#include "unity/unity.h"
#include "greentea-client/test_env.h"

using namespace utest::v1;

// This is how a test case looks
static control_t simple_test(const size_t call_count) {
    /* test content here */
    TEST_ASSERT_EQUAL(4, 2 * 2);

    return CaseNext;
}

utest::v1::status_t greentea_setup(const size_t number_of_cases) {
    // Here, we specify the timeout (60s) and the host test (a built-in host test or the name of our Python file)
    GREENTEA_SETUP(60, "default_auto");

    return greentea_test_setup_handler(number_of_cases);
}

// List of test cases in this file
Case cases[] = {
    Case("simple test", simple_test)
};

Specification specification(greentea_setup, cases);

int main() {
    return !Harness::run(specification);
}
```

### Running the test

<span class="tips">**Tip:** To see all tests, run `mbed test --compile-list`.</span>

Run the test:

```
# run the test with the GCC_ARM toolchain, automatically detect the target, and run in verbose mode (-v)
$ mbed test -t GCC_ARM -m auto -v -n tests-test-group-simple-test
```

This yields (on a NUCLEO F411RE):

```
mbedgt: test suite report:
+-----------------------+---------------+------------------------------+--------+--------------------+-------------+
| target                | platform_name | test suite                   | result | elapsed_time (sec) | copy_method |
+-----------------------+---------------+------------------------------+--------+--------------------+-------------+
| NUCLEO_F411RE-GCC_ARM | NUCLEO_F411RE | tests-test-group-simple-test | OK     | 16.84              | default     |
+-----------------------+---------------+------------------------------+--------+--------------------+-------------+
mbedgt: test suite results: 1 OK
mbedgt: test case report:
+-----------------------+---------------+------------------------------+-------------+--------+--------+--------+--------------------+
| target                | platform_name | test suite                   | test case   | passed | failed | result | elapsed_time (sec) |
+-----------------------+---------------+------------------------------+-------------+--------+--------+--------+--------------------+
| NUCLEO_F411RE-GCC_ARM | NUCLEO_F411RE | tests-test-group-simple-test | simple test | 1      | 0      | OK     | 0.01               |
+-----------------------+---------------+------------------------------+-------------+--------+--------+--------+--------------------+
mbedgt: test case results: 1 OK
mbedgt: completed in 18.64 sec
```

Change the test in a way that it fails (for example, expect 6 instead of 4), rerun the test and observe the difference.

## Writing integration tests using host tests

The previous test was self-contained. Everything that ran only affected the microcontroller. However, typical test cases involve peripherals in the real world. This raises questions such as: Did my device actually get an internet connection, or did my device actually register with my cloud service? (We have [a lot of these](https://github.com/ARMmbed/simple-mbed-cloud-client/tree/master/TESTS) for Pelion Device Management.) To test these scenarios, you can use a host test that runs on your computer. After the device says it did something, you can verify that it happened and then pass or fail the test accordingly.

To interact with the host test from the device, you can use two functions: `greentea_send_kv` and `greentea_parse_kv`. The latter blocks until it gets a message back from the host.

### Creating the host test

This example writes an integration test that sends `hello` to the host and waits until it receives `world`. Create a file called `hello_world_tests.py` in the `TESTS/host_tests` folder, and fill it with:

```py
from mbed_host_tests import BaseHostTest
from mbed_host_tests.host_tests_logger import HtrunLogger
import time

class HelloWorldHostTests(BaseHostTest):
    def _callback_init(self, key, value, timestamp):
        self.logger.prn_inf('Received \'init\' value=%s' % value)

        # sleep...
        time.sleep(2)

        # if value equals 'hello' we'll send back world, otherwise not
        if (value == 'hello'):
            self.send_kv('init', 'world')
        else:
            self.send_kv('init', 'not world')

    def setup(self):
        # all functions that can be called from the client
        self.register_callback('init', self._callback_init)

    def result(self):
        pass

    def teardown(self):
        pass

    def __init__(self):
        super(HelloWorldHostTests, self).__init__()

        self.logger = HtrunLogger('TEST')
```

This registers one function you can call from the device: `init`. The function checks whether the value was `hello`, and if so, returns `world` back to the device using the `send_kv` function.

### Creating the Greentea test

This example writes the embedded part of this test. Create a new file `main.cpp` in `TESTS/tests/integration-test`, and fill it with:

```cpp
#include "mbed.h"
#include "utest/utest.h"
#include "unity/unity.h"
#include "greentea-client/test_env.h"

using namespace utest::v1;

static control_t hello_world_test(const size_t call_count) {
    // send a message to the host runner
    greentea_send_kv("init", "hello");

    // wait until we get a message back
    // if this takes too long, the timeout will trigger, so no need to handle this here
    char _key[20], _value[128];
    while (1) {
        greentea_parse_kv(_key, _value, sizeof(_key), sizeof(_value));

        // check if the key equals init, and if the return value is 'world'
        if (strcmp(_key, "init") == 0) {
            TEST_ASSERT_EQUAL(0, strcmp(_value, "world"));
            break;
        }
    }

   return CaseNext;
}

utest::v1::status_t greentea_setup(const size_t number_of_cases) {
   // here, we specify the timeout (60s) and the host runner (the name of our Python file)
   GREENTEA_SETUP(60, "hello_world_tests");
   return greentea_test_setup_handler(number_of_cases);
}

Case cases[] = {
   Case("hello world", hello_world_test)
};

Specification specification(greentea_setup, cases);

int main() {
   return !Harness::run(specification);
}
```

You see the calls to and from the host through the `greentea_send_kv` and `greentea_parse_kv` functions. Note the `GREENTEA_SETUP` call. This specifies which host test to use, and the test is then automatically loaded when running (based on the Python name).

Run the test:

```
$ mbed test -v -n tests-test-group-integration-test
```

## Debugging tests

Debugging tests is a crucial part of the development and porting process. This section covers exporting the test and driving the test with the test tools while the target is attached to a debugger.

### Exporting tests

The easiest way to export a test is to copy the test's source code from its test directory to your project's root. This way, the tools treat it like a normal application.

You can find the path to the test that you want to export by running the following command:

```
mbed test --compile-list -n <test name>
```

Once you've copied all of the test's source files to your project root, export your project:

```
mbed export -i <IDE name>
```

You can find your exported project in the root project directory.

### Running a test while debugging

Assuming your test was exported correctly to your IDE, build the project and load it onto your target by using your debugger.

Bring the target out of reset and run the program. Your target waits for the test tools to send a synchronizing character string over the serial port. Do not run the `mbed test` commands because that will attempt to flash the device, which you've already done with your IDE.

Instead, you can use the underlying test tools to drive the test. [`htrun`](https://github.com/ARMmbed/mbed-os-tools/tree/master/packages/mbed-host-tests) is the tool you need to use in this scenario. Installing the requirements for Mbed OS also installs `htrun`. You can also install `htrun` by running `pip install mbed-host-tests`.

First, find your target's serial port by running the following command:

```
$ mbed detect

[mbed] Detected KL46Z, port COM270, mounted D:

...
```

From the output, take note of your target's serial port (in this case, it's `COM270`).

Run the following command when your device is running the test in your debugger:

```
mbedhtrun --skip-flashing --skip-reset -p <serial port>:9600
```

Replace `<serial port>` with the serial port that you found by running `mbed detect` above. So, for the example above, the command is:

```
mbedhtrun --skip-flashing --skip-reset -p COM270:9600
```

This detects your attached target and drives the test. If you need to rerun the test, reset the device with your debugger, run the program and run the same command.

For an explanation of the arguments used in this command, please run `mbedhtrun --help`.

## Command-line use

This section highlights a few of the capabilities of the Greentea command-line interface. For a full list of the available options, please run `mbed test --help`.

### Listing all tests

You can use the `--compile-list` argument to list all available tests:

```
$ mbed test --compile-list
[mbed] Working path "/Users/janjon01/repos/first-greentea-test" (program)
Test Case:
    Name: mbed-os-components-storage-blockdevice-component_flashiap-tests-filesystem-fopen
    Path: ./mbed-os/components/storage/blockdevice/COMPONENT_FLASHIAP/TESTS/filesystem/fopen
Test Case:
    Name: mbed-os-features-cellular-tests-api-cellular_device
    Path: ./mbed-os/features/cellular/TESTS/api/cellular_device

...
```

After compilation, you can use the `--run-list` argument to list all tests that are ready to be ran.

### Executing all tests

The default action of Greentea using `mbed test` is to execute all tests found. You can also add `-v` to make the output more verbose.

### Limiting tests

You can select test cases by name using the `-n` argument. This command executes all tests named `tests-mbedmicro-rtos-mbed-mail` from all builds in the test specification:

```
$ mbed test -n tests-mbedmicro-rtos-mbed-mail
```

When using the `-n` argument, you can use the `*` character as a wildcard. This command executes all tests that start with `tests-` and have `-rtos-` in them.

```
$ mbed test -n tests-*-rtos-*
```

You can use a comma (`,`) to separate test names (argument `-n`) and build names (argument `-t`). This command executes the tests `tests-mbedmicro-rtos-mbed-mail` and `tests-mbed_drivers-c_strings` for the `K64F-ARM` and `K64F-GCC_ARM` builds in the test specification:

```
$ mbed test -n tests-mbedmicro-rtos-mbed-mail,tests-mbed_drivers-c_strings -t K64F-ARM,K64F-GCC_ARM
```

### Selecting platforms

You can limit which boards Greentea uses for testing by using the `--use-tids` argument.

```
$ mbed test --use-tids 02400203C3423E603EBEC3D8,024002031E031E6AE3FFE3D2 --run
```

Where `02400203C3423E603EBEC3D8` and `024002031E031E6AE3FFE3D` are the target IDs of platforms attached to your system.

You can view target IDs using [mbed-ls](https://github.com/ARMmbed/mbed-os-tools/tree/master/packages/mbed-ls), which is installed as part of Mbed CLI.

```
$ mbedls
+--------------+---------------------+------------+------------+-------------------------+
|platform_name |platform_name_unique |mount_point |serial_port |target_id                |
+--------------+---------------------+------------+------------+-------------------------+
|K64F          |K64F[0]              |E:          |COM160      |024002031E031E6AE3FFE3D2 |
|K64F          |K64F[1]              |F:          |COM162      |02400203C3423E603EBEC3D8 |
|LPC1768       |LPC1768[0]           |G:          |COM5        |1010ac87cfc4f23c4c57438d |
+--------------+---------------------+------------+------------+-------------------------+
```

In this case, you won't test one target, the LPC1768.

### Creating reports

Greentea supports a number of report formats.

#### HTML

This creates an interactive HTML page with test results and logs.

```
mbed test --report-html html_report.html --run
```

#### JUnit

This creates an XML JUnit report, which you can use with popular Continuous Integration software, such as [Jenkins](https://jenkins.io/index.html).

```
mbed test --report-junit junit_report.xml --run
```

#### JSON

This creates a general JSON report.

```
mbed test --report-json json_report.json --run
```

#### Plain text

This creates a human-friendly text summary of the test run.

```
mbed test --report-text text_report.text --run
```

## Test specification JSON format

The Greentea test specification format decouples the tool from your build system. It provides important data, such as test names, paths to test binaries and the platform on which the binaries should run. This file is automatically generated when running tests through Mbed CLI, but you can also provide it yourself. This way you can control exactly which tests are run and through which compilers.

Greentea automatically looks for files called `test_spec.json` in your working directory. You can also use the `--test-spec` argument to direct Greentea to a specific test specification file.

When you use the `-t` / `--target` argument with the `--test-spec` argument, you can select which "build" to use. In the example below, you could provide the arguments `--test-spec test_spec.json -t K64F-ARM` to only run that build's tests.

### Example of test specification file

The below example uses two defined builds:

- Build `K64F-ARM` for NXP `K64F` platform compiled with `ARMCC` compiler.
- Build `K64F-GCC` for NXP `K64F` platform compiled with `GCC ARM` compiler.

Place this file in your root folder, and name it `test_spec.json`.

```json
{
    "builds": {
        "K64F-ARM": {
            "platform": "K64F",
            "toolchain": "ARM",
            "base_path": "./BUILD/K64F/ARM",
            "baud_rate": 9600,
            "tests": {
                "tests-mbedmicro-rtos-mbed-mail": {
                    "binaries": [
                        {
                            "binary_type": "bootable",
                            "path": "./BUILD/K64F/ARM/tests-mbedmicro-rtos-mbed-mail.bin"
                        }
                    ]
                },
                "tests-mbed_drivers-c_strings": {
                    "binaries": [
                        {
                            "binary_type": "bootable",
                            "path": "./BUILD/K64F/ARM/tests-mbed_drivers-c_strings.bin"
                        }
                    ]
                }
            }
        },
        "K64F-GCC": {
            "platform": "K64F",
            "toolchain": "GCC_ARM",
            "base_path": "./BUILD/K64F/GCC_ARM",
            "baud_rate": 9600,
            "tests": {
                "tests-mbedmicro-rtos-mbed-mail": {
                    "binaries": [
                        {
                            "binary_type": "bootable",
                            "path": "./BUILD/K64F/GCC_ARM/tests-mbedmicro-rtos-mbed-mail.bin"
                        }
                    ]
                }
            }
        }
    }
}
```

If you run `mbed test --run-list`, this will now list only these tests:

```
mbedgt: greentea test automation tool ver. 1.2.5
mbedgt: using multiple test specifications from current directory!
        using 'BUILD\tests\K64F\ARM\test_spec.json'
        using 'BUILD\tests\K64F\GCC_ARM\test_spec.json'
mbedgt: available tests for built 'K64F-GCC_ARM', location 'BUILD/tests/K64F/GCC_ARM'
        test 'tests-mbedmicro-rtos-mbed-mail'
mbedgt: available tests for built 'K64F-ARM', location 'BUILD/tests/K64F/ARM'
        test 'tests-mbed_drivers-c_strings'
        test 'tests-mbedmicro-rtos-mbed-mail'
```


## Known issues

There cannot be a `main()` function outside of a `TESTS` directory when building and running tests. This is because this function will be included in the nontest code build, as described in the [building process](#building-process) section. When the test code is compiled and linked with the nontest code build, a linker error will occur, due to there being multiple `main()` functions defined. This is why you should either rename your main application file if you need to build and run tests, or use a different project. Note that this does not affect building projects or applications, only building and running tests.
