# Workflow

All code changes and additions to Mbed OS are handled through GitHub. If you want to contribute, either by adding features or by fixing bugs, please follow the guidelines for [new features](#functionality-change) and [bugs](#reporting-bugs). In both cases, please follow the [code style guide](../contributing/style.html) and [GitHub pull request guidelines](#guidelines-for-github-pull-requests).

## Mbed OS maintainers

The maintainers are a small group of Mbed OS engineers who are responsible for the Mbed OS codebase. Their primary role is to progress contributions, both internal and external, from the initial pull request state through to released code. They carry out pull request reviews at least twice a week.

Responsibilities:

- Ensure the relevant stakeholders review pull requests.
- Guide contributors both technically and procedurally.
- Run pull requests through the CI systems.
- Put label version.
- Merge pull requests into the requested branches.
- Make periodic patch and feature releases.

The current maintainers are:

- [Anna Bridge](https://os.mbed.com/users/AnnaBridge).
- [Martin Kojtal](https://os.mbed.com/users/Kojto).

## Contributions

Before contributing an enhancement (for example, a new feature or new port), please [discuss it on the forums](https://os.mbed.com/forum/bugs-suggestions/) to avoid duplication of work, as we or others might be working on a related feature.

We can only accept contributions through GitHub if you create a pull request from forked versions of our repositories. This allows us to review the contributions in an easy-to-use and reliable way, under public scrutiny.

For security purposes, we require our GitHub contributors to use two-factor authentication on their GitHub accounts. Two-factor authentication adds a layer of security, which reduces the risk of your account being hacked. To enable two-factor authentication, please see [GitHub’s instructions](https://help.github.com/articles/configuring-two-factor-authentication/).

Please create separate pull requests for each topic; each pull request needs a clear unity of purpose. In particular, separate code formatting and style changes from functional changes. This makes each pull request’s true contribution clearer, so review is quicker and easier.

### Reporting bugs

You can submit Mbed OS bugs directly on [GitHub](https://github.com/ARMmbed/mbed-os). Please submit questions or enhancement requests on the [forums](https://os.mbed.com/forum/bugs-suggestions/).

The bug report should be reproducible (fails for others) and specific (where and how it fails). We will close insufficient bug reports.

We copy issues reported on GitHub to our internal tracker and regularly triage them. Our ciarcom bot adds an internal tracking reference to each issue: "Internal Jira reference: https://jira.arm.com/browse/MBOTRIAGE-xxxx" and provides labels showing the current state of the mirrored issues.

## Guidelines for GitHub pull requests

Pull requests on GitHub have to meet the following requirements to keep the code and commit history clean:

- Commits must always contain a proper description of their content. Start with a concise and sensible one-line description. Then, elaborate on reasoning of the choices made, descriptions for reviewers and other information that might otherwise be lost.
- You should always write commits that allow publication. They must not contain confidential information, references to private documents, links to intranet locations or rude language.
- Each commit should be the minimum self-contained commit for a change. A commit should always result in a new state that is again in a compilable state. You should (if possible) split large changes into logical smaller commits that help reviewers follow the reasoning behind the full change.
- Commits and pull request titles should follow [Chris Beam’s seven rules of great commit messages](http://chris.beams.io/posts/git-commit#seven-rules).
- Because we use GitHub, special commit tags that other projects may use, such as “Reviewed-by”, or “Signed-off-by”, are redundant and should be omitted. GitHub tracks who reviewed what and when.
- Prefixing your commit message with a domain is acceptable, and we recommend doing so when it makes sense. However, prefixing the domain with the name of the repo is not useful. For example, making a commit entitled "mbed-drivers: Fix doppelwidget frobulation" to the `mbed-drivers` repo is not acceptable because it is already understood that the commit applies to `mbed-drivers`. Renaming the commit to "doppelwidget: Fix frobulation" would be better, if we presume that "doppelwidget" is a meaningful domain for changes, because it communicates that the change applies to the doppelwidget area of `mbed-drivers`.
- All new features and enhancements require documentation, tests and user guides for us to accept them. Please link each pull request to all relevant documentation and test pull requests.
- Avoid merging commmits. (Always rebase when possible.)
- Comment in the pull request on every change (rebase or new commits). This helps reviewers to be up to date with changes
- Pull requests should fix a bug, add a feature or refactor.
   The only exceptions are third-party version updates (for example, Mbed TLS or Nanostack releases for Mbed OS). These updates should provide Mbed OS release notes in the pull request description, or link to an external changelog or release notes.
- Smaller pull requests are easier to review and faster to integrate. Use dependencies – split your work by pull request type or functional changes. To add a third-party driver, send it in a separate pull request, and add it as a dependency to your pull request.

If commits do not follow the above guidelines, we may request that you modify the commit history (often to add more details to address _what_ and _why_ rather than _how_).

### Release versioning

[How We Release Arm Mbed OS](../introduction/versions-and-releases.html) explains Mbed OS versioning.

## Pull request template

The following template is automatically provided when you raise a pull request against `mbed-os`. The details required depend on the type of pull request you create:

    ## Description (*required*)

    #### Summary of change (*What the change is for and why*)

    ###### Impact of changes

    ###### Migration actions required

    #### Documentation (*Details of any document updates required*)


    ----------------------------------------------------------------------------------------------------------------
    ## Pull request type (*required*)

        [] Patch update (Bug fix / Target update / Docs update / Test update / Refactor)
        [] Feature update (New feature / Functionality change / New API)
        [] Major update (Breaking change E.g. Return code change / API behaviour change)

    ----------------------------------------------------------------------------------------------------------------
    ## Test results (*required*)

        [] No Tests required for this change (E.g docs only update)
        [] Covered by existing mbed-os tests (Greentea or Unittest)
        [] Tests / results supplied as part of this PR


    ----------------------------------------------------------------------------------------------------------------
    ## Reviewers (*optional*)

    ----------------------------------------------------------------------------------------------------------------
    ## Release Notes (*required for feature/major PRs*)

### Description field

There are two parts to the description, both of which are required:

- The summary of the pull request clearly states the reason for the PR and what the changes involve.
- The documentation section requires you to state what, if any, documentation changes need to accompany the code changes.

### Pull request type

There are three pull request types, and these correspond to the three main categories specified in semantic versioning: patch, feature (minor) and major.

#### Patch update

This can contain any of the following changes:

##### Bug Fix

A bug fix is a change that fixes a specific defect in the codebase with backward compatibility. These are the highest priority because of the positive effect the change will have on users developing against the same code. A bug fix should be limited to restoring the documented or proven otherwise, originally intended behavior. Every bug fix should contain a test to verify results before and after the pull request. Bug fixes are candidates for patch releases. Large, nontrivial bug fixes approaching the size of refactors run the risk of being considered refactors themselves.

##### Refactor

A refactor is a contribution that modifies the codebase without fixing a bug or changing the existing behavior. Examples of this are moving functions or variables between translation units, renaming source files or folders, scope modification for nonpublic code, documentation structure changes and test organization changes. There is always the risk that someone depended on the location or name before a refactor; therefore, these are lower in priority than bug fixes and might require detailed justification for the change. 

##### Target update

Updating target implementation (adding a new target or updating already supported target) is a change for a patch release.

A test report for the new target must be part of the pull request. The new target must pass all Mbed OS functional and system validation tests (using `mbed test` command) for the current Mbed OS major release, including all Mbed OS supported toolchains.

##### Documentation update

Documentation updates include changes to markdown files or Doxygen documentation (comment-only changes).

##### Test update

Test updates include updates to a new test unit or test case.

#### Feature update

This can be any change in the functionality, including adding a new feature, a new method or a function. Software language does not matter.

A feature contribution contains a new API, capability or behavior. It does not break backward compatibility with existing APIs, capabilities or behaviors. New feature contributions are very welcome in Mbed OS. However, because they add capability to the codebase, a new feature may introduce bugs and a support burden. New features should also come with documentation, support for most targets and comprehensive test coverage. Feature PRs are treated cautiously, and new features require a new minor version for the codebase. 

We initially implement new features on separate branches in the Mbed OS repository. Mbed OS maintainers or Mbed OS technical leads may create the new branches by following the naming convention: "feature-" prefix. A feature branch exists as long as the feature is in development; when it is ready for release, the branch will be merged back into the Mbed OS release branch. This does not happen in some cases, instead, tags are used to informally release the feature on the branch.

Each feature has a Mbed OS technical lead. This person is responsible for:

- Rebasing often to track master development.
- Reviewing any addition to the feature branch.
- Approving all feature change pull requests.

Feature branches do not need to comply with our workflow. They are an exception, along with the following: 
- Merging pull requests to feature branches by a tech lead.
- Cases where breaking CI is possible (it is recommended to fix errors but not always feasible).

#### Major update

This is for breaking changes and should be rare. A breaking change is any change that results in breaking user space. It should have strong justification for us to consider it. Often, such changes can be backward compatible, for example, deprecating the old functionality and introducing the new replacement.

A contribution containing a breaking change is the most difficult PR to get merged. Any breaking changes in a codebase can have a large negative effect on any users of the codebase. Breaking changes are always limited to a major version release.

A project technical lead and the Mbed OS technical lead must approve breaking change pull requests.

### Test results

This section is to indicate what test results, if any, are required for the PR. The three options are:

- No tests required for this change (for example, a documentation-only update).
- Changes will be tested by existing `mbed-os` tests (Greentea or Unittest).
- Tests and results will be supplied as part of this PR. For this option, post the tests and test results
  below the tick boxes.

### Reviewers

A bot automatically adds reviewers based on the files that are actually changed. It uses an internal reviewers database. However, this section gives you the option to specify additional, specific reviewers. Tag required reviewers here, such as @adbridge, @0xc0170.

### Release notes

Every pull request changing or adding functionality must fill in the "Summary of changes" section.

For major PRs, it is also compulsory to complete the "Impact of changes" and "Migration actions required".

The impact of changes must contain an analysis of effects: components affected and potential consequences for users.

The migration actions required should describe how to migrate from a previous version of the code being changed to the new version. Please include code snippets to illustrate before and after the addition or change.

The release notes section is automatically pulled into the overall release notes for a feature or major release. This should be considered when you write the entries.

# GitHub pull requests workflow

Each pull request goes through the following workflow:

<span class="images">![Pull request workflow](../../images/Workflow3.png)<span>Pull request workflow</span></span>

## Pull request states

Mergify bot drives our workflow. The mergify rules are defined in the Mbed OS repository in the .mergify.yml file. The Mbed OS maintainers are responsible for moving pull requests through the workflow states with help from the mergify bot.

Each state is time-boxed. In most cases, this is sufficient time to move to another state. The pull request can be closed if no update is provided within the time frame.

If a pull request is idle for more than two weeks, it will be closed. The author or the maintainer can reopen it at any time.

### Reviews

All pull requests must be reviewed. The Arm Mbed CI bot determines the most suitable person to review the pull request (based on the files changed) and tags that person accordingly. A PR creator can request specific reviewers by @ tagging people or teams in the *Reviewers* section of the pull request template. For example, @personA @TeamB.

Mergify dismisses a reviewer's status after any change to the pull request commit history (such as adding a new commit or rebasing). Smaller changes, such as documentation edits or rebases on top of latest master, only require additional review by maintainers. Their approval is sufficient because a team assigned as a reviewer already approved the pull request.

- Label: `needs: review`.
- Time: Three days for reviewers to leave feedback after the autoreviewer bot has added the label.

### The Continuous Integration (CI) testing

There are many [CI systems available](../contributing/ci.html) for testing Mbed OS pull requests and braches. Which CI tests we run against a particular pull request depends on the effect that it has on the code base. Irrespective of which CI tests run, Mbed OS has an all-green policy, meaning that all triggered CI jobs must pass before we merge the pull request.

- Label: `needs: CI`.
- Time: One day for CI to complete and report back results.

### Work needed

A pull request in the "work needed" state requires additional work due to failed tests, or rework as a result of the review. If a pull request is in this state, our maintainers request changes from the pull request author.

- Label: `needs: work`.
- Time: Three days for the pull request author to action the review comments.

### Ready for integration

A pull request is ready for merge after all the reviews and tests are complete.

Maintainers merge pull requests because they have write access to the main master branch. Pull request integration happens at any time of the day. This may be automated in the future.

- Label: `Ready for merge`.
- Time: One day.

### Releases

When we merge a pull request that we will publish in a patch release, we tag it with the specific patch release version. This is the release in which we first publish this pull request. For patch releases, we allow only bug fixes, new targets and enhancements to existing functionality. New features are typically published in feature releases.

The release tag has the format:

*release-version: m.f.p*

Where:

- `m` is the major release.
- `f` is the feature release.
- `p` is the patch release.

We may add additional suffixes, which could represent a release candidate, alpha or beta release or so on.

## Additional labels

We use many other labels to summarize the scope and effect of the changes:

- *needs: preceding PR* - Cannot yet be merged because it has a dependency on another pull request that needs to merge first.
- *needs: architectural review* - A major pull request or feature update that changes the architecture, and requires review from internal teams.
- *do not merge* - Contains changes that may be in a draft state and submitted purely for review, or may contain breaking changes that have not been considered.
- *devices: 'name'* - Specifically affects the named device(s).
- *component: 'name'* - Specifically affects the named component. Component names follow the structure of Mbed OS (for example `ble`, `storage`, `tls`).
- *Release review required* - Additional release version approval is required.
- *release version missing* - A merged pull request does not contain a release label; the maintainers team should fix this.
- *BREAKING-CHANGE* - This pull request introduces a breaking change.
- *mirrored* - The git2jira bot mirrored an issue to our internal Jira.
- *JIRA status:* - An internal Jira ticket status propagated to Github issues. It can be: OPEN, IN PROGRESS, CLOSED, RESOLVED or REOPENED.
- *closed in jira* - Mirrored internal Jira issue was closed.
- *Manually patch* - A pull request needs manual cherry-picking for the release candidate to resolve conflicts.
- *risk: x* - The pull request risk level. Options are green, amber or red.
- *open for community contributions* - Arm does not intend to fix this issue in the near future.
- *mirror internally* - This pull request will be manually mirrored to our internal Jira.

The following labels summarize the scope of the pull request:

- *scope: bug-fix*.
- *scope: feature*.
- *scope: new-target*.
- *scope: refactor*.

### Documentation contribution labels

The [documentation repository](https://github.com/ARMmbed/mbed-os-5-docs) uses some of the same labels that the `mbed-os` repository does. In addition, it includes: 

- *code dependency* - The feature or change this pull request describes has not yet merged into `master` in `mbed-os`. Even if all the required reviewers have reviewed and approved this pull request, it must wait to merge until its code does.
- *wait to merge* - This pull request is a work in progress and is not yet ready for full review. 
- *Scripting work - not for writers* - This issue requires a change too large or frequent for us to do manually. Instead, a script needs to be created to fix this issue.
- *help wanted* - The documentation team does not know how to answer this question and welcomes help in answering it.

## Deprecated repositories

If repository contains the following note in Readme.md, it was archived (read-only). The repository is no longer maintained.

```
## Deprecation note!

**Please note: This repository is deprecated and it is no longer actively maintained**.
```

To deprecate a repository, please do:

1. Add deprecation note to Readme.md in the repository. 
1. Add "DEPRECATED:" to "About" section (it is useful in Github search).
1. Set repository to read only (Github archive option).
1. Update references in our CI or documentation (deprecation notice or updated references to available replacement).

