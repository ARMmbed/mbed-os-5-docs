# Toolchain profiles

## User perspective

A toolchain or build system profile is a set of flags that is guaranteed to be passed to the underyling compiler suite.

These flags are stored in a JSON file that may be merged with other JSON files of the same structure.

## JSON toolchain profile format

The JSON object that represents a toolchain profile is a dictionary mapping from toolchains, like `GCC_ARM`, to their flags, like `-O3`.

The structure is as follows: each toolchain supported by a toolchain profile has a dictionary in the root dictionary. 

This dictionary contains a mapping from a flag type to a list of flags that should be passed the corresponding part of the compiler suite.

The required flag types are:

| Key      | Description                           |
|:---------|:--------------------------------------|
| `c`      | Flags for the C Compiler              |
| `cxx`    | Flags for the C++ Compiler            |
| `common` | Flags for both the C and C++ Compilers|
| `asm`    | Flags for the Assembler               |

## Example

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

From this Toolchain profile, we can tell that:

- `GCC_ARM`, `ARM`, and `IAR` compiler suites are supported.
- The `ARM` C and C++ compilers will be using optimization level `-O3`.
- The `IAR` linker will skip dynamic initialization.

And so on.

## API perspective

The toolchains take in an optional argument, ``build_profile``, that will contain a map from flag types to lists of flags. This looks exactly the same in Python as it does in the JSON format above.

The meaning of the flags, and which ones are required, is the same as the user perspective.

A developer using the API must parse the user-provided files themselves and extract the appropriate sub-dictionary from the file afterwards.

A convenience function that does this for a developer is `tools.options.extract_profile`; it calls ``args_error`` when a toolchain profile JSON file does not provide flags for the selected toolchain.
