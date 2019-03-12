<h2 id="crypto-port">Testing PSA service compliance</h2>

Mbed OS provides an integrated version of the Platform Security Architecture (PSA) test suite running over the Greentea test infrastructure. You can use these tests on PSA services that you develop or customize on PSA-enabled platforms to verify the compliance of the services to the PSA specification.

For information about PSA compliance tests, see [the PSA compliance test repository](https://github.com/ARM-software/psa-arch-tests).

### Test directory layout

The tests are divided into three groups, corresponding to the PSA services:

* Cryptography test suite (`components/TARGET_PSA/TESTS/compliance_crypto` in the Mbed OS directory).
* Internal trusted storage test suite (`components/TARGET_PSA/TESTS/compliance_its` in the Mbed OS directory).
* Initial attestation test suite (`components/TARGET_PSA/TESTS/compliance_attestation` in the Mbed OS directory).

Every test suite contains a folder for each of the test scenarios. Each test scenario may run one or more test vectors.

### Compiling and running tests

To compile and run PSA compliance tests in Mbed OS, run the following command:

```
mbed test -t <toolchain> -m <target> -n components-target_psa-tests-compliance_<test suite>_<test case number>
```
Where:

* `<toolchain>` may be `ARM`, `ARMC6`, `GCC_ARM` or `IAR`.

* `<target>` is your PSA-compliant target platform.

* `<test suite>` is:
    * For crypto tests: `crypto-test`.
    * For internal trusted storage tests: `its-test`.
    * For attestation tests: `attestation-test`.

* `<test case number>` is:
    * For crypto tests: `c001`, `c002`, and so on.
    * For internal trusted storage tests: `s001`, `s002`, and so on.
    * For attestation tests: `a001`, `a002`, and so on.
    
You can also use an asterisk (`*`) to compile and run the entire set of PSA compliance tests:

```
mbed test -t <toolchain> -m <target> -n components-target_psa-tests-compliance_*
```

### Cryptographic configuration
By default, the PSA compliance tests run using the default Mbed OS cryptography configuration (the configuration can be found at `features/mbedtls/inc/mbedtls/config.h` in the Mbed OS directory). When you use the default configuration, only tests supported by the configuration run.

You can override the default Mbed OS cryptography configuration using an `mbed_app.json` file, or by supplying your custom configuration file directly using a command line compilation flag. For an example of how to use an `mbed_app.json` file to override the default cryptography configuration, see the [mbed-os-psa-compliance-tests-example repository](https://github.com/ARMmbed/mbed-os-psa-compliance-tests-example).

### Sample test output
When the tests run, they output state information to the serial output. Below is an example of a successful run (running the first crypto test scenario):
```
TEST: 201 | DESCRIPTION: Testing psa_crypto_init API: Basic
[Info] Executing tests from non-secure{{__testcase_start;Check1}}

[Check 1] Test calling crypto functions before psa_crypto_init
{{__testcase_finish;Check1;1;0}}

{{__testcase_start;Check2}}

[Check 2] Test psa_crypto_init
{{__testcase_finish;Check2;1;0}}

{{__testcase_start;Check3}}

[Check 3] Test multiple psa_crypto_init
{{__testcase_finish;Check3;1;0}}

{{end;success}}

{{__exit;0}}
```
