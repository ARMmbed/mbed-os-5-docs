# Publishing code

Publishing copies your program or library from your **private** workspace to your **public** mbed website profile.

The public copy of your repository is the home of your project on mbed. This is the place for:

* Documentation about your project.
* Guides on how to use it.
* Discussion by users of your project.

If you want to share your work:

1. Click **Publish** from the right-click context menu in the mbed Online Compiler:

	<span class="images">![](images/publish.png)</span>

1. If you have uncommitted changes, you will be prompted to commit your work. 

1. If this is the first time you have published this program or library, you will see a dialog like this one:

	<span class="images">![](images/publish_deatils.png)</span>

1. Enter a description of what you are publishing.

1. Select a **Publish in** option. You have the choice to publish your repository to your user account or to a team that you are a member of. When publishing to a team, all members of that team will be able to collaborate on your work with the permissions managed by the team as well as the repository. 

	Note: You must be a member of a team before trying to publish to it. You can **Send a Join Request** on the team's homepage if it has public enrollment enabled.

1. Select **Visibility**: This controls who can see your repository. There are three options:

	 * **Public**: For a normal repository. It will be visible in the site code listings and in your personal profile. It's readable by everyone, but only writable by you (or people you add).

	 * **Public (unlisted)**: A sub-type of public; the repository is public and anyone can view it, but it's not advertised in any listings. Users will need to know the URL of the repository to be able to reach it. 

	* **Private**: Only you (the owner), or users you add, can see and access the repository. To allow users to see it, use the repository's Admin settings. Users you *don't* add will not be able to see the repository, even if they have the URL. 

1. Click OK. 

That copies your private repository to the mbed public website, where other users can import it. It also copies a reference to any libraries you used in your code; if those libraries are not published, you will be prompted to publish them. 

The end result is that a published repository is an **exact copy** of your program or library as it exists in your workspace. This ensures that the code works as expected when another user imports your code.

<span class="images">![](images/published_repo.png)</span>
