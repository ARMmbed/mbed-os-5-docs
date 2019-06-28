<h1 id="collab-online-comp">Collaborate</h1>

The Arm Mbed Online Compiler offers collaboration and version control functions to help the community benefit from and improve individual work.

## Terminology

Remote repository:	A library or program published on `mbed.org`.

Local repository:	A library or program in your private workspace.

Commit:	Create a checkpoint within your program's local repository. This does not publish or make it public.

Pull:	Copy changes from a remote repository to a local repository in your workspace.

Push:	Copy changes from a local repository to a remote one.

Fork:	Create a remote repository on `mbed.org` from an imported local repository (that may also contain local changes and modifications). The fork is created under your profile.

Publish:	Copy changes from a local repository to an existing remote one (push) or create a new one (fork).

Update:	Pull from a remote repository and switch your local repository to the latest revision.

## Basic collaboration

The most basic (and the most popular) usage of the collaboration system is the traditional workflow in which one author develops a project, then multiple users import and use it.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/basic_collab.png)<span>Many developers can use code that one author wrote</span></span>

When you import a repository, you are making a clone of a public repository in your private workspace. An imported repository can either be a whole program or a library for a program, and can contain dependencies to other repositories. For example, a library may need another library in order to work. All dependencies will be imported for you automatically when you import a repository.

Once imported, the local repository in your workspace will be `linked` to the remote repository by URL to let you check its status, receive new changes and even contribute code to it.

To import a repository, simply click the Import link on the repository's page on the Arm Mbed website, or use the Import button within the Mbed Online Compiler.

## Getting updates

While browsing a program or a library, you will receive notifications of new versions in the Browser panel under the Summary tab:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/updates.png)<span>Viewing the program description</span></span>

It is also possible to view detailed information about the new changes in the Revisions panel. The top list represents the local repository revisions, where revision numbers marked in green are outgoing revisions, currently not present in the remote repository:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/green_revisions.png)<span>The Revisions panel highlights local changes that are not yet in the remote repository</span></span>

The bottom list represents the remote repository revisions currently not present in your local repository. Just like with local revisions, you can click on revisions in the remote list to see change sets and individual changes per file.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/incoming_revisions.png)<span>Viewing remote revisions not yet in your local repository</span></span>

To get the latest version of the code, simply click the **Update** button.
