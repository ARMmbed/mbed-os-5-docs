<h2 id="migrating">Mbed OS 2 to 5 migration guide</h2>

This guide is to assist you in the process of updating an existing [component](https://os.mbed.com/components/), library or program from Mbed OS 2 to Mbed OS 5.

### Prerequisites

- [Mbed CLI](../tools/developing-mbed-cli.html).
- An [offline compiler](../tools/index.html#compiler-versions).

### Identifying old versions of Mbed OS

This guide uses the Grove temperature and humidity sensor as an example: [Grove-TempHumi-Sensor](https://os.mbed.com/components/Grove-TempHumi-Sensor/).

First, navigate to the Hello World repository for the component.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/hello_world_import.png)<span>Hello World repository for the component</span></span>


Next, view the files in the Hello World repository. The presence of an `mbed.bld` or `mbed-rtos.lib` file signifies that this program uses an older version of Mbed OS (older than Mbed OS 5).

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/old_mbed_file.png)<span>Older version of Mbed OS `mbed.bld` or `mbed-rtos.lib` files in the Hello World repository</span></span>


A program that uses and has been tested with Mbed OS 5 or later has an `mbed-os.lib` file.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/new_mbed_file.png)<span>Mbed OS 5 or later `mbed-os.lib` file in the Hello World respository</span></span>

Some repositories may have both an `mbed.bld` file and an `mbed-rtos.lib` file present. Mbed-RTOS is the precursor to Mbed OS 5, which combines the older Mbed OS 2 library with Mbed-RTOS. So, Mbed OS 5 can replace both `mbed.bld` and `mbed-rtos.lib`.

### Migrating to Mbed OS 5

Migrating to Mbed OS 5 results in two possible outcomes:

1. Replacing the old Mbed library with Mbed OS is successful because the APIs in the library have not changed. In this instance, you're finished.
2. Replacing the old Mbed library with Mbed OS produces some compilation errors. These errors can occur in the library or in the application code for the following two reasons:
  - The Mbed OS API calls are out of date, and you need to migrate to the updated Mbed OS API syntax.
  - There is target specific code, and you need to migrate it to use the code for the specific target you are compiling for.

To update to Mbed OS 5 with the [Mbed CLI](../tools/developing-mbed-cli.html), run:

```
mbed import [URL of Project]
cd [Project Name]
mbed remove mbed

mbed add mbed-os
```

To determine the success of migration, run:

`mbed compile -m [platform] -t [toolchain]`

To update to Mbed OS 5 with the [Mbed Online Compiler](../tools/developing-mbed-online-compiler.html):

1. Open your project in the Online Compiler.
1. Right click on **mbed** and select **Delete...**:

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/mbed2-delete-mbed.png)<span>Delete mbed</span></span>

1. If your project includes `mbed-rtos`, you also need to delete this library to successfully update to Mbed OS 5. Right click on **mbed-rtos**, and select **Delete...**:

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/mbed2-delete-mbed-rtos.png)<span>Delete mbed-rtos</span></span>

1. Right click on the name of your project, hover over **Import Library** and then select **From URL**:

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/mbed2-import-url.png)<span>Import library from URL</span></span>

1. Copy and paste the URL for Mbed OS 5 `https://github.com/armmbed/mbed-os`, and then click **Import**:

    <span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/import-mbed-os.png)<span>Mbed OS 5 URL</span></span>

To determine the success of migration, select your board in the top right corner of the Online Compiler, and click  **Compile**.

### Enabling Mbed OS bare metal

Enabling the Mbed OS bare metal profile allows you to build Mbed OS without an RTOS. To enable it, you have to complete the [migration to Mbed OS 5](#migrating-to-mbed-os-5). Once the migration is complete, you can enable Mbed OS bare metal by creating an `mbed_app.json` with the following contents:

```
{
    "requires": ["bare-metal"]
}
```

### Runtime errors

Although the program or library now compiles successfully, runtime errors may still be present. Please visit the [compile-time errors tutorial](compile-time-errors.html#runtime-errors-and-lights-of-the-dead) for further debugging tips about common errors.

