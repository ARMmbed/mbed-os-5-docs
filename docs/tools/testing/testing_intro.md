## Testing

Testing is a critical step in the development process. The Arm Mbed ecosystem offers several tools to help you test your code. 

Greentea, `htrun` and `mbed-ls` are testing tools written in Python. Greentea tests serve as functional unit tests in C++, as well as integration tests for complex use cases that execute on microcontrollers. The Mbed CLI tool has a verb test that drives these tools to form a testing system. These comprise our automated testing framework for Mbed OS development. 

The testing system automates the process of flashing Mbed boards, driving the tests and accumulating test results into test reports. Developers and Mbed Partners use this system for local development, as well as for automation in a Continuous Integration environment.

This section explains how to build, run and write tests. It also includes details about our Greentea and utest testing tools.
