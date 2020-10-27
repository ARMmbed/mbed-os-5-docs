# Collaborate

## Importing from a cloned repository

If you have manually cloned a Git repository into your workspace and you want to add all missing libraries, then you can use the `deploy` command:

```
$ mbed deploy
[mbed] Adding library "mbed-os" from "https://github.com/ARMmbed/mbed-os" at rev #dd36dc4228b5
```

Don't forget to set the current directory as the root of your program:

```
$ mbed new .
```

## Publishing changes

### Checking status

As you develop your program, you'll edit parts of it. You can get the status of all the repositories in your program (recursively) by running `mbed status`. If a repository has uncommitted changes, this command displays these changes.

Here's an example:

```
[mbed] Status for "mbed-os-program":
 M main.cpp
 M mbed-os.lib
?? gdb_log.txt
?? test_spec.json

[mbed] Status for "mbed-os":
 M tools/toolchains/arm.py
 M tools/toolchains/gcc.py

[mbed] Status for "mbed-client-classic":
 M source/m2mtimerpimpl.cpp

[mbed] Status for "mbed-mesh-api":
 M source/include/static_config.h
```

You can then commit or discard these changes through that repository's version control system.

### Pushing upstream

To push the changes in your local tree upstream, run `mbed publish`. `mbed publish` works recursively, pushing the leaf dependencies first, then updating the dependents and pushing them too.

Let's assume that the list of dependencies of your program (obtained by running `mbed ls`) looks like this:

```
my-mbed-os-example (a5ac4bf2e468)
|- mbed-os (5fea6e69ec1a)
`- my-libs (e39199afa2da)
   |- my-libs/iot-client (571cfef17dd0)
   `- my-libs/test-framework (cd18b5a50df4)
```

Let's assume that you make changes to `iot-client`. `mbed publish` detects the change on the leaf `iot-client` dependency and asks you to commit it. Then `mbed publish` detects that `my-libs` depends on `iot-client`, updates the `my-libs` dependency on `iot-client` to its latest version by updating the `iot-client.lib` file and asks you to commit it. This propagates up to `my-libs` and finally to your program, `my-mbed-os-example`.

### Publishing a local program or library

When you create a new (local) version control managed program or library, its revision history exists only locally. The repository is not associated with the remote one. To publish the local repository, please follow these steps:

1. Create a new empty repository on the remote site. This can be on a public repository hosting service (GitHub, Bitbucket, mbed.org), your own service or a different location on your system.
1. Copy the URL/location of the new repository in your clipboard.
1. Open command-line in the local repository directory (for example, change directory to `mbed-os-example/local-lib`).
1. To associate the local repository:

   - For Git, run `git remote add origin <url-or-path-to-your-remote-repo>`.
   - For Mercurial, edit .hg/hgrc and add (or replace if exists):

      ```
      [paths]
      default = <url-or-path-to-your-remote-repo>
      ```

1. Run `mbed publish` to publish your changes.

In a scenario with nested local repositories, start with the leaf repositories first.

## The forking workflow

Git enables a workflow where the publish/push repository may be different than the original ("origin") one. This allows new revisions in a fork repository while maintaining an association with the original repository. To use this workflow, first import an Mbed OS program or Mbed OS itself, and then associate the push remote with your fork. For example:

```
$ git remote set-url --push origin https://github.com/screamerbg/repo-fork
```

Both `git commit & git push` and `mbed publish` push the new revisions to your fork. You can fetch from the original repository using `mbed update` or `git pull`. If you explicitly want to fetch or pull from your fork, then you can use `git pull https://github.com/screamerbg/repo-fork [branch]`.

Through the workflow explained above, Mbed CLI maintains association to the original repository (which you may want to send a pull request to) and records references with the revision hashes that you push to your fork. Until your pull request (PR) is accepted, all recorded references are invalid. Once the PR is accepted, all revision hashes from your fork become part the original repository, making them valid.
