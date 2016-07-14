## Porting guide

This document guides you through the process of porting a new platform to mbed OS.

We recomend getting familar with Git and branching. If you are not too sure, see [here](http://learngitbranching.js.org/).

### Fetching the source to start porting

To get the full mbed OS source:

``` bash
cd /wherever/you/do/development
mbed new porting #mbed is an alias for the mbed-cli tool
cd porting
```

These steps create a directory called "porting" and fetch the full mbed OS code base to that directory. We need to call mbed CLI from within our project directory, so we use `cd` to enter it.

We're now ready to start working on our project.

Please check out the EPR release branch:

```bash
cd mbed-os
mbed update mbed-os-5.0.1-epr
```

And finally, install all Python development requirements:

```bash
pip install -r core/requirements.txt
```

To verify this all worked:

- On Windows:  `type core.lib`
- On Unix: `cat core.lib`

For both, the result should be `https://github.com/mbedmicro/mbed#ce830296d0297a8da543c24134bf859710fd7698`

**Warning:** Do not edit this by hand if you get a different result!

### Replacing the default mbed library with your development version

mbed OS includes a reference to a 'core' library, which is the mbed SDK (mbed drivers, hardware abstraction, and target implementations).   

It isn't practical to make all our changes on the mainline `mbedmicro/mbed` repository, so we need to make a fork of this repository and point our local mbed OS porting project at this development fork.

Because `core` is a dependency of `mbed-os` (via the `core.lib` link inside mbed-os), you also need to change that `.lib` file:

1. Remove the existing dependency on the `core` repository:

    ``` bash
    mbed remove core
    ```

1. Add a dependency on your fork of the mbed repository:

    ``` bash
    mbed add https://github.com/<developername>/mbed core
    ```

Now your local copy of `mbed-os` is pointing to your clone of the `core` repository and you are ready to start porting.

You will need to contact your ARM mbed partner lead to get a branch created in mbed-os against which you can make these pull requests. This will enable system-wide CI and testing.

### Building the tests for the first time on a known-good platform

When porting, the most common task is to build the full mbed OS test suite and run the tests to verify your port. So even before you start porting, it's a good idea to run the tests to make sure you're correctly set up for that.

Start by building for a known-good platform. If you have a platform that you know works well on developer.mbed.org, then you can build for it. If not, we recommend you try the FRDM-K64F.

You can list all the supported platforms by adding the `--supported` option to the `mbed compile` command. Note that this will not actually run the compilation, just report a table of possible combinations of boards (`-m`) and toolchains (`-t`):

```bash
mbed compile --supported
```

When you've chosen a supported combination of target and toolchain, run the mbed test command. By default, running `mbed test` will build *and* attempt to run the tests:

```bash
mbed test -m K64F -t GCC_ARM
```

You can add the `--compile` command to indicate that you do not want to run the tests. Likewise, the `--run` command tells the tool to only run the tests (and not recompile).

#### Setting the chosen target and toolchain as default

By running the following commands you can set the default target and toolchain for mbed CLI commands:

```bash
mbed target <YOUR_TARGET>
mbed toolchain <YOUR_TOOLCHAIN>
```
Now you can just run `mbed` commands without explicitly specifying the `–m` and `–t` arguments.

**Note:** These parameters are saved for each project, so you don't need to reset them every time you restart mbed CLI or change projects.

#### Running just one test

There are many tests and they take a long time to run. If you’d like to run just a single test (for example, to quickly prove the sanity of your environment):

```bash
mbed test --run -n mbed-os-tests-integration-threaded_blinky
```

### Building and testing for a new target

Once you have verified that you can run the tests on your platform for a known-good board, you are ready to start porting to a new target.

In order to do this, you should follow the [porting documentation](../mbed_OS/Porting.md).

### Creating and running your own tests

See the [Greentea page](../Testing/Porting.md) for instructions for creating and running tests.

#### Getting your board into the continuous integration system

The continuous integration (CI) system automates your tests so you can verify your port as you work. Your hardware has to match requirements (such as DAPLink versions).
