<h1 id="psa-compliance-port">Testing PSA service compliance</h1>

Mbed OS provides an integrated version of the Platform Security Architecture (PSA) test suite running over the Greentea test infrastructure. You can use these tests on PSA services that you develop or customize on PSA-enabled platforms to verify the compliance of the services to the PSA specification.

For information about PSA compliance tests, please see [the PSA compliance test repository](https://github.com/ARM-software/psa-arch-tests).

## Test directory layout

The tests are divided into three groups, corresponding to the PSA services:

- Cryptography test suite (`components/TARGET_PSA/TESTS/compliance_crypto` in the Mbed OS directory).
- Internal trusted storage test suite (`components/TARGET_PSA/TESTS/compliance_its` in the Mbed OS directory).
- Initial attestation test suite (`components/TARGET_PSA/TESTS/compliance_attestation` in the Mbed OS directory).

Every test suite contains a folder for each of the test scenarios. Each test scenario may run one or more test vectors.

## Compiling and running tests

To compile and run PSA compliance tests in Mbed OS, run the following command:

```
mbed test -t <toolchain> -m <target> -n components-target_psa-tests-compliance_<test suite>_<test case number>
```
Where:

- `<toolchain>` may be `ARM`, `ARMC6`, `GCC_ARM` or `IAR`.

- `<target>` is your PSA-compliant target platform.

- `<test suite>` is:
   - For crypto tests: `crypto-test`.
   - For internal trusted storage tests: `its-test`.
   - For attestation tests: `attestation-test`.

- `<test case number>` is:
   - For crypto tests: `c001`, `c002`, and so on.
   - For internal trusted storage tests: `s001`, `s002`, and so on.
   - For attestation tests: `a001`, `a002`, and so on.

You can also use an asterisk (`*`), or other wildcards, to compile and run the entire set of PSA compliance tests:

```
mbed test -t <toolchain> -m <target> -n components-target_psa-tests-compliance_*
```

## Cryptographic configuration

By default, the PSA compliance tests run using the default Mbed OS cryptography configuration. (You can find the configuration at `features/mbedtls/inc/mbedtls/config.h` in the Mbed OS directory). When you use the default configuration, only tests supported by the configuration run.

You can override the default Mbed OS cryptography configuration using an `mbed_app.json` file, or by passing the `MBEDTLS_USER_CONFIG_FILE=<path to your custom configuration file>` flag in the compilation command.

For an example of how to use an `mbed_app.json` file to override the default cryptography configuration, please see the [mbed-os-psa-compliance-tests-example repository](https://github.com/ARMmbed/mbed-os-psa-compliance-tests-example).

## Sample test output

When the tests run, they output state information to the serial output. Below is an example of a successful run:

```
mbedgt: mbed-host-test-runner: started
mbedgt: checking for GCOV data...
mbedgt: test on hardware with target id: 190000006c0f1507036c0f1500000000000000002e127069
mbedgt: test suite 'components-target_psa-tests-compliance_its-test_s009' ............................ OK in 55.01 sec
test case: 'Check1' .......................................................................... OK in 0.40 sec
mbedgt: mbed-host-test-runner: started
mbedgt: checking for GCOV data...
mbedgt: test on hardware with target id: 190000006c0f1507036c0f1500000000000000002e127069
mbedgt: test suite 'components-target_psa-tests-compliance_its-test_s008' ............................ OK in 55.21 sec
test case: 'Check1' .......................................................................... OK in 0.10 sec
test case: 'Check2' .......................................................................... OK in 0.09 sec

mbedgt: test suite report:
| target | platform_name | test suite | result | elapsed_time (sec) | copy_method |
|---------------------------------|---------------------|------------------------------------------------------|---------|--------------------|-------------|
| CY8CKIT_062_WIFI_BT_PSA-GCC_ARM | CY8CKIT_062_WIFI_BT | components-target_psa-tests-compliance_its-test_s001 | OK | 19.45 | default |
| CY8CKIT_062_WIFI_BT_PSA-GCC_ARM | CY8CKIT_062_WIFI_BT | components-target_psa-tests-compliance_its-test_s002 | OK | 55.34 | default |
```
