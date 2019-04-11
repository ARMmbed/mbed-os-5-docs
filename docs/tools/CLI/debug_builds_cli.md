<h1 id="debug-builds-cli">Debug builds</h1>

After you've set up your [local debug toolchain](../tools/build-profiles.html), you need firmware that includes program symbols (an `.elf` file). Because the Arm Mbed Online Compiler only produces binaries that omit the program symbols, you need to compile locally using [Arm Mbed CLI](../tools/developing-mbed-cli.html).

<span class="notes">**Note:** Make sure to do a clean build when switching to and from debug and release by removing the `BUILD` folder.</span>

## Compile commands

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
$ mbed compile --profile debug
```

## Exporting with debug symbols

You can also enable debug symbols when [exporting your project](exporting.html) by using:

```
$ mbed export -i uvision -m K64F --profile debug
```

Make release builds by using:

```
$ mbed export -i uvision -m K64F --profile release
```
