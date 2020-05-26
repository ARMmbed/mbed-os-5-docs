# Test and debug

## Testing

Use the `mbed test` command to compile and run tests.

The testing framework is Greentea, which provides tests designed for driver porting and target verification.

The arguments to `test` are:

- `-m <MCU>`: to select a target for the compilation. If the `detect` or `auto` parameter is passed, then Mbed CLI will attempt to detect the connected target and compile against it.
- `-t <TOOLCHAIN>`: to select a toolchain from those defined in `mbed_settings.py`, where `toolchain` can either be `ARM` (Arm Compiler 6) or `GCC_ARM` (GNU Arm Embedded).
- `--compile-list`: to list all the tests that can be built.
- `--run-list`: to list all the tests that can be run, after they have been built.
- `--compile`: to only compile the tests.
- `--run`: to only run the tests.
- `-n <TESTS_BY_NAME>`: to limit the tests built or run to a comma separated list, for example, `test1, test2, test3`.
- `--source <SOURCE>`: to select the source directory. The default is `.` for the the current directory. You can specify multiple source locations, even outside the program tree. Find more details about the `--source` switch in the [build rules documentation](../program-setup/build-rules.html).
- `--build <BUILD>`: to select the build directory. The default is `BUILD/` inside your program.
- `--profile <PATH_TO_BUILD_PROFILE>`: to select a path to a build profile configuration file, for example, `mbed-os/tools/profiles/debug.json`. See the dedicated [build profile documentation](../program-setup/build-profiles-and-rules.html) for more detail.
- `-c or --clean`: to clean the build directory before compiling.
- `--test-spec <TEST_SPEC>`: to set the path for the test specification file used when building and running tests. The default path is the build directory.
- `--build-data <BUILD_DATA>`: dumps build_data to this file.
- `--app-config <APP_CONFIG>`: the path of an app configuration file. The default is to look for `mbed_app.json`.
- `--test-config <TEST_CONFIG>`: the path or Mbed OS keyword of a test configuration file, for example, `ethernet`, `odin_wifi` or `path/to/config.json`.
- `--greentea`: to run Greentea tests. As a default, it only runs Greentea tests.
- `-v` or `--verbose`: for verbose diagnostic output.
- `-vv` or `--very_verbose`: for very verbose diagnostic output.

To invoke the `mbed test`:

```
$ mbed test -m K64F -t GCC_ARM
Building library mbed-build (K64F, GCC_ARM)
Building project GCC_ARM to TESTS-unit-myclass (K64F, GCC_ARM)
Compile: main.cpp
Link: TESTS-unit-myclass
Elf2Bin: TESTS-unit-myclass
+-----------+-------+-------+------+
| Module    | .text | .data | .bss |
+-----------+-------+-------+------+
| Fill      |   74  |   0   | 2092 |
| Misc      | 47039 |  204  | 4272 |
| Subtotals | 47113 |  204  | 6364 |
+-----------+-------+-------+------+
Allocated Heap: 65540 bytes
Allocated Stack: 32768 bytes
Total Static RAM memory (data + bss): 6568 bytes
Total RAM memory (data + bss + heap + stack): 104876 bytes
Total Flash memory (text + data + misc): 48357 bytes
Image: build\tests\K64F\GCC_ARM\TESTS\mbedmicro-rtos-mbed\mutex\TESTS-unit-myclass.bin
...[SNIP]...
mbedgt: test suite report:
+--------------+---------------+---------------------------------+--------+--------------------+-------------+
| target       | platform_name | test suite                      | result | elapsed_time (sec) | copy_method |
+--------------+---------------+---------------------------------+--------+--------------------+-------------+
| K64F-GCC_ARM | K64F          | TESTS-unit-myclass              | OK     | 21.09              |    shell    |
+--------------+---------------+---------------------------------+--------+--------------------+-------------+
mbedgt: test suite results: 1 OK
mbedgt: test case report:
+--------------+---------------+------------------------------------------+--------+--------+--------+--------------------+
| target       | platform_name | test suite         | test case           | passed | failed | result | elapsed_time (sec) |
+--------------+---------------+--------------------+---------------------+--------+--------+--------+--------------------+
| K64F-GCC_ARM | K64F          | TESTS-unit-myclass | TESTS-unit-myclass1 | 1      | 0      | OK     | 5.00               |
| K64F-GCC_ARM | K64F          | TESTS-unit-myclass | TESTS-unit-myclass2 | 1      | 0      | OK     | 5.00               |
| K64F-GCC_ARM | K64F          | TESTS-unit-myclass | TESTS-unit-myclass3 | 1      | 0      | OK     | 5.00               |
+--------------+---------------+--------------------+---------------------+--------+--------+--------+--------------------+
mbedgt: test case results: 3 OK
mbedgt: completed in 21.28 sec
```

