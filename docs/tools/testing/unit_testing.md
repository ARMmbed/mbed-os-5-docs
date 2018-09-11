## Unit testing

We perform integration and system testing in an environment where we run the tests with the full Mbed OS. Other testing tools for Mbed OS require specific embedded hardware, which means traditional unit testing is not possible.

Unit testing takes place in a build environment where we test each C or C++ class or module in isolation. This means we build test suites into separate test binaries and stub all access outside to remove dependencies on any specific embedded hardware or software combination. This allows us to complete the testing using native compilers on the build machine.

### Using unit tests

#### Test code structure

Unit tests are located in Mbed OS repository under `UNITTESTS`. Each unit test uses an identical directory tree structure to the file to be tested. This makes it easier to find unit tests for a particular class or a module. For example, if the file to be tested is `rtos/Semaphore.cpp`, then all the test files are in the `UNITTESTS/rtos/Semaphore` directory.

##### Test discovery

Registering unit tests for running is automatic, and the test runner handles registration. However, test files are not automatically assigned to be built. We build unit tests by using a separate build system, which searches for unit tests under the `UNITTESTS` directory.

For the build system to find and build any test suite automatically, a unit test configuration file named `unittest.cmake` is required to be included with each unit test. This configuration file contains a name for the test and other source files the build requires.

##### Test names

Each test suite requires a name to be configured in the `unittest.cmake` file. This name is used for generated files and when running a subset of tests.

#### Building, running and writing tests

Unit testing requires external tools you need to install. See the developer [documentation](https://github.com/ARMmbed/mbed-os/blob/master/UNITTESTS/README.md) in GitHub for the full installation guide.

You can build and run unit tests through Arm Mbed CLI. You can also use the tool to generate new test files. For information on using Mbed CLI, please see the [CLI documentation](/docs/development/tools/arm-mbed-cli.html).
