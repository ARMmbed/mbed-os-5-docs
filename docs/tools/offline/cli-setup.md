## Setup options

You can install Mbed CLI on Windows, Linux and Mac OS X.

<span class="tips">If you're working on Windows, we recommend you use the [Windows installer for Mbed CLI](#windows-installer-for-mbed-cli). For Linux and Mac OS X, refer to the section [Installing Mbed CLI standalone stable version](#installing-mbed-cli-standalone-stable-version)</span>

## Requirements

- **Python:** Mbed CLI is a Python script, so you'll need Python to use it:
    - We test Mbed CLI with <a href="https://www.python.org/downloads/release/python-2711/" target="_blank">version 2.7.11 of Python</a>. It is not compatible with Python 3.
    - pip.

- **Git and Mercurial:** Mbed CLI supports both Git and Mercurial repositories, and you may need libraries from both sources as you work, so please to install both:
    - <a href="https://git-scm.com/" target="_blank">Git</a> - version 1.9.5 or later.
    - <a href="https://www.mercurial-scm.org/" target="_blank">Mercurial</a> - version 2.2.2 or later.

- **Command-line compiler or IDE toolchain:** Mbed CLI invokes the <a href="https://github.com/ARMmbed/mbed-os" target="_blank">Mbed OS 5</a> tools for various features, such as compiling, testing and exporting to industry standard toolchains. To compile your code, you need either a compiler or an IDE:
    - Compilers: Arm GCC, Arm Compiler 5, IAR.
    - IDE: Keil uVision, DS-5, IAR Workbench.

    <span class="notes">**Note:** When installing the Arm Compiler 5 on a 64-bit Linux machine, you may need to also install the i386 architecture package:</span>

    ```
    $ sudo dpkg --add-architecture i386
    $ sudo apt-get update
    $ sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386
    ```

### Working with virtual environments

Mbed CLI is compatible with <a href="https://pypi.python.org/pypi/virtualenv" target="_blank">Virtual Python Environment (virtualenv)</a>.

You may want to install Mbed CLI on a virtual environment if your main environment has an unsupported Python version.


## Installing with the Windows installer

Mbed CLI for Windows installs <a href="https://github.com/ARMmbed/mbed-cli" target="_blank">Mbed CLI</a> with all requirements on Windows 7 and newer (both the 32- and 64-bit versions).

### Included components

The Windows installer for Mbed CLI includes the following components:

- **Python** - Mbed CLI is a Python script, so you need Python to use it. The installer installs <a href="https://www.python.org/downloads/release/python-2713/" target="_blank">version 2.7.13 of Python</a>. It is not compatible with Python 3.
- **Mbed CLI version 1.2.2** - <a href="https://github.com/ARMmbed/mbed-cli" target="_blank">Mbed CLI</a>.
- **Git and Mercurial** - Mbed CLI supports both Git and Mercurial repositories. Both Git and Mercurial are being installed. `git` and `hg` are added to system's PATH.
    - <a href="https://git-scm.com/" target="_blank">Git</a> - version 2.12.2.
    - <a href="https://www.mercurial-scm.org/" target="_blank">Mercurial</a> - version 4.1.1.
- **GNU Arm Embedded Toolchain** - <a href="https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads" target="_blank">GNU Embedded Toolchain for Arm</a>.
- **Mbed Windows serial port driver** - <a href="/docs/v5.7/tutorials/windows-serial-driver.html" target="_blank">serial port driver</a>.

### Running the installer

1. Download the latest executable from <a href="https://mbed-media.mbed.com/filer_public/50/38/5038849b-16a8-42f3-be7a-43d98c7a3af3/mbed_installer_v043.exe" target="_blank">`mbed-windows-installer v0.4.3`</a>.
2. Run `mbed_installer_v042.exe`.
3. Set the installation path.
4. Choose the installation type:
    - Default: Installs all components.
    - Advanced: Allows you to select components.
5. Installer installs all selected components. Close it after it finishes.

### Optional: silent install

You can execute the installer silently without user interaction. Add `/S` flag in Windows command prompt during installation.

```
$ mbed_installer_{version}.exe /S
```


4. Check <a href="https://github.com/ARMmbed/mbed-cli" target="_blank">Mbed CLI</a> for more examples.

## Installing manually

### Installing the stable version

You can get the latest stable version of Mbed CLI through pip by running:

