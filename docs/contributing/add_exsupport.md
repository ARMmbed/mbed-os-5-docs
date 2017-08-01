
## Adding export support for a target

If you have added a new target to mbed OS 5, exporting will allow users to transition from mbed source code to the offline development environment of their choice. More people can use your device.

### Eclipse and Make

Eclipse project export uses a generated Makefile for building. If `mbed compile -t <toolchain> -m <target>` works, then mbed `export -i make_<toolchain> -m <target>` will also work. You can find more information about adding and configuring targets [here](mbed_targets.md).

### GNU Arm Eclipse managed projects

The GNU Arm Eclipse exporter is available for all targets that use the GCC Arm toolchain.

### Qt Creator and Make

The Qt Creator project export is available for the GCC Arm toolchain; it generates a [Qt Creator generic project](http://doc.qt.io/qtcreator/creator-project-generic.html) and a Makefile, in a similar fashion to the *Eclipse and Make* exporter.

You can open the generated `.creator` project in Qt Creator, enabling integration with the project pane, syntax highlighting and automatic code completion. You can use the Makefile to compile the project; the IDE should automatically invoke the Makefile when you issue the Build command.

### uVision and IAR

#### CMSIS Packs

uVision and IAR both use [CMSIS packs](http://www.keil.com/pack/doc/CMSIS/Pack/html/index.html) to find target information necessary to create a valid project file. 

We use the tool [ArmPackManager](https://github.com/ARMmbed/mbed-os/tree/master/tools/arm_pack_manager) to scrape [MDK5 Software Packs](https://www.keil.com/dd2/Pack/) for target information by parsing [http://www.keil.com/pack/index.idx](http://sadevicepacksprod.blob.core.windows.net/idxfile/index.idx). [index.json](https://github.com/ARMmbed/mbed-os/blob/master/tools/arm_pack_manager/index.json) stores the relevant information in the [PDSC (Pack Description)](http://www.keil.com/pack/doc/CMSIS/Pack/html/_pack_format.html) retrieved from each URL in the index. 

A `.pdsc` file typically describes a family of devices. Each device is uniquely identified by its [device name](mbed_targets.md#device_name). This name makes a natural key to associate a device with its information in `index.json`. 

#### What's in a device name?
There is no reliable way to map an mbed alias such as [NUCLEO_F030R8](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json#L603) to its unique identifier, [STM32F030R8](https://github.com/ARMmbed/mbed-os/blob/master/targets/targets.json#L615), because it is listed in a CMSIS pack (and subsequently `index.json`). So, we added a [device name](mbed_targets.md#device_name) field in `targets.json`. **This field is required for IAR or uVision exporter support**.

#### Code usage
[http://www.keil.com/pack/Keil.Kinetis_K20_DFP.pdsc](http://www.keil.com/pack/Keil.Kinetis_K20_DFP.pdsc) is the PDSC that contains TEENSY_31 device (MK20DX256xxx7). ArmPackManager has parsed it, and `index.json` stores it. The device information begins on line 156:
```xml
      <device Dname="MK20DX256xxx7">
        <processor Dfpu="0" Dmpu="0" Dendian="Little-endian" Dclock="72000000"/>
        <compile header="Device\Include\MK20D7.h"  define="MK20DX256xxx7"/>
        <debug      svd="SVD\MK20D7.svd"/>
        <memory     id="IROM1"                      start="0x00000000"  size="0x40000"    startup="1"   default="1"/>
        <memory     id="IROM2"                      start="0x10000000"  size="0x8000"     startup="0"   default="0"/>
        <memory     id="IRAM1"                      start="0x20000000"  size="0x8000"     init   ="0"   default="1"/>
        <memory     id="IRAM2"                      start="0x1FFF8000"  size="0x8000"     init   ="0"   default="0"/>
        <algorithm  name="Flash\MK_P256.FLM"        start="0x00000000"  size="0x40000"                  default="1"/>
        <algorithm  name="Flash\MK_D32_72MHZ.FLM"   start="0x10000000"  size="0x8000"                   default="1"/>
        <book name="Documents\K20P100M72SF1RM.pdf"         title="MK20DX256xxx7 Reference Manual"/>
        <book name="Documents\K20P100M72SF1.pdf"           title="MK20DX256xxx7 Data Sheet"/>
      </device>
```

#### uVision
The `dname` (device name) field on line 156 directly corresponds to that in the uVision5 IDE Target Selection window. [`tools/export/uvision/uvision.tmpl`](https://github.com/ARMmbed/mbed-os/blob/master/tools/export/uvision/uvision.tmpl#L15) uses target information from these packs to generate valid uVision5 projects. If the program cannot find the device name, we use a generic Arm CPU target in uVision5.

#### IAR
[`tools/export/iar/iar_definitions.json`](https://github.com/ARMmbed/mbed-os/blob/master/tools/export/iar/iar_definitions.json) uses this device name to store information necessary to set the target in an IAR project.

#### Updating index.json
You can regenerate `index.json` to contain a newly made CMSIS pack with the following command:

`mbed export -i [IDE] --update-packs`

You should include the changes to `index.json` in the PR that adds support for the new target.