You can find the compiled binaries and test artifacts in the `BUILD/tests/<TARGET>/<TOOLCHAIN>` directory of your program.

## Finding available tests

You can find the tests that are available for **building** by using the `--compile-list` option:

```
$ mbed test --compile-list
Test Case:
    Name: TESTS-functional-test1
    Path: .\TESTS\functional\test1
Test Case:
    Name: TESTS-functional-test2
    Path: .\TESTS\functional\test2
Test Case:
    Name: TESTS-functional-test3
    Path: .\TESTS\functional\test3
```


You can find the tests that are available for **running** by using the `--run-list` option:

```
$ mbed test --run-list
mbedgt: test specification file '.\build\tests\K64F\ARM\test_spec.json' (specified with --test-spec option)
mbedgt: using '.\build\tests\K64F\ARM\test_spec.json' from current directory!
mbedgt: available tests for built 'K64F-ARM', location '.\build\tests\K64F\ARM'
        test 'TESTS-functional-test1'
        test 'TESTS-functional-test2'
        test 'TESTS-functional-test3'
```

## Compiling and running tests

You can specify that the tests only **build** by using the `--compile` option:

```
$ mbed test -m K64F -t GCC_ARM --compile
```

You can specify that the tests only **run** by using the `--run` option:

```
$ mbed test -m K64F -t GCC_ARM --run
```

If you don't specify any of these, `mbed test` first compiles all available tests and then runs them.

## Limiting the test scope

You can limit the scope of the tests built and run by using the `-n` option. This takes a comma-separated list of test names as an argument:

```
$ mbed test -m K64F -t GCC_ARM -n TESTS-functional-test1,TESTS-functional-test2
```

You can use the wildcard character `*` to run a group of tests that share a common prefix without specifying each test individually. For instance, if you only want to run the three tests, `TESTS-functional-test1`, `TESTS-functional-test2` and `TESTS-functional-test3`, but you have other tests in your project, you can run:

```
$ mbed test -m NUCLEO_F429ZI -t GCC_ARM -n TESTS-functional*
```

<span class="notes">**Note:** Some shells expand the wildcard character `*` into file names that exist in your working directory. To prevent this behavior, please see your shell's documentation.</span>

## Test directory structure

Test code must follow this directory structure:

```
mbed-os-program
 |- main.cpp            ## Optional main.cpp with main() if it is an application module.
 |- pqr.lib             ## Required libs
 |- xyz.lib
 |- mbed-os
 |  |- frameworks        ## Test dependencies
 |  |  `_greentea-client ## Greentea client required by tests.
 |  |...
 |  `- TESTS              ## Tests directory. Special name upper case TESTS is excluded during application build process
 |     |- TestGroup1      ## Test Group directory
 |     |  `- TestCase1    ## Test case source directory
 |     |      `- main.cpp ## Test source
 |     |- TestGroup2
 |     |   `- TestCase2
 |     |      `- main.cpp
 |     `- host_tests      ## Python host tests script directory
 |        |- host_test1.py
 |        `- host_test2.py
 `- build                 ## Build directory
     |- <TARGET>          ## Target directory
     | `- <TOOLCHAIN>     ## Toolchain directory
     |   |- TestCase1.bin ## Test binary
     |   `- TestCase2.bin
     | ....
