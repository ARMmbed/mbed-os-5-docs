# Mbed OS build profile

The build profile defines the set of flags that is passed to the underlying compiler suite. In cmake based build system, `CMAKE_BUILD_TYPE` usually determines the build profile and normally this type is set by application target CMake to select the profile.

## User-defined build profile

In Mbed OS CMake based build system has dedicated cmake profile scripts for every build profiles:

1. [develop.cmake](https://github.com/ARMmbed/mbed-os/blob/master/tools/cmake/profiles/develop.cmake)
2. [debug.cmake](https://github.com/ARMmbed/mbed-os/blob/master/tools/cmake/profiles/debug.cmake)
3. [release.cmake](https://github.com/ARMmbed/mbed-os/blob/master/tools/cmake/profiles/release.cmake)

The build system includes one of the profile scripts into the build depending on CMAKE_BUILD_TYPE. The CMAKE_BUILD_TYPE is set by Mbed CLI 2 based on the argument it receives in the "-b" or "--profile" command line. If Mbed CLI 2 does not receive any argument, then it sets CMAKE_BUILD_TYPE to "Develop" based on that build system includes the corresponding "develop.cmake" script into the build.

### Example

Select `debug` profile using Mbed CLI 2 command:

```
 mbedtools compile -t GCC_ARM -m k64f -b debug
 ```

In case the application is using the direct CMake command then selecting the build type by passing `-DCMAKE_BUILD_TYPE` argument and if there is no `CMAKE_BUILD_TYPE` argument passed with cmake configuration command then the build system sets `CMAKE_BUILD_TYPE` to `develop`.

### Example

Select `release` profile using direct CMake command:

```
cmake -GNinja .. -DCMAKE_BUILD_TYPE=release
```

## Build profile script

Every profile script has the function `mbed_set_profile_options` which expects target and toolchain as an argument. This function is setting the necessary flags to the target using generator expression and target link options according to the toolchain argument. This function gets called from Mbed OS root CMake.

### Comparison between different profile script target configuration

#### GCC_ARM toolchain

| Target config                | debug.cmake                           | develop.cmake                    | release.cmake                         |
|:-----------------------------|:--------------------------------------|:---------------------------------|:--------------------------------------|
| `profile_c_compile_options`  |             "-c" <br/> <font color='red'>"-Og"</font>               | "-c" <br/> <font color='red'>"-Os"</font>     | "-c" <br/> <font color='red'>"-Os"</font>    |
| `profile_cxx_compile_options`  | "-fno-rtti"<br/>"-Wvla"<br/><font color='red'>"-Og"<br/></font><font color='red'>"-c"</font>| "-fno-rtti"<br/>"-Wvla"<br/><font color='red'>"-Os"</font>    | "-fno-rtti"<br/>"-Wvla"<br/><font color='red'>"-Os"</font><br/><font color='red'>"-c"</font>| 
| `profile_asm_compile_options`| <font color='red'>"-c"</font><br/>"-x"<br/>"assembler-with-cpp"            | "-x"<br/>"assembler-with-cpp"    | <font color='red'>"-c"</font><br/>"-x"<br/>"assembler-with-cpp" |
| `profile_link_options`       | "-Wl,--gc-sections"<br/>"-Wl,--wrap,main"<br/>"-Wl,--wrap,_malloc_r"<br/>"-Wl,--wrap,_free_r"<br/>"-Wl,--wrap,_realloc_r"<br/>"-Wl,--wrap,_memalign_r"<br/>"-Wl,--wrap,_calloc_r"<br/>"-Wl,--wrap,exit"<br/>"-Wl,--wrap,atexit"<br/>"-Wl,-n"<br/>                  | "-Wl,--gc-sections"<br/>"-Wl,--wrap,main"<br/>"-Wl,--wrap,_malloc_r"<br/>"-Wl,--wrap,_free_r"<br/>"-Wl,--wrap,_realloc_r"<br/>"-Wl,--wrap,_memalign_r"<br/>"-Wl,--wrap,_calloc_r"<br/>"-Wl,--wrap,exit"<br/>"-Wl,--wrap,atexit"<br/>"-Wl,-n"<br/>    | "-Wl,--gc-sections"<br/>"-Wl,--wrap,main"<br/>"-Wl,--wrap,_malloc_r"<br/>"-Wl,--wrap,_free_r"<br/>"-Wl,--wrap,_realloc_r"<br/>"-Wl,--wrap,_memalign_r"<br/>"-Wl,--wrap,_calloc_r"<br/>"-Wl,--wrap,exit"<br/>"-Wl,--wrap,atexit"<br/>"-Wl,-n"<br/>             |
| `target_compile_definitions`  |             MBED_TRAP_ERRORS_ENABLED=1<br/>MBED_DEBUG     | MBED_TRAP_ERRORS_ENABLED=1   | NDEBUG   |


#### ARM toolchain

| Target config                | debug.cmake                           | develop.cmake                    | release.cmake                         |
|:-----------------------------|:--------------------------------------|:---------------------------------|:--------------------------------------|
| `profile_c_compile_options`  |             "-c" <br/> <font color='red'>-O1</font>               | "-c" <br/> <font color='red'>"-Os"</font>     | "-c" <br/> <font color='red'>"-Oz"</font>    |
| `profile_cxx_compile_options`  | "-fno-rtti"<br/>"-fno-c++-static-destructors"<br/><font color='red'>"-O1"</font>| "-fno-rtti"<br/>"-fno-c++-static-destructors"<br/><font color='red'>"-Os"</font>   | "-fno-rtti"<br/>"-fno-c++-static-destructors"<br/><font color='red'>"-Oz"</font>| 
| `profile_link_options`  |             <font color='red'>"--verbose"</font><br/><font color='red'>"--remove"</font><br/>"--show_full_path"<br/>"--legacyalign"<br/>"--any_contingency"<br/>"--keep=os_cb_sections"               | "--show_full_path"<br/>"--legacyalign"<br/>"--any_contingency"<br/>"--keep=os_cb_sections"<br/><font color='red'>"--inline"</font>     | "--show_full_path"<br/>"--legacyalign"<br/>"--any_contingency"<br/>"--keep=os_cb_sections"<br/><font color='red'>"--inline"</font>    |
| `target_compile_definitions`  |             __ASSERT_MSG<br/>MBED_TRAP_ERRORS_ENABLED=1<br/>MBED_DEBUG<br/>MULADDC_CANNOT_USE_R7     | __ASSERT_MSG<br/>MBED_TRAP_ERRORS_ENABLED=1   | __ASSERT_MSG<br/>NDEBUG   |


