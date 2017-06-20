## Updating and configuring programs and libraries with mbed CLI

You can update programs and libraries on your local machine so that they pull in changes from the remote sources (Git or Mercurial). 

As with any mbed CLI command, `mbed update` uses the current directory as a working context. Before calling `mbed update`, you should change your working directory to the one you want to update. For example, if you're updating mbed-os, use `cd mbed-os` before you begin updating.

<span class="tips">**Tip: Synchronizing library references:** Before triggering an update, you may want to synchronize any changes that you've made to the program structure by running ``mbed sync``, which updates the necessary library references and removes the invalid ones.</span>

### Protection against overwriting local changes

The update command fails if there are changes in your program or library that `mbed update` could overwrite. This is by design. mbed CLI does not run operations that would result in overwriting uncommitted local changes. If you get an error, take care of your local changes (commit or use one of the options below), and then rerun `mbed update`.

### Updating to an upstream version

#### Updating a program

To update your program to another upstream version, go to the root folder of the program, and run:

```
$ mbed update [branch|tag|revision]
```

This fetches new revisions from the remote repository, updating the program to the specified branch, tag or revision. If you don't specificy any of these, then `mbed update` updates to the latest revision of the current branch. `mbed update` performs this series of actions recursively against all dependencies in the program tree.

#### Updating a library

You can change the working directory to a library folder and use `mbed update` to update that library and its dependencies to a different revision than the one referenced in the parent program or library. This allows you to experiment with different versions of libraries/dependencies in the program tree without having to change the parent program or library.

There are three additional options that modify how unpublished local libraries are handled:

* `mbed update --clean-deps` - Update the current program or library and its dependencies, and discard all local unpublished repositories. Use this with caution because your local unpublished repositories cannot be restored unless you have a backup copy.

* `mbed update --clean-files` - Update the current program or library and its dependencies, discard local uncommitted changes and remove any untracked or ignored files. Use this with caution because your local unpublished repositories cannot be restored unless you have a backup copy.

* `mbed update --ignore` - Update the current program or library and its dependencies, and ignore any local unpublished libraries (they won't be deleted or modified, just ignored).

### Update examples

There are two main scenarios when updating:

* Update with local uncommitted changes: *dirty* update.

Run `mbed update [branch|revision|tag_name]`. You might have to commit or stash your changes if the source control tool (Git or Mercurial) throws an error that the update will overwrite local changes.

* Discard local uncommitted changes: *clean* update.

Run `mbed update [branch|revision|tag_name] --clean`

Specifying a branch to `mbed update` will only check out that branch and won't automatically merge or fast-forward to the remote/upstream branch. You can run `mbed update` to merge (fast-forward) your local branch with the latest remote branch. On Git you can do `git pull`.

<span class="warnings">**Warning**: The `--clean` option tells mbed CLI to update that program or library and its dependencies and discard all local changes. This action cannot be undone; use with caution.</span>

#### Combining update options

You can combine the options of the mbed update command for the following scenarios:

* `mbed update --clean --clean-deps --clean-files` - Update the current program or library and its dependencies, remove all local unpublished libraries, discard local uncommitted changes and remove all untracked or ignored files. This wipes every single change that you made in the source tree and restores the stock layout.

* `mbed update --clean --ignore` - Update the current program or library and its dependencies, but ignore any local repositories. mbed CLI will update whatever it can from the public repositories.

Use these with caution because your uncommitted changes and unpublished libraries cannot be restored.

### mbed CLI configuration

You can streamline many options in mbed CLI with global and local configuration.

The mbed CLI configuration syntax is:
```
mbed config [--global] <var> [value] [--unset]
```

* The **global** configuration (via `--global` option) defines the default behavior of mbed CLI across programs unless overridden by *local* settings.
* The **local** configuration (without `--global`) is specific to mbed program and allows overriding of global or default mbed CLI settings.
* If you do not specify a value, then mbed CLI prints the value for this setting in this context.
* The `--unset` option allows you to remove a setting.
* The `--list` option allows you to list global and local configuration.

Here is a list of configuration settings and their defaults:

 * `target` - defines the default target for `compile`, `test` and `export`; an alias of `mbed target`. Default: none.
 * `toolchain` - defines the default toolchain for `compile` and `test`; can be set through `mbed toolchain`. Default: none.
 * `ARM_PATH`, `GCC_ARM_PATH`, `IAR_PATH` - defines the path to ARM Compiler, GCC ARM and IAR Workbench toolchains. Default: none.
 * `protocol` - defines the default protocol used for importing or cloning of programs and libraries. The possible values are `https`, `http` and `ssh`. Use `ssh` if you have generated and registered SSH keys (Public Key Authentication) with a service such as GitHub, GitLab, Bitbucket and so on. Read more about SSH keys [here](https://help.github.com/articles/generating-an-ssh-key/). Default: `https`.
 * `depth` - defines the *clone* depth for importing or cloning and applies only to *Git* repositories. Note that though this option may improve cloning speed, it may also prevent you from correctly checking out a dependency tree when the reference revision hash is older than the clone depth. Read more about shallow clones [here](https://git-scm.com/docs/git-clone). Default: none.
 * `cache` - defines the local path that stores small copies of the imported or cloned repositories, and mbed CLI uses it to minimize traffic and speed up future imports of the same repositories. Use `on` or `enabled` to turn on caching in the system temp path. Use `none` to turn caching off. Default: none (disabled).
