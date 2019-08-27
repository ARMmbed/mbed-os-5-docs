# Installers

The installers are a great way to get started with Mbed OS:

- [Windows installer](https://github.com/ARMmbed/mbed-cli-windows-installer/releases/latest).
- [macOS installer](https://github.com/ARMmbed/mbed-cli-osx-installer/releases/latest).

There is no installer for Linux; please follow the manual installation guide.

<span class="notes">**Note:** The GNU Arm embedded toolchain (GCC) is bundled with the installers. If you want to compile using the Arm Compiler or IAR, visit the [supported compilers page](../tools/index.html#compiler-versions).</span>

# Manual installation

## 1. Install dependencies

### Instructions for Windows

1. Download and install [Python 2.7.x](https://www.python.org/downloads/windows/) (which includes `pip`).
1. Download and install [Git](https://git-scm.com/downloads) (versions 1.9.5 or later are supported).
1. Download and install [Mercurial](https://www.mercurial-scm.org/downloads) (versions 2.2.2 or later are supported).

### Instructions for macOS

1. macOS 10.8 and later comes with Python 2.7 preinstalled.

   - If you are using the preinstalled version but need to install `pip`, you can run the following command (taken from the [pip installation guide](https://pip.pypa.io/en/stable/installing/)):
   
      ```
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        python get-pip.py
      ```
      
   - If you are running an earlier version of macOS, download and install [Python from the official website](https://www.python.org/downloads/mac-osx/). This package includes `pip`.

1. Download and install [Git](https://git-scm.com/downloads) (versions 1.9.5 or later are supported).
1. Download and install [Mercurial](https://www.mercurial-scm.org/downloads) (versions 2.2.2 or later are supported).

### Instructions for Linux

Linux distributions typically manage software through package managers. The specific commands to install the dependencies will vary depending on your distribution. Please see your distribution's documentation for more information.

As an example, the following is a command to install all dependencies on Ubuntu:

```
sudo apt install python2.7 python-pip git mercurial
```

## 2. Install Mbed CLI

<span class="notes">**Note:** We suggest you install Mbed CLI from within a virtual environment and run all commands from within your virtual environment. This will ensure that changes made by the Mbed CLI installation do not propagate to the rest of your system and cause unexpected changes in behavior in any existing Python installation.</span>

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

### Configure compiler location with Mbed CLI

If you cannot place the compiler in the system PATH, or if you have to use a different version of the compiler than the one in your system path, you must configure the location of the compiler with Mbed CLI. Use the `mbed config` command to set the compiler's location:

```
$ mbed config -G ARM_PATH "C:\Program Files\ARM"
[mbed] C:\Program Files\ARM now set as global ARM_PATH
```

The `-G` argument sets the location globally, so that it applies to all projects. You can omit the argument if you are configuring a compiler location for a specific project.

Mbed CLI supports a setting for each toolchain path:

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

### Install compilers in the system PATH

Installing the compilers in the system PATH will allow the tools to automatically discover the compilers without further configuration. Most compiler installers have an option to add the compiler to the system PATH for you.

## Optional configuration

### Bash completion

To install `mbed-cli` bash completion:

1. Clone the Mbed CLI repository: `git clone https://github.com/ARMmbed/mbed-cli`.
1. Navigate to the `mbed-cli/tools/bash_completion` directory.
1. Copy the `mbed` script into the  `~/.bash_completion.d` directory (you may need to create this directory first).
1. Restart the terminal.

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
