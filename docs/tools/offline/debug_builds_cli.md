<h2 id="debug-builds-cli">Debug builds</h2>

After you've set up your <a href="/docs/v5.7/tools/toolchain-profiles.html" target="_blank">local debug toolchain</a>, you need firmware that includes program symbols (an `.elf` file). Because the Arm Mbed Online Compiler only produces binaries that omit the program symbols, you need to compile locally using <a href="/docs/v5.7/tools/arm-mbed-cli.html" target="_blank">Arm Mbed CLI</a>.

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

You can also enable debug symbols when <a href="/docs/v5.7/tools/exporting.html" target="_blank">exporting your project</a> by using:

```
$ mbed export -i uvision -m K64F --profile mbed-os/tools/profiles/debug.json
```

Make release builds by using:

```
$ mbed export -i uvision -m K64F --profile mbed-os/tools/profiles/default.json
```
