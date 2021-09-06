<h1 id="ci">Continuous integration (CI) testing</h1>

Continuous integration (CI) testing is an integral part of the Mbed OS contribution workflow. CI testing refers mainly to automatic testing for pull requests.

## Github Actions

Mbed OS uses Github actions as the primary automatic testing and checking run environment.

Its configuration is located in the [github/workflows/basic_checks.yml](https://github.com/ARMmbed/mbed-os/blob/master/.github/workflows/basic_checks.yml) file in the Mbed OS root directory.

### Tests

- **coding-style** - Checks code style using [astyle](http://astyle.sourceforge.net/).
- **docs_check** - [Doxygen](http://www.doxygen.org/), naming and spelling checks:
   - Asserts the Doxygen build produces no warnings.
   - Asserts all binary libraries are named correctly.
   - Asserts all assembler files are named correctly.
- **licence-check** - Checks that there is only a permissive license in the files, including SPDX identifier.
- **include-check** - Including mbed.h within Mbed OS is not allowed.
- **cmake-checks** - Build unittests with mbed tools.
- **frozen-tools-check** - Old build tools were frozen and we verify they keep unchanged.

## Jenkins

We use [Jenkins](https://jenkins.io/) as an internal testing and checking environment. We execute tests that have special requirements for the execution enviroment in our internal Jenkins. In most cases, we publish test logs.

How it works:

- Jenkins uses a [scripted pipeline syntax](https://jenkins.io/doc/book/pipeline/).
- Jenkins scripts are not publicly available. There is a Jenkinsfile in the Mbed OS root folder, but that is just a trigger for tests.
- Jenkins selects required tests dynamically based on the code changes. For example, no tests execute if only markdown (.md) files change.
- Jenkins first runs a small number of tests to provide fast feedback, and then it runs additional tests.

### Tests

- **continuous-integration/jenkins/pr-head** - Jenkins main pipeline script execution status.
- **jenkins-ci/build-greentea-ARM** - Builds Mbed OS tests with the [ARM compiler](https://developer.arm.com/products/software-development-tools/compilers/arm-compiler). Related commands:
   - `mbed test --compile -t <toolchain> -m <target> `.
   - `python -u mbed-os/tools/test/examples/examples.py compile <toolchain> --mcu <target>`.
- **jenkins-ci/build-greentea-GCC_ARM** - Builds Mbed OS tests with GCC_ARM.
- **jenkins-ci/build-cloud-example-ARM** - Builds the cloud example with ARM.
- **jenkins-ci/build-cloud-example-GCC_ARM** - Builds the cloud example with GCC ARM.
- **jenkins-ci/build-example-ARM** - Builds supported examples with ARM.
- **jenkins-ci/build-example-GCC_ARM** - Builds supported examples with GCC ARM.
- **jenkins-ci/cmake-cloud-example-ARM** - CMake build for the cloud example with GCC ARM.
- **jenkins-ci/cmake-cloud-example-GCC_ARM** - CMake build for the cloud example with GCC ARM.
- **jenkins-ci/cmake-example-ARM** - Builds supported examples with CMake and ARM.
- **jenkins-ci/cmake-example-GCC_ARM** - Builds supported examples with CMake and GCC ARM.
- **jenkins-ci/cloud-client-test** - Tests the change with [mbed-cloud-client](https://github.com/ARMmbed/mbed-cloud-client) using the [mbed-cloud-client-example](https://github.com/ARMmbed/mbed-cloud-client-example).
- **jenkins-ci/greentea-test** - Runs [greentea tests](../debug-test/greentea-for-testing-applications.html).
   - `python tools/build_release.py -p <target> -t <toolchain>`.
- **jenkins-ci/unittests** - Runs [unit tests](../debug-test/unit-testing.html).
