# Creating and publishing your own libraries and contributing to mbed OS

This chapter covers the different aspects of developing your own libraries for use in mbed devices, as well as items to keep in mind during development, like licensing. It covers:

[The mbed OS code base](#contributing-to-the-mbed-os-code-base): Use GitHub to contribute additions and bug fixes to mbed OS itself.

[//]: # (TODO add section about the index service when available)

### Licensing binaries and libraries

When you write original code you own the copyright and can choose to make it available to others under a license of your choice. A license gives rights and puts limitations on the reuse of your code by others. Not having a license means others cannot use your code. We encourage you to choose a license that makes possible (and encourages!) reuse by others. 

If you create new software, such as drivers, libraries and examples, you can apply whatever license you like as the author and copyright holder of that code. Having said that, we encourage you to use a well known license such as one of the ones listed [on spdx.org](http://spdx.org/licenses/), preferably an [OSI-approved] (https://opensource.org/licenses/alphabetical), permissive open source software license. Specifically, we recommend the following:

* For original source code, use the Apache 2.0 license.  

* For binary releases (for example, private source code you can’t or don’t want to release but want to share as a binary library and headers available for others to use), consider the [Permissive Binary License](https://www.mbed.com/licenses/PBL-1.0). This is designed to be compatible with Apache 2.0 and the mbed OS code base.

* If your software incorporates or is derived from other third party open source code, please be sure to retain all notices and identify the license for the third party licensed code in the same manner as described below. Remember, you cannot change the license on someone else’s code, because you are not the copyright holder! Instead, choose a license that is compatible with the license used by the third party open source code, or use the same license as that code. For example, if your software is derived from GPL source code, GPL requires you to license the rest of your code in that software under the GPL too. Note that many commercial users won’t be able to use GPL source code in their products, so we don't recommend this license if you're not obligated to use it. 

You must either write all the code you provide yourself, or have the necessary rights to provide code written by someone else. 

In all cases, whatever license you use, please use an [SPDX](https://spdx.org/about-spdx/what-is-spdx) [license identifier](http://spdx.org/licenses/) to make it easier for users to understand and legally review licenses.

#### When to use Apache 2.0

Apache 2.0 is a permissive, free and open source software license that allows other parties to use, modify, and redistribute the code in source and binary form. Compared to the often used BSD license, Apache 2.0 provides an express patent grant from contributors to users.

The full text of the license can be found on the [Apache website](http://www.apache.org/licenses/LICENSE-2.0). For more information about Apache 2.0, see [the FAQ](http://www.apache.org/foundation/license-faq.html).

#### How to apply Apache 2.0 correctly

In order to clearly reflect the Apache 2.0 license, please create two text files:

* A *LICENSE* file with the following text:</br>

<pre>Unless specifically indicated otherwise in a file, files are licensed under the Apache 2.0 license, 
as can be found in: LICENSE-apache-2.0.txt</pre>

* The full original [Apache 2.0 license text](http://www.apache.org/licenses/LICENSE-2.0) in *LICENSE-apache-2.0.txt*

Each source header should *start with* your copyright line, the SPDX identifier and the Apache 2.0 header as shown here:

```
Copyright (c) [First year]-[Last year], **Your Name or Company Here**
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License.

You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, 
either express or implied.

See the License for the specific language governing permissions and limitations under the License.
```

#### When to use the Permissive Binary License

The Permissive Binary License (PBL) is a permissive license based on BSD-3-Clause and designed specifically for binary blobs. It's minimal, but covers the basics, including an express patent grant.

It allows you to share a binary blob and the relevant headers, and allows others to use that binary blob as part of their product - as long as they provide it with all the relevant dependencies and don't modify it or reverse engineer it.

The full text can be found on [mbed.com](https://www.mbed.com/licenses/PBL-1.0).

#### How to apply PBL correctly

In order to clearly reflect the PBL license, please create three text files:

* A *LICENSE* file with:

<pre>Unless specifically indicated otherwise in a file, files are licensed under the Public Binary License, 
as can be found in: LICENSE-permissive-binary-license-1.0.txt</pre>

* The full original [Public Binary License 1.0 text](https://www.mbed.com/licenses/PBL-1.0) in *LICENSE-permissive-binary-license-1.0.txt*.

* A *DEPENDENCIES* file with the dependencies that this binary requires to work properly. This is to make sure that third parties integrating the binary in their own distribution are aware that they need to include the relevant dependencies. If your binary does not have any dependencies, the file should state so (that is, say “No dependencies”); don't omit this file.

Each source header should *start with* your copyright line, the SPDX identifier and the BPL header:

```
Copyright (c) [First year]-[Last year], **Your Name Here**, All Rights Reserved
SPDX-License-Identifier: LicenseRef-PBL

Licensed under the Permissive Binary License, Version 1.0 (the "License"); 
you may not use this file except in compliance with the License.

You may obtain a copy of the License at https://www.mbed.com/licenses/PBL-1.0

See the License for the specific language governing permissions and limitations under the License.
```

### Using a different license

If you decide to use a different license for your work, follow the same pattern:

* Create a *LICENSE* file with a description of the license situation, following the pattern described in the sections above.

* Put the full original license texts in separate documents named *LICENSE-XYZ.txt*, where XYZ is the corresponding [SPDX identifier](http://spdx.org/licenses/) for your license.

* Begin each source header with your copyright line, the SPDX identifier and the standard header for the license that applies to that single file, if it has one.

* If more than one license applies to the source file, then use an SPDX license expression (see Appendix IV in [this document](http://spdx.org/sites/spdx/files/SPDX-2.0.pdf)), to reflect the presence of multiple licenses in your *LICENSE* file and in each source file.

## Contributing to the mbed OS code base

### mbed OS principles

mbed OS uses these same basic principles for its source code and library distributions. So source code we own is distributed under the Apache 2.0 license and binary blobs are released under the Permissive Binary License. Software parts from third parties that were already licensed under a different license are available under that original license.

All the source code and binary blobs that end up in mbed OS are maintained in public GitHub repositories.

### Contributions

All code changes and additions to mbed OS are handled through GitHub. If you want to contribute, either by adding features or by fixing bugs, please follow the guidelines for [new features](#contributing-new-features-to-mbed-os) and [bugs](#reporting-and-fixing-bugs), and in both cases please follow the [code style guide and GitHub pull request guidelines](code_style.md).

### Licensing

If you want to contribute code to mbed OS, you must sign an mbed Contributor License Agreement (CLA). Please ask for a CLA before submitting any code (for example, while discussing the issue on GitHub), then wait for ARM to confirm acceptance of your CLA before making contributions. 

<span style="background-color:#E6E6E6;border:1px solid #000;display:block; height:100%; padding:10px">**Note:** If you publish a feature or a solution to a problem before signing the CLA, then find out that you are not able or allowed to sign the CLA, we will not be able to use your solution anymore. That may prevent us from solving the problem for you.</span>

When you ask for the CLA, we'll send you the agreement and ask you to sign it *before* we handle any pull request from you: 

* Individuals who want to contribute their own work must sign and return an Individual CLA.

* Companies that want employees to contribute on its behalf must sign and return a Corporate CLA.

The same agreement is then valid for all future pull requests from that GitHub username.  

### Contributing new features to mbed OS

Before contributing an enhancement (new feature, new port and so on) please [discuss it on the forums](https://developer.mbed.org/forum/) to avoid duplication of work, as we or others might be working on a related feature.

Patch contributions can only be accepted through GitHub by creating a pull request from forked versions of our repositories. This allows us to review the contributions in a user friendly and reliable way, under public scrutiny.

Please create separate patches for each concern; each patch should have a clear unity of purpose. In particular, separate code formatting and style changes from functional changes. This makes each patch’s true contribution clearer, and therefore quicker and easier to review.

### Reporting and fixing bugs

Before submitting a bug report or a bug fix, please [discuss it on the forums](https://developer.mbed.org/forum/) to avoid duplication of work, as we or others might be working on it already.

#### Bug reports (issues) on GitHub

All mbed OS is on GitHub; please use GitHub's [issues mechanism](https://guides.github.com/features/issues/) to open a bug report directly against the relevant GitHub repository.

#### Bug fixes

Please refer to the [code contributions chapter](code_style.md). 

Bug fixes must be verified by a member of the mbed team before they're pulled into the main branch. You must therefore use GitHub to fork the repo, then submit a pull request with your changes. 

The last line in your commit message description should say “Fixes #deadbeef”, where “deadbeef” is the issue number in GitHub. This allows GitHub to automatically close the issue when the commit is merged into the default branch.

## Further reading

Please see the [code contributions chapter](code_style.md) for the guidelines to GitHub pull requests and the coding style guide.
