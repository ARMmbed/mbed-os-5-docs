## Publishing a local program or library with mbed CLI

When you create a new (local) version control managed program or library, its revision history exists only locally. The repository is not associated with the remote one. To publish the local repository, please follow these steps:

1. Create a new empty repository on the remote site. This can be on a public repository hosting service (GitHub, Bitbucket, mbed.org), your own service or a different location on your system.
1. Copy the URL/location of the new repository in your clipboard. 
1. Open command-line in the local repository directory (for example, change directory to `mbed-os-example/local-lib`).
1. To associate the local repository:
 * For Git, run `git remote add origin <url-or-paht-to-your-remote-repo>`.
 * For Mercurial, edit .hg/hgrc and add (or replace if exists):
 
            ```
            [paths]
            default = <url-or-paht-to-your-remote-repo>
            ```

1. Run `mbed publish` to publish your changes.

In a scenario with nested local repositories, start with the leaf repositories first.

### Forking workflow

Git enables a workflow where the publish/push repository may be different than the original ("origin") one. This allows new revisions in a fork repository while maintaining an association with the original repository. To use this workflow, first import an mbed OS program or mbed OS itself, and then associate the push remote with your fork. For example:

```
$ git remote set-url --push origin https://github.com/screamerbg/repo-fork
```

Both `git commit & git push` and `mbed publish` push the new revisions to your fork. You can fetch from the original repository using `mbed update` or `git pull`. If you explicitly want to fetch or pull from your fork, then you can use `git pull https://github.com/screamerbg/repo-fork [branch]`.

Through the workflow explained above, mbed CLI maintains association to the original repository (which you may want to send a pull request to) and will record references with the revision hashes that you push to your fork. Until your pull request (PR) is accepted, all recorded references are invalid. Once the PR is accepted, all revision hashes from your fork become part the original repository, making them valid.
