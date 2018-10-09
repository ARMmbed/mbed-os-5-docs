## Continuous integration

Continuous integration (CI) means mainly automatic testing for pull requests

### Travis CI

In Mbed OS [Travis CI](https://travis-ci.org/) is used as primary automatic testing and checking run environment.

Travis configuration is located in .travis.yml file in Mbed OS root directory. Mbed OS use public travis so test results are publicly available and there are public [documentation available](https://docs.travis-ci.com/).

### Jenkins

[Jenkins](https://jenkins.io/) is used to run tests behind firewall. There are multiple reasons to run tests in Jenkins but typically those are related to high amount of concurrent builds or shared secrets.

#### How it works:
* Jenkins uses [scripted pipeline syntax](https://jenkins.io/doc/book/pipeline/)
* There is Jenkinsfile in Mbed OS root folder but that is just trigger for tests. Jenkins scripts are not publicly available at the moment.
* Jenkins select required tests dynamically based on the code changes. For example. no tests are executed if only markdown (.md) file changes
* Jenkins run first small amount of tests to provide fast feedback and then more tests

#### What kind of tests jenkins runs?

* **continuous-integration/jenkins/pr-head** Jenkins main pipeline script execution status
* **jenkins-ci/cloud-client-test** - Test the change with [mbed-cloud-client](https://github.com/ARMmbed/mbed-cloud-client) using [mbed-cloud-client-example](https://github.com/ARMmbed/mbed-cloud-client-example)
* **jenkins-ci/unittests** - Run [unit tests](/docs/tools/testing/unit_testing.html)
