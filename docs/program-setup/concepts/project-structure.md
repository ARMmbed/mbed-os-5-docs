# Project structure

Every Mbed OS project is composed of a:

- Target, defined in `mbed-os/targets/targets.json` and optionally in `custom_targets.json`. See the [targets documentation](../program-setup/adding-and-configuring-targets.html) for more information about defining your custom targets for your custom boards.
- Configuration, optionally defined in `mbed_lib.json` and `mbed_app.json`. See the [configuration system documentation](../program-setup/advanced-configuration.html) for more information about configuring Mbed OS's build in libraries.
- Toolchain and build profile, which define the arguments to the compiler suite. See the build system either for [Mbed CLI 1](TODO_CMAKE: fix link here) or [Mbed CLI 2](TODO_CMAKE: fix link here) for more information about changing parameters in your C and C++ compiler.
- Resources such as C sources, C++ sources, and configuration files. See the [Mbed CLI 1](TODO_CMAKE: fix link here) or [Mbed CLI 2](TODO_CMAKE: fix link here) for more information on which files are included.
