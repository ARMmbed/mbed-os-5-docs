# Docker use in Mbed OS

The easiest and quickest way to get a build environment setup for Mbed OS projects is through the use of Docker.

We maintain an Mbed OS image which includes the following tooling:
* Arm Embedded GCC Toolchain
* CMake
* Mbed CLI 2
* Greentea
* PyOCD

Our image is maintained [on GitHub](https://github.com/ARMmbed/mbed-os-docker-images) and [is open for contributions](https://github.com/ARMmbed/mbed-os-docker-images/pulls).

<span class="notes">**Note:** Our Docker image leverages Mbed CLI 2, so only supports projects built with Mbed OS 6.4 or more recent.</span>

## Using the image
### Command line

#### Examples

Run interactively in current directory and compile the current application:

```
docker run -i -t --mount=type=bind,source="$(pwd)",destination=/var/mbed,consistency=delegated -w /var/mbed mbedos/mbed-os-env-cmake

mbed-tools compile -t GCC_ARM -m DISCO_L475VG_IOT01A
```

Build an Mbed OS application directly:

```
docker run -i -t --mount=type=bind,source="$(pwd)",destination=/var/mbed,consistency=delegated -w /var/mbed mbedos/mbed-os-env-cmake mbed-tools compile -t GCC_ARM -m DISCO_L475VG_IOT01A
```

Run GreenTea tests:



### Continuous integration

### Visual Studio Code

## Limitations

### Attaching USB Devices on Mac
Running PyOCD or GreenTea from the Docker

