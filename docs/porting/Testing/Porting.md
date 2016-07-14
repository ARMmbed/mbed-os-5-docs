# Testing

mbed provides a powerful testing and continuous integration (CI) framework for compiling and running embedded software tests. This testing framework is provided through the `mbed test` command.

## Running tests

You can find the tests that are available for **building** by using the `--compile-list` option:

``` bash
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

``` bash
$ mbed test --run-list
mbedgt: test specification file '.\.build/tests\K64F\ARM\test_spec.json' (specified with --test-spec option)
mbedgt: using '.\.build/tests\K64F\ARM\test_spec.json' from current directory!
mbedgt: available tests for built 'K64F-ARM', location '.\.build/tests\K64F\ARM'
        test 'TESTS-functional-test1'
        test 'TESTS-functional-test2'
        test 'TESTS-functional-test3'
```

You can run tests with the `mbed test` command. The `-n` option (not used below) is useful for selecting a specific set of tests:

``` bash
$ mbed test
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
Static RAM memory (data + bss): 6568
Heap: 65540
Stack: 32768
Total RAM memory (data + bss + heap + stack): 104876
Total Flash memory (text + data + misc): 48357
Image: .build\tests\K64F\GCC_ARM\TESTS\mbedmicro-rtos-mbed\mutex\TESTS-unit-myclass.bin
...[SNIP]...
mbedgt: test suite report:
+--------------+---------------+--------------------+--------+--------------------+-------------+
| target       | platform_name | test suite         | result | elapsed_time (sec) | copy_method |
+--------------+---------------+--------------------+--------+--------------------+-------------+
| K64F-GCC_ARM | K64F          | TESTS-unit-myclass | OK     | 21.09              | shell       |
+--------------+---------------+--------------------+--------+--------------------+-------------+
mbedgt: test suite results: 1 OK
mbedgt: test case report:
+--------------+---------------+--------------------+---------------------+--------+--------+--------+--------------------+
| target       | platform_name | test suite         | test case           | passed | failed | result | elapsed_time (sec) |
+--------------+---------------+--------------------+---------------------+--------+--------+--------+--------------------+
| K64F-GCC_ARM | K64F          | TESTS-unit-myclass | TESTS-unit-myclass1 | 1      | 0      | OK     | 5.00               |
| K64F-GCC_ARM | K64F          | TESTS-unit-myclass | TESTS-unit-myclass2 | 1      | 0      | OK     | 5.00               |
| K64F-GCC_ARM | K64F          | TESTS-unit-myclass | TESTS-unit-myclass3 | 1      | 0      | OK     | 5.00               |
+--------------+---------------+--------------------+---------------------+--------+--------+--------+--------------------+
mbedgt: test case results: 3 OK
mbedgt: completed in 21.28 sec
```

## Writing tests

Tests are picked up based on filename. Tests must reside in a folder named `TESTS`, with a test group folder, and a test case folder. For example:

```
TESTS/integration/basic
TESTS/integration/really-big-test
TESTS/quick-tests/quick-test
```

All source files in the test directory are compiled as a part of the test. A `main` function must exist in the test as the entry point into the test.

The following is an example of a simple test using the [Greentea client](https://github.com/ARMmbed/greentea-client) and [utest](https://github.com/ARMmbed/utest) frameworks:

``` cpp
#include "mbed.h"
#include "greentea-client/test_env.h"
#include "unity.h"
#include "utest.h"
#include "rtos.h"

using namespace utest::v1;


// Tests that assert are considered failing
void test_failure() {
    TEST_ASSERT(false);
}

// A test that returns successfully is considered successful
void test_success() {
    TEST_ASSERT(true);
}
    

utest::v1::status_t test_setup(const size_t number_of_cases) {
    // Setup Greentea using a reasonable timeout in seconds
    GREENTEA_SETUP(40, "default_auto");
    return verbose_test_setup_handler(number_of_cases);
}

// Test cases
Case cases[] = {
    Case("Testing failure test", test_failure),
    Case("Testing success test", test_success),
};

Specification specification(test_setup, cases);

// Entry point into the tests
int main() {
    return !Harness::run(specification);
}
```

## Further reading

The `mbed test` command is documented in more detail [here](https://github.com/armmbed/mbed-cli#testing).

More information about mbed Greentea (the tool used by `mbed test`) can be found [here](https://github.com/ARMmbed/greentea).  
More information about mbed CLI can be found [here](https://github.com/armmbed/mbed-cli).
