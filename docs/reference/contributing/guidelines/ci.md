<h2 id="ci">Continuous integration</h2>

Continuous integration (CI) means mainly automatic testing for pull requests.

### Travis CI

In Mbed OS [Travis CI](https://travis-ci.org/ARMmbed/mbed-os) is used as primary automatic testing and checking run environment.

Travis configuration is located in the [.travis.yml](https://github.com/ARMmbed/mbed-os/blob/master/.travis.yml) file in Mbed OS root directory. Mbed OS uses public travis so test results are publicly available and there are public [documentation available](https://docs.travis-ci.com/).

#### Tests

- **continuous-integration/travis-ci/pr** - Travis run main.
- **travis-ci/astyle** - Check code style using [astyle](http://astyle.sourceforge.net/).
- **travis-ci/docs** - [Doxygen](http://www.doxygen.org/) and naming checks:
   - Assert that the Doxygen build produces no warnings.
   - Assert that all binary libraries are named correctly.
   - Assert that all assembler files are named correctly.
- **travis-ci/events** - Check that Mbed OS compiles and run events tests.
- **travis-ci/gitattributestest** - Check there are no changes after clone. This checks that `.gitattributes` is used correctly.
- **travis-ci/licence_check** - Check there is no GPL licence text in the code.
- **travis-ci/littlefs** - Test littlefs without embedded hardware.
- **travis-ci/tools-py2.7** - Run Python tools tests with Python 2.7.
- **travis-ci/psa-autogen** - Runs PSA SPM code generator.
   - Asserts that all PSA manifests in the tree are in correct form.
   - Asserts that no changes need to be made.

### Jenkins

We use [Jenkins](https://jenkins.io/) as an internal testing and checking environment. We execute tests that have special requirements for the execution enviroment in our internal Jenkins. In most cases, we publish test logs.

How it works:

- Jenkins uses a [scripted pipeline syntax](https://jenkins.io/doc/book/pipeline/).
- Jenkins scripts are not publicly available. There is a Jenkinsfile in the Mbed OS root folder, but that is just a trigger for tests.
- Jenkins selects required tests dynamically based on the code changes. For example, no tests execute if only markdown (.md) files change.
- Jenkins runs a first small number of tests to provide fast feedback, and then it runs additional tests.

#### Tests

- **continuous-integration/jenkins/pr-head** - Jenkins main pipeline script execution status.
- **jenkins-ci/build-ARM** - Build Mbed OS and examples with [ARM compiler](https://developer.arm.com/products/software-development-tools/compilers/arm-compiler). Related commands:
   - `mbed test --compile -t <toolchain> -m <target> `.
   - `python -u mbed-os/tools/test/examples/examples.py compile <toolchain> --mcu <target>`.
- **jenkins-ci/build-GCC_ARM** - Build Mbed OS and examples with GCC_ARM.
- **jenkins-ci/build-IAR** - Build Mbed OS and examples with IAR.
- **jenkins-ci/cloud-client-test** - Test the change with [mbed-cloud-client](https://github.com/ARMmbed/mbed-cloud-client) using the [mbed-cloud-client-example](https://github.com/ARMmbed/mbed-cloud-client-example).
- **jenkins-ci/dynamic-memory-usage** - Report dynamic memory use compared to the master branch.
- **jenkins-ci/exporter** - Export and build exported code. Related commands:
   - `python -u mbed-os/tools/test/examples/examples.py export <exporter> --mcu <target>`.
- **jenkins-ci/greentea-test** - Run [greentea tests](../tools/greentea-testing-applications.html).
- **jenkins-ci/mbed2-build-ARM** - Build Mbed OS 2 with [ARM compiler](https://developer.arm.com/products/software-development-tools/compilers/arm-compiler). Related commands:
   - `python tools/build_release.py -p <target> -t <toolchain>`.
- **jenkins-ci/mbed2-build-GCC_ARM** - Build Mbed OS 2 with GCC_ARM.
- **jenkins-ci/mbed2-build-IAR** - Build Mbed OS 2 with IAR.
- **jenkins-ci/unittests** - Run [unit tests](../tools/unit-testing.html).
- **tools-test-linux** - Test that tools work on Linux.
- **tools-test-mac** - Test that tools work on macOS.
- **tools-test-windows** - Test that tools work on Windows.
