# Mbed OS build profile

The build profile defines a set of flags that is passed to the underlying compiler suite to specify the build type. In CMake based build system, `CMAKE_BUILD_TYPE` usually determines the build type and is set by the application CMake target.

## User-defined build profile

In Mbed OS CMake based build system has dedicated cmake profile scripts for every build profiles:

* Develop - Disable debugging with high speed optimization
* Debug - Enable debugging with low code size optimization
* Release - Disable debugging with high code size optimization

Each profile is [implemented as a CMake module](https://github.com/ARMmbed/mbed-os/blob/master/tools/cmake/profiles/) which is selected depending on the value of `CMAKE_BUILD_TYPE`. The `CMAKE_BUILD_TYPE` is set by Mbed CLI 2 based on the argument it receives for the `-b` or `--profile` optional command line argument. The default value for `CMAKE_BUILD_TYPE` is `Develop`.

### Example

Selecting the `Debug` profile using Mbed CLI 2 command:

```
 mbedtools compile -t GCC_ARM -m k64f -b debug
```

Advanced users who choose to run CMake directly should use `-D CMAKE_BUILD_TYPE=Debug`.

## Build profile script

Every profile CMake module implement the `mbed_set_profile_options()` function which expects a CMake target and toolchain identifier as arguments. The function sets the toolchain compiler and linker optional arguments as well as compile definitions for the CMake target. Compiler options are set per supported programming language.

### Comparison between different profile script target configuration

#### GCC_ARM toolchain

| Target config                | debug.cmake                           | develop.cmake                    | release.cmake                         |
|:-----------------------------|:--------------------------------------|:---------------------------------|:--------------------------------------|
| C compile options  |             "-c" <br/> <font color='red'>"-Og"</font>               | "-c" <br/> <font color='red'>"-Os"</font>     | "-c" <br/> <font color='red'>"-Os"</font>    |
| C++ compile options  | "-fno-rtti"<br/>"-Wvla"<br/><font color='red'>"-Og"<br/></font><font color='red'>"-c"</font>| "-fno-rtti"<br/>"-Wvla"<br/><font color='red'>"-Os"</font>    | "-fno-rtti"<br/>"-Wvla"<br/><font color='red'>"-Os"</font><br/><font color='red'>"-c"</font>| 
| ASM compile options | <font color='red'>"-c"</font><br/>"-x"<br/>"assembler-with-cpp"            | "-x"<br/>"assembler-with-cpp"    | <font color='red'>"-c"</font><br/>"-x"<br/>"assembler-with-cpp" |
| Linker options       | "-Wl,--gc-sections"<br/>"-Wl,--wrap,main"<br/>"-Wl,--wrap,_malloc_r"<br/>"-Wl,--wrap,_free_r"<br/>"-Wl,--wrap,_realloc_r"<br/>"-Wl,--wrap,_memalign_r"<br/>"-Wl,--wrap,_calloc_r"<br/>"-Wl,--wrap,exit"<br/>"-Wl,--wrap,atexit"<br/>"-Wl,-n"<br/>                  | "-Wl,--gc-sections"<br/>"-Wl,--wrap,main"<br/>"-Wl,--wrap,_malloc_r"<br/>"-Wl,--wrap,_free_r"<br/>"-Wl,--wrap,_realloc_r"<br/>"-Wl,--wrap,_memalign_r"<br/>"-Wl,--wrap,_calloc_r"<br/>"-Wl,--wrap,exit"<br/>"-Wl,--wrap,atexit"<br/>"-Wl,-n"<br/>    | "-Wl,--gc-sections"<br/>"-Wl,--wrap,main"<br/>"-Wl,--wrap,_malloc_r"<br/>"-Wl,--wrap,_free_r"<br/>"-Wl,--wrap,_realloc_r"<br/>"-Wl,--wrap,_memalign_r"<br/>"-Wl,--wrap,_calloc_r"<br/>"-Wl,--wrap,exit"<br/>"-Wl,--wrap,atexit"<br/>"-Wl,-n"<br/>             |
| Compile defintions  |             MBED_TRAP_ERRORS_ENABLED=1<br/>MBED_DEBUG     | MBED_TRAP_ERRORS_ENABLED=1   | NDEBUG   |


#### ARM toolchain

| Target config                | debug.cmake                           | develop.cmake                    | release.cmake                         |
|:-----------------------------|:--------------------------------------|:---------------------------------|:--------------------------------------|
| C compile options  |             "-c" <br/> <font color='red'>-O1</font>               | "-c" <br/> <font color='red'>"-Os"</font>     | "-c" <br/> <font color='red'>"-Oz"</font>    |
| C++ compile options  | "-fno-rtti"<br/>"-fno-c++-static-destructors"<br/><font color='red'>"-O1"</font>| "-fno-rtti"<br/>"-fno-c++-static-destructors"<br/><font color='red'>"-Os"</font>   | "-fno-rtti"<br/>"-fno-c++-static-destructors"<br/><font color='red'>"-Oz"</font>| 
| Linker options  |             <font color='red'>"--verbose"</font><br/><font color='red'>"--remove"</font><br/>"--show_full_path"<br/>"--legacyalign"<br/>"--any_contingency"<br/>"--keep=os_cb_sections"               | "--show_full_path"<br/>"--legacyalign"<br/>"--any_contingency"<br/>"--keep=os_cb_sections"<br/><font color='red'>"--inline"</font>     | "--show_full_path"<br/>"--legacyalign"<br/>"--any_contingency"<br/>"--keep=os_cb_sections"<br/><font color='red'>"--inline"</font>    |
| Compile defintions  |             __ASSERT_MSG<br/>MBED_TRAP_ERRORS_ENABLED=1<br/>MBED_DEBUG<br/>MULADDC_CANNOT_USE_R7     | __ASSERT_MSG<br/>MBED_TRAP_ERRORS_ENABLED=1   | __ASSERT_MSG<br/>NDEBUG   |
