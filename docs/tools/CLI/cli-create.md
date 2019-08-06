
# Create

## Understanding the working context and program root

Mbed CLI uses the current directory as a working context, in a similar way to Git, Mercurial and many other command-line tools. This means that before calling any Mbed CLI command, you must first change to the directory containing the code you want to act on. For example, if you want to update the Mbed OS sources in your `mbed-example-program` directory:

```
$ cd mbed-example-program
$ cd mbed-os
$ mbed update master   # This will update "mbed-os", not "my-program"
```

Various Mbed CLI features require a program root, which should be under version control - either [Mercurial](https://git-scm.com/). This makes it possible to switch between revisions of the whole program and its libraries, control the program history, synchronize the program with remote repositories, share it with others and so on. Version control is also the primary and preferred delivery mechanism for Mbed OS source code, which allows everyone to contribute to Mbed OS.

<span class="notes">**Note**: Mbed CLI stores information about libraries and dependencies in reference files that use the `.lib` extension (such as `lib_name.lib`). Although these files are human-readable, they should not be edited manually - let Mbed CLI manage them instead.</span>

## Application workflow

Mbed CLI can create and import programs based on both Mbed OS 2 and Mbed OS 5.

The basic workflow for Mbed CLI is to:

1. Initialize a new repository, for either a new application (or library) or an imported one. In both cases, this action also adds the Mbed OS codebase.
1. Build the application code.
1. Test your build.
1. Publish your application.

To support long-term development, Mbed CLI offers source control, including selective updates of libraries and the codebase, support for multiple toolchains and manual configuration of the system.

<span class="tips">**Tip:** To list all Mbed CLI commands, use `mbed --help`. A detailed command-specific help is available by using `mbed <command> --help`.</span>

## Creating a program

You can create new applications as Mbed OS 5, Mbed OS 2 or a non-versioned (blank) projects.

### For Mbed OS 5

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

### For Mbed OS 2

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

### Without OS version

You can create plain (empty) programs, without either Mbed OS 5 or Mbed OS 2, by using the `--create-only` option.

### Managing multiple Mbed projects

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

Find more details on the `--source` switch in the [build rules documentation](../reference/mbed-os-build-rules.html).

## Importing a program

You can import an existing program by using the `mbed import` command.

```
$ mbed import https://github.com/ARMmbed/mbed-os-example-blinky#mbed-os-5.11.0
[mbed] Working path "C:\dev" (directory)
[mbed] Importing program "mbed-os-example-blinky" from "https://github.com/ARMmbed/mbed-os-example-blinky" at branch/tag "mbed-os-5.11.0"
[mbed] Adding library "mbed-os" from "https://github.com/ARMmbed/mbed-os" at rev #6a0a86538c0b
```

You can specify which version to import using `#` followed by a commit hash, a branch name or a tag name. This syntax also works with an SSH link to a repository:

```
$ mbed import git@github.com:ARMmbed/mbed-os-example-blinky.git#mbed-os-5.11.0
```

If you do not provide any of these (nor the `#` character), the latest commit on the `master` branch will be imported.

A project's default name is the last part of the URL (excluding `#` and its value). In the example above, the imported program's project folder is `mbed-os-example-blinky`. To specify a different name, supply it as an extra positional argument in the `mbed import` command. For example, to name your project `my-blinky`, run:

```
$ mbed import https://github.com/ARMmbed/mbed-os-example-blinky#mbed-os-5.11.0 my-blinky
```

<span class="tips">**Tip**: Running `mbed import` within an existing program will result in an error. To add a library to an existing project, use the `mbed add` command (reviewed below).</span>

## Adding libraries to programs

You can use the `mbed add` command to add a library to a program. Run the following command within your project directory:

```
$ mbed add https://github.com/ARMmbed/mbed-cloud-client
[mbed] Working path "C:\dev\mbed-os-example-blinky" (program)
[mbed] Adding library "mbed-cloud-client" from "https://github.com/ARMmbed/mbed-cloud-client" at latest revision in the current branch
[mbed] Updating reference "mbed-cloud-client" -> "https://github.com/ARMmbed/mbed-cloud-client/#377c6b8fb0f8b66be03408a438ff0cd96be0c454"
```

Like the `mbed import` command, you can specify which version to use by using `#` at the end of the URL followed by a commit hash, a branch name, or a tag name. If you do not provide any of these (nor the `#` character), the latest commit on the `master` branch will be used.

The `mbed add` command clones the repository specified, check out to the correct version, and write the URL and _commit hash_ to a `.lib` file. Branches and tags can point to different commits over the lifetime of a repository, so to ensure the project's state is always reproducible, the commit hash is written to the `.lib` file. This `.lib` file should be committed to the project repository to track the dependency.

A library's default name is the last part of the URL (excluding `#` and its value). In the example above, the cloned library's folder is `mbed-cloud-client`. To specify a different name, supply it as an extra positional argument in the `mbed add` command. For example, to name your library `my-mcc`, run:

```
$ mbed add https://github.com/ARMmbed/mbed-cloud-client my-mcc
```

## Removing libraries

To remove a library (and its `.lib` file) from your project, use the `mbed remove` command with the path to the library. Continuing the example above, run the following from your project directory to remove the library that you added previously:

```
$ mbed remove mbed-cloud-client
```

Commit the removal of the `.lib` file from your project to remove the dependency.

## Updating programs and libraries

You can update programs and libraries on your local machine, so they update to the latest released version from the remote sources (Git or Mercurial).

As with any Mbed CLI command, `mbed update` uses the current directory as a working context. Before calling `mbed update`, you should change your working directory to the one you want to update. For example, if you're updating `mbed-os`, use `cd mbed-os` before you begin updating.

<span class="tips">**Tip:** Synchronizing library references: Before triggering an update, you may want to synchronize any changes that you've made to the program structure by running `mbed sync`, which updates the necessary library references and removes the invalid ones.</span>

### Protection against overwriting local changes

The update command fails if there are changes in your program or library that `mbed update` could overwrite. This is by design. Mbed CLI does not run operations that would result in overwriting uncommitted local changes. If you get an error, take care of your local changes, and then rerun `mbed update`.

### Updating to an upstream version

Before updating a program or a library, it's good to know the names of the stable releases, usually marked with a tag using a common format, such as `1.2`, `v1.0.1`, `r5.6`, `mbed-os-5.6` and so on.

You can find stable release versions of a program or a library using the `mbed releases` command:

```
$ cd mbed-os
$ mbed releases
mbed-os (#182bbd51bc8d, tags: latest, mbed-os-5.6.5)
  ...
  * mbed-os-5.6.0
  * mbed-os-5.6.1
  * mbed-os-5.6.2
  * mbed-os-5.6.3
  * mbed-os-5.6.4
  * mbed-os-5.6.5  <- current
```

You can also recursively list stable releases for your program and libraries using the `-r` switch, for example `mbed releases -r`.

Lastly, you can list unstable releases, such as release candidates, alphas and betas by using the `-u` switch.

```
$ cd mbed-client
$ mbed releases -u
mbed-client (#31e5ce203cc0, tags: v3.0.0)
  * mbed-os-5.0-rc1
  * mbed-os-5.0-rc2
  * r0.5-rc4
  ...
  * v2.2.0
  * v2.2.1
  * v3.0.0  <- current
```

You can use the `-a` switch to print release and revision hash pairs.

Mbed CLI recognizes stable release if the tags are in standard versioning format, such as `MAJOR[.MINOR][.PATCH][.BUILD]`, and optionally prefixed with `v`, `r` or `mbed-os`. Unstable releases can be suffixed with any letter/number/hyphen/dot combination.

#### Updating a program

To update your program to another upstream version, go to the root folder of the program, and run:

```
$ mbed update [branch|tag|revision]
```

This fetches new revisions from the remote repository, updating the program to the specified branch, tag or revision. If you don't specify any of these, then `mbed update` updates to the latest revision of the current branch. `mbed update` performs this series of actions recursively against all dependencies in the program tree.

#### Updating a library

You can change the working directory to a library folder and use `mbed update` to update that library and its dependencies to a different revision than the one referenced in the parent program or library. This allows you to experiment with different versions of libraries/dependencies in the program tree without having to change the parent program or library.

There are three additional options that modify how unpublished local libraries are handled:

- `mbed update --clean-deps` - Update the current program or library and its dependencies, and discard all local unpublished repositories. Use this with caution because your local unpublished repositories cannot be restored unless you have a backup copy.

- `mbed update --clean-files` - Update the current program or library and its dependencies, discard local uncommitted changes and remove any untracked or ignored files. Use this with caution because your local unpublished repositories cannot be restored unless you have a backup copy.

- `mbed update --ignore` - Update the current program or library and its dependencies, and ignore any local unpublished libraries (they won't be deleted or modified, just ignored).

#### Updating examples

There are two main scenarios when updating:

- Update with local uncommitted changes: *dirty* update.

Run `mbed update [branch|revision|tag_name]`. You might have to commit or stash your changes if the source control tool (Git or Mercurial) throws an error that the update will overwrite local changes.

- Discard local uncommitted changes: *clean* update.

Run `mbed update [branch|revision|tag_name] --clean`

Specifying a branch to `mbed update` will only check out that branch and won't automatically merge or fast-forward to the remote/upstream branch. You can run `mbed update` to merge (fast-forward) your local branch with the latest remote branch. On Git, you can do `git pull`.

<span class="warnings">**Warning**: The `--clean` option tells Mbed CLI to update that program or library and its dependencies and discard all local changes. This action cannot be undone; use with caution.</span>

#### Combining update options

You can combine the options of the Mbed update command for the following scenarios:

- `mbed update --clean --clean-deps --clean-files` - Update the current program or library and its dependencies, remove all local unpublished libraries, discard local uncommitted changes and remove all untracked or ignored files. This wipes every single change that you made in the source tree and restores the stock layout.

- `mbed update --clean --ignore` - Update the current program or library and its dependencies, but ignore any local repositories. Mbed CLI updates whatever it can from the public repositories.

Use these with caution because your uncommitted changes and unpublished libraries cannot be restored.

## Repository caching

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

### Offline mode

Through the caching feature in Mbed CLI, you can enable offline mode, which uses the already cached repositories on your system. You can enable offline mode by adding the `--offline` switch to `mbed import`, `mbed add`, `mbed update` and `mbed new`.

In offline mode, Mbed CLI looks up locally cached repositories and uses them without fetching new content from their remote repositories. This is particularly useful if, for example, you are on a flight and you'd like to create another Mbed OS project (assuming you've imported or created one before), but you don't have access to the internet. By using the command `mbed new <project_name> --offline`, you can create the project with Mbed OS included.
