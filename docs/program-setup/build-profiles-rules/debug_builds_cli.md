<h1 id="debug-builds-cli">Debug builds</h1>

After you've set up your [local debug toolchain](../program-setup/build-profiles-and-rules.html), you need firmware that includes program symbols (an `.elf` file). Because the Arm Mbed Online Compiler only produces binaries that omit the program symbols, you need to compile locally using [Arm Mbed CLI](../build-tools/mbed_cli_1.html).

<span class="notes">**Note:** Make sure to do a clean build when switching to and from debug and release by removing the `BUILD` folder.</span>

## Compile command

```
$ mbed compile --profile mbed-os/tools/profiles/debug.json
```

## Exporting with debug symbols

You can also enable debug symbols when [exporting your project](../build-tools/third-party-build-tools.html) by using:

```
$ mbed export -i uvision -m K64F --profile debug
```

Make release builds by using:

```
$ mbed export -i uvision -m K64F --profile release
```
