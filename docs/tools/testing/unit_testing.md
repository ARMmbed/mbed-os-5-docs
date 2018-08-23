## Unit testing

### Introduction

Traditional software testing is defined into three main levels: unit testing, integration testing and system testing. These levels are often pictured as a pyramid to indicate the amount of testing per level.

```
^ Testing level
|
|       /\
|      /  \       System testing
|     /----\
|    /      \     Integration testing
|   /--------\
|  /          \   Unit testing
| /------------\
|
*-------------------> Amount of tests
```

Integration and system testing are performed in an environment where the tests are run with full Mbed OS. Other testing tools for Mbed OS require specific embedded hardware and whole Mbed OS to be built, which means traditional unit testing is not possible.

Unit testing takes place in a build environment where each C/C++ class or module is tested in isolation. This means test suites are built into separate test binaries and all access outside is stubbed to remove dependency of any specific embedded hardware or software combination. This allows the testing to be done quickly using native compilers on the build machine.

### Using unit tests

#### Test code structure

Unit tests are located in Mbed OS repository under `UNITTESTS`. Each unit test should use identical directory tree structure to the file to be tested. This makes it easier to find unit tests for a particular class or a module. For example if the file to be tested is `rtos/Semaphore.cpp` then all the test files should be in `UNITTESTS/rtos/Semaphore` directory.

##### Test discovery

Registering unit tests for running is automatic and handled by the test runner, but test files are not automatically assigned to be built. Unit tests are built using a separate build system, which will search for unit tests under `UNITTESTS` directory.

For the build system to find and build any test suite automatically, a unit test configuration file named `unittest.cmake` is required to be included with each unit test. This configuration file contains a name for the test and other source files required for the build.

##### Test names

Each test suite requires a name to be configured in the `unittest.cmake` file. This name is used for generated files and when running a subset of tests.

#### Building, running and writing tests

Unit testing requires external tools which need to be installed. See the developer [documentation](https://github.com/ARMmbed/mbed-os/blob/master/UNITTESTS/README.md) in GitHub for installation guide.

You can build and run unit tests through Arm Mbed CLI. The tool can also be used to generate new test files. For information on using Mbed CLI, please see the [CLI documentation](/docs/development/tools/arm-mbed-cli.html).

For more information about the framework, the build process or how to write unit tests, see the GitHub documentation.
