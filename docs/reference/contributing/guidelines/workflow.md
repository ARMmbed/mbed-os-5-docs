### Workflow

#### Contributions

All code changes and additions to Mbed OS are handled through GitHub. If you want to contribute, either by adding features or by fixing bugs, please follow the guidelines for [new features](#contributing-new-features-to-mbed-os) and [bugs](#reporting-and-fixing-bugs), and in both cases please follow the <a href="/docs/v5.6/reference/guidelines.html#style" target="_blank">code style guide and GitHub pull request guidelines</a>. Please also read the <a href="/docs/v5.6/reference/guidelines.html#cla" target="_blank">CLA</a> guidelines as pull requests submitted without a CLA in place will be immediately closed.

#### Contributing new features to Mbed OS

Before contributing an enhancement (new feature, new port and so on) please <a href="https://os.mbed.com/forum/bugs-suggestions/" target="_blank">discuss it on the forums</a> to avoid duplication of work, as we or others might be working on a related feature.

Patch contributions can only be accepted through GitHub by creating a pull request from forked versions of our repositories. This allows us to review the contributions in a user friendly and reliable way, under public scrutiny.

Please create separate patches for each concern; each patch should have a clear unity of purpose. In particular, separate code formatting and style changes from functional changes. This makes each patch’s true contribution clearer and therefore quicker and easier to review.

#### Reporting and fixing bugs

Before submitting a bug report or a bug fix, please <a href="https://os.mbed.com/forum/bugs-suggestions/" target="_blank">discuss it on the forums</a> to avoid duplication of work, as we or others might be working on it already.

##### Bug reports (issues) on GitHub

All Mbed OS is on GitHub; please use GitHub's <a href="https://guides.github.com/features/issues/" target="_blank">issues mechanism</a> to open a bug report directly against the relevant GitHub repository.

##### Bug fixes

Please refer to the <a href="/docs/v5.6/reference/guidelines.html#style" target="_blank">code contributions chapter</a>.

Bug fixes must be verified by a member of the Mbed team before they're pulled into the main branch. You must therefore use GitHub to fork the repo, then submit a pull request with your changes.

The last line in your commit message description should say “Fixes #deadbeef”, where “deadbeef” is the issue number in GitHub. This allows GitHub to automatically close the issue when the commit is merged into the default branch.

#### Further reading

Please see the <a href="/docs/v5.6/reference/guidelines.html#style" target="_blank">code contributions chapter</a> for the guidelines to GitHub pull requests and the coding style guide.

#### Guidelines for GitHub pull requests

Pull requests on GitHub have to meet the following requirements in order to keep the code and commit history clean:

- Commits should always contain a proper description of their content. Start with a concise and sensible one-line description, then elaborate on reasoning of the choices taken, descriptions for reviewers and other information that might otherwise be lost.
- Commits should always be written to allow publication, so they can never contain confidential information, reference private documents, links to intranet locations or rude language.
- Each commit should be the minimum self-contained commit for a change. A commit should always result in a new state that is again in a compilable state. Large changes should (if possible) be split up into logical smaller commits that help reviewers follow the reasoning behind the full change.
- Commits should follow <a href="http://chris.beams.io/posts/git-commit#seven-rules" target="_blank">Chris Beam’s seven rules of great commit messages</a>:
	1. Separate subject from body with a blank line.
	1. Limit the subject line to 72 characters (note that this is a deviation from Beam's standard).
	1. Capitalize the subject line.
	1. Do not end the subject line with a period.
	1. Use the imperative mood in the subject line.
	1. Wrap the body at 72 characters.
	1. Use the body to explain _what_ and _why_ vs _how_.
- Because we use GitHub and explicit CLAs, special commit tags that other projects may use, such as “Reviewed-by”, or “Signed-off-by”, are redundant and should be omitted. GitHub keeps track of who reviewed what and when, and our stack of signed CLAs shows us who has agreed to our development contribution agreement.
- Prefixing your commit message with a domain is acceptable and recommended where it makes sense to do so. However, prefixing one's domain with the name of the repo is not useful. For example, making a commit entitled "mbed-drivers: Fix doppelwidget frobulation" to the `mbed-drivers` repo would not be acceptable, as it is already understood that the commit applies to `mbed-drivers`. Renaming the commit to "doppelwidget: Fix frobulation" would be better, if we presume that "doppelwidget" is a meaningful domain for changes, as it communicates that the change applies to the doppelwidget area of mbed-drivers.

#### Mbed OS maintainers

The maintainers are a small group of Mbed OS engineers who are responsible for the Mbed OS codebase. Their primary role is to progress contributions, both internal and external, from the initial pull request state through to released code. They:

1. Check for CLA compliance.
2. Ensure the relevant stakeholders review pull requests.
3. Guide contributors both technically and procedurally.
4. Run pull requests through the CI systems.
5. Merge pull requests into the requested branches.
6. Make periodic patch and feature releases.

The current maintainers are:

* Anna Bridge (adbridge).
* Martin Kojtal (0xc0170).
* Jimmy Brisson (theotherjimmy).
* Shrikant Tudavekar (studavekar).
* Sam Grove (sg-).

#### GitHub pull requests workflow

Each pull request will go through the following workflow:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/workflow.png)<span>The workflow of merging a pull request</span></span>

##### Pull request states

Labels that the Mbed OS maintainers add to a pull request represent the pull request workflow states. The Mbed OS maintainers are responsible for moving pull requests through the workflow states.

##### Reviews

All pull requests must be reviewed. The Mbed OS maintainers determine the most suitable person to review the pull request and tag that person accordingly. If a pull request requires a review from partners, the maintainers tag the corresponding GitHub group instead.

##### The CI (Continuous Integration) testing

There are a number of CI systems that are available. Which CI tests we run against a particular pull request depends on the effect of that pull request to the code base. Irrespective of which CIs tests run, Mbed OS has an all green policy, meaning that all the CI jobs that are triggered must pass before we merge the pull request.

##### Releases 

Once we merge a pull request, we tag it with a release. This is the release in which we first publish this pull request. For patch releases, we allow only bug fixes, new targets and enhancements to existing functionality. New features only go to feature releases. 

The release tag has the following format:

* *release-version: 5.f.p* - Where `f` is the feature release and `p` the patch release.

##### Additional labels

We use many other labels to summarize the scope and/or effect of the changes.

* *needs: preceding PR* - This pull request cannot yet be merged because it has a dependency on another pull request that needs to merge first.

* *DO NOT MERGE* - This pull request contains changes that may be in a draft state and submitted purely for review, or may contain breaking changes that have not been considered.

* *devices: 'name'* - The pull request specifically affects the named device(s).

* *component: 'name'* - The pull request specifically affects the named component.

The following labels summarize the scope of the pull request.

* *scope: bug-fix*
* *scope: feature*
* *scope: new-target*

