# How We Release Arm Mbed OS

The three types of Arm Mbed OS releases are major, feature and patch.

## Major release

Major releases happen infrequently and indicate a possible change in the structure of the OS. In major releases, the first number after "Mbed OS" changes. For example, Arm Mbed OS 5.0 was a major release.

They can include:

- Incompatible functionality changes (including redesign, removal and new additions).
- Removal of deprecated functionality.

## Feature release

As their name suggests, feature releases introduce new features to the code base. Unlike major releases, feature releases are backward compatible (source compatible). The second digit in the release number indicates the feature release. For example, Mbed OS 5.1.0 indicates major version 5, feature version 1.

They can include:

- New Mbed OS features.
- New functionality (including the addition of functions, methods and classes).
- Large refactors.
- Deprecation of functionality (with an alternative functionality provided).
- Configuration changes.

## Patch release

Patch releases occur on the third Wednesday of every month. They are also backward compatible (source compatible). The last digit in the release number indicates the patch release. In Mbed OS 5.2.3, `3` shows the patch release is the third release in Mbed 5.2.

They can include:

- Bug fixes.
- Improvements to existing functionality (including target driver updates and implementation-specific improvements that don't change code flow or behavior).
- New target support.
- New tests.

Binary compatibility is not guaranteed with any release.

## The release process

Every release goes through a rigorous review and testing process. We stage changes to the `release-candidate` branch in the `mbed-os` repository.

Two weeks before each feature release, we implement a code freeze on the master branch while we produce the new release branch. Once the new branch is created, master is once again available. The release branch then goes into the release testing phase, in which we apply [our testing tools](../tools/testing.html). These tests include nightly runs through our continuous integration (CI) processes, as well as out-of-box QA. We also put our examples through this testing process. We apply no new code, except for critical bug fixes found during this period, to the release branch.

For patch releases, code freeze occurs the Thursday before the release. Patch releases also go through exporter tests and nightly CI tests.

After all tests return no errors, we release the latest updates. You can find the most recent release in the `mbed-os` repository with the `latest` tag. A release note accompanies each release. The release notes for major and feature releases are longer and give an overview of the new features. The release notes for the patch releases include only a list of changes and known issues, if applicable. You can find our release notes on [the releases page](https://os.mbed.com/releases/) and on [the blog](https://os.mbed.com/blog/).
