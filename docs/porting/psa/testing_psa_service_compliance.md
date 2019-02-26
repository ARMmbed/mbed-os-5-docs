<h2 id="crypto-port">Testing PSA service compliance</h2>

Mbed OS provides an integrated version of the Platform Security Architecture (PSA) Test Suite running over the green-tea test infrastructure. These tests can be used to verify the specification compliance of the PSA services on PSA enabled platforms.

For information about the PSA compliance tests, please refer to [the PSA compliance test repository](https://github.com/ARM-software/psa-arch-tests).

### Test Layout

The test are divided into 3 groups corresponding to the PSA services:
1. Cryptography tests (found in components/TARGET_PSA/TESTS/compliance_crypto)
1. Internal Trusted storage tests (found in components/TARGET_PSA/TESTS/compliance_its)
1. Initial attestation tests (found in components/TARGET_PSA/TESTS/compliance_attestation)

Each test contains contains a folder for each test scenario. Each test scenario may run one or more test vectors.

### Testing

#### Compile and run

To compile and run the PSA compliance tests over MbedOS, run the following command:

```
mbed test -t <toolchain> -m <target> -n mbed-os-components-target_psa-tests-compliance*
```
where mbed-os-components-target_psa-tests-compliance* will be:

* for crypto tests: mbed-os-components-target_psa-tests-compliance_crypto-test_c001 (with the number at the end corresponding to the test case)
* for its tests: mbed-os-components-target_psa-tests-compliance_its-test_s001 (with the number at the end corresponding to the test case)
* for attestation tests: mbed-os-components-target_psa-tests-compliance_attestation-test_a001(with the number at the 

##### Cryptographic configuration
The PSA compliance tests will run using the default MbedOS cryptography configuration by default (the configuration can be fount at features/mbedtls/inc/mbedtls/config.h). When using the the default configuration only tests supported by the configuration will run. In order to run the tests with a different configuration please refer to the [
mbed-os-psa-compliance-tests-example repository](https://github.com/ARMmbed/mbed-os-psa-compliance-tests-example)

### Sample test output
When the tests run they will output state information to the serial output. Below is an example of a successful run (running the first crypto test scenario):
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
