# New tools - draft

<!--this currently duplicates the intro in the general Tools Intro page-->

Starting with version 6.x, Mbed OS is moving from Mbed CLI to a new build tool: <!--that has no proper name yet-->. It uses Ninja as a build system, and CMake to generate the build environment and manage the build process in a compiler-independent manner. <!--need better phrasing-->

Mbed Tools parses the Mbed OS build configuration and outputs it to a format CMake can read. It also provides a use friendly interface to CMake and Ninja so you can configure, generte and execute builds with a single command.


<span class="notes">**Note:** You'll still need Mbed CLI for older versions of Mbed OS (6.x and older). You can install both tools side by side.</span>

# Install or upgrade

Mbed Tools is a Python package called `mbed-tools`, so you can install it with pip.
<!--other than being a super vague name, it's a problem that it's a single tool with a plural name. "Mbed Tools is"  just parses as an error!-->

<span class="tips">**Tip:** We recommend using a virtual environment to avoid any Python dependency conflicts. We recommend the [Pipenv](https://github.com/pypa/pipenv/blob/master/README.md) tool to manage your virtual development environment.

## Prerequisite

- Python 3. Install for [Windows](https://docs.python.org/3/using/windows.html), [Linux](https://docs.python.org/3/using/unix.html) or [macOS](https://docs.python.org/3/using/mac.html).
- Pip (if not included in your Python installation). [Install for all operating systems](https://pip.pypa.io/en/stable/installing/).
- CMake. [Install version 3.18.1 or newer for all operating systems](https://cmake.org/install/).
- Ninja [Install version 1.0 or newer for all operating systems](https://github.com/ninja-build/ninja/wiki/Pre-built-Ninja-packages).
<!--are there versions for cmake and ninja?-->

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

Use pip to upgrade:

```
python -m pip install mbed-tools --upgrade
```
