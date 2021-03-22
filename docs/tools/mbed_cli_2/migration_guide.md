# Migration guide

If you haven't already read the [introduction](./intro.md), then start from there.

The background color indicates:

* <span style="background-color:#ccffcc;">Green: New Functionality
  introduced in Mbed CLI 2 (mbed-tools)</span>
* <span style="background-color:#ffe6cc;">Orange: Functionality
  modified in Mbed CLI 2 (mbed-tools) compared to Mbed CLI 1 (mbed-cli)</span>
* <span style="background-color:#ffcccc;">Red: Functionality deprecated
  in Mbed CLI 2 (mbed-tools)</span>

## Installers
<span style="background-color:#ffe6cc;">Windows, macOS and Linux
installers may be made available at later point of time.</span><br>

## Commands

### Device management
<span style="background-color:#ffcccc;">The subcommand `mbed-cli
device-management` (device management) is deprecated. Refer to your cloud
provider's documentation on how to cloud-manage your devices.</span><br>

### Repository management
<span style="background-color:#ffcccc;">Support for Mercurial and the
subcommand `mbed-cli publish` (publish program or library) is deprecated.
Hosted repositories on "mbed.org" are not supported from Mbed CLI 2. Version
control with git can be used as an alternative. Hosting for git repositories is
available on [GitHub](https://github.com/).</span><br>

<span style="background-color:#ffcccc;">The subcommand `mbed-cli cache`
(repository cache management) is deprecated. No replacement is
supported.</span><br>

<span style="background-color:#ffcccc;">The subcommand `mbed-cli releases`
(show release tags) is deprecated. We recommend using standard `git` commands
instead, for example `git tag -l` to list all tagged releases.</span><br>

<span style="background-color:#ffe6cc;">The subcommand `mbed-cli
update` (update to branch, tag, revision or latest) is not implemented. Use
standard `git` commands instead. From your application directory: to check out
a branch of Mbed OS, `git -C mbed-os checkout branchname`; to checkout the Mbed
OS 6.8.0 release, `git -C mbed-os checkout mbed-os-6.8.0`; to check out Mbed OS
revision `3e24a7ea9602`, `git -C mbed-os checkout 3e24a7ea9602`; to checkout
the latest released version of Mbed OS `git -C mbed-os checkout
latest`.</span><br>

<span style="background-color:#ffcccc;">The subcommand `mbed-cli export`
(generate an IDE project) is deprecated. Use [CMake
generators](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html)
instead. While CMake supports many generators, including many not supported by
Mbed CLI 1, not all of Mbed CLI 1's exporters have replacements available yet.
The available project generators are listed below.</span><br>

- [CodeBlocks](https://cmake.org/cmake/help/latest/generator/CodeBlocks.html)
- [Eclipse](https://cmake.org/cmake/help/latest/generator/Eclipse%20CDT4.html)
- [Make](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html#id10)
- [Qt Creator](https://doc.qt.io/qtcreator/creator-project-cmake.html)
- [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)

<span style="background-color:#ffcccc;">If you'd like to help us prioritize
which CMake project generators to work on first, please give your thumbs up to
the following issues you care most about, or [raise a merge request to
CMake](https://gitlab.kitware.com/cmake/cmake/-/merge_requests):</span><br>

- [CrossCore® Embedded Studio](https://github.com/ARMmbed/mbed-tools/issues/249)
- [e<sup>2</sup> studio](https://github.com/ARMmbed/mbed-tools/issues/250)
- [Embitz](https://github.com/ARMmbed/mbed-tools/issues/251)
- [IAR Embedded Workbench for Arm](https://github.com/ARMmbed/mbed-tools/issues/252)
- [MCUXpresso](https://github.com/ARMmbed/mbed-tools/issues/253)
- [NetBeans](https://github.com/ARMmbed/mbed-tools/issues/254)
- [STM32CubeIDE](https://github.com/ARMmbed/mbed-tools/issues/257)
- [Keil uVision](https://github.com/ARMmbed/mbed-tools/issues/256)

### Library management

<span style="background-color:#ffcccc;">The subcommands `mbed-cli add` (add
library from URL) and `mbed-cli remove` (remove library) are deprecated.
Instead, use `git clone` or `mbed-tools import` to clone a library. Then,
manually create a `reponame.lib` file that contains a single line in the form
`https://github.com/ARMmbed/reponame#branch-or-tag` to fetch a specific branch
or tag. If you want to fetch the default branch, you don't need to add
`#branch-or-tag-name`.</span><br>

<span style="background-color:#ffcccc;">The subcommand `mbed-cli new --library`
(force creation of an Mbed library) is deprecated. Create a new Mbed library by
creating a new folder and adding it to git version control. Then, create a
`reponame.lib` in the application you wish to use the new library from, as
described above (in the `mbed-cli add` paragraph).</span><br>

<span style="background-color:#ffcccc;">The subcommand `mbed-cli ls` (view
dependency tree) is deprecated. The subcommand `mbed-tools deploy` will now
display all dependencies.</span><br>

### Tool configuration
<span style="background-color:#ffcccc;">The subcommand `mbed-cli config` (tool
configuration) is deprecated. There is no need to configure an Mbed-specific
compiler path in Mbed CLI 2; the compiler path is determined in a standard way
by CMake instead. Other configuration options, like `target`, `toolchain`,
`protocol`, `depth` and `cache`, are not supported in Mbed CLI 2.</span><br>

<span style="background-color:#ffcccc;">The subcommand `mbed-cli toolchain`
(set or get default toolchain) is deprecated. Pass the desired toolchain on the
command line when compiling with `mbed-tools compile --toolchain GCC_ARM`, to,
for example, select `GCC_ARM` as the toolchain.</span><br>

<span style="background-color:#ffcccc;">The subcommand `mbed-cli target` (set
or get default target) is deprecated. Pass the desired target on the command
line when compiling with `mbed-tools compile --mbed-target
DISCO_L475VG_IOT01A`, to, for example, select `DISCO_L475VG_IOT01A` as the
Mbed target.</span><br>


### Creating an Mbed program
<span style="background-color:#ffe6cc;">The subcommand `mbed-tools new` creates
a new Mbed program by default and supports only one command-line-option
`--create-only` (create a program without fetching mbed-os). The following
command-line options, previously supported in Mbed CLI 1, are deprecated:

* `--scm`: We now always use git.
* `--program`: There is no need to specify this. `mbed-tools new` always
  creates a program by creating a top-level application CMakeLists.txt that
  invokes `add_executable()`.
* `--library`: There is no need to specify this. `mbed-tools new` always
  creates a program. If you wish to create a library, you can edit the
  autogenerated top-level application CMakeLists.txt to replace
  `add_executable()` with `add_library()` and removing the call to
  `mbed_set_post_build()` for the CMake library target.
* `--mbedlib`: Importing Mbed 2 is no longer supported.
* `--depth`: This is no longer needed, as Mbed CLI 2 automatically uses the
  shallowest clone or fetch possible.
* `--protocol`: This is now determined from the URL instead.
* `--offline`: This is not needed, as there is no longer any Mbed-specific git
  cache.
* `--no-requirements`: Mbed CLI 2 never automatically installs requirements.
</span><br>

### Importing an Mbed program
<span style="background-color:#ffe6cc;">The subcommand `mbed-tools
import` clones an Mbed project and library dependencies. The following
command-line-options supported in Mbed CLI 1 are deprecated:

* `--depth`: The new CLI opportunistically imports the most shallow repository
  possible. Running `git clone --depth <depth> <repo_url> | cd <repo_name> &&
  mbed-tools deploy` will create an Mbed project with the required depth.
* `--protocol`: To select the protocol, use a URL with the
  desired protocol. For instance, you may import projects or libraries over SSH
  (Secure Shell) as follows `mbed-tools import
  git@github.com:ARMmbed/<some_driver>`, or with https `mbed-tools import
  https://github.com/ARMmbed/<some_driver>`. Alternatively, if you would prefer
  to always use SSH, even when your library or its dependencies specify https
  in their `.lib` files, you can add the following into your .gitconfig to
  force git to use SSH instead of https when fetching from GitHub.

```sh
[url "ssh://git@github.com/"]
  insteadOf = https://github.com/
```

* `--offline`: The new tool doesn't maintain a git cache so we don't have the
  option to use locally cached repositories.
* `--no-requirements`
* `--insecure`

</span><br>

### Configuring an Mbed program

<span style="background-color:#ccffcc;">The subcommand `mbed-tools configure`
generates an Mbed OS config CMake file named `mbed_config.cmake` in the path
`cmake_build/<TARGET_NAME>/<PROFILE>/<TOOLCHAIN>/`.</span><br>

### Compiling an Mbed program

<span style="background-color:#ffcccc;">The subcommand `mbed-tools
compile` can be used to compile the program. The command-line-option `mbed
compile --source` is deprecated. To control which libraries and directories you
want to build either modify your application's `CMakeLists.txt` to add/exclude
or use `cmake --build cmake_build --target <library_name> --target
<other_library_name>` to add any number of targets to your build.</span><br>

<span style="background-color:#ffcccc;">The command-line-option `mbed
compile --library` is deprecated. Use standard CMake `add_library()`
instead.</span><br>

<span style="background-color:#ffcccc;">The command-line-option `mbed compile
-DMACRO_NAME` is deprecated. Use `mbed-tools configure -m <TARGET_NAME> -t
<TOOLCHAIN>` followed by `cmake -S . -B
cmake_build/<TARGET_NAME>/<PROFILE>/<TOOLCHAIN> -GNinja -DMACRO_NAME` and
`cmake --build cmake_build` or use
[`target_compile_definitions()`](https://cmake.org/cmake/help/latest/command/target_compile_definitions.html)
in your application's `CMakeLists.txt` the add the define.</span><br>

<span style="background-color:#ffcccc;">The command-line-option `mbed compile
-m detect` to automatically build for the single target connected to your
computer is deprecated. Run `mbed-tools detect` to see which targets are
connected to your computer and then run `mbed-tools compile -m <TARGET_NAME> -t
<TOOLCHAIN>` to build for the target you which to build for.</span><br>

<span style="background-color:#ffe6cc;">The command-line-option `mbed
compile --build` will be supported at later point of time. Although we don't
currently have the option to explicitly state the application's build path, we
have a ticket open to track the issue
[#184](https://github.com/ARMmbed/mbed-tools/issues/184).</span><br>

### Testing an Mbed program

<span style="background-color:#ffe6cc;">The subcommand `mbed test` will be
supported at later point of time. Keep apprised of progress by following [the
issue to support mbed test on
GitHub](https://github.com/ARMmbed/mbed-tools/issues/151)</span><br>
