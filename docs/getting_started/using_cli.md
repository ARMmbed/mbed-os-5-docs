## Using mbed CLI

The basic workflow for mbed CLI is to:

1. Initialize a new repository, for either a new application (or library) or an imported one. In both cases, this action also adds the mbed OS codebase.
1. Build the application code.
1. Test your build.
1. Publish your application.

To support long-term development, mbed CLI offers source control, including selective updates of libraries and the codebase, support for multiple toolchains and manual configuration of the system.

<span class="tips">**Tip:** To list all mbed CLI commands, use `mbed --help`. A detailed command-specific help is available by using `mbed <command> --help`.</span>

### Installation

Windows, Linux and Mac OS X support mbed CLI. We're keen to learn about your experience with mbed CLI on other operating systems at the [mbed CLI development page](https://github.com/ARMmbed/mbed-cli).

#### Requirements

* **Python** - mbed CLI is a Python script, so you'll need Python to use it. We test mbed CLI with [version 2.7.11 of Python](https://www.python.org/downloads/release/python-2711/). It is not compatible with Python 3.

* **Git and Mercurial** - mbed CLI supports both Git and Mercurial repositories, so you need to install both:
    * [Git](https://git-scm.com/) - version 1.9.5 or later.
    * [Mercurial](https://www.mercurial-scm.org/) - version 2.2.2 or later.

The directories of Git and Mercurial executables (`git` and `hg`) need to be in your system's PATH.

* **Command-line compiler or IDE toolchain** - mbed CLI invokes the [mbed OS 5](https://github.com/ARMmbed/mbed-os) tools for various features, such as compiling, testing and exporting to industry standard toolchains. To compile your code, you need either a compiler or an IDE:
    * Compilers: GCC ARM, ARM Compiler 5, IAR.
    * IDE: Keil uVision, DS-5, IAR Workbench.

#### Video tutorial for manual installation 

<span class="images">[![Video tutorial](http://img.youtube.com/vi/cM0dFoTuU14/0.jpg)](https://www.youtube.com/watch?v=cM0dFoTuU14)</span>

#### Installing mbed CLI

You can get the latest stable version of mbed CLI through pip by running:

```
$ pip install mbed-cli
```

On Linux or Mac, you may need to run with `sudo`.

Alternatively, you can get the development version of mbed CLI by cloning the development repository [https://github.com/ARMmbed/mbed-cli](https://github.com/ARMmbed/mbed-cli):

```
$ git clone https://github.com/ARMmbed/mbed-cli
```

Once cloned, you can install mbed CLI as a python package:

```
$ python setup.py install
```

On Linux or Mac, you may need to run with `sudo`.

<span class="tips">**Note:** mbed CLI is compatible with [Virtual Python Environment (virtualenv)](https://pypi.python.org/pypi/virtualenv). You can read more about isolated Python virtual environments [here](http://docs.python-guide.org/en/latest/).</span>

#### Uninstalling mbed CLI

To uninstall mbed CLI, run:

```
pip uninstall mbed-cli
```

#### Adding Bash tab completion

To install mbed-cli bash tab completion navigate to the `tools/bash_completion` directory. Then copy the `mbed` script into your `/etc/bash_completion.d/` or `/usr/local/etc/bash_completion.d` directory and reload your terminal.  

[Full documentation here](tools/bash_completion/install.md)

## Quickstart video

<span class="images">[![Video tutorial](http://img.youtube.com/vi/PI1Kq9RSN_Y/0.jpg)](https://www.youtube.com/watch?v=PI1Kq9RSN_Y)</span>

### Before you begin: understanding the working context and program root

mbed CLI uses the current directory as a working context, in a similar way to Git, Mercurial and many other command-line tools. This means that before calling any mbed CLI command, you must first change to the directory containing the code you want to act on. For example, if you want to update the mbed OS sources in your ``mbed-example-program`` directory:

```
$ cd mbed-example-program
$ cd mbed-os
$ mbed update master   # This will update "mbed-os", not "my-program"
```

Various mbed CLI features require a program root, which should be under version control - either [Git](https://git-scm.com/) or [Mercurial](https://www.mercurial-scm.org/). This makes it possible to switch between revisions of the whole program and its libraries, control the program history, synchronize the program with remote repositories, share it with others and so on. Version control is also the primary and preferred delivery mechanism for mbed OS source code, which allows everyone to contribute to mbed OS.

<span class="warnings">**Warning**: mbed CLI stores information about libraries and dependencies in reference files that use the `.lib` extension (such as `lib_name.lib`). Although these files are human-readable, we *strongly* advise that you don't edit these manually - let mbed CLI manage them instead.</span>

### Creating and importing programs

mbed CLI can create and import programs based on both mbed OS 2 and mbed OS 5.

#### Creating a new program for mbed OS 5

When you create a new program, mbed CLI automatically imports the latest [mbed OS release](https://github.com/ARMmbed/mbed-os/). Each release includes all the components: code, build tools and IDE exporters. 

With this in mind, let's create a new program (we'll call it `mbed-os-program`):

```
$ mbed new mbed-os-program
[mbed] Creating new program "mbed-os-program" (git)
[mbed] Adding library "mbed-os" from "https://github.com/ARMmbed/mbed-os" at latest revision in the current branch
[mbed] Updating reference "mbed-os" -> "https://github.com/ARMmbed/mbed-os/#89962277c20729504d1d6c95250fbd36ea5f4a2d"
```

This creates a new folder "mbed-os-program", initializes a new repository and imports the latest revision of the mbed-os dependency to your program tree.

<span class="tips">**Tip:** You can instruct mbed CLI to use a specific source control management system or prevent source control management initialization, by using `--scm [name|none]` option.</span>

Use `mbed ls` to list all the libraries imported to your program:

```
$ cd mbed-os-program
$ mbed ls -a
mbed-os-program (mbed-os-program)
`- mbed-os (https://github.com/ARMmbed/mbed-os#89962277c207)
```

<span class="notes">**Note**: If you want to start from an existing folder in your workspace, you can use `mbed new .`, which initializes an mbed program, as well as a new Git or Mercurial repository in that folder. </span>

#### Creating a new program for mbed OS 2

mbed CLI is also compatible with mbed OS 2 programs based on the [mbed library](https://mbed.org/users/mbed_official/code/mbed/), and it automatically imports the latest [mbed library release](https://mbed.org/users/mbed_official/code/mbed/) if you use the `--mbedlib` option:

```
$ mbed new mbed-classic-program --mbedlib
[mbed] Creating new program "mbed-classic-program" (git)
[mbed] Adding library "mbed" from "https://mbed.org/users/mbed_official/code/mbed/builds" at latest revision in the current branch
[mbed] Downloading mbed library build "f9eeca106725" (might take a minute)
[mbed] Unpacking mbed library build "f9eeca106725" in "D:\Work\examples\mbed-classic-program\mbed"
[mbed] Updating reference "mbed" -> "https://mbed.org/users/mbed_official/code/mbed/builds/f9eeca106725"
[mbed] Couldn't find build tools in your program. Downloading the mbed 2.0 SDK tools...
```

#### Creating a new program without OS version selection

You can create plain (empty) programs, without either mbed OS 5 or mbed OS 2, by using the `--create-only` option.

#### Importing an existing program

Use `mbed import` to clone an existing program and all its dependencies to your machine:

```
$ mbed import https://github.com/ARMmbed/mbed-os-example-blinky
[mbed] Importing program "mbed-os-example-blinky" from "https://github.com/ARMmbed/mbed-os-example-blinky" at latest revision in the current branch
[mbed] Adding library "mbed-os" from "https://github.com/ARMmbed/mbed-os" at rev #dd36dc4228b5
$ cd mbed-os-example-blinky
```

mbed CLI also supports programs based on mbed OS 2, which it automatically detects and which do not require additional options:

```
$ mbed import https://mbed.org/teams/mbed/code/mbed_blinky/
[mbed] Importing program "mbed_blinky" from "https://mbed.org/teams/mbed/code/mbed_blinky" at latest revision in the current branch
[mbed] Adding library "mbed" from "http://mbed.org/users/mbed_official/code/mbed/builds" at rev #f9eeca106725
[mbed] Couldn't find build tools in your program. Downloading the mbed 2.0 SDK tools...
$ cd mbed-os-example-blinky
```

You can use the "import" command without specifying a full URL; mbed CLI adds a prefix (https://github.com/ARMmbed) to the URL if one is not present. For example, this command:
 
```
$ mbed import mbed-os-example-blinky
```

is equivalent to this command:
 
```
$ mbed import https://github.com/ARMmbed/mbed-os-example-blinky
```

#### Importing from a Git or GitHub clone

If you have manually cloned a Git repository into your workspace and you want to add all missing libraries, then you can use the `deploy` command:

```
$ mbed deploy
[mbed] Adding library "mbed-os" from "https://github.com/ARMmbed/mbed-os" at rev #dd36dc4228b5
```

Don't forget to set the current directory as the root of your program:

```
$ mbed new .
```

### Adding and removing libraries

While working on your code, you may need to add another library to your application or remove existing libraries. 

Adding a new library to your program is not the same as cloning the repository. Don't clone a library using `hg` or `git`; use `mbed add` to add the library. This ensures that all libraries and sublibraries are populated as well.

Removing a library from your program is not the same as deleting the library directory. mbed CLI updates and removes library reference files. Use `mbed remove` to remove the library; don't remove its directory with `rm`.

#### Adding a library

Use `mbed add` to add the latest revision of a library:

```
$ mbed add https://developer.mbed.org/users/wim/code/TextLCD/
```

Use the `URL#hash` format to add a library from a URL at a specific revision hash:

```
$ mbed add https://developer.mbed.org/users/wim/code/TextLCD/#e5a0dcb43ecc
```

##### Specifying a destination directory

If you want to specify a directory to which to add your library, you can give an additional argument to ``add``, which names that directory. For example, If you'd rather add the previous library in a directory called "text-lcd" (instead of TextLCD):

```
$ mbed add https://developer.mbed.org/users/wim/code/TextLCD/ text-lcd
```

Although mbed CLI supports this functionality, we don't encourage it. Adding a library with a name that differs from its source repository can lead to confusion.

#### Removing a library

If at any point you decide that you don't need a library any more, you can use `mbed remove` with the path of the library:

```
$ mbed remove text-lcd
```
