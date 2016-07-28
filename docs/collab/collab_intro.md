# Collaboration and version control with the mbed Online Compiler

The mbed Online Compiler offers collaboration and version control functions to help the community benefit from and improve individual work.

## Terminology

Remote repository
:	A library or program published on mbed.org.

Local repository
:	A library or program in your private workspace. 

Commit
:	Create a checkpoint within your program's local repository. This does not publish or make it public.

Pull
:	Copy changes from a remote repository to a local repository in your workspace.

Push
:	Copy changes from a local repository to a remote one.

Fork
:	Create a remote repository on mbed.org from an imported local repository (that may also contain local changes and modifications). The fork is created under your profile.

Publish
:	Copy changes from a local repository to an existing remote one (push) or create a new one (fork).

Update
:	Pull from a remote repository and switch your Local repository to the latest revision.

## Basic collaboration

The most basic (and the most popular) usage of the collaboration system is the traditional workflow where one author develops a project, then multiple users import and use it.

<span class="images">![](images/basic_collab.png)</span>

When you import a repository, you are making a clone of a public repository in your private workspace. An imported repository can either be a whole program or a library for a program, and can contain dependencies to other repositories. For example, a library may need another library in order to work. All dependencies will be imported for you automatically when you import a repository.

Once imported, the local repository in your workspace will be 'linked' to the remote repository by URL to let you check its status, receive new changes and even contribute code to it.

To import a repository, simply click the Import link on the repository's page on the mbed website, or use the Import button within the mbed Compiler. You can read more about importing on the [mbed Online Compiler page](../dev_tools/online_comp.md).

## Getting updates

While browsing a program or a library, you will receive notifications of new versions in the Browser panel under the Summary tab:

<span class="images">![](images/updates.png)</span>

It is also possible to view detailed information about the new changes in the Revisions panel. The top list represents the local repository revisions, where revision numbers marked in green are outgoing revisions, currently not present in the remote repository:

<span class="images">![](images/green_revisions.png)</span>

The bottom list represents the remote repository revisions currently not present in your local repository. Just like with local revisions, you can click on revisions in the remote list to see change sets and individual changes per file.

<span class="images">![](images/incoming_revisions.png)</span>

To get the latest version of the code, simply click the **Update** button.

## Forking a repository

When you add changes to an imported repository in your private workspace, you might want to publish them for others to use.

Unless you are the author of the imported repository or have developer access (see [Multiple Authors](mult_auth.md)), you will be forced to fork (or re-publish).

1. Open the context menu of the imported program or library and click **Publish**:

	<span class="images">![](images/publish.png)</span>

1. You are prompted to publish to the linked remote repository:

	<span class="images">![](images/publish_prompt.png)</span>

1. As you do not have permission to publish to the repository, click the **Fork...** button:

	<span class="images">![](images/fork.png)</span>

1. Your repository, with all its changes, is published to your profile on the mbed.org website.

The forking process is identical to the [code publishing](publishing_code.md) workflow, with the exception that the forked repository will be recognized as a fork of the original or imported one:

<span class="images">![](images/fork_indication.png)</span>

<span class="notes">**Note:** When you fork a repository, the Local repository in your workspace will be linked to the forked Remote repository - the URL changes to the forked repository URL. You can change the URL by clicking the pencil icon next to the URL in the [[/handbook/Compiler-Version-Control|Revisions panel]].</span>

**Once the fork is complete you can send a Pull Request to the ancestor (imported) repository to pull from your fork. This is covered in the [[/handbook/Collaboration/Pull-requests|Pull Requests]] wiki page.**

== Updating from a fork ==

If someone forks one of your repositories and modifies it, you can easily pull in any changes they have made into your own workspace. First click the 'Update From ...' button as shown below:

{{/media/uploads/screamer/revision-history-update-from.png?v=2}} 

Then, enter the URL of their published repository you want to pull changes from.

{{/media/uploads/screamer/update-from-dialog.png?v=4}}  

Once you click OK, all their changes will pulled into your Local repository.

<<warning title="Notice">>
This won't change the URL of your Local repository.
<</warning>>

== Comparing with a fork ==

The [[/handbook/Compiler-Version-Control|Revisions panel]] lets you compare Local repository with Remote one if they are 'related'. The term 'related repositories' means that either repository is ancestor to the other through direct or indirect relationship (e.g. fork of the fork of the fork).

To compare Local repository with Remote one, open the [[/handbook/Compiler-Version-Control|Revisions panel]] and click "Compare WIth ..." button located on the bottom panel like shown here:

 {{/media/uploads/screamer/revision-history-compare.png}}

Then, enter the URL of the Remote repository you want to compare with.

{{/media/uploads/screamer/compare-with-dialog.png?v=3}}

Comparing repositories doesn't apply any actions or changes to your Local repository, so you can safely review the remote revisions without affecting your local work.

Once you click OK in the dialog, both repositories relativity will be validated and if successful some UI elements in the Revisions panel will be changed to reflect the comparison mode:

{{/media/uploads/screamer/revision-history-comparing.png}}

You can view remote changes by clicking on revisions in the bottom (remote) panel and once happy with them you can pull individual revision through 'Pull this revision' context menu item or by simply dragging and dropping them in the upper (local) panel.

Alternatively you can pull all changes via the 'Pull All' button or pull and switch to the latest revision via the 'Update' button as you would normally do in non-comparison mode (see [[/handbook/Collaboration/Getting-started#getting-updates|Getting updates]]).
