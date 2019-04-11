# Mbed OS build rules

The Mbed OS build tools scan your project for source files every time you compile. This document describes the rules that the build tools use to decide which source files to include in each build. The Mbed OS build tools use the [target configuration](adding-and-configuring-targets.html) found in `targets.json`, `mbed_app.json` and `mbed_lib.json` as input to these rules. If you are looking for how to pass options to the compilers, please see the [build profiles documentation](../tools/build-profiles.html).

The build tools include every source file found in the project unless it is in a label directory, it is in a test directory or it matches a pattern in an `.mbedignore file`.

## Source files

Mbed OS build tools determine the type of source file found based on the file's extension. The following table lists all files used in a build:

| Extension                   | File type         | Used by                        |
|-----------------------------|-------------------|--------------------------------|
| `.a`, `.ar`                 | Archive           | Toolchain's linker             |
| `.c`                        | C source          | Toolchain's C compiler         |
| `.cc`, `.cpp`               | C++ source        | Toolchain's C++ compiler       |
| `.h`, `.hpp`, `.hh`, `.inc` | C/C++ header      | Toolchain's C and C++ compiler |
| `.icf`                      | IAR linker file   | IAR's linker                   |
| `.ld`                       | GCC linker script | GCC's linker (`ld`)            |
| `.o`                        | Object            | Toolchain's linker             |
| `.s`, `.S`                  | Assembly          | Toolchain's assembler          |
| `.sct`                      | ARM scatter file  | ARM's linker (`armlink`)       |


## Label directories

Label directories are directories that follow a naming convention: an upper case label type followed by an underscore followed by a label. The Mbed OS build tools define four label types:

- `TARGET`, constructed from the configuration value `target.extra_labels` and the name of the targets.
- `FEATURE`, constructed from the configuration value `target.features`.
- `COMPONENT`, controlled from the configuration value `target.components`.
- `TOOLCHAIN`, controlled completely by the toolchain used to build.

The Mbed OS build tools skip all label directories, unless you configure them explicitly, as described above.

For more information about using, extending and removing labels, please see [Adding and configuring targets](../reference/adding-and-configuring-targets.html#extra-labels-extra-labels-add-and-extra-labels-remove).

### Target directories

The target labeled directories are used for selecting sources specific to an MCU or MCU family. The set of directories included in a given build is all of the names of the targets in the inheritance hierarchy and the `target.extra_labels`. The following is an example `targets.json`:

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

The above example includes source files in directories named `TARGET_MCUXPRESSO` and `TARGET_TEENSY3_1` from the inheritance hierarchy and `TARGET_K20XX` and `TARGET_K20DX256` from the `target.extra_labels` value. It does not include source files within the `TARGET_NORDIC`, `TARGET_K66F` or `TARGET_NUCLEO_F411` directories because they are not in the list of labels included in the label type `TARGET`.

### Feature directories

The feature labeled directories are used for software that implements functionality that requires some amount of space even when it's not used. The configuration value `target.features` entirely controls the set of directories the `FEATURE` label type includes. The following is a trimmed down version of an example `targets.json`:

```json
{
    "NRF52_DK": {
        "inherits": ["Target"],
        "features": ["BLE"]
    }
}
```

In the above example, `mbed compile` includes files in directories named `FEATURE_BLE`, and not directories such as `FEATURE_STORAGE` or `FEATURE_CRYTOCELL310`.

### Component directories

The component labeled directories are used for software that implements funtionality. They are within label directories primarily because we don't expect every program to use this software, and including this software in every build would needlessly increase build time.  The configuration value `target.components` entirely controls the set of directories the `COMPONENT` label type includes. The following is a shortened version of an example `targets.json`:

```json
{
    "NRF52_DK": {
        "inherits": ["Target"],
        "components": ["SPIF"]
    }
}
```

In the above example, `mbed compile` includes files in directories named `COMPONENT_SPIF`, and not directories such as `COMPONENT_SD` or `COMPONENT_FLASHIAP`.

### Toolchain directories

The toolchain labeled directories are used for toolchain specific files, such as assembly or linker files. The compilers use the following label sets:

| Toolchain                    | Labels                                                     |
|------------------------------|------------------------------------------------------------|
| ARM compiler 5               | `TOOLCHAIN_ARM` and `TOOLCHAIN_ARM_STD`                    |
| ARM compiler 5 with microlib | `TOOLCHAIN_ARM` and `TOOLCHAIN_ARM_MICRO`                  |
| ARM compiler 6               | `TOOLCHAIN_ARM`, `TOOLCHAIN_ARM_STD` and `TOOLCHAIN_ARMC6` |
| IAR EWARM                    | `TOOLCHAIN_IAR`                                            |
| GCC ARM Embedded             | `TOOLCHAIN_GCC` and `TOOLCHAIN_GCC_ARM`                    |

When compiling with `-t GCC_ARM` or `mbed toolchain GCC_ARM`, source files found within `TOOLCHAIN_GCC` and `TOOLCHAIN_GCC_ARM` are included, and files found within `TOOLCHAIN_IAR` and `TOOLCHAIN_ARM` are not.

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

## `.mbedignore`

The `.mbedignore` rules override other rules for excluding files from a build. Files matching patterns in an `.mbedignore` file are excluded from a build even if a label rule or a test directory would include the file.

### Usage

You can place an `.mbedignore` file in any searched directory.

Avoid defining rules that would cross library boundaries because these can lead to side effects or build problems that are hard to find.

### Syntax

Each line in the `.mbedignore` file is a pattern for matching files. No files that matches any pattern found in any `.mbedignore` file are included when building or exporting.

The following wildcards are accepted:

|Pattern | Meaning|
|--------|--------|
| `*` | Matches everything. |
| `?` | Matches any single character. |
| `[seq]` | Matches any character in seq. |
| `[!seq]` | Matches any character not in seq. |

The file is parsed with Python's [fnmatch](https://docs.python.org/2/library/fnmatch.html). The syntax follows basic shell patterns with the following exceptions:

- Each line is treated as though it were prefixed with the path of the `.mbedignore` file.
- A line cannot start with `.` or `/` (because of the previous rule).

The globbing functionality is not used, so you cannot recursively match a specific file pattern. Instead, you need to define a rule per directory.

### Example

A file located in `source/obsolete/.mbedignore` has the following content:

```
*.c
*.h
second_level/*.c
```

After applying the first rule, the actual patterns used internally for matching the source files are:

```
source/obsolete/*.c
source/obsolete/*.h
source/obsolete/second_level/*.c
```
