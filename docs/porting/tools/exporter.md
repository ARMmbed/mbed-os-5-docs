# Adding exporters

This is a guide for adding exporters to the Arm Mbed OS tools. First, this document describes what an exporter is and what rules it follows. Then, it covers the structure of the export subsystem and the individual exporter. Finally, this document gives some implementation suggestions.

<span class="notes">**Note:** All paths are relative to [https://github.com/ARMmbed/mbed-os/](https://github.com/ARMmbed/mbed-os/).</span>

## What an exporter is

An exporter is a Python plugin to the Mbed OS tools that converts a project using Arm Mbed CLI into one specialized for a particular IDE. For the best user experience, an exporter:

 - Takes input from the resource scan.
 - Uses the flags in the build profiles.
 - Has a single template file for each file type produced. For example, an Eclipse CDT project would have one template for `.project` files and one for `.cproject` files.
 - Does not call Mbed CLI. It is possible to export from the website, which does not include Mbed CLI in the resulting zip.

## Export subsystem structure

The export subsystem is organized as a group of common code and a group of IDE or toolchain specific plugins.

The **common code** is contained in three files:

 * `tools/project.py` contains the command-line interface and handles the differences between Mbed OS 2 tests and Mbed OS 5 projects.
 * `tools/export/__init__.py` contains an API used by the Arm Mbed Online Compiler and `project.py`. This file is responsible for boilerplate actions that every exporter must do, such as scanning for resources or collecting toolchain flags.
 * `tools/export/exporters.py` contains the base class for all plugins. It offers useful exporter-specific actions.

An **IDE or toolchain specific plugin** is a Python class that inherits from the `Exporter` class and is listed in the `tools/export/__init__.py` exporter map.

### Common code

The common code does two things: setting things up for the plugins, and providing a library of useful tools for plugins to use.

#### Setup

The setup code scans for the resources used in the export process and collects the configuration required to build the project.

These steps construct an object of one of the exporter plugin classes listed in the exporter map and populate that object with useful attributes, including:

 * `toolchain` - an `mbedToolchain` object that may be used to query the configuration of the toolchain.
   * `toolchain.target` - a `Target` object that may be use to query target configuration.
 * `project_name` - the name of the project.
 * `flags` - the flags that the mbedToolchain instance will use to compile the `c/cpp/asm` files if invoked.
 * `resources` - a `Resources` object that contains many lists of files that an exporter will find useful, such as C and Cpp sources and header search paths. The plugin should use only the attributes of the Resources object because the methods are only used during setup time. You can view all available Resources class attributes in `tools/toolchains/__init__.py`.

#### Plugin tools

The other half of the common code is a library for use by a plugin. This API includes:

 * `gen_file` use Jinja2 to generate a file from a template.
 * `get_source_paths` returns a list of directories that contain assembly, C, C++ files and so on.
 * `group_project_files` group all files passed in by their containing directory. The groups are suitable for an IDE.

### Plugin code

Plugin code is contained within a subdirectory of the `tools/export` directory named after the IDE or toolchain that the plugin is exporting for.

For example, the uVision exporter's templates and Python code is contained within the directory `tools/export/uvision` and the Makefile exporter's code and templates within `tools/export/makefile`.

The Python code for the plugin is:

1. Placed into an `__init__.py` file.
1. Imported into `tools/export/__init__.py`.
1. Added to the exporter map.

#### The `generate` method

Each exporter is expected to implement one method, `generate`, which is responsible for creating all of the required project files for the IDE or toolchain that the plugin targets.

This method may use any of the attributes and APIs included by the common code.

#### The `is_target_supported` class method

Each exporter reports its specific target support through a class method, `is_target_supported`. This class method is called with a target, and expected to return `True` when a target is supported by the exporter and `False` otherwise. Requesting an export to a target that `is_target_supported` returns `False` for is an error.

#### The `TOOLCHAIN` class variable

Each exporter reports its specific toolchain it will use to compile the source code through a class variable `TOOLCHAIN`.

#### The `NAME` class variable

Each exporter reports the name of the exporter through the class variable `NAME`. This matches the key in the `tools/export/__init__.py` exporter map.

#### The `build` static method

A plugin tested by CI must implement the `build` method.

This static method runs after `generate` on an class that inherits from `Exporter`. It is responsible for invoking the build tools that the IDE or toolchain needs when a user instructs it to compile. It must return `0` on success or `-1` on failure.

## Implementing an example plugin

This sections walks through implementing an exporter, `my_makefile`, which is a Makefile using one template.

You will create two files and discuss their contents: `__init__.py` with the Python plugin code, and `Makefile.tmpl` with the template.

As this plugin is named `my_makefile`, you will place all of the support code into `tools/export/my_makefile`.

### Python code for `__init__.py`

First, make a class a subclass of Exporter:

```python
from tools.targets import TARGET_MAP
from tools.export.exporters import Exporter

class My_Makefile(Exporter):
```

Define the name, toolchain and target compatibility list. Class-level **static** variables contain these.

Name the exporter `my_makefile`:

```python
NAME = 'my_makefile'
```

This exporter compiles with the `GCC_ARM` toolchain:

```python
TOOLCHAIN = 'GCC_ARM'
```

All targets the IDE supports are a subset of those `TARGET_MAP` contain. Import this map like this:

```python
from tools.targets import TARGET_MAP
```

You can say the targets supported will be the subset of Mbed targets that support `GCC_ARM`:

```python
@classmethod
def is_target_supported(cls, target_name):
    target = TARGET_MAP[target_name]
    return "GCC_ARM" in target.supported_toolchains
```

#### Implementing the `generate` method

To generate the Makefile, you need a list of object files the executable will use. You can construct the list from the sources if you replace the extensions with `.o`.

To do this, use the following Python code in the required `generate` method:

```python
to_be_compiled = [splitext(src)[0] + ".o" for src in
                  self.resources.s_sources +
                  self.resources.c_sources +
                  self.resources.cpp_sources]
```

Further, you may need to link against some libraries. Use the `-l:` GCC command-line syntax to specify the libraries:

```python
libraries = ["-l:" + lib for lib in self.resources.libraries]
```

Now, construct a context for the Jinja2 template rendering engine by filling in the less complicated resources:

```python
ctx = {
    'name': self.project_name,
    'to_be_compiled': to_be_compiled,
    'object_files': self.resources.objects,
    'include_paths': self.resources.inc_dirs,
    'library_paths': self.resources.lib_dirs,
    'linker_script': self.resources.linker_script,
    'libraries': libraries,
    'hex_files': self.resources.hex_files,
}
```

To render the template, pass the template file name, the context and the destination location within the exported project to the library-provided `gen_file` method:

```python
self.gen_file('my_makefile/Makefile.tmpl', ctx, 'Makefile')
```

### Template

Now that you have a context object have passed control to the Jinja2 template rendering engine, you can look at the template Makefile, `tools/export/my_makefile/Makefile.tmpl`.

For more information, please see the [documentation on what is available within a Jinja2 template](http://jinja.pocoo.org/docs/dev/templates/).

```make
##############################################################################
# Project settings

PROJECT := {{name}}

# Project settings
##############################################################################
# Objects and Paths

{% for obj in to_be_compiled %}OBJECTS += {{obj}}
{% endfor %}
{% for obj in object_files %} SYS_OBJECTS += {{obj}}
{% endfor %}
{% for path in include_paths %}INCLUDE_PATHS += -I{{path}}
{% endfor %}
LIBRARY_PATHS :={% for p in library_paths %} {{user_library_flag}}{{p}} {% endfor %}
LIBRARIES :={% for lib in libraries %} {{lib}} {% endfor %}
LINKER_SCRIPT := {{linker_script}}

# Objects and Paths
##############################################################################
# Tools

AS      = arm_none_eabi_gcc -x assembler-with-cpp
CC      = arm_none_eabi_gcc -std=gnu99
CPP     = arm_none_eabi_gcc -std=gnu++98
LD      = arm_none_eabi_gcc

# Tools
##############################################################################
# Rules

.PHONY: all lst size

all: $(PROJECT).bin $(PROJECT).hex size

.asm.o:
	+@$(call MAKEDIR,$(dir $@))
	+@echo "Assemble: $(notdir $<)"
	@$(AS) -c $(INCLUDE_PATHS) -o $@ $<

.s.o:
	+@$(call MAKEDIR,$(dir $@))
	+@echo "Assemble: $(notdir $<)"
	@$(AS) -c $(INCLUDE_PATHS) -o $@ $<

.S.o:
	+@$(call MAKEDIR,$(dir $@))
	+@echo "Assemble: $(notdir $<)"
	@$(AS) -c $(INCLUDE_PATHS) -o $@ $<

.c.o:
	+@$(call MAKEDIR,$(dir $@))
	+@echo "Compile: $(notdir $<)"
	@$(CC) $(INCLUDE_PATHS) -o $@ $<

.cpp.o:
	+@$(call MAKEDIR,$(dir $@))
	+@echo "Compile: $(notdir $<)"
	@$(CPP) $(INCLUDE_PATHS) -o $@ $<

$(PROJECT).elf: $(OBJECTS) $(SYS_OBJECTS) $(LINKER_SCRIPT)
	+@echo "link: $(notdir $@)"
	@$(LD) -T $(filter %{{link_script_ext}}, $^) $(LIBRARY_PATHS) --output $@ $(filter %.o, $^) $(LIBRARIES)
```

## Suggested implementation

There are several paths forward that can lead to an easily maintained exporter:

 - Specialize or alias the GNU Arm Eclipse exporter.
 - Specialize or alias the Eclipse + Make exporter.
 - Specialize the Make exporter.

### GNU Arm Eclipse

If your IDE uses Eclipse and uses the GNU Arm Eclipse plugin, then specialize or alias your exporter with the generic GNU ARM Eclipse.

#### Alias

If you do not need any specialization of the export, then replace your exporters class in the `EXPORT_MAP` with the `GNUARMEclipse` class. For example, if KDS met all of these requirements, you could:

```diff
EXPORTERS = {
     'iar': iar.IAR,
     'embitz' : embitz.EmBitz,
     'coide' : coide.CoIDE,
+    'kds' : gnuarmeclipse.GNUARMEclipse,
     'simplicityv3' : simplicity.SimplicityV3,
     'atmelstudio' : atmelstudio.AtmelStudio,
     'sw4stm32'    : sw4stm32.Sw4STM32,
```

#### Specialization

If you need more specialization and are using an Eclipse-based IDE and the GNU Arm Eclipse plugin, then your exporter class inherits from the `GNUARMEclipse` class. For example (with KDS again):

```python
from tools.export.gnuarmeclipse import GNUARMEcilpse

class KDS(GNUARMEcilpse):
     NAME = 'Kinetis Design Studio'
     TOOLCHAIN = 'GCC_ARM'
     ...

     def generate(self):
         """Generate eclipes project files, and some KDS specific files"""
         super(KDS, self).generate()
         ...

```

After inheriting from the `GNUARMEclipse` class, specialize the generate method in any way you need.

### Eclipse + Make

If your IDE uses Eclipse and does not use the GNU Arm Eclipse plugin, you can use the "Unmanaged makefile" Eclipse exporter classes, `EclipseGcc`, `EclipseArmc5` and `EclipseIar`. Much like the GNU Arm Eclipse section, you may decide to alias or specialize.

### Make

If your IDE is not Eclipse based but can still use a Makefile, then you can specialize the Makefile exporter. Specializing the Makefile is actually how Arm Mbed implemented the Eclipse + Make exporter.

Creating an exporter based on the Makefile exporter is a two-step process: inherit from the appropriate Makefile class, and call its generate method. Taking Eclipse + Make using GCC Arm as an example, your exporter looks like:

```python
class EclipseGcc(GccArm):
    NAME = "Eclipse-GCC-ARM"
```

Your generate method looks similar to:

```python
    def generate(self):
        """Generate Makefile, .cproject & .project Eclipse project file,
        py_ocd_settings launch file, and software link .p2f file
        """
        super(EclipseGcc, self).generate()
        ...
```
