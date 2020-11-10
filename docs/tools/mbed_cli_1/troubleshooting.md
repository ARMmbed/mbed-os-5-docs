# Troubleshooting

## Missing Python dependencies

Mbed CLI attempts to automatically install missing Python dependencies. If Mbed CLI doesn't have the necessary permissions, installation fails and Mbed CLI prints out a warning and a suggested command to run with the necessary permissions:

```
Missing Python modules were not auto-installed.
The Mbed OS tools in this program require the following Python modules: <missing modules>
You can install all missing modules by running "pip install -r mbed-os/requirements.txt" in "."
```

This command installs all the dependencies listed in the [`requirements.txt`](https://github.com/ARMmbed/mbed-os/blob/master/requirements.txt) file within Mbed OS.

You can read more about requirements files and Python dependency management in the [`pip` documentation](https://pip.pypa.io/en/stable/user_guide/#requirements-files).
