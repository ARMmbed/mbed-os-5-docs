### Workflow

#### Contributions

All code changes and additions to Mbed OS are handled through GitHub. If you want to contribute, either by adding features or by fixing bugs, please follow the guidelines for [new features](#contributing-new-features-to-mbed-os) and [bugs](#reporting-and-fixing-bugs), and in both cases please follow the [code style guide and GitHub pull request guidelines](code_style.md).

#### Contributing new features to Mbed OS

Before contributing an enhancement (new feature, new port and so on) please [discuss it on the forums](https://developer.mbed.org/forum/) to avoid duplication of work, as we or others might be working on a related feature.

Patch contributions can only be accepted through GitHub by creating a pull request from forked versions of our repositories. This allows us to review the contributions in a user friendly and reliable way, under public scrutiny.

Please create separate patches for each concern; each patch should have a clear unity of purpose. In particular, separate code formatting and style changes from functional changes. This makes each patch’s true contribution clearer and therefore quicker and easier to review.

#### Reporting and fixing bugs

Before submitting a bug report or a bug fix, please [discuss it on the forums](https://developer.mbed.org/forum/) to avoid duplication of work, as we or others might be working on it already.

##### Bug reports (issues) on GitHub

All Mbed OS is on GitHub; please use GitHub's [issues mechanism](https://guides.github.com/features/issues/) to open a bug report directly against the relevant GitHub repository.

##### Bug fixes

Please refer to the [code contributions chapter](code_style.md).

Bug fixes must be verified by a member of the Mbed team before they're pulled into the main branch. You must therefore use GitHub to fork the repo, then submit a pull request with your changes.

The last line in your commit message description should say “Fixes #deadbeef”, where “deadbeef” is the issue number in GitHub. This allows GitHub to automatically close the issue when the commit is merged into the default branch.

#### Further reading

Please see the [code contributions chapter](code_style.md) for the guidelines to GitHub pull requests and the coding style guide.
