## Mbed OS Build Rules

The Mbed OS Build Tools scan your project for source files every time you compile. This document describes the rules that the build tools use to decide which source files to include in each build. The Mbed OS Build Tools use the [target configuration](mbed_targets.md) found in `targets.json`, `mbed_app.json` and `mbed_lib.json` as input to these rules.

The Build Tools include every source file found in the project unless it is in a label directory, it is in a test directory or it matches a pattern in an `.mbedignore file`.

### Source Files

Mbed OS Build tools determine what sort of source file it has found based on the file's extension. The following table lists all files that are used in a build.

| Extension           | File Type         | Used by                        |
|---------------------|-------------------|--------------------------------|
| `.a`, `.ar`         | Archive           | Toolchain's Linker             |
| `.c`                | C Source          | Toolchain's C Compiler         |
| `.cc`, `.cpp`       | C++ Source        | Toolchain's C++ Compiler       |
| `.h`, `.hpp`, `.hh` | C/C++ Header      | Toolchain's C and C++ Compiler |
| `.icf`              | IAR Linker File   | IAR's Linker                   |
| `.ld`               | GCC Linker Script | GCC's Linker (`ld`)            |
| `.o`                | Object            | Toolchain's Linker             |
| `.s`, `.S`          | Assembly          | Toolchain's assebler           |
| `.sct`              | ARM Scatter File  | ARM's Linker (`armlink`)       |


### Label Directories

Label directories are directories that follow a naming convention: an upper case label type followed by an underscore followed by a label. The Mbed OS Build tools define 4 label types:

 * `TARGET`, constructed from the configuration value `target.extra_labels` and the name of the targets.
 * `FEATURE`, constructed from the configuration value `target.features`.
 * `COMPONENT`, controlled from the configuration value `target.components`.
 * `TOOLCHAIN`, controlled completely by the toolchain used to build.


#### Target Directories

The target labeled directories are used for selecting sources that are specific to an MCU or MCU family. The set of directories included in a given build is all of the names of the targets in the inheritance heirachy and the `target.extra_labels`. The following is an example `targets.json`:

```json
{
    "MCUXPRESSO": {
        "inherits": ["Target"],
        "public": false
    },
    "TEENSY3_1": {
        "inherits": ["MCUXPRESSO"],
        "extra_labels": ["K20XX", "K20DX256"]
    }
}
```

The above example will include source files in directories named `TARGET_MCUXPRESSO` and `TARGET_TEENSY3_1`, from the inheritance heirachy and `TARGET_K20XX` and `TARGET_K20DX256` from the `target.extra_labels` value. It will not include source files within `TARGET_NORDIC`, `TARGET_K66F` or `TARGET_NUCLEO_F411` directories as they are not in the list of labels included in the label type `TARGET`

#### Feature Directories

The feature labeled directories are used for software that implements some funtionality that requires some amount of space even when it's not used. The set of directories include by the `FEATURE` label type is entirely controlled by the configuration value `target.features`. The following is a trimmed down version of an example `targets.json`:

```json
{
    "NRF52_DK": {
        "inherits": ["Target"],
        "features": ["BLE"]
    }
}
```

In the above example, `mbed compile` will include files in directories named `FEATURE_BLE`, and not directories such as `FEATURE_STORAGE` or `FEATURE_CRYTOCELL310`.

#### Component Directories

The component labeled directories are used for software that implements some funtionality. They are within label directory primarily because we don't expect every program to use this software, and including this software in every build would needlessly increase build time.  The set of directories include by the `COMPONENT` label type is entirely controlled by the configuration value `target.components`. The following is a trimmed down version of an example `targets.json`:

```json
{
    "NRF52_DK": {
        "inherits": ["Target"],
        "components": ["SPIF"]
    }
}
```

In the above example, `mbed compile` will include files in directories named `COMPONENT_SPIF`, and not directories such as `COMPONENT_SD` or `COMPONENT_FLASHIAP`.

#### Toolchain Directories

The toolchain labeled directories are used for toolchain specific files such as assembly or linker files. The compilers use the following label sets:

| Toolchain                    | Labels                                                     |
|------------------------------|------------------------------------------------------------|
| ARM compiler 5               | `TOOLCHAIN_ARM` and `TOOLCHAIN_ARM_STD`                    |
| ARM compiler 5 with microlib | `TOOLCHAIN_ARM` and `TOOLCHAIN_ARM_MICRO`                  |
| ARM compiler 6               | `TOOLCHAIN_ARM`, `TOOLCHAIN_ARM_STD` and `TOOLCHAIN_ARMC6` |
| IAR EWARM                    | `TOOLCHAIN_IAR`                                            |
| GCC ARM Embedded             | `TOOLCHAIN_GCC` and `TOOLCHAIN_GCC_ARM`                    |

When compiling with `-t GCC_ARM` or `mbed toolchain GCC_ARM`, source files found within `TOOLCHAIN_GCC` and `TOOLCHAIN_GCC_ARM` are included and files found within `TOOLCHAIN_IAR` and `TOOLCHAIN_ARM` are not.

### Test Directories

Functional tests are organised into test case and test suite directories within a `TESTS` directory. Each test suite is a subdirectory of the `TESTS` and each test case is a subdirectory of a test suite. When tests are built, each test case is compiled independently. The test suite `host_tests` is reserved for scripts that run and validate a test case. The following tree is a ruduced version of the tests subdirectory of Mbed OS:

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

None of these files are included in a build run with `mbed compile`. When running `mbed test` or `mbed test --compile`, the `TESTS/events/queue` test case will be compiled without the sources from `TESTS/events/timing` or `TESTS/integration/basic`

### `.mbedignore`

The `.mbedignore` rules have the last say in excluding files from a build. Files matching patters in an `.mbedignore` file will be excluded from a build even if the file would be included by a label rule or a test directory. Patterns within a `.mbedignore` have the syntax and meaning of [fnmatch python module](https://docs.python.org/3/library/fnmatch.html) and only match files within the directory of the `.mbedignore` file. For example, consider the following `.mbedignore file`:

```
events/*
```

With this file, no sources found within the subdirectory `events` are include.

