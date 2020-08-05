# New tools - draft

<!--well this is a disaster-->

Here be an introduction
<!--The new Mbed Tools

The existing [Mbed Tools](https://pypi.org/project/mbed-cli/) have a number of limitations. Please refer to the [blog](Blog from Jaeden) for additional information. Due to those limitations, legacy Mbed Tools cannot be extended to support cmake based build system, without additional maintenance overhead. Therefore we took the drastic decision to rewrite the tools [Mbed Tools](https://pypi.org/project/mbed-tools/) (being sure to leverage existing open source tools as far as possible to reduce maintenance costs).

Current plan is to roll-out new [Mbed Tools](https://pypi.org/project/mbed-tools/) with Mbed OS 7.0 release which will contain the cmake related changes. The new [Mbed Tools](https://pypi.org/project/mbed-tools/) will not support Mbed OS versions prior to 7.x. Therefore new [Mbed Tools](https://pypi.org/project/mbed-tools/) **MUST** be used to build Mbed OS 7.x. The "legacy" [Mbed Tools](https://pypi.org/project/mbed-cli/) **MUST** be used to build Mbed OS versions prior to Mbed OS 7.x. It'll be possible to run both `mbed-cli` and `mbedtools` side-by-side without any python virtual environment. But we strongly recommend running `mbedtools` in virtual environment created with [pipenv](https://pypi.org/project/pipenv/).

<!--the blog says "The new tools will support only the forthcoming Mbed OS 6 and versions that follow. Mbed 5.x users should continue using the existing legacy tools." whereas the text here says 7.x and newer. Which is it?-->
-->

# Install or upgrade

## Prerequisite

- Python 3. Install for [Windows](https://docs.python.org/3/using/windows.html), [Linux](https://docs.python.org/3/using/unix.html) or [macOS](https://docs.python.org/3/using/mac.html).
- Pip (if not included in your Python installation). [Install for all operating systems](https://pip.pypa.io/en/stable/installing/).
- cmake. [Install for all operating systems](https://cmake.org/install/).
- [Ninja]. [Install for all operating systems](https://github.com/ninja-build/ninja/wiki/Pre-built-Ninja-packages).

## Install Mbed Tools with pip

<span class="tips">**Tip:** We recommend using a virtual environment such as [Pipenv](https://github.com/pypa/pipenv/blob/master/README.md) to avoid Python dependency conflicts.</span>

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
