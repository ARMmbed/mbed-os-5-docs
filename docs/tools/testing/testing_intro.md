<h1 id="tools-testing">Testing</h1>

Testing is a critical step in the development process. Traditional software testing can be described as three levels of testing: unit testing, integration testing and system testing. These levels are often pictured as a pyramid to indicate the amount of testing needed for each level.

```
^ Testing level
|
|       /\
|      /  \       System testing
|     /----\
|    /      \     Integration testing
|   /--------\
|  /          \   Unit testing
| /------------\
|
*-------------------> Amount of tests
```

The Arm Mbed ecosystem offers several tools to help you test your code.

You can use unit testing tools to build and run Mbed OS unit tests. Each unit test is built into an isolated test executable using a separate build system and build tools native to the development machine without any hardware or software dependencies. You can use the tool with Mbed CLI using the keyword `test` with `--unittests` flag.

Greentea, Icetea, `htrun` and `mbed-ls` are testing tools written in Python. Greentea tests serve as functional unit tests in C++, as well as integration tests for complex use cases that execute on microcontrollers. The Icetea test tool adds more support for interoperability testing by making it easier to handle multiple devices and external services during testing. Arm Mbed CLI has a verb `test` that drives these tools to form a testing system. These comprise our automated testing framework for Mbed OS development. 

The testing system automates the process of flashing Mbed boards, driving the tests and accumulating test results into test reports. Developers and Mbed Partners use this system for local development, as well as for automation in a Continuous Integration environment.

This section explains how to build, run and write tests. It also includes details about our Greentea and utest testing tools.
