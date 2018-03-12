<h2 id="debug-builds-cli">Debug builds</h2>

After you've set up your [local debug toolchain](/docs/development/tools/toolchain-profiles.html), you need firmware that includes program symbols (an `.elf` file). Because the Arm Mbed Online Compiler only produces binaries that omit the program symbols, you need to compile locally using [Arm Mbed CLI](/docs/development/tools/arm-mbed-cli.html).

<span class="notes">**Note:** Make sure to do a clean build when switching to and from debug and release by removing the `BUILD` folder.</span>

### Compile commands

**Arm Mbed OS 5.2 and later**

```
$ mbed compile --profile mbed-os/tools/profiles/debug.json
```

**Arm Mbed OS 5.0 and 5.1**

```
$ mbed compile -o debug-info
```

**Arm Mbed 2.0**

```
$ mbed compile --profile .temp/tools/profiles/debug.json
```

### Exporting with debug symbols

You can also enable debug symbols when [exporting your project](/docs/development/tools/exporting.html) by using:

```
$ mbed export -i uvision -m K64F --profile mbed-os/tools/profiles/debug.json
```

Make release builds by using:

```
$ mbed export -i uvision -m K64F --profile mbed-os/tools/profiles/default.json
```
