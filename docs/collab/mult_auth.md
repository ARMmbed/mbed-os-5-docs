# Multiple authors


Each author can publish to the repository. This allows a group of authors to collaborate on a project, while the consumers import the repository as normal.

{{/media/uploads/dan/pull-merge-push.png}}

** Adding a new author to your repository **

Granting permission for another author to commit to your repository is easy. Go to your repository on the mbed website and click the 'Repository Administration' link. Then start typing a username in the 'Developers' box to add them to the list as shown below:

 {{http://mbed.org/media/uploads/dan/privacy_settings.png}} 

== Day to day usage ==

The key difference between single author workflows and multiple author workflows is the necessity to **merge** the changes made by one author with those made by another author when they simultaneously commit to a single parent revision.

The following are some common operations you will need to do day to day. You won't necessarily need to do all of them, and not necessarily in the order shown.

===1 - Pulling from the public repository===

When there are changes which exist on the public repository but not in your workspace repository, we call them "incoming" changes. The revisions panel tells you when and what incoming changes are available.

To bring the changes into your own workspace repository, simply click the 'Update' button in the Revisions panel for the relevant program/library.

 {{/media/uploads/dan/revs7_incoming.png}} 


===2 - Merging your changes if necessary ===

If you have not made any commits or changes while your co-author has been working, then no merging will be necessary.

However, if two people have worked at the same time on a program or library, it will be necessary to merge or combine the changes.

When you pull the changes into your workspace, you will see something like the below.

{{http://mbed.org/media/uploads/dan/revisions_branch.png}} 

The revisions panel shows one person's changes diverging from another person's changes. This is called a branch. 

To join up the two branches, press the Merge button.


===3 - Resolve merge conflicts if needed===

The merge function will attempt to merge the changes from one or more branches into one. Often, this will complete without issue.

However if two or more people have edited the same line of the same line, a merge conflict occurs. That means mercurial does not know who's changes to keep. It's up to you to decide how the file should really look. This is called resolving conflicts.

When a merge conflict occurs, you will get a warning. Also, all the files which have conflicts in them will be highlighted as below.

{{http://mbed.org/media/uploads/dan/revisions_conflict.png}} 

When this happens, open the file(s) in conflict and look for something like this:

{{http://mbed.org/media/uploads/dan/revisions_conflict_marks.png}} 

Wherever there is a conflict, mercurial will annotate the source code with markings showing your changes and other people's changes. You then have to choose one person's version, or blend the two. When you have finished, remove the <<<< and >>> and === marks, and save the file. 

The first save of a file after being opened in a conflicted state marks it as resolved and removes the red highlight.


===4 - Commit the merge===

Once you have merged the code if needed, you have to commit. This makes the join between two branches permanent. Once you commit, your revisions pane will look something like this:

 {{/media/uploads/dan/revs6_outgoing.png}} 

You can see the two branches coming back together at the revision 'merged changes'.


===5 - Pushing back to the repository ===

Once all branches and conflicts are resolved and joined back into one, you would typically re-test your program or library. If you're ready to push your changes and the merged result back to the public repository, simply click the 'Publish' button.
