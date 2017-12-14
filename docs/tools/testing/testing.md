## Testing applications

The way tests are run and compiled in Arm Mbed OS 5 is substantially different from previous versions of Mbed.

### Using tests

#### Test code structure

Tests can exist throughout Mbed OS and your project's code. They are located under a special directory called `TESTS` (case is important!).

Placing code under this directory means it is ignored when building applications and libraries. This code is only ever used when building tests. This is important because all tests require a `main()` function, and building it with your application would cause multiple `main()` functions to be defined.

In addition to being placed under a `TESTS` directory, test sources must exist under two other directories: a test group directory and a test case directory. The following is an example of this structure:

```
myproject/TESTS/test_group/test_case_1
```

In this example, `myproject` is the project root, and all the source files under the `test_case_1` directory are included in the test. The test build also includes any other source files from the OS, libraries and project that apply to the target's configuration.

<span class="notes">**Note:** You can name both the test group and test case directory anything you like. However, you **must** name the `TESTS` directory `TESTS` for the tools to detect the test cases correctly.</span>

##### Test discovery

Because test cases can exist throughout a project, the tools must find them in the project's file structure before building them.

Test discovery also obeys the same rules that are used when building your project. This means that tests that are placed under a directory with a prefix such as `TARGET_`, `TOOLCHAIN_` or `FEATURE_` are only discovered, built and run if your current configuration matches this prefix.

For example, if you place a test under the directory `FEATURE_BLE` with the following path:

```
myproject/mbed-os/features/FEATURE_BLE/TESTS/ble_tests/unit_test
```

This test case is only discovered if the target being tested supports the BLE feature. Otherwise, the test is ignored.

Generally, a test should not be placed under a `TARGET_` or `TOOLCHAIN_` directory because most tests should work for all target and toolchain configurations.

Tests can also be completely ignored by using the `.mbedignore` file described in the <a href="/docs/v5.7/tools/ignoring-files-from-mbed-build.html" target="_blank">documentation</a>.

##### Test names

A test case is named from its position in your project's file structure. For instance, in the above example, a test case with the path `myproject/TESTS/test_group/test_case_1` would be named `tests-test_group-test_case_1`. The name is created by joining the directories that make up the path to the test case with a "dash" (`-`) character. This is a unique name to identify the test case. You will see this name throughout the build and testing process.

#### Building tests

You can build tests through Arm Mbed CLI. For information on using Mbed CLI, please see the <a href="/docs/v5.7/tools/arm-mbed-cli.html" target="_blank">CLI documentation</a>.

When you build tests for a target and a toolchain, the script first discovers the available tests and then builds them in parallel. You can also create a "test specification" file, which our testing tools can use to run automated hardware tests. For more information on the test specification file, please see the <a href="https://github.com/ARMmbed/greentea#test-specification-json-formatted-input" target="_blank">Greentea documentation here</a>.

##### Building process

The `test.py` script (not to be confused with `tests.py`) located under the `tools` directory handles the process for building tests. This handles the discovery and building of all test cases for a target and toolchain.

The full build process is:

1. Build the nontest code (all code not under a `TESTS` folder), but do not link it. The resulting object files are placed in the build directory.
1. Find all tests that match the given target and toolchain.
1. For each discovered test, build all of its source files and link it with the nontest code that was built in step 1.
1. If specified, create a test specification file and place it in the given directory for use by testing tools. This is placed in the build directory by default when using Mbed CLI.

##### App config

When building an Mbed application, the presence of an `mbed_app.json` file allows you to set or override different configuration settings from libraries and targets. However, because the tests share a common build, this can cause issues when tests have different configurations that affect the OS.

The build system looks for an `mbed_app.json` file in your shared project files (any directory not inside of a `TESTS` folder). If the system finds it, this configuration file is used for both the nontest code as well as each test case inside your project's source tree. If there is more than one `mbed_app.json` file in the source tree, the config system will error.

If you need to test with multiple configurations, you can use the `--app-config` option. This overrides the search for an `mbed_app.json` file and uses the config file you specify for the build.

