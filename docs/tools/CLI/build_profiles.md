<h1 id="build-profiles">Build profiles</h1>

Arm Mbed OS 5 defines three collections of toolchain flags used during the build. These are __build profiles__.  The three build profiles are *develop*, *debug* and *release*. The Mbed Online Compiler uses the *develop* build profile. When building from Arm Mbed CLI, you may select the __build profile__ by passing your desired build profile, by name or path, to the `--profile` argument.

## Develop

- Small and fast code.
- Full error information. For example, asserts have file name and line number.
- Hard to follow code flow when using a debugger.
- Chip goes to sleep when idle:
   - Debugger is likely to drop connection.
   - Breaks the local file system on the [Arm Mbed interface](../introduction/index.html) on some boards.

## Debug

- Largest and slowest performance.
- Full error information. For example, asserts have file name and line number.
- Easy to step through code with a debugger.
- Disabled sleep mode.

## Release

- Smallest code size and still fast.
- Minimal error information.
- Chip goes to sleep when going idle:
   - Debugger is likely to drop connection.
   - Breaks the local file system on the [Mbed interface](../introduction/index.html) on some boards.

## User-defined build profile

As mentioned above, the __build profile__ defines the set of flags that is passed to the underlying compiler suite. You can also create a custom or user-defined __build profile__ using a JSON file according to the __build profile__ format mentioned in [JSON build profile format](#JSON-build-profile-format).

These flags stored in the JSON file are merged with other JSON files of the same structure when multiple `--profile` arguments are passed on the command line.

### JSON build profile format

The __build profiles__ are JSON files with the root object containing key-value pairs for each supported toolchain, such as `GCC_ARM`. Each key is a toolchain name and every value contains a mapping from a flag type to a list of flags that should be passed to the corresponding part of the compiler suite.

The required flag types are:

| Key      | Description                           |
|:---------|:--------------------------------------|
| `asm`    | Flags for the Assembler               |
| `c`      | Flags for the C Compiler              |
| `common` | Flags for both the C and C++ Compilers|
| `cxx`    | Flags for the C++ Compiler            |
| `ld`     | Flags for the Linker                  |

### Example

An example of a __build profile__:

```json
{
    "GCC_ARM": {
        "common": ["-c", "-Wall", "-Wextra",
                   "-Wno-unused-parameter", "-Wno-missing-field-initializers",
                   "-fmessage-length=0", "-fno-exceptions", "-fno-builtin",
                   "-ffunction-sections", "-fdata-sections", "-funsigned-char",
                   "-MMD", "-fno-delete-null-pointer-checks",
                   "-fomit-frame-pointer", "-Os"],
        "asm": ["-x", "assembler-with-cpp"],
        "c": ["-std=gnu99"],
        "cxx": ["-std=gnu++98", "-fno-rtti", "-Wvla"],
        "ld": ["-Wl,--gc-sections", "-Wl,--wrap,main", "-Wl,--wrap,_malloc_r",
               "-Wl,--wrap,_free_r", "-Wl,--wrap,_realloc_r",
               "-Wl,--wrap,_calloc_r", "-Wl,--wrap,exit", "-Wl,--wrap,atexit"]
    },
    "ARM": {
        "common": ["-c", "--gnu", "-Otime", "--split_sections",
                   "--apcs=interwork", "--brief_diagnostics", "--restrict",
                   "--multibyte_chars", "-O3"],
        "asm": [],
        "c": ["--md", "--no_depend_system_headers", "--c99", "-D__ASSERT_MSG"],
        "cxx": ["--cpp", "--no_rtti", "--no_vla"],
        "ld": []
    },
    "IAR": {
        "common": [
            "--no_wrap_diagnostics", "non-native end of line sequence", "-e",
            "--diag_suppress=Pa050,Pa084,Pa093,Pa082", "-Oh"],
        "asm": [],
        "c": ["--vla"],
        "cxx": ["--guard_calls", "--no_static_destruction"],
        "ld": ["--skip_dynamic_initialization", "--threaded_lib"]
    }
}
```

In the above example, you can tell that:

- `GCC_ARM`, `ARM` and `IAR` compiler suites are supported.
- The `ARM` C and C++ compilers use optimization level `-O3`.
- The `IAR` linker skips dynamic initialization.

And so on.
