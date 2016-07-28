# Version control

You can use the version control features to let you version, branch and merge code, with a nice representation of the state of your project history:
 
{{http://mbed.org/media/uploads/screamer/revision-history-overview.png?v=2}}

The approach should be familiar to those of you with experience of distributed version control models (as used by mercurial/git); each program and library has its own local repository, so you can commit and perform actions on it within your own workspace (such as switching, branching, showing changes). 

The main things you can do with a local repository include:
 * **Commit** a version of your project, and view the revision history
 * **View** changes a version made, and **compare** changes between versions
 * **Switch** and **revert** to a different version
 * **Branch** and **merge** versions

<<warning title="Notice">>
You can also do collaboration aspects with this - fork, push, pull, send pull request. These are covered in the [[/handbook/Collaboration/Getting-started|Collaboration wiki pages]].
<</warning>>

Your program is the "Working Copy". You can "Commit" changes to its local repository to create new "Revisions".

You can choose to "Switch" to a particular revision, which updates your working copy to that revision (e.g. a state of your program in the past). This is the way you can "Branch"; do some commits, switch to a previous revision, do some more commits; you now have two branches of development derived from a common revision.

You can then "Merge" a revision, often the head of one branch, in to your working copy. This creates a working copy that is the merge of these two branches, and when you commit, your back to one (less) branch of development.

There is also the option to "Discard" your working copy, and "Revert" your working copy to a particular revision; unlike "Switch", this creates a working copy with the changes you need to get back to that previous state, more like an "undo" than a branch.

You can see the changes between your current working copy to the previous revision, and changes between revisions.

{{/media/uploads/simon/screen_shot_2011-06-14_at_21.08.49.png}}

== Sub-repositories and synchronization ==
Programs and libraries can depend on other published code to deliver a functionality. These dependencies are stored in reference files (e.g. name.lib) that are present in the code base of the repository and when you import it the mbed Compiler will follow these references and import other sub-repositories, including referenced sub-sub-repositories.

This synchronization mechanism ensures that the imported repository and all its sub-repositories will be restored to the exact state they were when the author committed the changes to the parent repository (usually a program) and published it. This also makes it easy for everyone to use the code without worrying about dependencies, imports, revisions numbers etc.

The following is required when you publish to ensure that the repository can be imported successfully:
 * All sub-repositories (even sub-sub-repositories) must be published on the mbed Developer Site
 * All sub-repositories shouldn't contain uncommitted or unpublished changes.


Here is the video that shows how you get started:
{{http://www.youtube.com/watch?v=BWM21JzSDSs}}
