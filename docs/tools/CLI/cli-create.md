
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

Various Mbed CLI features require a program root, which should be under version control - either [Mercurial](https://git-scm.com/). This makes it possible to switch between revisions of the whole program and its libraries, control the program history, synchronize the program with remote repositories, share it with others and so on. Version control is also the primary and preferred delivery mechanism for Mbed OS source code, which allows everyone to contribute to Mbed OS.

<span class="notes">**Note**: Mbed CLI stores information about libraries and dependencies in reference files that use the `.lib` extension (such as `lib_name.lib`). Although these files are human-readable, they should not be edited manually - let Mbed CLI manage them instead.</span>

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

When you create a new program, Mbed CLI automatically imports the latest [Mbed OS release](https://github.com/ARMmbed/mbed-os/). Each release includes all the components: code, build tools and IDE exporters.

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

Mbed CLI is also compatible with Mbed OS 2 programs based on the [Mbed library](https://mbed.org/users/mbed_official/code/mbed/), and it automatically imports the latest [Mbed library release](https://mbed.org/users/mbed_official/code/mbed/) if you use the `--mbedlib` option:

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

#### Managing multiple Mbed projects

You can create multiple Mbed projects and use the same Mbed OS library directory for each of these projects with the following commands:

```
$ cd <projects directory>
$ mbed import mbed-os
$ mbed config -G MBED_OS_DIR <projects directory>/mbed-os
[mbed] <projects directory>/mbed-os now set as global MBED_OS_DIR
$ mbed new project1
[mbed] Creating new program "project1" (git)
$ mbed new project2
[mbed] Creating new program "project2" (git)
```

Add your `main.cpp` file and other project files to the `project1` and `project2` directories. Then compile each project from the root `<projects directory>` with the following example commands:

```
$ mbed compile -t ARM -m LPC1768 --source project1 --source mbed-os --build BUILD/project1
$ mbed compile -t ARM -m K64F --source project2 --source mbed-os --build BUILD/project2  
```

Find more details on the `--source` switch in the [build rules documentation](../tools/mbed-os-build-rules.html).

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

### Repository caching

To minimize traffic and reduce import times, Mbed CLI caches repositories by storing their indexes under the Mbed CLI user config folder - typically `~/.mbed/mbed-cache/` on UNIX systems, or `%userprofile%/.mbed/mbed-cache/` on Windows systems. Compared to a fully checked out repository, indexes are smaller in size and number of files and contain the whole revision history of that repository. This allows Mbed CLI to quickly create copies of previously downloaded repository indexes and pull or fetch only the latest changes from the remote repositories, therefore dramatically reducing network traffic and download times, especially for big repositories such as `mbed-os`.

You can manage the Mbed CLI caching behavior with the following subcommands:

```
mbed cache [on|off|dir <path>|ls|purge|-h|--help]
```

 - `on` - Turn repository caching on. This uses either the user specified cache directory or the default one. See "dir".
 - `off` - Turn repository caching off. Note that this doesn't purge cached repositories. See "purge".
 - `dir` - Set cache directory. Set to "default" to let Mbed CLI determine the cache directory location. Typically, this is `~/.mbed/mbed-cache/` on UNIX systems, or `%%userprofile%%/.mbed/mbed-cache/` on Windows systems.
 - `ls` - List cached repositories and their size.
 - `purge` - Purge cached repositories. Note that this doesn't turn caching off.
 - `-h` or `--help` - Print cache command options.

If no subcommand is specified to `mbed cache`, Mbed CLI prints the current cache setting (ENABLED or DISABLED) and the path to the local cache directory.

For safety reasons, Mbed CLI uses the `mbed-cache` subfolder to a user specified location. This ensures that no user files are deleted during `purge` even if the user has specified root/system folder as a cache location (for example, `mbed cache dir /` or `mbed cache dir C:\`).

**Security notice**: If you use cache location outside your user home/profile directory, then other system users might be able to access the repository cache and therefore the data of the cached repositories.
