# Contributing to Mbed OS

Mbed OS is an open source, device software ecosystem for the internet of things. Contributions are an important part of the ecosystem, and our goal is to make it as simple as possible to become a contributor.

You can make contributions to source code and documentation. We develop both on GitHub. Mbed uses the same open source license for contributions (inbound) as it uses for the the project (outbound). Our default and preferred software license is Apache License version 2.0 (Apache-2.0).

To encourage collaboration, as well as robust, consistent and maintainable code, we have built a set of guidelines for contributing to Mbed.

## How to contribute  

Mbed OS has a team of maintainers who provide guidance and direction to contributors. This team is responsible for helping you get your changes in, as well as controlling the overall quality and consistency of the software. For more information about the maintainers and their responsibilities, please see [our workflow](https://os.mbed.com/docs/development/contributing/workflow.html#mbed-os-maintainers).

We accept contributions in the form of pull requests. Each pull request must be reviewed by at least one other developer experienced with the functionality. For contributions that span multiple functionalities, multiple reviewers may be necessary. After reviews are complete, we test the changes as part of a larger system. The testing includes but is not limited to: functional correctness, static analysis, integration with other parts of the system, code style or formatting and regressions, such as code size increase or performance degredation. If any of the testing fails, more work will be needed before we accept the contribution. For more information about how to contribute, please see [our workflow](https://os.mbed.com/docs/development/contributing/workflow.html#mbed-os-maintainers).

## Types of contributions  
 
There are a few [types of contributions](../contributing/workflow.html#pull-request-types). Each type has different priorities and requirements. When contributing, it’s important not to mix types and instead to create multiple contributions if needed. The type of contribution affects how and when it is incorporated into Mbed OS.

## Licensing  

A license is the contract between the author permitting the use of software to others. It specifies what you can and cannot do when receiving the software. It provides protection for both the user and owner of the software. In an Mbed project, you can find the full terms of the license in a file named LICENSE. Additionally, all source files must contain the SPDX identifier as a comment at the beginning of the file.

Note that one repository may contain multiple, independent code bases, each with their own license. If you are integrating two libraries with different licenses, it is important that each library retain its original license. If a repository has software with multiple licenses, the contribution will be made according to the license of the file the contribution modifies. By creating a pull request on GitHub, you are agreeing to license your contributions under the same license as the original code. This is commonly referred to as "inbound=outbound". This enables contributions to happen in a quick and effortless way and encourages collaboration.  

Most Mbed OS software is licensed under a permissive license. The three most common permissive licenses are:

- Apache 2.0.
- BSD 3-Clause.
- MIT.

For new Mbed projects, we suggest adopting the Apache 2.0 license. Note that any Mbed software release under a permissive license cannot accept any code that is licensed under a "copyleft" license. Doing so would prevent us from continuing to distribute our code under the permissive license. You are welcome to use Mbed software with copyleft licenses, as long as the rules of the copyleft license are followed.

You can find a more detailed description on licenses in the [contributing guidelines](../contributing/license.html).

## Access to the ARMmbed organization on GitHub

You might require direct access to the ARMmbed organization for one of the following reasons:

- You need access to private repositories.
- You need push access to a repository.
- You are collaborating with Arm staff.

If so, you can request to become an organization member, but you must first ensure your GitHub profile meets the following requirements:

- All users must have two-factor authentication enabled.
- Arm staff must have their Name, Company (Arm) and Location publicly visible.
- All others should have their Name and Company visible. Including your Location helps us interpret response times according to time zones.

## Creating new repositories

If you create a new repository in the ARMmbed organization on GitHub, it must follow some rules. Each repository must contain a:

- `CONTRIBUTING.md` file (similar to [Mbed OS contributing](https://github.com/ARMmbed/mbed-os/blob/master/CONTRIBUTING.md)).
- `LICENSE` file, the full license text or overview of every license in the repository with links.
- `README.md` with a license and contributing section (similar to [Mbed OS license and contributions section](https://github.com/ARMmbed/mbed-os/blob/master/README.md#license-and-contributions)).

## Tips  

- The maintainers and reviewers are your friends. At times, programming can be personal. However, it's important to realize that we all share a common goal and that honest feedback is constructive feedback.
- Larger contributions take longer to be accepted than smaller contributions. The best contributions are small and purposeful, achieving a single goal. We may ask you to split up a contribution if it contains multiple unrelated changes.
- Consistency is an important aspect of a code base. To ensure consistency in Mbed OS code, we have created contributing guidelines. Any contribution to Mbed OS needs to meet the following criteria:
    - Design and coding style: Be consistent with your changes. The existing style of a code base overrules any personal preference. We define software design principles and coding style in [the style](../contributing/style.html) and [software design](../contributing/software-design.html) guidelines.
    - Contributions guidance: The [workflow](../contributing/workflow.html) document describes the contribution process and how we review contributions.
