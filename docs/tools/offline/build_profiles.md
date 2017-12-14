<h2 id="build-profiles">Build profiles</h2>

Arm Mbed OS 5 supports three primary build profiles: *develop*, *debug* and *release*. The Online Compiler uses the *develop* profile. When building from Arm Mbed CLI, you can select a profile by adding the `--profile <profile>` flag. You can specify custom user-defined profiles by giving the path to the profile.

### Develop profile

- Small and fast code.
- Full error information. For example, asserts have file name and line number.
- Hard to follow code flow when using a debugger.
- Chip goes to sleep when idle:
    * Debugger is likely to drop connection.
    * Breaks the local file system on the <a href="/docs/v5.6/introduction/index.html" target="_blank">Arm Mbed interface</a> on some boards.

### Debug profile

- Largest and slowest profile.
- Full error information. For example, asserts have file name and line number.
- Easy to step through code with a debugger.
- Disabled sleep mode.

### Release profile

- Smallest profile and still fast.
- Minimal error information.
- Chip goes to sleep when going idle:
    - Debugger is likely to drop connection.
    - Breaks the local file system on the <a href="/docs/v5.6/introduction/index.html" target="_blank">Mbed interface</a> on some boards.
