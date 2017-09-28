## Test anddebug

Use the `mbed test` command to compile and run tests.

The arguments to `test` are:
* `-m <MCU>` to select a target for the compilation. If `detect` or `auto` parameter is passed, then Mbed CLI will attempt to detect the connected target and compile against it.
* `-t <TOOLCHAIN>` to select a toolchain (of those defined in `mbed_settings.py`, see above), where `toolchain` can be either `ARM` (Arm Compiler 5), `GCC_ARM` (GNU Arm Embedded), or `IAR` (IAR Embedded Workbench for Arm).
* `--compile-list` to list all the tests that can be built.
* `--run-list` to list all the tests that can be run (they must be built first).
* `--compile` to only compile the tests.
* `--run` to only run the tests.
* `-n <TESTS_BY_NAME>` to limit the tests built or run to a comma separated list (ex. test1,test2,test3).
* `--source <SOURCE>` to select the source directory. Default is `.` (the current directory). You can specify multiple source locations, even outside the program tree.
* `--build <BUILD>` to select the build directory. Default: `BUILD/` inside your program.
* `--profile <PATH_TO_BUILD_PROFILE>` to select a path to a build profile configuration file. Example: `mbed-os/tools/profiles/debug.json`.
* `-c or --clean` to clean the build directory before compiling.
* `--test-spec <TEST_SPEC>` to set the path for the test spec file used when building and running tests (the default path is the build directory).
* `-v` or `--verbose` for verbose diagnostic output.
* `-vv` or `--very_verbose` for very verbose diagnostic output.

Invoke `mbed test`:

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

### Finding available tests

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

### Compiling and running tests

You can specify to only **build** the tests by using the `--compile` option:

```
$ mbed test -m K64F -t GCC_ARM --compile
```

You can specify to only **run** the tests by using the `--run` option:

```
$ mbed test -m K64F -t GCC_ARM --run
```

If you don't specify any of these, `mbed test` will first compile all available tests and then run them.

### Limiting the test scope

You can limit the scope of the tests built and run by using the `-n` option. This takes a comma-separated list of test names as an argument:

```
$ mbed test -m K64F -t GCC_ARM -n TESTS-functional-test1,TESTS-functional-test2
```

You can use the wildcard character `*` to run a group of tests that share a common prefix without specifying each test individually. For instance, if you only want to run the three tests `TESTS-functional-test1`, `TESTS-functional-test2` and `TESTS-functional-test3`, but you have other tests in your project, you can run:

```
$ mbed test -m NUCLEO_F429ZI -t GCC_ARM -n TESTS-functional*
```

<span class="notes">**Note:** Some shells expand the wildcard character `*` into file names that exist in your working directory. To prevent this behavior, please see your shell's documentation.</span>

### Test directory structure

Test code must follow this directory structure:

```
mbed-os-program
 |- main.cpp            # Optional main.cpp with main() if it is an application module.
 |- pqr.lib             # Required libs
 |- xyz.lib
 |- mbed-os
 |  |- frameworks        # Test dependencies
 |  |  `_greentea-client # Greentea client required by tests.
 |  |...
 |  `- TESTS              # Tests directory. Special name upper case TESTS is excluded during application build process
 |     |- TestGroup1      # Test Group directory
 |     |  `- TestCase1    # Test case source directory
 |     |      `- main.cpp # Test source
 |     |- TestGroup2
 |     |   `- TestCase2
 |     |      `- main.cpp
 |     `- host_tests      # Python host tests script directory
 |        |- host_test1.py
 |        `- host_test2.py
 `- build                 # Build directory
     |- <TARGET>          # Target directory
     | `- <TOOLCHAIN>     # Toolchain directory
     |   |- TestCase1.bin # Test binary
     |   `- TestCase2.bin
     | ....
```

As shown above, tests exist inside `TESTS\testgroup\testcase\` directories. Please note that `TESTS` is a special upper case directory that is excluded from module sources while compiling.

<span class="notes">**Note:** `mbed test` does not work in applications that contain a  `main` function that is outside of a `TESTS` directory.</span>

### Troubleshooting

#### Unable to import Mercurial (mbed.org) programs or libraries.
1. Check whether you have Mercurial installed in your system path by  running `hg` in command prompt. If you're receiving "command not found" or a similar message, then you need to install Mercurial, and add it to your system path.

2. Try to clone a Mercurial repository directly. For example, `hg clone https://developer.mbed.org/teams/mbed/code/mbed_blinky/`. If you receive an error similar to `abort: error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.:590)`, then your system certificates are out of date. You need to update your system certificates and possibly add the host certificate fingerprint of `mbed.com` and `mbed.org`. You can read more about Mercurial's [certificate management](https://www.mercurial-scm.org/wiki/CACertificates).

#### Various issues when running Mbed CLI in Cygwin environment
Currently Mbed CLI is not compatible with Cygwin environment and [cannot be executed inside it](https://github.com/ARMmbed/mbed-cli/issues/299).
