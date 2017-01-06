# Build Profiles
mbed OS 5 supports three primary build profiles: *default*, *debug* and *small*. The Online 
Compiler uses the *default* profile. When building from mbed CLI,
you can select a profile by adding the ```--profile <profile>```
flag. You can specify custom user defined profiles by giving the path
to the profile.

## Default profile
* Small and fast code.
* Full error information - e.g. asserts have file name and line number.
* Hard to follow code flow when using a debugger.

## Debug profile
* Easy to step through code with a debugger.
* Full error information - e.g. asserts have file name and line number.
* Largest and slowest profile.

## Small profile
* Smallest profile and still fast.
* Minimal error information.
* Hard to follow code flow when using a debugger.
