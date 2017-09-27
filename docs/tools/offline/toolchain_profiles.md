## Toolchain profiles

### User perspective

A toolchain or build system profile is a set of flags that is guaranteed to be passed to the underyling compiler suite.

These flags are stored in a JSON file that may be merged with other JSON files of the same structure.

### JSON toolchain profile format

The JSON object that represents a toolchain profile is a dictionary mapping from toolchains, such as `GCC_ARM`, to their flags, such as `-O3`.

The structure is as follows: each toolchain supported by a toolchain profile has a dictionary in the root dictionary.

This dictionary contains a mapping from a flag type to a list of flags that should be passed to the corresponding part of the compiler suite.

The required flag types are:

| Key      | Description                           |
|:---------|:--------------------------------------|
| `c`      | Flags for the C Compiler              |
| `cxx`    | Flags for the C++ Compiler            |
| `common` | Flags for both the C and C++ Compilers|
| `asm`    | Flags for the Assembler               |
| `ld`     | Flags for the Linker                  |

### Example

An example of a toolchain profile:

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

From this toolchain profile, we can tell that:

- `GCC_ARM`, `ARM` and `IAR` compiler suites are supported.
- The `ARM` C and C++ compilers will be using optimization level `-O3`.
- The `IAR` linker will skip dynamic initialization.

And so on.

### API perspective

The toolchains take in an optional argument, ``build_profile``, that maps from flag types to lists of flags. When provided, this argument must contain a dict mapping from flag types to a list of flags to provide to the compiler. Without this argument, the toolchain uses a build profile that contains no flags in each required flag type. The required flag types are:

| Key      | Description                           |
|:---------|:--------------------------------------|
| `c`      | Flags for the C Compiler              |
| `cxx`    | Flags for the C++ Compiler            |
| `common` | Flags for both the C and C++ Compilers|
| `asm`    | Flags for the Assembler               |
| `ld`     | Flags for the Linker                  |

A developer using the API must parse the user-provided files themselves and extract the appropriate subdictionary from the file afterwards.
The tools provide a convenience function, `tools.options.extract_profile`, that parses a build profile from a `--profile` option given on the command line. This function calls `args_error` when a toolchain profile JSON file does not provide flags for the selected toolchain.
