## Struture of an Mbed OS project

Every Mbed OS project is composed of a:

 * Target defined in `mbed-os/targets/targets.json` and optionally in `custom_targets.json`. See the [targets documentation](/docs/tools/mbed_targets.htm) for more information.
 * Config*uration optionally defined in `mbed_lib.json` and `mbed_app.json`. See the [configuration system documentation](/docs/reference/configuration/configuration.html) for more information.
 * Toolchain and build profile define the arguments to the compiler suite. See the [build profile documentation](/docs/tools/CLI/build_profiles.html) for more information.
 * Resources such as C sources, C++ sources, and configuration files. See the [build rules documentation](/docs/tools/build_rules.html) for more information.
