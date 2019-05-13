# Installers

The installers are a great way to get started with Mbed OS:

- [Windows installer](https://github.com/ARMmbed/mbed-cli-windows-installer/releases/latest).
- [macOS installer](https://github.com/ARMmbed/mbed-cli-osx-installer/releases/latest).

There is no installer for Linux; please follow the manual installation guide.

<span class="notes">**Note:** The GNU Arm embedded toolchain (GCC) is bundled with the installers. If you want to compile using the Arm Compiler or IAR, visit the [supported compilers page](../tools/index.html#compiler-versions).</span>

# Manual installation

## Dependencies

- [Python](https://www.python.org/) - we support versions 2.7.x, 3.6.x, and 3.7.x.

    We recommend using Python 2, since [Python 3 support for Mercurial is still in the early stages](https://www.mercurial-scm.org/wiki/Python3).

    <span class="notes">Python 3 is not supported for Mbed OS versions earlier than 5.9.0.</span>

- [pip](https://pip.pypa.io/en/stable/)

    <span class="notes">**Note:** Mbed CLI versions 1.5.0 and earlier are **not compatible** with `pip` version 10.0 (or newer). Please use Mbed CLI versions 1.5.1 or later with recent versions of `pip`.</span>

- [Git](https://git-scm.com/) - versions 1.9.5 or later are supported.

- [Mercurial](https://www.mercurial-scm.org/) - versions 2.2.2 or later are supported.

<span class="notes">**Note:** You need both Git and Mercurial, to ensure all applications and libraries can be retrieved.</span>

## 1. Install dependencies

<!--this is repeating the dependencies list-->

### Instructions for Windows

1. Download and install [Python](https://www.python.org/downloads/windows/) (which includes `pip`).
1. Download and install [Git](https://git-scm.com/downloads).
1. Download and install [Mercurial](https://www.mercurial-scm.org/downloads).

### Instructions for macOS
1. macOS 10.8 and later comes with Python 2.7 preinstalled.

    * If you are using the preinstalled version but need to install `pip`, you can run the following command (taken from the [pip installation guide](https://pip.pypa.io/en/stable/installing/)):
       ```
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        python get-pip.py
        ```
    * If you are running an earlier version of macOS, download and install [Python from the official website](https://www.python.org/downloads/mac-osx/). This package includes `pip`.
1. Download and install [Git](https://git-scm.com/downloads).
1. Download and install [Mercurial](https://www.mercurial-scm.org/downloads).

### Instructions for Linux

Linux distributions typically manage software through package managers. The specific commands to install the dependencies will vary depending on your distribution. Please see your distribution's documentation for more information.

As an example, the following is a command to install all dependencies on Ubuntu:

```
sudo apt install python2.7 python-pip git mercurial
```

## 2. Install Mbed CLI

To install Mbed CLI with pip:

```
pip install mbed-cli
```

To verify Mbed CLI installed correctly, run `mbed --help`.

To update Mbed CLI, run:

```
pip install -U mbed-cli
```

## 3. Install a compiler

Download and install one of the following compilers: [GCC Arm, Arm Compiler 5, Arm Compiler 6 or IAR](../tools/index.html#compiler-versions).

**Note:** When installing the Arm Compiler 5 on a 64-bit Linux system, you may also need to install the i386 architecture package. As as example on Ubuntu:

```
$ sudo dpkg --add-architecture i386
$ sudo apt-get update
$ sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386
```

## 4. Configure the compiler location

To build project, Mbed CLI needs to know where the compiler is installed. It checks three configuration options in the following order:

1. Mbed CLI config (local first, then global).
1. Environment variables.
1. System path.

<!--the order in the list is the same as the original text, but the content has been changed so that PATH is first rather than last. Why?-->

### Install compilers in the system PATH

Installing the compilers in the system PATH is most often the easiest method, as the compiler installation process will often place the executables in your system's PATH automatically.<!--often? what does it depend on?-->

<!--what was wrong with the original text

"In addition to toolchain-specific environment variables, Mbed CLI detects executables that are in your system PATH. This means that if you install a toolchain in the system PATH (different for each OS), Mbed CLI will automatically find the toolchain."

-->

### Configure compiler location with Mbed CLI

If you cannot place the compiler in the system PATH, or if you have to use a different version of the compiler than the one in your system path, you must configure the location of the compiler with Mbed CLI. Use the `mbed config` command to set the compiler's location:

```
$ mbed config -G ARM_PATH "C:\Program Files\ARM"
[mbed] C:\Program Files\ARM now set as global ARM_PATH
```

The `-G` argument sets the location globally, so that it applies to all projects. You can omit the argument if you are configuring a compiler location for a specific project.

<!--Each toolchain requires a specific directory to be used when setting the location:--> <!--I don't think this sentence improves on the original. What it implies is "each toolchain has one universally correct path no all computers everywhere" which we know isn't true. The original version was "Mbed CLI supports a setting for each toolchain path:" which isn't great, but is far less confusing.-->

Each toolchain has its own setting name, and must have a path to <!--where? some of the example paths are down to `bin`, some are to a different level. what's the rule?-->

| Toolchain | Setting name | Example binary location | Example path |
| --------- | --------- | ---------| --------- |
| Arm Compiler 5.06u6 | `ARM_PATH` | `C:\Program Files\ARM_Compiler_5.06u6\bin\armcc` | `C:\Program Files\ARM_Compiler_5.06u6` |
| Arm Compiler 6.11 | `ARMC6_PATH` | `C:\Program Files\ARMCompiler6.11\bin\armclang` | `C:\Program Files\ARMCompiler6.11\bin` |
| IAR EWARM Compiler 8.32.1 | `IAR_PATH` | `C:\Program Files\IAR Systems\Embedded Workbench 8.2\arm\bin\iccarm.exe` |  `C:\Program Files\IAR Systems\Embedded Workbench 8.2\arm`|
| GCC Arm Embedded Compiler | `GCC_ARM_PATH` |`/usr/bin/arm-none-eabi-gcc` |  `/usr/bin`|

### Configure compiler location with environment variables

You can set the location of the compiler with environment variables. Use the path listed in the previous section [Configuring compiler location with Mbed CLI](#configuring-compiler-location-with-mbed-cli).

| Toolchain | Environment variable |
| --------- | --------- |
| Arm Compiler 5 | `MBED_ARM_PATH` |
| Arm Compiler 6 | `MBED_ARMC6_PATH` |
| IAR EWARM Compiler | `MBED_IAR_PATH` |
| GCC Arm Embedded Compiler | `MBED_GCC_ARM_PATH` |

## Optional configuration

### Bash completion

To install `mbed-cli` bash completion:

1. Clone the Mbed CLI repository: `git clone https://github.com/ARMmbed/mbed-cli`.
1. Navigate to the `mbed-cli/tools/bash_completion` directory.
1. Copy the `mbed` script into the  `~/.bash_completion.d` directory (you may need to create this directory first).
1. Restart the terminal

# Configuration options

The Mbed CLI configuration syntax is:

```
mbed config [--global] <var> [value] [--unset]
```

To see the active Mbed CLI configuration:

```
$ mbed config --list
[mbed] Global config:
ARM_PATH=C:\Program Files\ARM\armcc5.06
IAR_PATH=C:\Program Files\IAR Workbench 7.0\arm

[mbed] Local config (D:\temp\mbed-os-program):
No local configuration is set
```

Command options:

| Option | Explanation |
| --- | --- |
| `--global` | Defines the default behavior of Mbed CLI across all applications, unless overridden by *local* settings. |
| None | Any configuration done without `--global` is specific to a single Mbed application. It overrides global or default Mbed CLI settings. If you do not specify a value, then Mbed CLI prints the value for this setting in the current working context. |
| `--unset` | Remove a setting. |
| `--list` | List global and local configuration. |

Available configurations:

| Option | Explanation | Default value |
| --- | --- | --- |
| `target` | The default target for `compile`, `test` and `export`; an alias of `mbed target`. | No default. |
| `toolchain` | The default toolchain for `compile` and `test`; can be set through `mbed toolchain`. | No default. |
| `ARM_PATH`, `ARMC6_PATH`, `GCC_ARM_PATH`, `IAR_PATH` | Define the paths to Arm Compiler, GCC Arm and IAR Workbench toolchains. | No default. |
| `protocol` | The default protocol used for importing or cloning programs and libraries. The possible values are `https`, `http` and `ssh`. Use `ssh` if you have generated and registered SSH keys (Public Key Authentication) with a service such as GitHub, GitLab, or Bitbucket. For more information, see [SSH keys on GitHub](https://help.github.com/articles/generating-an-ssh-key/). | Default: `https`. |
| `depth` | The *clone* depth for importing or cloning. Applies only to *Git* repositories. Note that though this option may improve cloning speed, it may also prevent you from correctly checking out a dependency tree when the reference revision hash is older than the clone depth. For more information, see [shallow clones on GitHub](https://git-scm.com/docs/git-clone). | No default. |
| `cache` | The local path that stores small copies of the imported or cloned repositories. Mbed CLI uses it to minimize traffic and speed up future imports of the same repositories. Use `on` or `enabled` to turn on caching in the system temp path. Use `none` to turn caching off. | Default: none (disabled). |
