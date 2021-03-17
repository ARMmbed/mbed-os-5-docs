# The code structure

The build rules are different for python build tools and CMake. Please refer to [Build system] section for more details how sources are being picked. We only describe here common code structure between the build systems.

## Test directories

Functional tests are organized into test cases and test suite directories within a `TESTS` directory. Each test suite is a subdirectory of the `TESTS`, and each test case is a subdirectory of a test suite. When tests build, each test case compiles independently. The test suite `host_tests` is reserved for scripts that run and validate a test case. The following tree is a reduced version of the tests subdirectory of Mbed OS:

```
TESTS
├── events
│  ├── queue
│  │  └── main.cpp
│  └── timing
│     └── main.cpp
├── host_tests
│  ├── ...
│  └── timing_drift_auto.py
├── integration
│  └── basic
│     └── main.cpp
└── network
   ├── emac
   │  ├── ...
   │  └── main.cpp
   └── wifi
      ├── ...
      └── main.cpp
```

None of these files are included in a build run with `mbed compile`. When running `mbed test` or `mbed test --compile`, the `TESTS/events/queue` test case compiles without the sources from `TESTS/events/timing` or `TESTS/integration/basic`.

The similar naming is true also for UNITTESTS.

```
UNITTESTS
├── events
│  ├── queue
│  │  └── main.cpp
│  └── timing
│     └── main.cpp
├── host_tests
│  ├── ...
│  └── timing_drift_auto.py
├── integration
│  └── basic
│     └── main.cpp
└── network
   ├── emac
   │  ├── ...
   │  └── main.cpp
   └── wifi
      ├── ...
      └── main.cpp
```
