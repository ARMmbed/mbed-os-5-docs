# Bootloader configuration

This page describes each bootloader configuration parameter in detail. For a guide on using the managed and unmanaged bootloader modes, please see [the bootloader tutorial](../tutorials/bootloader.html).

The following configuration parameters affect the location of an application in ROM:

- `target.mbed_app_start`
- `target.mbed_app_size`
- `target.bootloader_img`
- `target.restrict_size`
- `target.header_format`
- `target.header_offset`
- `target.app_offset`

All of these parameters are valid in `targets.json`, `mbed_lib.json` and `mbed_app.json`. You may define them for individual targets and the wildcard target, `*`. A parameter in `mbed_lib.json` overrides a parameter in `targets.json`, and a parameter in `mbed_app.json` overrides one in `mbed_lib.json`.

The presence of any of these parameters defines `APPLICATION_ADDR` and `APPLICATION_SIZE` for C and C++ and `MBED_APP_START` and `MBED_APP_SIZE` for the linker.

## target.mbed_app_start

This parameter defines the start address of your application. You are responsible for the alignment of this address with respect to the flash layout and vector table size of the MCU you are using. When not used in conjunction with `target.mbed_app_size`, the application being built uses the remainder of ROM.

The value of this parameter is available to C and C++ as `APPLICATION_ADDR` and to the linker as `MBED_APP_START`.

This configuration parameter conflicts with `target.bootloader_img` and `target.restrict_size`.

## target.mbed_app_size

This parameter defines the size of your application. You may use `target.mbed_app_start` in conjunction with this parameter to set the start address, as well as the size. When `target.mbed_app_start` is not present, the application starts at the beginning of ROM. You are responsible for the alignment of the end address of the application with respect to the flash layout and vector table size of the MCU you are using.

The value of this parameter is available to C and C++ as `APPLICATION_SIZE` and to the linker as `MBED_APP_SIZE`.

This parameter conflicts with `target.bootloader_img` and `target.restrict_size`.

## target.bootloader_img

This parameter defines the bootloader image to be used during the built-in postbuild merge process. The path specified in `target.bootloader_img` is relative to the configuration file that overrides it. `target.bootloader_img` implicitly defines the start of the current application's code segment by taking the size of the bootloader and rounding up to the next flash erase block boundary. The built-in postbuild merge process automatically combines the current application with the image this parameter references.

The start address of the current application, as computed above, is available to C and C++ as `APPLICATION_ADDR` and to the linker as `MBED_APP_START`. The size of the current application is available as `APPLICATION_SIZE` and `MBED_APP_SIZE`. This parameter also defines `BOOTLOADER_ADDR` and `BOOTLOADER_SIZE` as the start address and size of the provided bootloader.

You may use this parameter in conjunction with `target.restrict_size`, `target.header_format`, `target.header_offset` and `target.app_offset`. It conflicts with `target.mbed_app_start` and `target.mbed_app_size`. When you use it with `target.restrict_size`, that parameter defines the size of the application. Otherwise, the size is the remainder of ROM.

## target.restrict_size

This parameter restricts the size of the application to be at most the specified size rounded down to the nearest integer multiple of flash erase blocks. When `target.bootloader_img` is present, the start of the current application's code segment is computed as above; otherwise, the start address is the beginning of ROM. The postbuild merge process pads the resulting bootloader binary to its end address.

The start address of the current application, as computed above, is available to C and C++ as `APPLICATION_ADDR` and to the linker as `MBED_APP_START`. The size of the current application is available as `APPLICATION_SIZE` and `MBED_APP_SIZE`. This parameter also defines `POST_APPLICATION_ADDR` and `POST_APPLICATION_SIZE` as the start address and size of the region after the application.

You may use this parameter in conjunction with `target.bootloader_img`, `target.header_format`, `target.header_offset` and `target.app_offset`. It conflicts with `target.mbed_app_start` and `target.mbed_app_size`. When used with `target.bootloader_img`, that parameter defines the start of the application. Otherwise, the start is the start of ROM.

## target.header_format

The `target.header_format` configuration key defines an application header as a list of tuples. Each tuple represents a single element of the header format as a name (a valid C identifier), a type, a subtype and finally a single argument. For example, the const type defines subtypes for common sizes of constants, including the 32be subtype that indicates the constant is represented as 32-bit big endian. The following is a list of all types and subtypes that the Mbed OS build tools support.

- `const` A constant value.
    - `8be` A value represented as 8 bits.
    - `16be` A value represented as 16 bits big endian.
    - `32be` A value represented as 32 bits big endian.
    - `64be` A value represented as 64 bits big endian.
    - `8le` A value represented as 8 bits.
    - `16le` A value represented as 16 bits little endian.
    - `32le` A value represented as 32 bits little endian.
    - `64le` A value represented as 64 bits little endian.

- `timestamp` A time stamp value in seconds from epoch in the timezone GMT/UTC. The argument to this type is always null.
    - `64be` A time stamp value truncated to 64 bits big endian.
    - `64le` A time stamp value truncated to 64 bits little endian.

- `digest` A digest of an image. All digests are computed in the order they appear. A digest of the header digests the header up to its start address.
    - `CRCITT32be` A big endian 32-bit checksum of an image with an initial value of `0xffffffff`, input reversed, and output reflected.
    - `CRCITT32le` A little endian 32bit checksum of an image with an initial value of `0xffffffff`, input reversed, and output reflected.
    - `SHA256` A SHA-2 using a block-size of 256 bits.
    - `SHA512` A SHA-2 using a block-size of 512 bits.

- `size` The size of a list of images, added together.
    - `32be` A size represented as 32 bits big endian.
    - `64be` A size represented as 64 bits big endain.
    - `32le` A size represented as 32 bits little endian.
    - `64le` A size represented as 64 bits little endain.

The Mbed OS tools build items in the application header starting where the previous field ended; the tools build items in the header using the C "packed" struct semantics. The presence of the `target.header_format` format field defines two macros `MBED_HEADER_START`, which expands to the start address of the firmware header, and `MBED_HEADER_SIZE`, containing the size in bytes of the firmware header. The region following the application header starts at `MBED_HEADER_START + MBED_HEADER_SIZE` rounded up to a multiple of 8 bytes.

You may use this parameter in conjunction with `target.bootloader_img`, `target.restrict_size`, `target.header_offset` and `target.app_offset`. It conflicts with `target.mbed_app_start` and `target.mbed_app_size`. When used with `target.bootloader_img`, that parameter defines the start of the application. Otherwise, the start is the start of ROM.

## target.header_offset

This parameter directly assigns the offset of the beginning of the header section defined in `target.header_format`. This parameter creates space between the bootloader and application header or asserts that the bootloader is at most as big as the specified offset.

<span class="notes">**Note:** This offset is relative to the start of ROM. This is important for targets with ROM that does not start at address `0x0`.</span>

You may use this parameter in conjunction with `target.bootloader_img`, `target.restrict_size`, `target.header_format` and `target.app_offset`. It conflicts with `target.mbed_app_start` and `target.mbed_app_size`.

## target.app_offset

This parameter assigns the offset of the beginning of the application section that follows the header. This parameter creates space between the application header and the application.

<span class="notes">**Note:** This offset is relative to the start of ROM. This is important for targets with ROM that does not start at address `0x0`.</span>

You may use this parameter in conjunction with `target.bootloader_img`, `target.restrict_size`, `target.header_format` and `target.header_offset`. It conflicts with `target.mbed_app_start` and `target.mbed_app_size`.
