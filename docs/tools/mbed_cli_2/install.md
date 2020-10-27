# Install or upgrade

Mbed CLI 2 is a Python package called `mbed-tools`, so you can install it with pip.

<span class="tips">**Tip:** We recommend using a virtual environment to avoid any Python dependency conflicts. We recommend the [Pipenv](https://github.com/pypa/pipenv/blob/master/README.md) tool to manage your virtual development environment.

## Prerequisite

- Python 3.6 or newer. Install for [Windows](https://docs.python.org/3/using/windows.html), [Linux](https://docs.python.org/3/using/unix.html) or [macOS](https://docs.python.org/3/using/mac.html).
- Pip (if not included in your Python installation). [Install for all operating systems](https://pip.pypa.io/en/stable/installing/).
- CMake. [Install version 3.18.1 or newer for all operating systems](https://cmake.org/install/).
- Ninja. [Install version 1.0 or newer for all operating systems](https://github.com/ninja-build/ninja/wiki/Pre-built-Ninja-packages).
- One of the support toolchains listed [in the build tools overview](../build-tools/index.html).

## Install

Use pip to install:

- To install the latest release:

    ```
    python -m pip install mbed-tools
    ```

- To install a specific version:

    ```
    python -m pip install mbed-tools==<version number in major.minor.patch format>
    ```

- To install a pre-release or development version:

    ```
    python -m pip install mbed-tools --pre
    ```

## Upgrade

Use pip to upgrade your version:

```
python -m pip install mbed-tools --upgrade
```
