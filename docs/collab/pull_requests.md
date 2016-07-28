# Pull requests

<<warning title="Notice">>
This article covers features that are currently available on beta mode of the mbed Online Tools. If you are interested in beta testing, open [[http://mbed.org/betamode/]] and activate it.
<</warning>>

A pull request lets you tell others about changes you've added to [[/handbook/Collaboration/Getting-started#forking-a-repository|a fork]] of their (or ancestor) repository, effectively granting them permission to include and use your code in their code base. Once the pull request is created, the other party can review, accept or reject the set of changes, discuss further modifications and even add follow-up changes or merges.

Think of pull requests as for simplified [[/handbook/Collaboration/Getting-started#forking-a-repository|fork and update]] workflow, where the changes contributed by non-repository developers are being moderated by the repository author(s).

== Day to day usage ==

An important thing to know about pull requests is that they can only exist between related repositories. The term 'related repositories' means that either repository is ancestor or sibling to the other through direct or indirect relationship (e.g. fork of the fork of the fork). Pull requests usually originate from a forked repository to ancestor repository, though the functionality is flexible and allows pull requests from ancestor repository to a forked repository for cases where the original author wants to contribute later added code to a fork.

=== Creating a pull request ===

When you publish a fork of another repository, the mbed Developer Site will display the ancestor repository under repository details:

[[/media/uploads/screamer/fork-published.png|{{/media/uploads/screamer/fork-published.png?v=6|Click to enlarge|600}}]]

An additional "Create Pull Request" button will be displayed on top that is only visible to you and other repository authors (if any).

Click it and you'll be taken to the "Create Pull Request" page, where the URLs of the forked and the ancestor repository will be prefilled like shown below:

[[/media/uploads/screamer/pull-request-create.png|{{/media/uploads/screamer/pull-request-create.png?v=2|Click to enlarge|600}}]]

You can change the remote repository URL if you want to send a pull request to another related repository. The form will validate the repository URL addresses as you type or paste, and it will warn if either of them is wrong, missing or unrelated. It will also check whether the forked repository (on left) has changes that aren't present in the remote repository (on right).

Add a suitable title and description that summarize the set of changes they should expect and specify any additional information they might find useful. It is also a good place to describe any licensing matter. As always, being polite goes a long way and they might even add you as author to their repository!

Click the "Send Pull Request" button when ready and the pull request will be added to the "Pull Requests" page of their repository, which will also send them an email notification with the title and description you specified.

[[/media/uploads/screamer/pull-request-created.png|{{/media/uploads/screamer/pull-request-created.png?v=1|Click to enlarge|600}}]]

All pull requests are created and recorded against the remote repository, the one receiving the modifications if the pull request is accepted.

<<warning title="Notice">>
Pull requests are 'limited' to the latest revision at the moment of sending. This means that you can publish more changes to your repository and the other party will only see the changes that were available when the pull request was created. To update your pull request to the latest revision, click the "Edit" button on the pull request page and check "Update request to latest revision(s)?" checkbox before you finish editing it. The other party will be notified that you edited the pull request. 
<</warning>>

=== Managing a pull request ===

When a pull request is sent to a repository to which you're author or co-author, you would receive an email notification with the pull request details and an http link to the pull request page. Alternatively, you can visit the repository page and click on the "Pull Requests" tab:

[[/media/uploads/screamer/pull-request-list.png|{{/media/uploads/screamer/pull-request-list.png?v=3|Click to enlarge|600}}]]

This will only list the open pull requests. To view all pull requests, including the closed ones (accepted or rejected) click the "Show all pull requests" button.

On each pull request page you can discuss changes, coding standards etc before accepting or rejecting it, but once closed you won't be able to add more comments.

[[/media/uploads/screamer/pull-request-review.png|{{/media/uploads/screamer/pull-request-review.png?v=4|Click to enlarge|600}}]]

To quickly close a pull request without reviewing it, click the "Close" button.

=== Reviewing a pull request ===

Most online services that offer source code and version control hosting let you review and merge pull requests.\\
We made a step further by letting you review, compile, test and add more changes if necessary before accepting a pull request by harnessing the power of the mbed Online Compiler.

To review a pull request click the "Review" button on the pull request page (like shown above) and the mbed Online Compiler will open in a new browser tab. If you already have the mbed Compiler open, then switch to that tab.

 {{/media/uploads/screamer/pull-request-import.png}}

To review a pull request you need to import it in your workspace as a separate program or a library, so it won't interfere with the codebase of your original program, letting you to freely and safely experiment with the changes. The mbed Compiler will suggest an import name based on your repository name and a '_pullrequest' suffix to remind you that this was imported as part of a pull request.

Once you click "Import" the pull request will be imported in your workspace and the Revisions panel will open:

{{/media/uploads/screamer/revision-history-pullrequest.png}} 

Newly introduced revisions will be marked in green (like shown above). These are the proposed changes, the ones you are requested to pull. To review individual changes click on the files list on right. 

The mbed Compiler will remember the pull request status of an imported program or library across sessions, so you can always close the Revision History panel and continue the review later on. For example you can open one of the changed files in the Editor, click "Compile" to check whether their code compiles successfully and if it does, you can download and test it on your mbed-enabled device.

==== Accepting a pull request ====

Click the "Accept" button in the bottom panel and an accept confirmation dialog will appear:

{{/media/uploads/screamer/pull-request-accept.png}} 

This will publish their changes and your later added changes (if any) altogether in your repository and mark the pull request as accepted. 

{{/media/uploads/screamer/pull-request-accepted.png}} 

[[/media/uploads/screamer/pull-request-closed.png|{{/media/uploads/screamer/pull-request-closed.png?v=1|Click to enlarge|600}}]]


==== Rejecting a pull request ====

If you choose to reject the pull request, click the "Reject" button in the bottom panel and a reject confirmation dialog will appear:

{{/media/uploads/screamer/pull-request-reject.png?v=3}}

This requires you to enter a comment and once you click "Reject", the comment will be posted on the pull request page on your behalf and the pull request will be marked as rejected.

<<warning title="Notice">>
If you're not satisfied with their code you can always attempt to enhance it by introducing your own changes on top of theirs. Once happy with the result you can accept the pull request, which will publish all changes, including yours.
<</warning>>

Whether you choose to accept or reject the pull request, you can cleanup the imported program or library by using the checkbox in the bottom.
