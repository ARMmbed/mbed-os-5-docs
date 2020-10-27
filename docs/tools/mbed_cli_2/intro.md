# Mbed CLI 2

Starting with version 6.x, Mbed OS is moving to Mbed CLI 2. It uses Ninja as a build system, and CMake to generate the build environment and manage the build process in a compiler-independent manner.

Mbed CLI 2 parses the Mbed OS build configuration and outputs it to a format CMake can read. It also provides a user friendly interface to CMake and Ninja so you can configure, generate and execute builds with a single command.

<span class="notes">**Note:** You'll still need Mbed CLI 1 for older versions of Mbed OS (6.x and older). You can install both tools side by side.</span>