#### Running tests

You can run automated tests through Mbed CLI.

The testing process requires tests to be built and that a test specification JSON file exist that describes these available tests. See the <a href="https://github.com/ARMmbed/greentea#test-specification-json-formatted-input" target="_blank">test specification format</a>.

The Greentea tool handles the actual testing process. To read more about this tool, please visit its <a href="https://github.com/ARMmbed/greentea" target="_blank">GitHub repository</a>.

#### Writing tests

You can write tests for your own project, or add more tests to Mbed OS. You can write tests using the <a href="https://github.com/ARMmbed/mbed-os/tree/master/features/frameworks/greentea-client" target="_blank">Greentea client</a>, <a href="https://github.com/ARMmbed/mbed-os/tree/master/features/frameworks/unity" target="_blank">UNITY</a> and <a href="https://github.com/ARMmbed/mbed-os/tree/master/features/frameworks/utest" target="_blank">utest</a> frameworks, located in `/features/frameworks`. Below is an example test that uses all of these frameworks:

```c++
#include "mbed.h"
#include "greentea-client/test_env.h"
#include "unity.h"
#include "utest.h"
#include "rtos.h"

using namespace utest::v1;

// A test that returns successfully is considered successful
void test_success() {
    TEST_ASSERT(true);
}

// Tests that assert are considered failing
void test_failure() {
    TEST_ASSERT(false);
}

utest::v1::status_t test_setup(const size_t number_of_cases) {
    // Setup Greentea using a reasonable timeout in seconds
    GREENTEA_SETUP(40, "default_auto");
    return verbose_test_setup_handler(number_of_cases);
}

// Test cases
Case cases[] = {
    Case("Testing success test", test_success),
    Case("Testing failure test", test_failure),
};

Specification specification(test_setup, cases);

// Entry point into the tests
int main() {
    return !Harness::run(specification);
}
```

This test first runs a case that succeeds, then a case that fails. This is a good template to use when creating tests. For more complex testing examples, please see the documentation for <a href="https://github.com/ARMmbed/mbed-os/tree/master/features/frameworks/utest" target="_blank">utest</a>.

### Debugging tests

Debugging tests is a crucial part of the development and porting process. This section covers exporting the test, then driving the test with the test tools while the target is attached to a debugger.

#### Exporting tests

Currently, the easiest way to export a test is to copy the test's source code from its test directory to your project's root. This way, the tools treat it like a normal application.

You can find the path to the test you wish to export by running the following command:

```
mbed test --compile-list -n <test name>
```

Once you've copied all of the test's source files to your project root, export your project:

```
mbed export -i <IDE name>
```

You can find your exported project in `projectfiles/<IDE>_<target>`.

#### Running a test while debugging

Assuming your test was exported correctly to your IDE, build the project, and load it onto your target via your debugger.

Bring the target out of reset, and run the program. Your target waits for the test tools to send a synchronizing character string over the serial port. Do not run the `mbed test` commands because that will attempt to flash the device, which you've already done with your IDE.

Instead, you can use the underlying test tools to drive the test. <a href="https://github.com/ARMmbed/htrun" target="_blank">`htrun`</a> is the tool you need to use in this case. Install the requirements for Mbed OS also installs `htrun`. You can also intall `htrun` by running `pip install mbed-host-tests`.

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

Replace `<serial port>` with the serial port you found by running `mbed detect` above. So for the example above, the command is:

```
mbedhtrun --skip-flashing --skip-reset -p COM270:9600
```

This detects your attached target and drives the test. If you need to rerun the test, reset the device with your debugger, run the program and run the same command.

For an explanation of the arguments used in this command, please run `mbedhtrun --help`.

### Known issues

There cannot be a `main()` function outside of a `TESTS` directory when building and running tests. This is because this function will be included in the nontest code build as described in the [Building process](#building-process) section. When the test code is compiled and linked with the nontest code build, a linker error will occur due to their being multiple `main()` functions defined. For this reason, please either rename your main application file if you need to build and run tests or use a different project. Note that this does not affect building projects or applications, just building and running tests.
