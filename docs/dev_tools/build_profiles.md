# Build Profiles
mbed OS 5 supports three primary build profiles: *develop*, *debug* and *release*. The Online Compiler uses the *develop* profile. When building from mbed CLI, you can select a profile by adding the ```--profile <profile>``` flag. You can specify custom user-defined profiles by giving the path to the profile.

## Develop profile
* Small and fast code.
* Full error information. For example, asserts have file name and line number.
* Hard to follow code flow when using a debugger.

## Debug profile
* Largest and slowest profile.
* Full error information. For example, asserts have file name and line number.
* Easy to step through code with a debugger.

## Release profile
* Smallest profile and still fast.
* Minimal error information.
* Chip is put to sleep when going idle:
  * Debugger is likely to drop connection.
  * Breaks the local file system on the [mbed interface](https://docs.mbed.com/docs/mbed-os-handbook/en/latest/getting_started/mbed_interface/) on some boards.
