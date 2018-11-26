## Windows

We recommend installing Mbed CLI with our installer. If you need more customization, you can perform a manual install.

### Prebuilt Mbed CLI installer

Download and run the [Mbed CLI Windows .exe installer](https://github.com/ARMmbed/mbed-cli-windows-installer/releases/latest).

<span class="notes">**Note:** The Windows installer installs the GNU Arm embedded toolchain. If you want to compile using Arm Compiler 5 or IAR, visit the [supported compilers page](../tools/index.html#compiler-versions).</span>

You can verify Mbed CLI installed correctly by running `mbed help` from your command-line.

### Manual installation

#### 1. Download and install prerequisites

- **Python:** Mbed CLI is a Python script, so [you'll need Python to use it](https://www.python.org/downloads/). We test Mbed CLI with Python versions 2.7.11, and with 3.6.5 and greater.

    <span class="notes">**Note:** Python 3 usage is **not compatible** with Mbed OS versions older than 5.9 and Mbed CLI toolchain versions older than 1.7.2. </span>

- **pip**.

    <span class="notes">**Note:** Mbed CLI toolchain versions older than 1.5.1 are **not compatible** with `pip` version 10.0 (or newer). Please use the latest Mbed CLI with newer version of `pip`.</span>

- **Git and Mercurial:** Mbed CLI supports both Git and Mercurial repositories, and you may need libraries from both sources as you work, so please install both:
    - [Git](https://git-scm.com/) - version 1.9.5 or greater.
    - [Mercurial](https://www.mercurial-scm.org/) - version 2.2.2 or greater.

**Optional: Using a virtual environments**

If your main environment has an unsupported Python version, you may want to install Mbed CLI on a virtual environment. Mbed CLI is compatible with [Virtual Python Environment (virtualenv)](https://pypi.python.org/pypi/virtualenv).

#### 2. Install a compiler

Download and install one of the following compilers: GCC Arm, Arm Compiler 5, Arm Compiler 6 or IAR. To download the latest toolchains, visit the [supported compilers page](../tools/index.html#compiler-versions).

#### 3. Install Mbed CLI

To install Mbed CLI, run `pip install mbed-cli` from your command-line.

You can verify Mbed CLI installed correctly by running `mbed --version`.

#### 4. Set up the environment

After installation is complete, be sure to add any available toolchains to Mbed CLI's global configuration. Below is an example using the ARM compiler:

```
> mbed config -G ARM_PATH <path to ARM bin\>"
[mbed] <path to ARM bin\> now set as global ARM_PATH

> mbed config --list
[mbed] Global config:
ARM_PATH=<path to ARM bin\>

```

<span class="notes">**Note:** You can also apply the same configuration to the IAR and GNU toolchains using `IAR_PATH` or `GCC_ARM_PATH`.</span>

## macOS

We recommend installing Mbed CLI with our installer. If you need more customization, you can perform a manual install.

### Prebuilt Mbed CLI installer

Download and run the [macOS installer for Mbed CLI](https://github.com/ARMmbed/mbed-cli-osx-installer/releases/latest).

### Manual installation


#### 1. Download and install prerequisites

- **Python:** Mbed CLI is a Python script, so [you'll need Python to use it](https://www.python.org/downloads/). We test Mbed CLI with Python versions 2.7.11, and with 3.6.5 and greater.

    macOS 10.8+ comes with Python 2.7 preinstalled by Apple. If you are running an earlier version of macOS, download and install [Python versions 2.7.11 or 3.6.5](https://www.python.org/downloads/mac-osx/) or later.

    <span class="notes">**Note:** Python 3 usage is **not compatible** with Mbed OS versions older than 5.9 and Mbed CLI toolchain versions older than 1.7.2. </span>

- **pip**.

    To install Pip, run `easy_install --user pip` from your command-line.

    <span class="notes">**Note:** Mbed CLI toolchain versions older than 1.5.1 are **not compatible** with `pip` version 10.0 (or newer). Please use the latest Mbed CLI with newer version of `pip`.</span>

- **Git and Mercurial:** Mbed CLI supports both Git and Mercurial repositories, and you may need libraries from both sources as you work, so please install both:
    - [Git](https://git-scm.com/) - version 1.9.5 or greater.
    - [Mercurial](https://www.mercurial-scm.org/) - version 2.2.2 or greater.

**Optional: Using a virtual environments**

If your main environment has an unsupported Python version, you may want to install Mbed CLI on a virtual environment. Mbed CLI is compatible with [Virtual Python Environment (virtualenv)](https://pypi.python.org/pypi/virtualenv).


#### 2. Install a compiler

Download and install one of the following compilers: GCC Arm, Arm Compiler 5, Arm Compiler 6 or IAR. To download the latest toolchains, visit the [supported compilers page](../tools/index.html#compiler-versions).

#### 3. Install Mbed CLI

To install Mbed CLI, run `pip install mbed-cli --user` from your command-line.

You can verify Mbed CLI installed correctly by running `mbed --version`.

<span class="notes">**Note:** You may also need to add the new Mbed CLI Python `--user` installation location (for example: `/Users/{username}/Library/Python/2.7/bin`) to the PATH.</span>

#### 4. Set up the environment

For any installed toolchain, be sure to add the Mbed CLI global configuration:

```
$ mbed config -G ARM_PATH <path to ARM bin\>"
[mbed] <path to ARM bin\> now set as global ARM_PATH

$ mbed config --list
[mbed] Global config:
ARM_PATH=<path to ARM bin\>

```

<span class="notes">**Note:** You can also apply the same configuration to the IAR and GNU toolchains using `IAR_PATH` or `GCC_ARM_PATH`.</span>

## Linux


#### 1. Download and install prerequisites

- **Python:** Mbed CLI is a Python script, so [you'll need Python to use it](https://www.python.org/downloads/). We test Mbed CLI with Python versions 2.7.11, and with 3.6.5 and greater.

    You can download and install Python, or use your package manager. For example, you can use the following in Ubuntu (note that it includes pip, the following item on our list):

    ```console
    $ sudo apt-get install python2.7 python-pip
    ```

    <span class="notes">**Note:** Python 3 usage is **not compatible** with Mbed OS versions older than 5.9 and Mbed CLI toolchain versions older than 1.7.2. </span>

- **pip**.

    To install Pip, run `easy_install --user pip` from your command-line.

    <span class="notes">**Note:** Mbed CLI toolchain versions older than 1.5.1 are **not compatible** with `pip` version 10.0 (or newer). Please use the latest Mbed CLI with newer version of `pip`.</span>

- **Git and Mercurial:** Mbed CLI supports both Git and Mercurial repositories, and you may need libraries from both sources as you work, so please install both:
    - [Git](https://git-scm.com/) - version 1.9.5 or greater.
    - [Mercurial](https://www.mercurial-scm.org/) - version 2.2.2 or greater.

**Optional: Using a virtual environments**

If your main environment has an unsupported Python version, you may want to install Mbed CLI on a virtual environment. Mbed CLI is compatible with [Virtual Python Environment (virtualenv)](https://pypi.python.org/pypi/virtualenv).

### 2. Install a compiler

Download and install one of the following compilers: GCC Arm, Arm Compiler 5, Arm Compiler 6 or IAR. To download the latest toolchains, visit the [supported compilers page](../tools/index.html#compiler-versions).

<span class="notes">**Note:** When installing the Arm Compiler 5 on a 64-bit Linux machine, you may also need to install the i386 architecture package:</span>

    ```
    $ sudo dpkg --add-architecture i386
    $ sudo apt-get update
    $ sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386
    ```

### 3. Install Mbed CLI

To install Mbed CLI, run `pip install mbed-cli` from your command-line.

You can verify Mbed CLI installed correctly by running `mbed help`.

### 4. Set up the environment

For any installed toolchain, be sure to add the Mbed CLI global configuration:

```
$ mbed config -G ARM_PATH <path to ARM bin\>"
[mbed] <path to ARM bin\> now set as global ARM_PATH

$ mbed config --list
[mbed] Global config:
ARM_PATH=<path to ARM bin\>

```

<span class="notes">**Note:** You can also apply the same configuration to the IAR and GNU toolchains using `IAR_PATH` or `GCC_ARM_PATH`.</span>

## After installation - configuring Mbed CLI

Mbed CLI will not work properly without some manual configuration.

### Mandatory: setting PATH variables

Add the following to the system `PATH`:

- The paths for the Git and Mercurial executables (`git` and `hg`).

### Mandatory: setting compiler location

You must inform Mbed CLI about the location of your compiler using one of the following methods:

- The Mbed CLI configuration command.
- Adding the compiler's directory to your PATH.
- Setting an environment variable.
- The `mbed_settings.py` file in the root of your program. The tools<!--which tools?--> will automatically create this file if it doesn't already exist.

<span class="tips">**Tip:** You may configure more than one toolchain. However, you may only use one toolchain at a time. For more information, see [the multiple toolchains section below](#optional-configuring-multiple-toolchains)</span>

<!--this comment should be in the index page with the other tool information, if at all.
When using C++98 and GNU C99, the only difference between the toolchains is performance.
-->

#### Method 1: Mbed CLI configuration

Mbed CLI stores its own configuration about compiler locations in both project local settings and user wide global settings. You may set and view these settings with the `mbed config` command. For example, set the Arm Compiler 5 location for your user with the command:

```
$ mbed config -G ARM_PATH "C:\Program Files\ARM"
[mbed] C:\Program Files\ARM now set as global ARM_PATH
```

The `-G` switch tells Mbed CLI to set this as a global setting, allowing all projects your user owns to compile with Arm Compiler 5. If you want only a local setting for `ARM_PATH`, omit the `-G` switch.

Mbed CLI supports a setting for each toolchain path. Below is a list of these settings, along with a description of what path is expected in each setting:

<!--this strikes me as using way more words than it needs to-->
- `ARM_PATH`: The path to the *base* directory of your Arm Compiler 5 installation. This should be the directory containing the binaries for `armcc`. For example, if your Arm Compiler 5 executable `armcc` is located at `/home/redacted/ARM_Compiler_5.06u5/bin/armcc`, you set `ARM_PATH` to `/home/redacted/ARM_Compiler_5.06u5`
- `ARMC6_PATH`: The path to the *binary* directory of your Arm Compiler 6 installation. This should be the directory containing the binaries for `armclang`. For example, if your Arm Compiler 6 executable `armclang` is located at `C:/Program Files/ARM/armcc6.10/bin/armclang`, you set `ARMC6_PATH` to `C:/Program Files/ARM/armcc6.10/bin`
- `IAR_PATH`: The path to the *base* directory of your IAR EWARM Compiler installation. This should be the directory containing the binaries for `iccarm`. For example, if your IAR EWARM compiler executable is located at `C:/Program Files/IAR Systems/Embedded Workbench 7.5/arm/bin/iccarm.exe`, you set `IAR_PATH` to `C:/Program Files/IAR Systems/Embedded Workbench 7.5/arm`.
- `GCC_ARM_PATH`: The path to the *binary* directory of your GCC Arm Embedded Compiler installation. This should be the directory containing the binaries for `arm-none-eabi-gcc`. For example, if your GCC Arm Embedded toolchain gcc<!--did we mean to use gcc twice in this sentence?--> executable is in `/usr/bin/arm-none-eabi-gcc`, you set `GCC_ARM_PATH` to `/usr/bin`.

#### Method 2: setting the PATH

The `mbed compile` command checks your `PATH` for an executable that is part of the compiler suite in question<!-- what does "in question" mean? that it was part of the compilation command?-->. This check is the same as a shell would perform to find the executable on the command-line. When `mbed compile` finds the executable it is looking for, it prefaces the executable name with the path it found. Mbed CLI does not prefix any executable found for `GCC_ARM`.<!--so what do I do in this section - set paths? This feels more like background info than instructions. And is the GCC_ARM thing part of the previous sentence, or in contradiction? what should I do with GCC_ARM, if it's in contradiction?-->

#### Method 3: environment variable

Mbed CLI detects compilers with specially named environment variables. These environment variables are the same as their corresponding configuration <!--where is the corresponding configuration variable?-->variable, with a prefix of `MBED_` added. For example, when configuring Arm Compiler 5, you set the `MBED_ARM_PATH` environment variable to the base directory of your Arm Compiler 5 installation.<!--what do I actually do in this section? And is it a standalone, or does it go with something else (since you used "also" I'm not sure)-->

#### Method 4: editing mbed_settings.py

Mbed CLI uses `mbed_settings.py` to configure toolchains. This file must be a Python module, and uses the exact same configuration variables as the Mbed CLI configuration.<!--maybe they should be methods 1 and 2, then, rather than 1 and 4-->
<!--what do I do in this? there are no instructions here, and no link to anywhere else-->

<span class="notes">**Note:** Because `mbed_settings.py` contains local settings (possibly relevant only to a single OS on a single machine), you should not check it into version control.</span>

#### Optional: configuring multiple toolchains

All the settings described in the previous sections can configure a different version of the same toolchain, and Mbed CLI has a set of rules to seamlessly switch between these versions for an individual `mbed compile` or `mbed test` invocation. Mbed CLI picks the most specific version, from most specific to least specific, in this order:

<!--I think you should organise the methods above to match this order-->

1. `mbed_settings.py`
2. Mbed CLI local configuration
3. Mbed CLI global configuration
4. Environment variables
5. The `PATH` environment variable

To use a standard toolchain for general purpose development, you may use any method from 3 to 5. To override a toolchain version for a specific project, you may use methods 1 and 2. All of these methods may coexist.

### Optional: add bash tab completion

To install `mbed-cli` bash tab completion:

1. Navigate to the `tools/bash_completion` directory.
1. Copy the `mbed` script into your `/etc/bash_completion.d/` or `/usr/local/etc/bash_completion.d` directory.
1. Reload your terminal.

[For more information, see the full documentation](https://github.com/ARMmbed/mbed-cli/blob/master/tools/bash_completion/install.md).

## Reference: Working with `mbed config`

<!--should this be here, or in another part of the CLI docs?-->

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
| `--global` | Defines the default behavior of Mbed CLI across programs, unless overridden by *local* settings. |
| None | Any configuration done without `--global` is specific to the Mbed program. It overrides global or default Mbed CLI settings. If you do not specify a value, then Mbed CLI prints the value for this setting in the current working context. |
| `--unset` | Remove a setting. |
| `--list` | List global and local configuration. |

<!--what does "Mbed program" mean? This isn't a term I've seen us use before-->

Available configurations:

| Option | Explanation | Default value |
| --- | --- | --- |
| `target` | The default target for `compile`, `test` and `export`; an alias of `mbed target`. | No default. |
| `toolchain` | The default toolchain for `compile` and `test`; can be set through `mbed toolchain`. | No default. |
| `ARM_PATH`, `GCC_ARM_PATH`, `IAR_PATH` | Define the paths to Arm Compiler, GCC Arm and IAR Workbench toolchains. | No default. |
| `protocol` | The default protocol used for importing or cloning programs and libraries. The possible values are `https`, `http` and `ssh`. Use `ssh` if you have generated and registered SSH keys (Public Key Authentication) with a service such as GitHub, GitLab, or Bitbucket. For more information, see [SSH keys on GitHub](https://help.github.com/articles/generating-an-ssh-key/). | Default: `https`. |
| `depth` | The *clone* depth for importing or cloning. Applies only to *Git* repositories. Note that though this option may improve cloning speed, it may also prevent you from correctly checking out a dependency tree when the reference revision hash is older than the clone depth. For more information, see [shallow clones on GitHub](https://git-scm.com/docs/git-clone). | No default. |
| `cache` | The local path that stores small copies of the imported or cloned repositories. Mbed CLI uses it to minimize traffic and speed up future imports of the same repositories. Use `on` or `enabled` to turn on caching in the system temp path. Use `none` to turn caching off. | Default: none (disabled). |
