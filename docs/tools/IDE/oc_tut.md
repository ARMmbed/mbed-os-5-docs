# Importing code

There are two methods of importing the code into the online compiler: directly from a program presented on the site, or using the compiler’s Import button:

1. Directly from the site: wherever you see a program on the site, you should see an **`Import into Mbed IDE`** button:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/import_button_site.png)<span>Most code snippets on the site can be directly imported</span></span>

	Clicking that button will take you to the compiler; you can then give the program a new name and import it to your workspace:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/import_popup.png)<span>Importing to the Mbed Online Compiler</span></span>


1. The compiler's Import button: click the **Import** button in the compiler to open the Import Wizard:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/import_button_comp.png)<span>Triggering the Import Wizard from within the Mbed Online Compiler</span></span>

	You can search for a program by name, or perform an empty search to show all available programs:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/all_programs.png)<span>The applications list</span></span>

	Double click a program to import it.

# Creating a new program

1. From the **New** menu, select **New Program**:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/new.png)<span>Triggering a new program</span>

1. The **Create new program** pop-up opens.
	1. Select your platform (board).
	1. You can create from an existing template or from an empty program.
	1. Enter a unique name.

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/new_program.png)<span>Creating a new program</span></span>

1. Create a `main.cpp` file in your program:
	1. Right click on the program and select **New File...**. The **Create new file** pop-up opens. If you created from an existing template, this file already exists.

		<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/new_file.png)<span>Adding a file</span></span>

	1. Enter `main.cpp` as the file name.

		<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/main_cpp.png)<span>Naming the new file</span></span>

1. Import the Arm Mbed OS library, so you can build your program with the Mbed OS codebase:
	1. Right click on the program, and hover over **Import Library...**. Then, click **From URL...**

        <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/import_from_url.PNG)<span>Import from URL</span></span>

	1. The Import Wizard opens. In the **Source URL:** field, enter `https://github.com/armmbed/mbed-os`.

        <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/import_wizard.PNG)<span>Import Mbed OS from GitHub</span></span>

    1. Select **Import**.

# Getting your program on your board

The Arm Mbed Online Compiler builds a file that can run on your board. All you need to do is:

1. Select the correct board.
1. Compile the code and download the compiled file.
1. Copy the file to your board.

## Selecting your board

Mbed programs can be built to run on multiple boards. The hard work is done behind the scenes by Arm Mbed OS itself. All you need to do is tell the Mbed Online Compiler which board you're building for.

To select a board as the build target:

1. The compiler shows the current build board's name on the upper right corner:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/show_board.png)<span>Showing current board. Click the board to open the full list</span></span>

1. Click the name of the board you need:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/select_board.png)<span>Click a board to set it as the compilation board</span></span>

	If the board isn't already on your list, go to the board's page on `mbed.com` and click the **`Add to your mbed Compiler`** button:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/add_board.png)<span>Adding a board to the Mbed Online Compiler list</span></span>

## Compiling and downloading

The **Compile** menu offers five options:

1. **Compile:** builds code that you have modified since your last compile and downloads the resulting binary file.
1. **Compile All:** same as *compile*, but rebuilds all source code, even if it hasn't changed since the last compile.
1. **Build Only:** compiles your code but doesn't download the result.
1. **Compile Macros:** defines additional macros at compile time.
1. **Update Docs**: adds documentation.

## Copying the file to the board

<span class="notes">**Note:** If you're working on Windows, you might need to install a driver to allow you to copy to your board. Please see the [Windows Serial Driver section](../tutorials/serial-communication.html).</span>

Your board should appear on your computer as removable storage. To run your program on the board, simply drag and drop the file you downloaded in the previous section.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/device_on_mac.png)<span>The device appears as removable storage, under the name `MBED`</span></span>

# Forking a repository

When you add changes to an imported repository in your private workspace, you may want to publish them for others to use.

Unless you are the author of the imported repository or have developer access, you will be forced to fork (or republish).

1. Open the context menu of the imported program or library and click **Publish**:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/publish.png)<span>Making changes from your private workspace public</span></span>

1. You are prompted to publish to the linked remote repository:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/publish_prompt.png)<span>Publishing your changes to the remote repository</span></span>

1. As you do not have permission to publish to the repository, click the **Fork...** button:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/fork.png)<span>Forking and describing your forked repository</span></span>

1. Your repository, with all its changes, is published to your profile on the `mbed.org` website.

The forking process is identical to the [code publishing](publishing-code.html) workflow, with the exception that the forked repository will be recognized as a fork of the original or imported one:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/fork_indication.png)<span>Identifying a forked repository and its ancestor</span></span>

<span class="notes">**Note:** When you fork a repository, the local repository in your workspace is linked to the forked remote repository - the URL changes to the forked repository's URL. You can change the URL by clicking the pencil icon next to the URL in the Revisions panel.</span>

**Once the fork is complete, you can send a *pull request*, asking the ancestor (imported) repository to pull from your fork. This is covered in the [Pull requests](pr-tutorial.html) page.**

## Updating from a fork

If someone forks one of your repositories and modifies it, you can easily pull in any changes they have made into your own workspace.

1. Click the `Update From...` button:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/update_from.png)</span>

1. Enter the URL of the published repository you want to pull changes from:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/repo_url.png)<span>Choosing the repository whose changes you want to pull</span></span>

1. Click OK. The changes are pulled into your local repository.

<span class="notes">**Note:** This won't change the URL of your local repository.</span>

## Comparing with a fork

The Revisions panel lets you compare a local repository with a remote one, if they are "related". The term "related repositories" means that one repository is the ancestor of the other, through direct or indirect relationship (for example, a fork of the fork of the fork).

Comparing repositories doesn't apply any actions or changes to your local repository, so you can safely review the remote revisions without affecting your local work.

To compare the local repository with the remote one:

1. Open the Revisions panel and click the "Compare With ..." button on the bottom panel:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/compare_repo.png)<span>Comparing a local and a remote repository</span></span>

1. Enter the URL of the remote repository you want to compare with.

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/repo_url_compare.png)<span>Choosing the remote repository to compare</span></span>

1. Click OK. The repositories are compared, and the Revisions panel reflects the comparison mode:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/comparing_repos.png)<span>Viewing the comparison in the Revisions panel</span></span>

You can view the remote changes by clicking on revisions in the bottom (remote) panel. You can then

- Pull individual revisions through the **Pull this revision** context menu item, or by dragging and dropping them to the upper (local) panel.
- Pull all changes using the **Pull All** button.
- Pull and switch to the latest revision using the **Update** button as you would normally do in noncomparison mode.