```
$ pip install mbed-cli
```

On Linux or Mac, you may need to run with `sudo`.

### Optional: installing the development version

If you are interested in working with the development version (and perhaps contributing to Mbed CLI), clone the <a href="https://github.com/ARMmbed/mbed-cli" target="_blank">development repository</a>:

```
$ git clone https://github.com/ARMmbed/mbed-cli
```

Once cloned, you can install Mbed CLI as a Python package:

```
$ python setup.py install
```

On Linux or Mac, you may need to run with `sudo`.

### Video tutorial for manual installation

<span class="images">[![Video tutorial](https://img.youtube.com/vi/cM0dFoTuU14/0.jpg)](https://www.youtube.com/watch?v=cM0dFoTuU14)</span>

## Configuring Mbed CLI

There are some configuration that you must set before you can work with Mbed CLI.

### Mandatory: setting PATH variables

Mbed CLI requires adding the following to the system `PATH`:

- The paths for the Git and Mercurial executables (`git` and `hg`).

### Mandatory: toolchain selection

You need to tell Mbed CLI where to find the toolchains that you want to use for compiling. Mbed CLI supports the following toolchains:

- <a href="https://developer.arm.com/products/software-development-tools/compilers/arm-compiler-5/downloads" target="_blank">Arm Compiler 5</a>. Use version 5.06 of Arm Compiler 5. Versions older than 5.06 might be incompatible with the tools.
- <a href="https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads" target="_blank">GNU Arm Embedded toolchain (GCC) version 6</a>. Use version 6 of GCC Arm Embedded; version 5.0 or any older version might be incompatible with the tools.
- <a href="https://www.iar.com/iar-embedded-workbench/#!?architecture=ARM" target="_blank">IAR EWARM 7</a>. Use versions 7.70 to 7.80.x of the IAR EWARM; other versions might be incompatible with the tools.

You must inform Mbed CLI about the location of your compiler using one of the following methods.

- The Mbed CLI configuration command.
- Adding the compiler's directory to your PATH.
- Setting an environment variable.
- The `mbed_settings.py` file in the root of your program. The tools will automatically create this file if it doesn't already exist.

#### Through Mbed CLI configuration

Mbed CLI stores its own configuration about compiler locations both in project local settings, and user wide "global" settings. You may set and view these settings with the `mbed config` command. For example, you set the Arm Compiler 5 location for your user with the command:

```
$ mbed config -G ARM_PATH "C:\Program Files\ARM"
[mbed] C:\Program Files\ARM now set as global ARM_PATH
```

The `-G` switch tells Mbed CLI to set this as a global setting, allowing all projects this user owns to compile with Arm Compiler 5. You may instead set the `ARM_PATH` using a project local setting by omitting the `-G` command-line switch.

Mbed CLI supports a setting for each toolchain path. Below is a list of these settings, along with a description of what path is expected in each setting.

- `ARM_PATH`: The path to the *base* directory of your Arm Compiler installation. This should be the directory containing the directory containing the binaries for `armcc` and friends. For example, if your Arm Compiler 5 executable `armcc` is located at `/home/redacted/ARM_Compiler_5.06u5/bin/armcc`, you set `ARM_PATH` to `/home/redacted/ARM_Compiler_5.06u5`
- `IAR_PATH`: The path to the *base* directory of your IAR EWARM Compiler installation. This should be the directory containing the binaries for `iccarm` and friends. For example, if your IAR EWARM compiler executable is located at `C:/Program Files/IAR Systems/Embedded Workbench 7.5/arm/bin/iccarm.exe`, you set `IAR_PATH` to `C:/Program Files/IAR Systems/Embedded Workbench 7.5/arm`.
- `GCC_ARM_PATH`: The path to the *binary* directory of your GCC Arm Embedded Compiler installation. This should be the directory containing the binaries for `arm-none-eabi-gcc` and friends. For example, if your Gcc Arm Embedded toolchain gcc executable is in `/usr/bin/arm-none-eabi-gcc`, you set `GCC_ARM_PATH` to `/usr/bin`.

#### Compiler detection through the `PATH`

The `mbed compile` command checks your `PATH` for an executable that is part of the compiler suite in question. This check is the same as a shell would perform to find the executable on the command-line. When `mbed compile` finds the executable it is looking for, it prefaces the executable name with the path it found. Mbed CLI does not prefix any executable found for `GCC_ARM`.

#### Set environment variable

Mbed CLI also detects compilers with specially named environment variables. These environment variables are the same as their corresponding configuration variable, with a prefix of `MBED_` added. For example, when configuring Arm Compiler 5, you set the `MBED_ARM_PATH` environment variable to the base directory of your Arm Compiler 5 installation.

#### Through `mbed_settings.py`

Mbed CLI also uses `mbed_settings.py` to configure toolchains. This file must be a python module, and uses the exact same configuration variables as the Mbed CLI configuration.

<span class="notes">**Note:** Because `mbed_settings.py` contains local settings (possibly relevant only to a single OS on a single machine), you should not check it into version control.</span>

#### Optional: configuring multiple toolchains

Mbed CLI has a few rules that allow you to seamlessly switch between different versions of the same toolchain when switching between different projects. The settings described in prior sections all can configure a different version of the same toolchain. When multiple settings are available for a single toolchain, Mbed CLI picks the most specific setting. The settings, from most specific to least specific are:

 1) `mbed_settings.py`
 2) Mbed CLI Local Configuration
 3) Mbed CLI Global Configuration
 4) Environment Variables
 5) The `PATH` Environment Variable

