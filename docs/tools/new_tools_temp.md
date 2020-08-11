# New tools - draft

<!--well this is a disaster-->

Starting with version 6.x, Mbed OS is moving from Mbed CLI to a new build tool: it's cmake-based,

You'll still need Mbed CLI for older versions of Mbed OS. You can install both tools side by side.<!--seems like Mbed CLI also requires Python 3, so there shouldn't be any issues-->


# Install or upgrade

Mbed Tools is Python based, so you can install it with pip.
<!--other than being a super vague name, it's a problem that it's a single tool with a plural name. "Mbed Tools is"  just parses as an error!-->

<span class="tips">**Tip:** We recommend using a virtual environment such as [Pipenv](https://github.com/pypa/pipenv/blob/master/README.md) to avoid Python dependency conflicts.</span>

## Prerequisite

- Python 3. Install for [Windows](https://docs.python.org/3/using/windows.html), [Linux](https://docs.python.org/3/using/unix.html) or [macOS](https://docs.python.org/3/using/mac.html).
- Pip (if not included in your Python installation). [Install for all operating systems](https://pip.pypa.io/en/stable/installing/).
- cmake. [Install version 3.18.1 or newer for all operating systems](https://cmake.org/install/).
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
