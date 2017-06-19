# Producing debug builds with mbed CLI

After you've set up your [local debug toolchain](toolchain.md), you'll need firmware that includes program symbols (an `.elf` file). Because the Online Compiler only produces binaries that omit the program symbols, you need to compile locally using [mbed CLI](https://docs.mbed.com/docs/mbed-os-handbook/en/latest/dev_tools/cli/).

<span class="notes">**Note:** Make sure to do a clean build when switching to and from debug and release by removing the `BUILD` folder.</span>

## Compile commands

**mbed OS 5.2 and later**

```
$ mbed compile --profile mbed-os/tools/profiles/debug.json
```

**mbed OS 5.0 and 5.1**

```
$ mbed compile -o debug-info
```

**mbed 2.0**

```
$ mbed compile --profile .temp/tools/profiles/debug.json
```

## Exporting with debug symbols

You can also enable debug symbols when [exporting your project](https://docs.mbed.com/docs/mbed-os-handbook/en/latest/dev_tools/cli/#exporting-to-desktop-ides) by using:

```
$ mbed export -i uvision -m K64F --profile mbed-os/tools/profiles/debug.json
```

Make release builds by using:

```
$ mbed export -i uvision -m K64F --profile mbed-os/tools/profiles/default.json
```
