# New tools - draft

<!--well this is a disaster-->

Starting with version 6.x, Mbed OS is moving from Mbed CLI to a new build tool: it's cmake-based,

You'll still need Mbed CLI for older versions of Mbed OS. You can install both tools side by side.<!--seems like Mbed CLI also requires Python 3, so there shouldn't be any issues-->


# Install or upgrade

## Prerequisite

- Python 3. Install for [Windows](https://docs.python.org/3/using/windows.html), [Linux](https://docs.python.org/3/using/unix.html) or [macOS](https://docs.python.org/3/using/mac.html).
- Pip (if not included in your Python installation). [Install for all operating systems](https://pip.pypa.io/en/stable/installing/).
- cmake. [Install for all operating systems](https://cmake.org/install/).
- Ninja [Install for all operating systems](https://github.com/ninja-build/ninja/wiki/Pre-built-Ninja-packages).
<!--are there versions for cmake and ninja?-->

## Install Mbed Tools with pip

<span class="tips">**Tip:** We recommend using a virtual environment such as [Pipenv](https://github.com/pypa/pipenv/blob/master/README.md) to avoid Python dependency conflicts.</span><!--but.... should I have put that where I told them to install Python, or is the problem that during install certain dependencies may be reinstalled?-->

- To install the latest release:

    ```
    python -m pip install mbed-tools
    ```
- To install a specific version:

    ```
    python -m pip install mbed-tools==3.1.2
    ```

- To install a pre-release or development version:

    ```
    python -m pip install mbed-tools --pre
    ```

## Upgrade Mbed Tools with pip

To upgrade your installed version (uninstall your version and install the latest version):

```
python -m pip install mbed-tools --upgrade
```
