## Continuous integration

Continuous integration (CI) means mainly automatic testing for pull requests

### Travis CI

In Mbed OS [Travis CI](https://travis-ci.org/ARMmbed/mbed-os) is used as primary automatic testing and checking run environment.

Travis configuration is located in [.travis.yml](https://github.com/ARMmbed/mbed-os/blob/master/.travis.yml) file in Mbed OS root directory. Mbed OS use public travis so test results are publicly available and there are public [documentation available](https://docs.travis-ci.com/).

#### Tests

* **continuous-integration/travis-ci/pr** - Main run main
* **travis-ci/astyle** - Check code style using [astyle](http://astyle.sourceforge.net/)
* **travis-ci/docs** - [Doxygen](http://www.doxygen.org/) and naming checks:
** Assert that the Doxygen build produced no warnings
** Assert that all binary libraries are named correctly
** Assert that all assebler files are named correctly
* **travis-ci/events** - Check that Mbed OS compiles and run events tests
* **travis-ci/gitattributestest** - Check that no changes after clone. This check that .gitattributes is used right way
* **travis-ci/licence_check** - Checking that there is no GPL licence text in code
* **travis-ci/littlefs** - Testing littlefs without embedded hardware
* **travis-ci/tools-py2.7** - Run python tools tests with python 2.7

### Jenkins

[Jenkins](https://jenkins.io/) is used to run tests behind firewall. There are multiple reasons to run tests in Jenkins but typically those are related to high amount of concurrent builds or shared secrets.

#### How it works:
* Jenkins uses [scripted pipeline syntax](https://jenkins.io/doc/book/pipeline/)
* There is Jenkinsfile in Mbed OS root folder but that is just trigger for tests. Jenkins scripts are not publicly available at the moment.
* Jenkins select required tests dynamically based on the code changes. For example. no tests are executed if only markdown (.md) file changes
* Jenkins run first small amount of tests to provide fast feedback and then more tests

#### Tests

* **continuous-integration/jenkins/pr-head** Jenkins main pipeline script execution status
* **jenkins-ci/cloud-client-test** - Test the change with [mbed-cloud-client](https://github.com/ARMmbed/mbed-cloud-client) using [mbed-cloud-client-example](https://github.com/ARMmbed/mbed-cloud-client-example)
* **jenkins-ci/unittests** - Run [unit tests](/docs/tools/testing/unit_testing.html)
* **jenkins-ci/greentea-test** - Run [greentea tests](/docs/tools/testing/testing_greentea.html)
* **jenkins-ci/build-GCC_ARM** - Build Mbed OS and examples with GCC_ARM. Related commands:
 * `mbed test --compile -t <toolchain> -m <target> `
 * `python -u mbed-os/tools/test/examples/examples.py compile <toolchain> --mcu <target>`
* **jenkins-ci/build-ARM** - Build Mbed OS and examples with ARM
* **jenkins-ci/build-IAR** - Build Mbed OS and examples with IAR
* **jenkins-ci/mbed2-build-GCC_ARM** - Build Mbed OS 2 with GCC_ARM. Related commands:
 * `python tools/build_release.py -p <target> -t <toolchain>`
* **jenkins-ci/mbed2-build-ARM** - Build Mbed OS 2 with ARM
* **jenkins-ci/mbed2-build-IAR** - Build Mbed OS 2 with IAR
* **jenkins-ci/exporter** - Export and build exported code. Related commands:
 * `python -u mbed-os/tools/test/examples/examples.py export <exporter> --mcu <target>`
* **jenkins-ci/dynamic-memory-usage** - Report dynamic memory usage compared to the master branch
