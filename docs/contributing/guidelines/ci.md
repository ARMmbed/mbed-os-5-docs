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
- **jenkins-ci/build-ARM** - Builds Mbed OS and examples with the [ARM compiler](https://developer.arm.com/products/software-development-tools/compilers/arm-compiler). Related commands:
   - `mbed test --compile -t <toolchain> -m <target> `.
   - `python -u mbed-os/tools/test/examples/examples.py compile <toolchain> --mcu <target>`.
- **jenkins-ci/build-GCC_ARM** - Builds Mbed OS and examples with GCC_ARM.
- **jenkins-ci/build-IAR** - Builds Mbed OS and examples with IAR.
- **jenkins-ci/cloud-client-test** - Tests the change with [mbed-cloud-client](https://github.com/ARMmbed/mbed-cloud-client) using the [mbed-cloud-client-example](https://github.com/ARMmbed/mbed-cloud-client-example).
- **jenkins-ci/dynamic-memory-usage** - Reports dynamic memory use compared to the master branch.
- **jenkins-ci/exporter** - Exports and builds exported code. Related commands:
   - `python -u mbed-os/tools/test/examples/examples.py export <exporter> --mcu <target>`.
- **jenkins-ci/greentea-test** - Runs [greentea tests](../debug-test/greentea-for-testing-applications.html).
- **jenkins-ci/mbed2-build-ARM** - Builds Mbed OS 2 with the [ARM compiler](https://developer.arm.com/products/software-development-tools/compilers/arm-compiler). Related commands:
   - `python tools/build_release.py -p <target> -t <toolchain>`.
- **jenkins-ci/mbed2-build-GCC_ARM** - Builds Mbed OS 2 with GCC_ARM.
- **jenkins-ci/mbed2-build-IAR** - Builds Mbed OS 2 with IAR.
- **jenkins-ci/unittests** - Runs [unit tests](../debug-test/unit-testing.html).
- **tools-test-linux** - Tests tools work on Linux.
- **tools-test-mac** - Tests tools work on macOS.
- **tools-test-windows** - Tests tools work on Windows.
