*Glossary*\
NSPE - Non-Secure Processing Environment\
PSA - Platform Security Architecture\
SPE - Secure Processing Environment\
SPM - Secure Partition Manager\
TF-M - Trusted Firmware M

# PSA targets in Mbed OS

Before start reading this, please read [porting a custom
board](https://os.mbed.com/docs/mbed-os/latest/porting/porting-a-custom-board.html)
and [porting
targets](https://os.mbed.com/docs/mbed-os/latest/porting/porting-targets.html)
which provide step-by-step guide to porting a new target to Mbed OS.

This document describes the process of adding new PSA targets to Mbed OS. The
focus is more on target configurations, build and validation. Mbed OS relies on
[TF-M](https://git.trustedfirmware.org/trusted-firmware-m.git/tree/) for PSA
Services and SPM. Therefore the PSA target being added to Mbed OS **MUST**
already be supported by TF-M.

# Adding new PSA targets
To help with the creation of PSA targets, a couple of generic targets have been
added to `targets/targets.json`.
* `PSA_Target` (Root level PSA target)
* `PSA_V7_M` (Single v7-M PSA generic target)
* `PSA_DUAL_CORE` (Dual-core PSA generic target)
* `PSA_V8_M` (v8-M generic PSA target)

A single-core Armv7-M PSA target doesn't employ hardware isolation between the
NSPE and the SPE. PSA secure service emulation enables PSA API compatibility.

A dual-core PSA target will have at least two cores that are either Armv7-M or
Armv6-M. One core will be used for the SPE and another for the NSPE. Hardware
isolation between the cores enables PSA compliance. On dual-core targets, TF-M
runs on the SPE and provides PSA services and Mbed OS runs on the NSPE.

An Armv8-M PSA target employs hardware to isolate the NSPE from the SPE. On
Armv8-M targets, TF-M runs on the SPE and provides PSA services and Mbed OS
runs on the NSPE.

Only PSA NSPE generic targets have been defined for dual-core (`PSA_DUAL_CORE`)
and Armv8-M (`PSA_V8_M`) targets because TF-M build tools are used to generate
SPE binary instead of Mbed OS build tools. Therefore, it is not necessary to
define SPE target while adding a new PSA target to Mbed OS, only defining NSPE
target is sufficient.

PSA targets **MUST** inherit from the generic PSA target that corresponds to
that target's architecture. The only exception is, when a PSA target has to
inherit from one of its family targets instead of generic target `Target`.
This is due to the limited support for `multiple inheritance` in Mbed OS build
tools. The handling of exception cases are explained in detail in next
sections.

*Note*\
The examples in this document are taken from `targets/targets.json`.

Example of a single-core Armv7-M PSA target:
```json
    "K64F": {
        "inherits": ["PSA_V7_M"]
    }
```

## Naming convention for dual-core and Armv8-M target names
As described in previous paragraphs, only NSPE target name **MUST** be defined
for dual-core and Armv8-M PSA targets. For Armv8-M non-PSA targets, both SPE
and NSPE target names can be defined. This section defines the naming
convention for the same.

`TargetName`         : PSA non-secure target (NSPE)\
`TargetName_NPSA_S`  : Non-PSA secure target\
`TargetName_NPSA`    : Non-PSA non-secure target

## Adding single-core PSA targets
Mbed OS's PSA service emulation provides PSA compatibility for single-core PSA
targets.

The following example shows a PSA-enabled single-core target, `K64F`.

```json
    "K64F": {
        "supported_form_factors": [
            "ARDUINO"
        ],
        "components_add": [
            "SD",
            "FLASHIAP"
        ],
        "core": "Cortex-M4F",
        "supported_toolchains": [
            "ARM",
            "GCC_ARM",
            "IAR"
        ],
        "extra_labels_add": [
            "Freescale",
            "MCUXpresso_MCUS",
            "KSDK2_MCUS",
            "FRDM",
            "KPSDK_MCUS",
            "KPSDK_CODE",
            "MCU_K64F",
            "Freescale_EMAC"
        ],
        "is_disk_virtual": true,
        "macros_add": [
            "CPU_MK64FN1M0VMD12",
            "FSL_RTOS_MBED",
            "MBED_SPLIT_HEAP",
            "MBED_TICKLESS"
        ],
        "inherits": [
            "PSA_V7_M"
        ],
        "detect_code": [
            "0240"
        ],
        "device_has_add": [
            "USTICKER",
            "LPTICKER",
            "RTC",
            "CRC",
            "ANALOGIN",
            "ANALOGOUT",
            "EMAC",
            "I2C",
            "I2CSLAVE",
            "INTERRUPTIN",
            "PORTIN",
            "PORTINOUT",
            "PORTOUT",
            "PWMOUT",
            "RESET_REASON",
            "SERIAL",
            "SERIAL_FC",
            "SERIAL_ASYNCH",
            "SLEEP",
            "SPI",
            "SPI_ASYNCH",
            "SPISLAVE",
            "STDIO_MESSAGES",
            "TRNG",
            "FLASH",
            "USBDEVICE",
            "WATCHDOG"
        ],
        "release_versions": [
            "2",
            "5"
        ],
        "device_name": "MK64FN1M0xxx12",
        "bootloader_supported": true,
        "overrides": {
            "network-default-interface-type": "ETHERNET"
        },
        "supported_c_libs": {
            "arm": [
                "std",
                "small"
            ],
            "gcc_arm": [
                "std",
                "small"
            ],
            "iar": [
                "std"
            ]
        }
    }
```

Please pay attention to the config options `macros_add`, `extra_labels_add` and
`device_has_add`. If needed, a PSA target definition **MUST** use
[macros/extra_labels/device_has]`_add` or
[macros/extra_labels/device_has]`_remove` (not `macros`, `extra_labels` or
`device_has`) to add/remove `macros`, `extra_labels` or target capabilities.
Also, use `feature_`[add/remove] to add/remove a feature.

Check
[macros]([extra_labels](https://os.mbed.com/docs/mbed-os/latest/reference/adding-and-configuring-targets.html)),
[extra_labels](https://os.mbed.com/docs/mbed-os/latest/reference/adding-and-configuring-targets.html),
[device_has](https://os.mbed.com/docs/mbed-os/latest/reference/adding-and-configuring-targets.html)
and
[features](https://os.mbed.com/docs/mbed-os/latest/reference/adding-and-configuring-targets.html)
for more information.

Another example of a single-core Armv7-M PSA target which inherits from one of it's family targets:
```json
    "GD32_F450ZI": {
        "inherits": [
            "GD32_Target"
        ]
    }
```
In this case, following additional attributes **MUST** be added,
```json
        "features_add": [
            "PSA"
        ],
        "extra_labels_add": [
            "MBED_PSA_SRV"
        ],
        "macros_add": [
            "MBEDTLS_PSA_HAS_ITS_IO",
            "MBEDTLS_USE_PSA_CRYPTO"
        ]
```

## Adding dual-core PSA targets
A target can be categorized as a dual-core target if it has at least two cores
that are either Armv7-M or Armv6-M. On dual-core PSA targets, TF-M runs on the
SPE and provides PSA services.

An Mbed OS (NSPE) target **MUST** contain the following attributes in addition
to other target attributes defined in [porting a custom
board](https://os.mbed.com/docs/mbed-os/latest/porting/porting-a-custom-board.html)
and [porting
targets](https://os.mbed.com/docs/mbed-os/latest/porting/porting-targets.html).

* `inherits`: PSA generic target `PSA_DUAL_CORE` unless target has to inherit
  from one of it's family targets
* `tfm_target_name`: Target name in TF-M
  `tfm_bootloader_supported`: If TF-M bootloader is supported by the target.
* Values supported are "true" and "false"
* `tfm_default_toolchain`: Default TF-M toolchain supported. Values supported
  are `ARMCLANG` and `GNUARM`
* `tfm_supported_toolchains`: Supported TF-M toolchains. Values supported are
  `ARMCLANG` and `GNUARM`
* `tfm_delivery_dir`: The directory to which TF-M binary will be copied to
* `TFM_OUTPUT_EXT`: Optional attribute that indicates the output extension of
  TF-M secure binary

The following example shows a PSA enabled dual-core target, `PSoC64`.

```json
    "CY8CKIT_064S2_4343W": {
        "inherits": [
            "MCU_PSOC6_M4"
        ],
        "features_add": [
            "BLE",
            "PSA"
        ],
        "components_add": [
            "WHD",
            "4343W",
            "CYW43XXX"
        ],
        "components_remove": [
            "QSPIF"
        ],
        "supported_form_factors": [
            "ARDUINO"
        ],
        "device_has_remove": [
            "ANALOGOUT",
            "QSPI"
        ],
        "extra_labels_add": [
            "PSOC6_02",
            "MXCRYPTO_02",
            "CORDIO",
            "TFM",
            "TFM_DUALCPU"
        ],
        "macros_add": [
            "CYB0644ABZI_S2D44",
            "CYBSP_WIFI_CAPABLE",
            "TFM_MULTI_CORE_MULTI_CLIENT_CALL=1",
            "MBEDTLS_PSA_HAS_ITS_IO",
            "MBEDTLS_USE_PSA_CRYPTO"
        ],
        "detect_code": [
            "190A"
        ],
        "post_binary_hook": {
            "function": "PSOC6Code.sign_image"
        },
        "forced_reset_timeout": 5,
        "overrides": {
            "network-default-interface-type": "WIFI"
        },
        "program_cycle_s": 10,
        "tfm_target_name": "psoc64",
        "tfm_bootloader_supported": false,
        "tfm_default_toolchain": "GNUARM",
        "tfm_supported_toolchains": [
            "GNUARM"
        ],
        "tfm_delivery_dir": "TARGET_Cypress/TARGET_PSOC6/TARGET_CY8CKIT_064S2_4343W",
        "TFM_OUTPUT_EXT": "hex"
    }
```

Please pay attention to the config options `macros_add`, `extra_labels_add` and
`device_has_remove`. If needed, a PSA target definition **MUST** use
[macros/extra_labels/device_has]`_add` or
[macros/extra_labels/device_has]`_remove` (not `macros`, `extra_labels` or
`device_has`) to add/remove `macros`, `extra_labels` or target capabilities.
Also, use `feature_`[add/remove] to add/remove a feature.

Check
[macros]([extra_labels](https://os.mbed.com/docs/mbed-os/latest/reference/adding-and-configuring-targets.html)),
[extra_labels](https://os.mbed.com/docs/mbed-os/latest/reference/adding-and-configuring-targets.html),
[device_has](https://os.mbed.com/docs/mbed-os/latest/reference/adding-and-configuring-targets.html)
and
[features](https://os.mbed.com/docs/mbed-os/latest/reference/adding-and-configuring-targets.html)
for more information.

By default TF-M build generates a `bin` file. If the target requires a `hex`
file then the attribute `"TFM_OUTPUT_EXT": "hex"` should be added to the target
definition. Then the build script will convert `bin` to `hex` before copying it
to `tfm_delivery_dir`.

This dual-core PSA target doesn't inherit from `PSA_DUAL_CORE` because it has
to inherit from one of its family targets. Hence following additional
attributes have been added,
```json
        "features_add": [
            "PSA"
        ],
        "extra_labels_add": [
            "TFM",
            "TFM_DUALCPU"
        ],
        "macros_add": [
            "MBEDTLS_PSA_HAS_ITS_IO",
            "MBEDTLS_USE_PSA_CRYPTO"
        ]
```

If a dual-core PSA target can inherit from `PSA_DUAL_CORE` then there is no need to add the additional attributes listed above.

## Adding Armv8-M PSA targets
An Mbed OS (NSPE) target **MUST** contain the following attributes in addition
to other target attributes defined in [porting a custom
board](https://os.mbed.com/docs/mbed-os/latest/porting/porting-a-custom-board.html)
and [porting
targets](https://os.mbed.com/docs/mbed-os/latest/porting/porting-targets.html).

* `inherits`: PSA generic target `PSA_V8_M` unless target has to inherit from
  one of it's family targets
* `tfm_target_name`: Target name in TF-M
* `tfm_bootloader_supported`: If TF-M bootloader is supported by the target.
  Values supported are "true" and "false"
* `tfm_default_toolchain`: Default TF-M toolchain supported. Values supported
  are `ARMCLANG` and `GNUARM`
* `tfm_supported_toolchains`: Supported TF-M toolchains. Values supported are
  `ARMCLANG` and `GNUARM`
* `tfm_delivery_dir`: The directory to which TF-M binary will be copied to
* `TFM_OUTPUT_EXT`: Optional attribute that indicates the output extension of
  TF-M secure binary

The following example shows a PSA-enabled Armv8-M PSA target, `ARM_MUSCA_A1`.

```json
    "ARM_MUSCA_A1": {
        "inherits": [
            "PSA_V8_M"
        ],
        "default_toolchain": "ARMC6",
        "forced_reset_timeout": 7,
        "release_versions": [
            "5"
        ],
        "core": "Cortex-M33-NS",
        "supported_toolchains": [
            "ARMC6",
            "GCC_ARM",
            "IAR"
        ],
        "device_has_add": [
            "INTERRUPTIN",
            "LPTICKER",
            "SERIAL",
            "SLEEP",
            "USTICKER"
        ],
        "macros_add": [
            "__STARTUP_CLEAR_BSS",
            "MBED_FAULT_HANDLER_DISABLED",
            "CMSIS_NVIC_VIRTUAL",
            "LPTICKER_DELAY_TICKS=1",
            "MBED_MPU_CUSTOM"
        ],
        "extra_labels_add": [
            "ARM_SSG",
            "MUSCA_A1",
            "MUSCA_A1_NS"
        ],
        "post_binary_hook": {
            "function": "ArmMuscaA1Code.binary_hook"
        },
        "secure_image_filename": "tfm_s.bin",
        "tfm_target_name": "MUSCA_A",
        "tfm_bootloader_supported": true,
        "tfm_default_toolchain": "ARMCLANG",
        "tfm_supported_toolchains": [
            "ARMCLANG",
            "GNUARM"
        ],
        "tfm_delivery_dir": "TARGET_ARM_SSG/TARGET_MUSCA_A1"
    }
```

Please pay attention to the config options `macros_add`, `extra_labels_add` and
`device_has_add`. If needed, a PSA target definition **MUST** use
[macros/extra_labels/device_has]`_add` or
[macros/extra_labels/device_has]`_remove` (not `macros`, `extra_labels` or
`device_has`) to add/remove `macros`, `extra_labels` or target capabilities.
Also, use `feature_`[add/remove] to add/remove a feature.

Check
[macros]([extra_labels](https://os.mbed.com/docs/mbed-os/latest/reference/adding-and-configuring-targets.html)),
[extra_labels](https://os.mbed.com/docs/mbed-os/latest/reference/adding-and-configuring-targets.html),
[device_has](https://os.mbed.com/docs/mbed-os/latest/reference/adding-and-configuring-targets.html)
and
[features](https://os.mbed.com/docs/mbed-os/latest/reference/adding-and-configuring-targets.html)
for more information.

By default TF-M build generates a `bin` file. If the target requires a `hex`
file then the attribute `"TFM_OUTPUT_EXT": "hex"` should be added to the target
definition. Then the build script will convert `bin` to `hex` before copying it
to `tfm_delivery_dir`. Also, `secure_image_filename` **MUST** be updated
accordingly.

If an Armv8-M PSA target cannot inherit from `PSA_V8_M` because it has to
inherit from one of it's family targets, then following attributes have to be
added.
```json
        "features_add": [
            "PSA"
        ],
        "extra_labels_add": [
            "TFM",
            "TFM_V8M"
        ],
        "macros_add": [
            "MBEDTLS_PSA_HAS_ITS_IO",
            "MBEDTLS_USE_PSA_CRYPTO"
        ]
```

#  Enabling PSA at application level
Having an entropy source is crucial for Mbed TLS and Mbed Crypto. The
[document](https://os.mbed.com/docs/mbed-os/latest/porting/entropy-sources.html)
talks about entropy and how to add an entropy source. Sometimes a target might
not have a True Random Number Generator (TRNG), in that case the target will be
configured as a non-PSA target in `targets/targets.json`. In that scenario, if
an application wants to use that target as a PAS target then it is the
responsibility of application to provide an entropy source and mark that target
as PSA target at application level. The config option
[target_overrides](https://os.mbed.com/docs/mbed-os/latest/reference/configuration.html)
can be used to enable PSA for a target.

example mbed_app.json:
```json
"target_overrides": {
    "K64F": {
        "inherits": ["PSA_V7_M"]
    }
}
```

# Build and validation
For dual-core and Armv8-M PSA targets, TF-M runs on the SPE and provides PSA
services. The python script `build_tfm.py` automates building TF-M and copying
the TF-M binary to a predefined location defined by the target attribute
`tfm_delivery_dir`. Another python script `build_psa_compliance.py` automates
building PSA API compliance tests.

The
[mbed-os-tf-m-regression-tests](https://github.com/ARMmbed/mbed-os-tf-m-regression-tests)
contains build scripts, TF-M regression tests and PSA API compliance tests.

## Building TF-M and running regression tests
Follow the steps below to build TF-M and regression tests:

1. Clone
   [mbed-os-tf-m-regression-tests](https://github.com/ARMmbed/mbed-os-tf-m-regression-tests)
   repo
1. Update `mbed-os.lib` to the version of Mbed OS that contains new target
   support including `targets.json` changes described in this document
1. Run `mbed deploy`
1. Run `python3 build_tfm.py -m <new target> -t <toolchain> -c
   ConfigRegressionIPC.cmake`
    * The command builds necessary services in TF-M to run regression tests
    *NOTE*\
    Use this config **ONLY TO** run regression tests. The secure binary copied
    to Mbed OS **MUST** be generated using the config option
    `ConfigCoreIPC.cmake`.
1. Ensure TF-M binary is copied to location defined by target attribute
   `tfm_delivery_dir`
1. Run `mbed compile -m <new target> -t <toolchain>` to build Mbed OS and run
   regression tests
1. Flash the regression tests binary on to the target and ensure all regression
   tests passes

*TIP*\
Supported options:
```console
usage: build_tfm.py [-h]
                    [-c {ConfigCoreIPC.cmake,ConfigRegressionIPC.cmake,ConfigPsaApiTestIPC.cmake}]
                    [-m {ARM_MUSCA_A1,ARM_MUSCA_B1,CY8CKIT_064S2_4343W,CYESKIT_064B0S2_4343W}]
                    [-t {ARMCLANG,GNUARM}] [-d] [-l] [--commit]
                    [-s {CRYPTO,INITIAL_ATTESTATION,PROTECTED_STORAGE,INTERNAL_TRUSTED_STORAGE}]

optional arguments:
  -h, --help            show this help message and exit
  -c {ConfigCoreIPC.cmake,ConfigRegressionIPC.cmake,ConfigPsaApiTestIPC.cmake}, --config {ConfigCoreIPC.cmake,ConfigRegressionIPC.cmake,ConfigPsaApiTestIPC.cmake}
                        Use the specified TF-M configuration
  -m {ARM_MUSCA_A1,ARM_MUSCA_B1,CY8CKIT_064S2_4343W,CYESKIT_064B0S2_4343W}, --mcu {ARM_MUSCA_A1,ARM_MUSCA_B1,CY8CKIT_064S2_4343W,CYESKIT_064B0S2_4343W}
                        Build for the given MCU
  -t {ARMCLANG,GNUARM}, --toolchain {ARMCLANG,GNUARM}
                        Build for the given toolchain (default is
                        tfm_default_toolchain)
  -d, --debug           Set build profile to debug
  -l, --list            Print supported TF-M secure targets
  --commit              Commit secure binaries (TF-M) and
                        features/FEATURE_PSA/TARGET_TFM/VERSION.txt
  -s {CRYPTO,INITIAL_ATTESTATION,PROTECTED_STORAGE,INTERNAL_TRUSTED_STORAGE}, --suite {CRYPTO,INITIAL_ATTESTATION,PROTECTED_STORAGE,INTERNAL_TRUSTED_STORAGE}
                        Suite name for PSA API Tests
```

## Building TF-M and running PSA compliance tests
Follow the steps below to build TF-M and compliance tests:

1. Switch to the `mbed-os-tf-m-regression-tests` directory.
1. Edit `main.cpp` to set `RUN_PSA_COMPLIANCE_TESTS` to `1` and
  `RUN_REGRESSION_TESTS` to `0`.
1. Run `python3 build_psa_compliance.py -m <new target> -t <toolchain> -s
   CRYPTO`
    * The command builds PSA API compliance tests for crypto suite
1. Run `python3 build_tfm.py -m <new target> -t <toolchain> -c
   configs/ConfigPsaApiTestIPC.cmake -s CRYPTO`
    * The command builds TF-M including PSA API compliance tests
1. Run `mbed compile -m <new target> -t <toolchain>` to build Mbed OS and run
   PSA API compliance tests
1. Flash the PSA API compliance tests binary on to the target and ensure all
   PSA API compliance tests passes
    *NOTE*\
    If any of the PSA API compliance tests fail in TF-M example application
    then those tests will fail in Mbed OS as well.

*TIP*\
Supported options:
```console
usage: build_psa_compliance.py [-h] -m
                               {ARM_MUSCA_A1,ARM_MUSCA_B1,CY8CKIT_064S2_4343W}
                               [-t {ARMCLANG,GNUARM}] [-v {1,2,3,4,5}]
                               [-s {CRYPTO,INITIAL_ATTESTATION,PROTECTED_STORAGE,INTERNAL_TRUSTED_STORAGE}]
                               [-r RANGE] [-i INCLUDE]

optional arguments:
  -h, --help            show this help message and exit
  -m {ARM_MUSCA_A1,ARM_MUSCA_B1,CY8CKIT_064S2_4343W}, --mcu {ARM_MUSCA_A1,ARM_MUSCA_B1,CY8CKIT_064S2_4343W}
                        Build for the given MCU
  -t {ARMCLANG,GNUARM}, --toolchain {ARMCLANG,GNUARM}
                        Build for the given toolchain (GNUARM)
  -v {1,2,3,4,5}, --verbose {1,2,3,4,5}
                        Verbose level of the build (default : 3)
  -s {CRYPTO,INITIAL_ATTESTATION,PROTECTED_STORAGE,INTERNAL_TRUSTED_STORAGE}, --suite {CRYPTO,INITIAL_ATTESTATION,PROTECTED_STORAGE,INTERNAL_TRUSTED_STORAGE}
                        Test suite name (default : CRYPTO)
  -r RANGE, --range RANGE
                        Test suite range (default : all tests), Format :
                        'test_start_number;test_end_number'
  -i INCLUDE, --include INCLUDE
                        Test include path, Format :
                        <include_path1>;<include_path2>;...;<include_pathn>
```

## Building TF-M and creating Mbed OS pull request
Follow the steps below to build TF-M and to create Mbed OS pull request:

1. Switch to `mbed-os-tf-m-regression-tests` directory
1. Run `python3 build_tfm.py -m <new target> -t <toolchain> --commit`
    * The command builds TF-M with config `ConfigCoreIPC.cmake`, copy TF-M
      binary onto location defined by target attribute `tfm_delivery_dir` and
      commit the changes to Mbed OS.
1. Switch to `mbed-os` directory and check the latest commit
1. If everything looks good then push the changes to your fork of Mbed OS
1. Create Mbed OS pull request at https://github.com/ARMmbed/mbed-os

*NOTE*\
Please ensure that both regression tests and PSA API compliance tests passes
before creating Mbed OS pull request.

*TIP*\
When the python script `build_tfm.py` is invoked without any options then TF-M
will be built for all supported targets and the secure binary (TF-M) for each
target is copied to a predefined location defined by the target attribute
`tfm_delivery_dir`. When `--commit` option is provided, a new Mbed OS commit is
created with new/modified TF-M binaries and
`features/FEATURE_PSA/TARGET_TFM/VERSION.txt`.

Example:
```console
python3 build_tfm.py --commit
```
