### Workflow

#### Contributions

All code changes and additions to Mbed OS are handled through GitHub. If you want to contribute, either by adding features or by fixing bugs, please follow the guidelines for [new features](#contributing-new-features-to-mbed-os) and [bugs](#reporting-and-fixing-bugs), and in both cases please follow the <a href="/docs/v5.6/reference/guidelines.html#style" target="_blank">code style guide and GitHub pull request guidelines</a>.

#### Contributing new features to Mbed OS

Before contributing an enhancement (new feature, new port and so on) please <a href="https://os.mbed.com/forum/" target="_blank">discuss it on the forums</a> to avoid duplication of work, as we or others might be working on a related feature.

Patch contributions can only be accepted through GitHub by creating a pull request from forked versions of our repositories. This allows us to review the contributions in a user friendly and reliable way, under public scrutiny.

Please create separate patches for each concern; each patch should have a clear unity of purpose. In particular, separate code formatting and style changes from functional changes. This makes each patch’s true contribution clearer and therefore quicker and easier to review.

#### Reporting and fixing bugs

Before submitting a bug report or a bug fix, please <a href="https://os.mbed.com/forum/" target="_blank">discuss it on the forums</a> to avoid duplication of work, as we or others might be working on it already.

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
