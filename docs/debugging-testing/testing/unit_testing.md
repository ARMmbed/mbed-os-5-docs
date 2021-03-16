# Unit testing

This document describes how to write and test unit tests for Mbed OS. To prevent and solve problems, please see the [troubleshooting](#troubleshooting) section.

## Introduction

Unit tests exercise code in small functional "units", such as a single function or a class. The unit tests are designed to be run on your host development machine and should not have any dependency on the underlying platform or external libraries. To achieve this, unit tests make extensive use of "stubs", "mocks" and "fakes" to isolate the code under test from any external dependencies. Unit tests are quick to run and provide targeted testing of your code during development. Mbed OS provides mock and stub implementations of the Mbed OS components to make unit testing easier.

## Prerequisites

Please install the following dependencies to use Mbed OS unit testing.

- GNU toolchains.
   - GCC 6 or later. We recommend you use MinGW-W64 on Windows, but any Windows port of the above GCC versions works.
- CMake 3.19.0 or newer.
- Python 2.7.x, 3.5 or newer.
- Pip 10.0 or newer.
- Gcovr 4.1 or newer.

Detailed instructions for supported operating systems are below.

### Installing dependencies on Debian or Ubuntu
1. Install the compilation packages to the host:
    ```
    sudo apt-get -y install build-essential cmake
    ```
1. Install Python and its package manager:
    ```
    sudo apt-get -y install python python-setuptools && sudo apt-get install python-pip
    ```
1. Install the additional Python package `gcovr` for code coverage report:
    ```
    pip install "gcovr>=4.1"
    ```

### Installing dependencies on macOS

In a terminal window:

1. Install [Homebrew](https://brew.sh/).
1. Install Xcode command-line tools with `xcode-select --install`.
1. Install CMake with: `brew install cmake`.
1. Install Python and Pip:

   ```
   brew install python
   ```

1. Install the additional Python package `gcovr` for code coverage report:
    ```
    pip install "gcovr>=4.1"
    ```
1. Install the GNU Compiler collection if required:
    ```
    brew install gcc
    ```

### Installing dependencies on Windows

In a terminal window:

1. Download and install MinGW-W64 from [SourceForge](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/).
1. Download CMake binaries from https://cmake.org/download/, and run the installer.
1. Download Python 2.7 or Python 3 from https://www.python.org/getit/, and run the installer.
1. Add MinGW, CMake and Python into system PATH.
1. Install the additional Python package `gcovr` for code coverage report:
    ```
    pip install "gcovr>=4.1"
    ```

## Test code structure

Unit tests are located in the `tests/UNITTESTS` subdirectory of each library. We recommend that unit test files use an identical directory path as the file under test. This makes it easier to find unit tests for a particular class or a module. For example, if the file you are testing is `some/example/path/ClassName.cpp`, then all the test files are in the `UNITTESTS/some/example/path/ClassName` directory. Each test suite needs to have its own `CMakeLists.txt` file for test CMake configuration.

All the stub source files are built in a stub CMake library target (e.g `mbed-stubs-rtos`) and linked to the `mbed-stubs` CMake target. The CMake target of the library unit under test is expected to link with the required stub libraries or `mbed-stubs` if it requires multiple stub libraries.


The new stub file should follow the naming convention `<CLASS_NAME>_stub.cpp` for the source file and `<CLASS_NAME>_stub.h` for the header file. They should be built as part of their respective stub CMake library. Alternatively, create a stub library if `<CLASS_NAME>_stub` is an implementation of an external source, not part of Mbed OS.


All the Mbed OS header files are built with CMake `INTERFACE` libraries (e.g `mbed-headers-platform`). Stubbed header files reside in the `UNITTESTS/target_h` directory and are built with the `mbed-headers-base` CMake library. All CMake libraries containing header files are linked with `mbed-headers`. The CMake target of the library unit under test is expected to link with the required header file libraries or `mbed-headers` in case of requiring multiple header libraries. 

All the stub libraries and header libraries are defined under `UNITTESTS/stubs/` directory.

Libraries for fakes are under the `UNITTESTS/fakes` directory. These provide mock implementations that are meant to replace the stub version that does nothing. Usually, these will replace the header files as well as the source files and cannot be used together with their stub equivalents.

The upcoming [Example](#Example) section describes how to write a unit test for a dummy example class (Unit Under Test). The example walks you through creating a header library and a stub interface library using CMake. 

### Test discovery

Every unit test suite CMake calls `add_test()` which adds a test to the project at CMake configuration time and to run the unit tests happens automatically by invoking the `ctest` command. However, test suites do not automatically build.

For the build system to build a unit test, pass the `ON` value to `BUILD_TESTING` in the CMake or CTest command-line argument

### Writing unit tests

A unit test suite consists of one or more test cases, which should cover all the functions in a class under test. Any external dependencies should be stubbed, including the other classes in the same module. Avoid stubbing header files. Finally, analyze code coverage to ensure all code is tested, and no dead code is found.

Please see the [documentation for Google Test](https://github.com/google/googletest/blob/master/docs/primer.md) to learn how to write unit tests using its framework. See the [documentation for Google Mock](https://github.com/google/googletest/tree/master/googlemock) if you want to write and use C++ mock classes instead of stubs.

#### Test suite configuration

Create two files in the test directory for each test suite:

- Unit test source file (`test_ClassName.cpp`).
- Unit test CMake configuration file (`CMakeLists.txt`).

List all the required files and libraries for the build in the `CMakeLists.txt` file.

#### Example

With the following steps, you can write a unit test. This example creates dummy classes to be tested, creates and configures unit tests for a class and stubs all external dependencies.

1. Create the following dummy classes header in `mbed-os/example/include/example`:

    **MyClass.h**

    ```
    #ifndef MYCLASS_H_
    #define MYCLASS_H_

    namespace example {

    class MyClass {
    public:
        int myFunction();
    };

    }

    #endif
    ```

1. Add a new `mbed-headers-example` interface library: 

    **mbed-os/stubs/CMakeLists.txt**
 
    ```
    add_library(mbed-headers-example INTERFACE)
 
    target_include_directories(mbed-headers-example
     INTERFACE
         ${mbed-os_SOURCE_DIR}/example
         ${mbed-os_SOURCE_DIR}/example/include
         ${mbed-os_SOURCE_DIR}/example/include/example
     )
    ```

1. Add the newly created `mbed-headers-example` library into existing `target_link_libraries` of target `mbed-headers` in `mbed-os/UNITTESTS/stubs/CMakeLists.txt`:

    ```
    target_link_libraries(mbed-headers
        INTERFACE
            mbed-headers-base
            mbed-headers-platform
            mbed-headers-example
    )
    ```
1. Create the following dummy classes source in `mbed-os/example/source`:

    **MyClass.cpp**

    ```
    #include "MyClass.h"
    #include "example_interface_api.h"

    namespace example {

    int MyClass::myFunction()
    {
        OtherClass o = OtherClass();
        example_interface_status_t status = example_interface_api_init();        
        example_interface_api_start();        
        return o.otherFunction();
    }

    }
    ```


1. Create an example stub directory in `mbed-os/UNITTESTS/stubs/example`.
1. Create the following example interface api stub source in `mbed-os/UNITTESTS/stubs/example` 

    **example_interface_api_stub.c**

    ```
    #include "example_interface/example_interface_api.h"
    
    example_interface_status_t example_interface_api_init()
    {
        return STATUS_OK;
    }
    
    void example_interface_api_start(void)
    {
    
    }
    
    ```

    **CMakeLists.txt**

    ```    
    add_library(mbed-stubs-example-interface)
    
    target_sources(mbed-stubs-example-interface
        PRIVATE
            example_interface_api_stub.c
    )    
  
    target_link_libraries(mbed-stubs-example-interface
        PRIVATE
            mbed-headers
            mbed-stubs-headers
    )

    ```

1. Add the newly created `mbed-stubs-example-interface` library into existing `target_link_libraries` of target `mbed-stubs` in `mbed-os/UNITTESTS/stubs/CMakeLists.txt`:


    ```
    target_link_libraries(mbed-stubs
        INTERFACE
            mbed-stubs-connectivity
            mbed-stubs-drivers
            mbed-stubs-events
            mbed-stubs-hal
            mbed-stubs-platform
            mbed-stubs-rtos
            mbed-stubs-storage
            mbed-stubs-example-interface
    )
    ```

1. Create a directory for MyClass unit tests in `mbed-os/example/tests/UNITTESTS/MyClass`.
1. Create a source and CMake configuration file for MyClass unit tests in `mbed-os/example/tests/unittests/MyClass`:

    **test_MyClass.cpp**

    ```
    #include "gtest/gtest.h"
    #include "example/MyClass.h"

    class TestMyClass : public testing::Test {
    protected:
        example::MyClass *obj;

        virtual void SetUp()
        {
            obj = new example::MyClass();
        }

        virtual void TearDown()
        {
            delete obj;
        }
    };

    TEST_F(TestMyClass, constructor)
    {
        EXPECT_TRUE(obj);
    }

    TEST_F(TestMyClass, myfunction)
    {
        EXPECT_EQ(obj->myFunction(), 0);
    }
    ```

    **CMakeLists.txt**
    ```
    set(TEST_NAME myclass-unittest)

    add_executable(${TEST_NAME})
  
    target_sources(${TEST_NAME}
        PRIVATE
            ${mbed-os_SOURCE_DIR}/example/tests/unittests/MyClass/MyClass.cpp
            test_MyClass.cpp
    )
    
    target_link_libraries(${TEST_NAME}
        PRIVATE
            mbed-headers
            mbed-stubs            
            gmock_main
    )
    
    add_test(NAME "${TEST_NAME}" COMMAND ${TEST_NAME})
    
    set_tests_properties(${TEST_NAME} PROPERTIES LABELS "example")
    ```

This example does not use any Mbed OS code. If your example depends on Mbed OS code, remember to use the existing stubs libraries. If there are any missing type or function declarations in the existing stubs, you must update the stubs in `UNITTESTS/target_h` and `UNITTESTS/stubs` accordingly.

### Building and running unit tests

#### Mbed CLI 1

- Install [Mbed CLI 1](../build-tools/mbed-cli-1.html) version 1.8.0 or newer using the `pip install "mbed-cli>=1.8.0"` command in Debian, Ubuntu, macOS or Windows.

- Mbed CLI 1 supports unit tests through the `mbed test --unittests` command. To learn how to use unit tests with Mbed CLI 1, please see the [unit testing documentation section](../build-tools/test-and-debug.html). For other information on using Mbed CLI 1, please see the [CLI documentation in handbook](../build-tools/mbed-cli-1.html).

#### Mbed CLI 2

- Mbed CLI 2 does not currently support the `mbed test --unittests` command, please use CMake and a Make command or `ctest --build-and-test` command directly.

#### Build tests directly with CMake

1. Create a build directory from Mbed OS root: `mkdir cmake_build`.
1. Run CMake configuration command from `mbed-os` root directory using `cmake -S . -B cmake_build -GNinja -DBUILD_TESTING=ON` and pass extra below arguments based on the build requirement.
   - Add `-DCMAKE_MAKE_PROGRAM=<value>`, `-DCMAKE_CXX_COMPILER=<value>` and `-DCMAKE_C_COMPILER=<value>` to use a specific Make program and compilers.
   - Add `-DCMAKE_BUILD_TYPE=Debug` for a debug build.
   - Add `-DCOVERAGE=ON` to add coverage compiler flags.
   - Add `-Dgtest_disable_pthreads=ON` to run in a single thread.
   - See the [CMake manual](https://cmake.org/cmake/help/v3.19/manual/cmake.1.html) for more information.
1. Build the tests using `cmake --build cmake_build`.
1. Run the tests using `cmake --build cmake_build --target test`

#### Run tests directly with CTest

Run a test binary in the build directory to run a unit test suite. To run multiple test suites at once, use the CTest test runner. Run CTest with `ctest`. Add `-v` to get results for each test case. See the [CTest manual](https://cmake.org/cmake/help/v3.19/manual/ctest.1.html) for more information.

#### Build and run the tests directly with CTest

1. Create a build directory from Mbed OS root: `mkdir cmake_build`.
1. Run CTest using a relative path to the Mbed OS root directory and created build directory `cmake_build` as an argument. From Mbed OS root use `ctest --build-and-test . cmake_build --build-generator Ninja --build-options -DBUILD_TESTING=ON --test-command ctest`.

   - `--build-generator [generator]` specifies the [build generator](https://cmake.org/cmake/help/v3.19/manual/cmake-generators.7.html#cmake-generators), the example above uses `Ninja`.

   - `--build-options [options]` to specify for Mbed OS unit tests CMake configuration, not for the build tool (e.g --build-options -DBUILD_TESTING=ON)
   - `--test-command [command]` to specify the command to invoke after the CMake build.
   - See the [CTest manual](https://cmake.org/cmake/help/v3.19/manual/ctest.1.html) for more information.

#### Run tests with GUI test runner

1. Install `gtest-runner` according to the [documentation](https://github.com/nholthaus/gtest-runner).
1. Run `gtest-runner`.
1. Add test executables into the list and run.

### Debugging

1. Use Mbed CLI to build a debug build. For advanced use, run CMake directly with `-DCMAKE_BUILD_TYPE=Debug`, and then run a Make program.
1. Run GDB with a test executable as an argument to debug unit tests.
1. Run tests with Valgrind to analyze the test memory profile.

### Get code coverage

Use Mbed CLI to generate code coverage reports. For advanced use, follow these steps:

1. Run CMake with both `-DCMAKE_BUILD_TYPE=Debug` and `-DCOVERAGE=ON`.
1. Run a Make program to build the tests.
1. Run the tests.
1. Run Gcovr or any other code coverage tool directly in the build directory.

### Troubleshooting

**Problem:** Generic problems with CMake or with the build process.
- **Solution**: Delete the build directory. Make sure that CMake, g++, GCC and a Make program can be found in the path and are correct versions.

**Problem:** (Windows) Virus protection identifies files generated by CMake as malicious and quarantines the files.
- **Solution**: Restore false-positive files from the quarantine.

**Problem:** (Windows) Git with shell installation adds sh.exe to the path and then CMake throws an error: sh.exe was found in your PATH. For MinGW make to work correctly, sh.exe must NOT be in your path.
- **Solution**:  Remove sh.exe from the system path.

**Problem:** (Mac OS) CMake compiler check fails on Mac OS Mojave when using GCC-8.
- **Solution**: Make sure gnm (binutils) is not installed. Uninstall binutils with `brew uninstall binutils`.