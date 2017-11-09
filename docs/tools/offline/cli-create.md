
## Create

### Quickstart video

<span class="images">[![Video tutorial](https://img.youtube.com/vi/PI1Kq9RSN_Y/0.jpg)](https://www.youtube.com/watch?v=PI1Kq9RSN_Y)</span>

### Understanding the working context and program root

Mbed CLI uses the current directory as a working context, in a similar way to Git, Mercurial and many other command-line tools. This means that before calling any Mbed CLI command, you must first change to the directory containing the code you want to act on. For example, if you want to update the Mbed OS sources in your `mbed-example-program` directory:

```
$ cd mbed-example-program
$ cd mbed-os
$ mbed update master   # This will update "mbed-os", not "my-program"
```

Various Mbed CLI features require a program root, which should be under version control - either <a href="https://git-scm.com/" target="_blank">Git</a> or <a href="https://www.mercurial-scm.org/" target="_blank">Mercurial</a>. This makes it possible to switch between revisions of the whole program and its libraries, control the program history, synchronize the program with remote repositories, share it with others and so on. Version control is also the primary and preferred delivery mechanism for Mbed OS source code, which allows everyone to contribute to Mbed OS.

<span class="warnings">**Warning**: Mbed CLI stores information about libraries and dependencies in reference files that use the `.lib` extension (such as `lib_name.lib`). Although these files are human-readable, we *strongly* advise that you don't edit these manually - let Mbed CLI manage them instead.</span>

### Application workflow

Mbed CLI can create and import programs based on both Mbed OS 2 and Mbed OS 5.

The basic workflow for Mbed CLI is to:

1. Initialize a new repository, for either a new application (or library) or an imported one. In both cases, this action also adds the Mbed OS codebase.
1. Build the application code.
1. Test your build.
1. Publish your application.

To support long-term development, Mbed CLI offers source control, including selective updates of libraries and the codebase, support for multiple toolchains and manual configuration of the system.

<span class="tips">**Tip:** To list all Mbed CLI commands, use `mbed --help`. A detailed command-specific help is available by using `mbed <command> --help`.</span>

### Creating a program

You can create new applications as Mbed OS 5, Mbed OS 2 or a non-versioned (blank) projects.

#### For Mbed OS 5

When you create a new program, Mbed CLI automatically imports the latest <a href="https://github.com/ARMmbed/mbed-os/" target="_blank">Mbed OS release</a>. Each release includes all the components: code, build tools and IDE exporters.

With this in mind, let's create a new program (we'll call it `mbed-os-program`):

```
$ mbed new mbed-os-program
[mbed] Creating new program "mbed-os-program" (git)
[mbed] Adding library "mbed-os" from "https://github.com/ARMmbed/mbed-os" at latest revision in the current branch
[mbed] Updating reference "mbed-os" -> "https://github.com/ARMmbed/mbed-os/#89962277c20729504d1d6c95250fbd36ea5f4a2d"
```

This creates a new folder "mbed-os-program", initializes a new repository and imports the latest revision of the `mbed-os` dependency to your program tree.

<span class="tips">**Tip:** You can instruct Mbed CLI to use a specific source control management system or prevent source control management initialization, by using `--scm [name|none]` option.</span>

Use `mbed ls` to list all the libraries imported to your program:

```
$ cd mbed-os-program
$ mbed ls -a
mbed-os-program (mbed-os-program)
`- mbed-os (https://github.com/ARMmbed/mbed-os#89962277c207)
```

<span class="notes">**Note**: If you want to start from an existing folder in your workspace, you can use `mbed new .`, which initializes an Mbed program, as well as a new Git or Mercurial repository in that folder. </span>

#### For Mbed OS 2

Mbed CLI is also compatible with Mbed OS 2 programs based on the <a href="https://mbed.org/users/mbed_official/code/mbed/" target="_blank">Mbed library</a>, and it automatically imports the latest <a href="https://mbed.org/users/mbed_official/code/mbed/" target="_blank">Mbed library release</a> if you use the `--mbedlib` option:

```
$ mbed new mbed-classic-program --mbedlib
[mbed] Creating new program "mbed-classic-program" (git)
[mbed] Adding library "mbed" from "https://mbed.org/users/mbed_official/code/mbed/builds" at latest revision in the current branch
[mbed] Downloading mbed library build "f9eeca106725" (might take a minute)
[mbed] Unpacking mbed library build "f9eeca106725" in "D:\Work\examples\mbed-classic-program\mbed"
[mbed] Updating reference "mbed" -> "https://mbed.org/users/mbed_official/code/mbed/builds/f9eeca106725"
[mbed] Couldn't find build tools in your program. Downloading the mbed 2.0 SDK tools...
```

#### Without OS version

You can create plain (empty) programs, without either Mbed OS 5 or Mbed OS 2, by using the `--create-only` option.

### Compiling workflow

#### Compiling your application

Use the `mbed compile` command to compile your code:

```
$ mbed compile -t ARM -m K64F
Building project mbed-os-program (K64F, GCC_ARM)
Compile: aesni.c
Compile: blowfish.c
Compile: main.cpp
... [SNIP] ...
Compile: configuration_store.c
Link: mbed-os-program
Elf2Bin: mbed-os-program
+----------------------------+-------+-------+------+
| Module                     | .text | .data | .bss |
+----------------------------+-------+-------+------+
| Fill                       |   170 |     0 | 2294 |
| Misc                       | 36282 |  2220 | 2152 |
| core/hal                   | 15396 |    16 |  568 |
| core/rtos                  |  6751 |    24 | 2662 |
| features/FEATURE_IPV4      |    96 |     0 |   48 |
| frameworks/greentea-client |   912 |    28 |   44 |
| frameworks/utest           |  3079 |     0 |  732 |
| Subtotals                  | 62686 |  2288 | 8500 |
+----------------------------+-------+-------+------+
Allocated Heap: 65540 bytes
Allocated Stack: 32768 bytes
Total Static RAM memory (data + bss): 10788 bytes
Total RAM memory (data + bss + heap + stack): 109096 bytes
Total Flash memory (text + data + misc): 66014 bytes
Image: BUILD/K64F/GCC_ARM/mbed-os-program.bin
```

The arguments for *compile* are:

- `-m <MCU>` to select a target. If `detect` or `auto` parameter is passed to `-m`, then Mbed CLI detects the connected target.
- `-t <TOOLCHAIN>` to select a toolchain (of those defined in `mbed_settings.py`, see above). The value can be `ARM` (Arm Compiler 5), `GCC_ARM` (GNU Arm Embedded) or `IAR` (IAR Embedded Workbench for Arm).
- `--source <SOURCE>` to select the source directory. The default is `.` (the current directory). You can specify multiple source locations, even outside the program tree.
- `--build <BUILD>` to select the build directory. Default: `BUILD/` inside your program root.
- `--profile <PATH_TO_BUILD_PROFILE>` to select a path to a build profile configuration file. Example: `mbed-os/tools/profiles/debug.json`.
- `--library` to compile the code as a [static .a/.ar library](#compiling-static-libraries).
- `--config` to inspect the runtime compile configuration (see below).
- `-S` or `--supported` shows a matrix of the supported targets and toolchains.
- `-f` or `--flash` to flash/program a connected target after successful compile.
- `-c ` to build from scratch, a clean build or rebuild.
- `-j <jobs>` to control the compile processes on your machine. The default value is 0, which infers the number of processes from the number of cores on your machine. You can use `-j 1` to trigger a sequential compile of source code.
- `-v` or `--verbose` for verbose diagnostic output.
- `-vv` or `--very_verbose` for very verbose diagnostic output.

You can find the compiled binary, ELF image, memory usage and link statistics in the `BUILD` subdirectory of your program.

For more information on build profiles, see <a href="/docs/v5.6/tools/build-profiles.html" target="_blank">our build profiles</a> and <a href="/docs/v5.6/tools/toolchain-profiles.html" target="_blank">toolchain profiles</a> pages.

#### Compiling static libraries

You can build a static library of your code by adding the `--library` argument to `mbed compile`. Static libraries are useful when you want to build multiple applications from the same Mbed OS codebase without having to recompile for every application. To achieve this:

1. Build a static library for `mbed-os`.
2. Compile multiple applications or tests against the static library:

```
$ mbed compile -t ARM -m K64F --library --no-archive --source=mbed-os --build=../mbed-os-build
Building library mbed-os (K64F, ARM)
[...]
Completed in: (47.4)s

$ mbed compile -t ARM -m K64F --source=mbed-os/TESTS/integration/basic --source=../mbed-os-build --build=../basic-out
Building project basic (K64F, ARM)
Compile: main.cpp
Link: basic
Elf2Bin: basic
Image: ../basic-out/basic.bin

$ mbed compile -t ARM -m K64F --source=mbed-os/TESTS/integration/threaded_blinky --source=../mbed-os-build --build=..\/hreaded_blinky-out
Building project threaded_blinky (K64F, ARM)
Compile: main.cpp
Link: threaded_blinky
Elf2Bin: threaded_blinky
Image: ../threaded_blinky-out/threaded_blinky.bin
```

### The compile configuration system

The <a href="/docs/v5.6/tools/the-configuration-system.html" target="_blank">compile configuration system</a> provides a flexible mechanism for configuring the Mbed program, its libraries and the build target.

#### Inspecting the configuration

You can use `mbed compile --config` to view the configuration:

```
$ mbed compile --config -t GCC_ARM -m K64F
```

To display more verbose information about the configuration parameters, use `-v`:

```
$ mbed compile --config -t GCC_ARM -m K64F -v
```

It's possible to filter the output of `mbed compile --config` by specifying one or more prefixes for the configuration parameters that Mbed CLI displays. For example, to display only the configuration defined by the targets:

```
$ mbed compile --config -t GCC_ARM -m K64F --prefix target
```

You may use `--prefix` more than once. To display only the application and target configuration, use two `--prefix` options:

```
$ mbed compile --config -t GCC_ARM -m K64F --prefix target --prefix app
```

#### Compile-time customizations

##### Macros

You can specify macros in your command-line using the -D option. For example:

```
$ mbed compile -t GCC_ARM -m K64F -c -DUVISOR_PRESENT
```

##### Compile in debug mode

To compile in debug mode (as opposed to the default *develop* mode), use `--profile mbed-os/tools/profiles/debug.json` in the compile command-line:

```
$ mbed compile -t GCC_ARM -m K64F --profile mbed-os/tools/profiles/debug.json
```

<span class="tips">**Tip:** If you have files that you want to compile only in debug mode, put them in a directory called `TARGET_DEBUG` at any level of your tree (then use `--profile` as explained above).
</span>

#### Automate toolchain and target selection

Using `mbed target <target>` and `mbed toolchain <toolchain>`, you can set the default target and toolchain for your program. You won't have to specify these every time you compile or generate IDE project files.

You can also use `mbed target detect`, which detects the connected target board and uses it as a parameter to every subsequent compile and export.

#### Update programs and libraries

You can update programs and libraries on your local machine so that they pull in changes from the remote sources (Git or Mercurial).

As with any Mbed CLI command, `mbed update` uses the current directory as a working context. Before calling `mbed update`, you should change your working directory to the one you want to update. For example, if you're updating `mbed-os`, use `cd mbed-os` before you begin updating.

<span class="tips">**Tip: Synchronizing library references:** Before triggering an update, you may want to synchronize any changes that you've made to the program structure by running `mbed sync`, which updates the necessary library references and removes the invalid ones.</span>

##### Protect against overwriting local changes

The update command fails if there are changes in your program or library that `mbed update` could overwrite. This is by design. Mbed CLI does not run operations that would result in overwriting uncommitted local changes. If you get an error, take care of your local changes (commit or use one of the options below), and then rerun `mbed update`.

### Updating to an upstream version

#### Updating a program

To update your program to another upstream version, go to the root folder of the program, and run:

```
$ mbed update [branch|tag|revision]
```

This fetches new revisions from the remote repository, updating the program to the specified branch, tag or revision. If you don't specify any of these, then `mbed update` updates to the latest revision of the current branch. `mbed update` performs this series of actions recursively against all dependencies in the program tree.

#### Updating a library

You can change the working directory to a library folder and use `mbed update` to update that library and its dependencies to a different revision than the one referenced in the parent program or library. This allows you to experiment with different versions of libraries/dependencies in the program tree without having to change the parent program or library.

There are three additional options that modify how unpublished local libraries are handled:

* `mbed update --clean-deps` - Update the current program or library and its dependencies, and discard all local unpublished repositories. Use this with caution because your local unpublished repositories cannot be restored unless you have a backup copy.

* `mbed update --clean-files` - Update the current program or library and its dependencies, discard local uncommitted changes and remove any untracked or ignored files. Use this with caution because your local unpublished repositories cannot be restored unless you have a backup copy.

* `mbed update --ignore` - Update the current program or library and its dependencies, and ignore any local unpublished libraries (they won't be deleted or modified, just ignored).

#### Updating examples

There are two main scenarios when updating:

* Update with local uncommitted changes: *dirty* update.

Run `mbed update [branch|revision|tag_name]`. You might have to commit or stash your changes if the source control tool (Git or Mercurial) throws an error that the update will overwrite local changes.

* Discard local uncommitted changes: *clean* update.

Run `mbed update [branch|revision|tag_name] --clean`

Specifying a branch to `mbed update` will only check out that branch and won't automatically merge or fast-forward to the remote/upstream branch. You can run `mbed update` to merge (fast-forward) your local branch with the latest remote branch. On Git, you can do `git pull`.

<span class="warnings">**Warning**: The `--clean` option tells Mbed CLI to update that program or library and its dependencies and discard all local changes. This action cannot be undone; use with caution.</span>

#### Combining update options

You can combine the options of the Mbed update command for the following scenarios:

* `mbed update --clean --clean-deps --clean-files` - Update the current program or library and its dependencies, remove all local unpublished libraries, discard local uncommitted changes and remove all untracked or ignored files. This wipes every single change that you made in the source tree and restores the stock layout.

* `mbed update --clean --ignore` - Update the current program or library and its dependencies, but ignore any local repositories. Mbed CLI updates whatever it can from the public repositories.

Use these with caution because your uncommitted changes and unpublished libraries cannot be restored.