When resolving which setting is used for an individual `mbed compile` or `mbed test` invocation, Mbed CLI picks the lowest numbered present setting.

To use a standard toolchain for general purpose development, you may use any method 3 through 5. For overriding a toolchain version for a specific project, you may use methods 1 and 2. All of these methods for configuring a toolchain may coexist.

### Optional: add Bash tab completion

To install `mbed-cli` bash tab completion:

1. Navigate to the `tools/bash_completion` directory.
1. Copy the `mbed` script into your `/etc/bash_completion.d/` or `/usr/local/etc/bash_completion.d` directory.
1. Reload your terminal.

<a href="https://github.com/ARMmbed/mbed-cli/blob/master/tools/bash_completion/install.md" target="_blank">Full documentation</a>

### Working with `mbed config`

The Mbed CLI configuration syntax is:

```
mbed config [--global] <var> [value] [--unset]
```

You can see the active Mbed CLI configuration via:

```
$ mbed config --list
[mbed] Global config:
ARM_PATH=C:\Program Files\ARM\armcc5.06
IAR_PATH=C:\Program Files\IAR Workbench 7.0\arm

[mbed] Local config (D:\temp\mbed-os-program):
No local configuration is set
```

Command options:

| Key | Name | Meaning |
| --- | --- | --- |
| `--global` | Global | Defines the default behavior of Mbed CLI across programs unless overridden by *local* settings. |
| None | Local | Any configuration done without `--global` is specific to the Mbed program. It overrides global or default Mbed CLI settings. If you do not specify a value, then Mbed CLI prints the value for this setting in the current working context. |
| `--unset` | Unset  | Remove a setting. |
| `--list` | List | List global and local configuration. |

Available configurations:

| Key | Explanation | Default value |
| --- | --- | --- |
| `target` | The default target for `compile`, `test` and `export`; an alias of `mbed target`. | No default. |
| `toolchain` | The default toolchain for `compile` and `test`; can be set through `mbed toolchain`. | No default. |
| `ARM_PATH`, `GCC_ARM_PATH`, `IAR_PATH` | Define the paths to Arm Compiler, GCC Arm and IAR Workbench toolchains. | No default. |
| `protocol` | The default protocol used for importing or cloning of programs and libraries. The possible values are `https`, `http` and `ssh`. Use `ssh` if you have generated and registered SSH keys (Public Key Authentication) with a service such as GitHub, GitLab, Bitbucket and so on. Read more about <a href="https://help.github.com/articles/generating-an-ssh-key/" target="_blank">SSH keys</a>. | Default: `https`. |
| `depth` | The *clone* depth for importing or cloning and applies only to *Git* repositories. Note that though this option may improve cloning speed, it may also prevent you from correctly checking out a dependency tree when the reference revision hash is older than the clone depth. Read more about <a href="https://git-scm.com/docs/git-clone" target="_blank">shallow clones</a>. | No default. |
| `cache` | The local path that stores small copies of the imported or cloned repositories. Mbed CLI uses it to minimize traffic and speed up future imports of the same repositories. Use `on` or `enabled` to turn on caching in the system temp path. Use `none` to turn caching off. | Default: none (disabled). |
