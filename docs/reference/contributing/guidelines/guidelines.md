## Contributing to Mbed OS

Mbed OS is an open source, device software, ecosystem for the internet of things. Contributions are an important part of the ecosystem and our goal is to make it as simple as possible to become a contributor. 

Contributions can be made to source code and documentation. Both are developed on Github. Mbed uses the same open source license for contributions (inbound) as is used for the license to the project (outbound). Our default and preferred software license is Apache License version 2.0 (Apache-2.0). 

To encourage frictionless collaboration, as well as robust, consistent, and maintainable code, we have built up a set of guidelines for contributing to Mbed. 

### Types of contributions  
 
There are a few categories a contribution may fall under. Each type has different risks and benefits. When contributing it’s important to not mix types, rather, create multiple contributions if needed. Once a contribution is accepted it will appear in the next release based on type of contribution.  

The type of contribution will impact how it is incorporated into Mbed OS, as explained [here](../contributing/workflow.html)

### How to contribute  

Mbed OS has a team of people called maintainers who will help move contributions along, providing guidance and direction. This team is responsible for helping you get your changes in, as well as controlling the overall quality and consistency of the software. Contributions are accepted in the form of pull requests. Before any contributions are accepted to any Mbed software there must be a review by at least one other developer experienced with the functionality. For contributions that span multiple functionalities, multiple reviewers may be necessary. Once reviewed the changes will be tested as part of a larger system. The testing includes but is not limited to: functional correctness, static analysis, integration with other parts of the system, code style or formatting and regressions such as code size increase or performance degredation. If any of the testing fails, more work will be needed before the contribution is accepted.

### Licensing  

A license is the contract between the author permitting the use of software to others. It specifies what you can and cannot do when receiving the software. It provides protection for both the user and owner of the software. In an Mbed project, the full terms of the license can be found in a file named LICENSE. Additionally, all source files must contain the SPDX identifier as a comment at the beginning of the file.  

Note that one repository may contain multiple, independent codebases, each with their own license. If you are integrating two libraries with different licenses, it is important that each library retains its original license. In the case of a repository having software with multiple licenses, the contribution will be made according to the license of the file the contribution modifies. By creating a pull request on GitHub, you are agreeing to license your contributions under the same license as the original code. Is commonly reffered to as "inbound=outbound". This enables contributions to happen in a quick and effortless way and encourages collaboration.  

Most Mbed OS software is licensed under a permissive license. The three most common permissive licenses are:  
- Apache 2.0  
- BSD 3-Clause  
- MIT

For new Mbed projects, we suggest adopting the Apache 2.0 license. Note that any Mbed software release under a permissive license cannot accept any code that is licensed under a "copyleft" license. Doing so would prevent us from continuing to distribute our code under the permissive license. You are welcome to use Mbed software with copyleft licenses, as long as the rules of that license are followed.  

A more detailed description on licenses can be found in the [guidelines/contributing](../contributing/guidelines/license.html).

### Tips  

- The maintainers and reviewers are your friends. At times, programming can be very personal. However, it's important to realize that we all share a common goal, and that honest feedback is constructive feedback. 
- Code consistency and maintainability is more important than functionality. The existing style of a codebase overrules any personal preference. 
- Larger contributions take longer to be accepted than smaller contributions. The best contributions are small and purposeful, achieving a single goal. You may be asked to split up a contribution if it contains multiple unrelated changes. 
- Consistency is an important aspect of a codebase. To ensure consistency in Mbed OS code, we have created contributing guidelines. Any contribution to Mbed OS needs to meet the following criteria:
    - Design and coding style: Be consistent with your changes. We define software design principles and coding style in [this document](../contributing/style.html).
    - Contributions guidance: The process and how we review contributions is described in the [workflow](../contributing/workflow.html) document.
    - Licenses: Licenses should comply with the [licenses described here](../contributing/license.html).

### Access to the ARMmbed organization on GitHub

You might require direct access to the ARMmbed organization for one of the following reasons:

- You need access to private repositories.
- You need push access to a repository.
- You are collaborating with Arm staff.

If so, you can request to become an organization member, but you must first ensure your GitHub profile meets the following requirements:

- All users must have 2 Factor Authentication enabled.
- Arm staff must have their Name, Company (Arm), Location and Arm email address publicly visible.
- All others should have their Name and Company visible. Entering your Location will help us interpret response times according to time zones.

### New repository

Each repository must contain:

- `CONTRIBUTING.md` file (similar to [Mbed OS contributing](https://github.com/ARMmbed/mbed-os/blob/master/CONTRIBUTING.md)).
- `LICENSE` file - the full license text or overview of every license in the repo with links.
- `README.md` has a license and contributing section (similar to [Mbed OS license and contributions section](https://github.com/ARMmbed/mbed-os/blob/master/README.md#license-and-contributions)).
