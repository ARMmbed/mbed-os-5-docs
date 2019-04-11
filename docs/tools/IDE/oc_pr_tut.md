<h1 id="pr-tutorial">Creating and reviewing pull requests</h1>

## Creating a new request

All pull requests are created and recorded against the remote repository, the one receiving the modifications if the pull request is accepted.

To create a pull request:

1. When you publish a fork of another repository, the Arm Mbed developer site displays the ancestor repository under **Repository details**. If you are the repository owner, an additional **Create Pull Request** button is displayed on top.

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/repo_details.png)<span>A forked repository shows the details of its ancestry</span></span>

1. Click the **Create Pull Request** button. The **Create Pull Request** page opens, showing the URLs of the forked and the ancestor repositories:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/create_pull_request.png)<span>Creating a pull request with a forked repostiory</span></span>

1. You can change the remote repository URL if you want to send a pull request to another related repository. The form validates the repository URL addresses as you type or paste and warns if either of them is wrong, missing or unrelated. It also checks whether the forked repository (on the left) has changes that aren't present in the remote repository (on the right).

1. Add a suitable title and description that summarize the set of changes in the pull request, and specify any additional information the repository owners might find useful. It is also a good place to describe any licensing matters. As always, being polite goes a long way, and they might even add you as author to their repository!

1. Click the **Send Pull Request** button.

The pull request is added to the **Pull Requests** page of the repository, and an email is sent to the repository owners with the title and description you specified.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/pull_request_created.png)<span>Sending the pull request</span></span>

## Editing an existing pull request

Pull requests are `limited` to the latest revision at the moment of sending. This means that you can publish more changes to your repository, and the other party only sees the changes that were available when the pull request was created.

To update your pull request to the latest revision:

1. Click the **Edit** button on the pull request page.
1. Check the **Update request to latest revision(s)?** checkbox.
1. Submit the edit. The other party is notified that you edited the pull request.

## Managing a pull request you receive

### Viewing pull requests

When a pull request is sent to a repository to which you're author or coauthor, you receive an email notification with the pull request details and a link to the pull request page.

You can also see all existing pull requests by visiting the repository page and clicking on the **Pull Requests** tab:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/open_pull_requests.png)<span>Viewing all open pull requests by using the Pull Requests tab</span></span>

<span class="tips">**Tip:** This only lists the open pull requests. To view all pull requests, including the closed ones (accepted or rejected), click the **Show all pull requests** button.</span>

On each pull request page, you can discuss changes, coding standards and so on before accepting or rejecting the request. Once closed, you won't be able to add more comments.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/review_pull_request.png)<span>Reviewing and commenting on a pull request</span></span>

To quickly close a pull request without reviewing it, click the **Close** button.

### Reviewing a pull request

Most online services that offer source code and version control hosting let you review and merge pull requests.

We went a step further by letting you review, compile, test and add more changes before accepting a pull request, by harnessing the power of the Arm Mbed Online Compiler.

You need to import a pull request to your Mbed Online Compiler workspace as a separate program or library, so it won't interfere with the codebase of your original program. You can then freely and safely experiment with the changes.

To review a pull request:

1. Click the **Review** button on the pull request page (as shown above). The Mbed Online Compiler opens in a new browser tab; if you already have the Mbed Compiler open, switch to that tab.

1.  The Mbed Online Compiler suggests an import name based on your repository name and a `_pullrequest` suffix, to remind you that this was imported as part of a pull request. You're free to change the name:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/import_pull_request.png)<span>The Online Compiler's default import name suggestion</span></span>

1. Click "Import".

1. The pull request is imported to your workspace, and the Revisions panel opens:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/revision_history_pull_request.png)<span>Viewing the pull request in the Revisions panel</span></span>

Newly introduced revisions are marked in green. These are the proposed changes - the ones you are being asked to pull. To review individual changes, click on the files list on the right.

The Mbed Online Compiler remembers the pull request status of an imported program or library across sessions, so you can always close the Revision History panel and continue the review later. For example, you can open one of the changed files in the Editor and click **Compile** to check whether the code compiles successfully. If it does, you can download and test it on your Mbed Enabled device.

### Accepting a pull request

Click the **Accept** button in the bottom panel, and an accept confirmation dialog opens:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/accept_pull_request.png)<span>Accepting a pull request makes its changes public</span></span>

You can clean up the imported program by checking the **Delete this program when complete (cleanup)** button.

Accepting a pull request publishes to your repository both the contents of that pull request, and any changes you made to the pull request. It also marks the pull request as accepted:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/pull_request_accepted.png)<span>Another dialog box appears and informs you that your acceptance of the pull request was successful</span></span>

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/pull_request_closed.png)<span>Viewing the pull request after accepting it</span></span>

### Rejecting a pull request

If you choose to reject the pull request:

1. Click the **Reject** button in the bottom panel. A confirmation dialog opens:

	<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/reject_pull_request.png)<span>Commenting on a pull request rejection</span></span>

1. Enter a comment explaining the rejection.

1. You can clean up the imported program by checking the **Delete this program when complete (cleanup)** button.

1. Click **Reject**.

1. The comment is posted on the pull request page on your behalf, and the pull request is marked as rejected.

<span class="notes">**Note:** If you're not satisfied with the code, you can always attempt to enhance it by introducing your own changes on top of the pull request. You can then accept the pull request; the published pull request will include the changes you have made to the original content.
</span>