```

As shown above, tests exist inside `TESTS\testgroup\testcase\` directories. Please note that `TESTS` is a special upper-case directory that is excluded from module sources while compiling.

<span class="notes">**Note:** `mbed test` does not work in applications that contain a `main` function that is outside of a `TESTS` directory.</span>

## Unit testing

Use the `mbed test --unittests` command to build and run unit tests, or to generate files for new unit tests.

Build and run unit tests with `mbed test --unittests`. The arguments are:

* `--compile` to only compile unit tests.
* `--run` to only run unit tests.
* `-c` or `--clean` to clean build directory.
* `-d` or `--debug` to prepare debug build.
* `--coverage <TYPE>` to generate code coverage report where TYPE can be "html", "xml" or "both".
* `-m <NAME>` or `--make-program <NAME>` to select which make build tool to use where NAME can be "make", "gmake", "mingw32-make" or "ninja".
* `-g <NAME>` or `--generator <NAME>` to select which CMake generator to use where NAME can be "Unix Makefiles", "MinGW Makefiles" or "Ninja".
* `-r <EXPRESSION>` or `--regex <EXPRESSION>` to run tests matching the regular expression.
* `--build <PATH>` to specify build directory.
* `-v` or `--verbose` for verbose diagnostic output.

Generate files for a new unit test with `mbed test --unittests --new <FILE>`.

## Building and running unit tests

You can specify to only **build** the unit tests by using the `--compile` option:

```
$ mbed test --unittests --compile
```

You can specify to only **run** the unit tests by using the `--run` option:

```
$ mbed test --unittests --run
```

If you do not specify any of these, `mbed test --unittests` builds all available unit tests and runs them.

## Running a subset of tests

You can run a **limited set** of unit tests by using the `-r` or `--regex` option. This takes a regular expression, which it compares against the test names. For example, to run all cellular unit tests, you can specify:

```
$ mbed test --unittests -r cellular
```

## Getting code coverage

You can generate a code coverage report by using the `--coverage` option. For example, to create an html report, you can specify:

```
$ mbed test --unittests --coverage html
```

## Creating new unit tests

All unit tests are under the `mbed-os/UNITTESTS` directory. You can **generate** the necessary files for a unit test by using the `--new` option. For example, to create the files for `rtos/Semaphore.cpp`, you can specify:

```
$ mbed test --unittests --new rtos/Semaphore.cpp
```

## Serial terminal

You can open a serial terminal to the serial port of a connected Mbed target (usually board) using the `mbed sterm` command. If no serial port is specified, Mbed CLI will attempt to detect the connected Mbed targets and their serial ports.

There are various options to `mbed sterm`:

- `--port <serial port>` to specify a system serial port to connect to.
- `--baudrate <numeric>` to select the communication baudrate; the default value is 9600.
- `--echo <on|off>` to switch local echo (default is `on`).
- `--reset` to reset the connected target by sending Break before opening the serial terminal.

You can also set default port, baudrate and echo mode using the `TERM_PORT`, `TERM_BAUDRATE` and `TERM_ECHO` Mbed CLI configuration options.

The following shortcuts are available within the serial terminal:

- <kbd>Ctrl</kbd>+<kbd>B</kbd> - Send Break (reset target)
- <kbd>Ctrl</kbd>+<kbd>C</kbd> - Exit terminal
- <kbd>Ctrl</kbd>+<kbd>E</kbd> - Toggle local echo
- <kbd>Ctrl</kbd>+<kbd>H</kbd> - Help
- <kbd>Ctrl</kbd>+<kbd>T</kbd> - Menu escape key

You can view more shortcuts in the serial terminal's help menu (<kbd>Ctrl</kbd>+<kbd>H</kbd>).

You can also add the `--sterm` option to `mbed compile -f` to compile a new program, flash the program/firmware image to the connected target and then open the serial terminal to its serial port:

```
$ mbed compile -t GCC_ARM -m K64F -f --sterm
```

## Troubleshooting

### Import Mercurial (mbed.org) programs or libraries

1. Check whether you have Mercurial installed in your system path by  running `hg` in the command prompt. If you are receiving "command not found" or a similar message, then you need to install Mercurial and add it to your system path.
1. Try to clone a Mercurial repository directly. For example, `hg clone https://developer.mbed.org/teams/mbed/code/mbed_blinky/`. If you receive an error similar to `abort: error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.:590)`, then your system certificates are out of date. You need to update your system certificates and possibly add the host certificate fingerprint of `mbed.com` and `mbed.org`. You can read more about Mercurial's [certificate management](https://www.mercurial-scm.org/wiki/CACertificates).

### Various issues when running Mbed CLI in the Cygwin environment

Mbed CLI is not currently compatible with the Cygwin environment and [cannot be executed inside it](https://github.com/ARMmbed/mbed-cli/issues/299).
