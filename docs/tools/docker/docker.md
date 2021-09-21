# Docker use in Mbed OS

The easiest and quickest way to get a build environment setup for Mbed OS projects is through the use of Docker.

We maintain Mbed OS Docker images which includes the following tooling:
* Arm Embedded GCC Toolchain
* CMake
* Mbed CLI 1 and Mbed CLI 2
* Greentea


The Docker images are stored in [GitHub Packages](https://github.com/ARMmbed/mbed-os/pkgs/container/mbed-os-env). Corresponding Dockerfiles are maintained [on GitHub](https://github.com/ARMmbed/mbed-os/tree/master/docker_images/mbed-os-env) and [is open for contributions](https://github.com/ARMmbed/mbed-os/pulls). 

The image is built and tested for the following architectures:
* 64-bit ARM / aarch64
* 64-bit x86 / x86_64

## Using the image

### Selecting the appropriate Docker tag

The Docker images are built, tested and published by GitHub Actions. When using the Docker image, make sure you are using the appropriate Docker tag that is compatible with Mbed OS version of your project. [Design document](https://github.com/ARMmbed/mbed-os/tree/master/docs/design-documents/docker_management) contains the detailed explanation of Docker image versioning strategy. 

As a quick overview, use `ghcr.io/armmbed/mbed-os-env:mbed-os-6-latest` for Docker image compatible with released version of Mbed OS, or `ghcr.io/armmbed/mbed-os-env:latest` for Docker image compatible with `HEAD` of Mbed OS `master branch`.

### Command line

The Mbed OS Docker container can be used using Docker Desktop on any supported platform (Windows, Linux & Mac).

#### Examples

Run interactively in current directory and compile the current application:

```
git clone https://github.com/ARMmbed/mbed-os-example-blinky.git && cd mbed-os-example-blinky

docker run -i -t --mount=type=bind,source="$(pwd)",destination=/var/mbed -w /var/mbed ghcr.io/armmbed/mbed-os-env

mbed-tools deploy
mbed-tools compile -t GCC_ARM -m DISCO_L475VG_IOT01A
```

💡 When building the Mbed OS project inside Docker container with shared workspace from Docker host, there could be  performance issues as filesystem needs to be synced between Docker host and container. For better performance make sure, `gRPC FUSE for file sharing` [is enabled in Docker settings](https://www.docker.com/blog/deep-dive-into-new-docker-desktop-filesharing-implementation/).

### Continuous integration

We are in the process of moving our CI to use the GitHub Actions, and this can provide a great basis for your own CI for your Mbed-based projects.

#### Examples

For a real-life example you can check out the [GitHub Actions workflow](https://github.com/ARMmbed/mbed-os-example-blinky/blob/master/.github/workflows/main.yml) for the Mbed OS Blinky example.


## Limitations

### Running GreenTea against USB devices in Docker Container

There are various limitations with connecting USB devices to a Docker container. Depending on the host machines, complexity to setup such environment will vary. On Mac, you will need to capture the device first in the underlying VM.

For this reason, running GreenTea from the Docker container is not trivial at the moment! We will be looking at future-proof solutions.

Having said that, if you are running Docker container in Linux host machine, you will be able to connect and run GreenTea tests by following these steps:

```bash
git clone https://github.com/ARMmbed/mbed-os && cd mbed-os
sudo docker run -it --privileged -v "$(pwd)":/var/mbed -v /dev/disk/by-id:/dev/disk/by-id -v /dev/serial/by-id:/dev/serial/by-id -v /run/udev:/run/udev:ro -w /var/mbed ghcr.io/armmbed/mbed-os-env
```

Then you will have a container with an Mbed OS development environment.
To make sure your Mbed targets have been detected, you might want to manually run the mount command and `mbedls` to check

```bash
mount /dev/sdb /mnt
mbedls
```
If `mbedls` detected  your connected target, then you should be able to run Mbed tests/examples as recommended in the Mbed documentation.
``` bash
mbed test -t GCC_ARM -m <target> 
```
