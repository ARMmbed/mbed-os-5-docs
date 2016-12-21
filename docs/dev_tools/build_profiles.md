# Build Profiles
mbed 5.0 supports three primary build profiles, *default*, *debug* and *small*. The Online 
Compiler uses the *default* profile. When building from the command-line,
you can select the desired profile by adding the ```--profile <profile>```
command-line flag. You can specify custom user defined profiles by giving the path
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
