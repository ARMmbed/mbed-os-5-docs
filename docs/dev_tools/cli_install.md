# mbed CLI for Windows Installer

mbed CLI for Windows installs [mbed CLI](https://github.com/ARMmbed/mbed-cli) with all requirements on Windows 7 and newer.

## Supported platforms

* Windows 7 and newer (both the 32- and 64-bit versions).

## List of components

mbed CLI for Windows installs the following components:

* **Python** - mbed CLI is a Python script, so you need Python to use it. Installers installs [version 2.7.13 of Python](https://www.python.org/downloads/release/python-2713/). It is not compatible with Python 3.
* **mbed CLI version 1.1.1** - [mbed CLI](https://github.com/ARMmbed/mbed-cli).
* **Git and Mercurial** - mbed CLI supports both Git and Mercurial repositories. Both Git and Mercurial are being installed. (`git` and `hg`) are added to system's PATH.
    * [Git](https://git-scm.com/) - version 2.12.2.
    * [Mercurial](https://www.mercurial-scm.org/) - version 4.1.1.
* **GNU ARM Embedded Toolchain** - [GNU Embedded Toolchain for ARM](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads).
* **mbed Windows serial port driver** - [serial port driver](https://developer.mbed.org/handbook/Windows-serial-configuration).

## Installation

1. Download the latest executable from [mbed-windows-installer v0.4.0](https://mbed-media.mbed.com/filer_public/27/4d/274d9cf1-ea06-4459-b4a7-90b7addd6f07/mbed_installer_v040.exe).
2. Run mbed_installer_v040.exe.
3. Set the installation path.
4. Choose the installation type:
  * Default: Installs all components.
  * Advanced: Allows you to select components.
5. Installer installs all selected components. Close it after it finishes.

### Silent install

Installer can be executed silently without user interaction. Add `/S` flag in Windows command prompt during installation. 

```
$ mbed_installer_{version}.exe /S
```

## Usage

1. Open Windows command prompt.
2. Run: 

```
$ mbed
```

3. To see help:

```
$ mbed --help
```

4. Check [mbed CLI](https://github.com/ARMmbed/mbed-cli) for more examples.

## Uninstallation

* You can install mbed CLI for Windows either from `Programs and Features` or directly by running `mbed_uninstall.exe`, which is in the installation folder.
* **Important** Uninstaller uninstalls only mbed CLI, GNU ARM Embedded Toolchain and the mbed Windows serial port driver. Python, Git and Mercurial have seperate uninstallers. You can uninstall them separately.
