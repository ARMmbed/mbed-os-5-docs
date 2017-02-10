# Adding exporters 

This is a guide for adding exporters to the mbed-os tools. It covers the structure of the export subsystem and the individual exporter.

<span class="notes">**Note:** All paths are relative to [https://github.com/ARMmbed/mbed-os/](https://github.com/ARMmbed/mbed-os/).</span>

## Export subsystem structure

The export subsystem is organized as a group of common code and a group of IDE or toolchain specific plugins.

The **common code** is contained in four files: 

 * `tools/project.py` contains the command-line interface and handles the differences between mbed OS 2 tests and mbed OS 5 projects.
 * `tools/project_api.py` contains a high-level API for use by the mbed Online Compiler and mbed CLI. Responsible for doing boilerplate-like things, such as scanning for resources.
 * `tools/export/__init__.py` contains the mapping of exporter names to plugin classes, and handles printing of toolchain support information.
 * `tools/export/exporters.py` contains the base class for all plugins. It offers useful exporter-specific actions.

An **IDE or toolchain specific plugin** is a Python class that inherits from the `Exporter` class and is listed in the `tools/export/__init__.py` exporter map.

### Common code

The common code does two things: setting things up for the plugins, and providing a library of useful tools for plugins to use.

___Setup___

The setup code scans for the resources used in the export process and collects the configuration required to build the project at hand.

These steps construct an object of one of the exporter plugin classes listed in the exporter map and populate that object with useful attributes, including:

 * `toolchain` an `mbedToolchain` object that may be used to query the configuration of the toolchain.
   * `toolchain.target` a `Target` object that may be use to query target configuration.
 * `project_name` the name of the project.
 * `flags` the flags that the mbedToolchain instance will use to compile the `c/cpp/asm` files if invoked.
 * `resources` a `Resources` object that contains many lists of files that an exporter will find useful, such as C and Cpp sources and header search paths. The plugin should use only the attributes of the Resources object because the methods are only used during setup time. You can view all available Resources class attributes in `tools/toolchains/__init__.py`.

___Plugin tools___

The other half of the common code is a library for use by a plugin. This API includes:

 * `gen_file` use Jinja2 to generate a file from a template.
 * `get_source_paths` returns a list of directories that contain assembly, C, C++ files and so on.
 * `group_project_files` group all files passed in by their containing directory. The groups are suitable for an IDE. 

### Plugin code

Plugin code is contained within a subdirectory of the `tools/export` directory named after the IDE or toolchain that the plugin is exporting for.
For example, the uVision exporter's templates and Python code is contained within the directory `tools/export/uvision` and the Makefile exporter's code and templates within `tools/export/makefile`.

The Python code for the plugin should be:

1. Placed into an `__init__.py` file.
1. Imported into `tools/export/__init__.py`.
1. Added to the exporter map.

___The `generate` method___

Each exporter is expected to implement one method, `generate`, which is responsible for creating all of the required project files for the IDE or toolchain that the plugin targets. 

This method may use any of the attributes and APIs included by the common code.

___The `TARGETS` class variable___

Each exporter reports its specific target support through a class varibale, `TARGETS`. This class variable is simply a list of targets to which you can export. Requesting an export to a target that's not on the list will generate an error.

___The `TOOLCHAIN` class variable___

Each exporter reports its specific toolchain it will use to compile the source code through a class variable `TOOLCHAIN`.

___The `NAME` class variable___

Each exporter reports the name of the exporter through the class variable `NAME`. This matches the key in the `tools/export/__init__.py` exporter map.

___The `build` method___

A plugin that would like to be tested by CI may implement the `build` method. 

This method runs after `generate` on an object that inherits from `Exporter`. It is responsible for invoking the build tools that the IDE or toolchain needs when a user instructs it to compile. It must return `0` on success or `-1` on failure.

## Implementing an example plugin

In this section, we walk through implementing a simple exporter, `my_makefile`, which is a simplified Makefile using one template.

We will create two files and discuss their contents: `__init__.py` with the Python plugin code, and `Makefile.tmpl` with the template.

As this plugin is named `my_makefile`, all of the support code will be placed into `tools/export/my_makefile`.

### Python code for `__init__.py`

First, we will make our class a subclass of Exporter:
```python
from tools.export.exporters import Exporter

class My_Makefile(Exporter):
```

We must define the name, toolchain and target compatibility list. Class-level **static** variables contain these.

We will name our exporter `my_makefile`:

```python
NAME = 'my_makefile'
```

This exporter will compile with the `GCC_ARM` toolchain:
```python
TOOLCHAIN = 'GCC_ARM'
```

All targets the IDE supports are a subset of those `TARGET_MAP` contain. We need to import this map like this:
```python
from tools.targets import TARGET_MAP
```

We can say the targets supported will be the subset of mbed targets that support `GCC_ARM`:

```python
TARGETS = [target for target, obj in TARGET_MAP.iteritems()
           if "GCC_ARM" in obj.supported_toolchains]
```

#### Implementing the `generate` method

To generate our Makefile, we need a list of object files the executable will use. We can construct the list from the sources if we replace the extensions with `.o`.

To do this, we use the following Python code in our required `generate` method:

```python
to_be_compiled = [splitext(src)[0] + ".o" for src in
                  self.resources.s_sources +
                  self.resources.c_sources +
                  self.resources.cpp_sources]
```

Further, we may need to link against some libraries. We use the `-l:` gcc command-line syntax to specify the libraries:

```python
libraries = ["-l:" + lib for lib in self.resources.libraries]
```

Now we construct a context for the Jinja2 template rendering engine, filling in the less complicated resources:

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

To render our template, we pass the template file name, the context and the destination location within the exported project to the library-provided `gen_file` method:

```python
self.gen_file('my_makefile/Makefile.tmpl', ctx, 'Makefile')
```

### Template

Now that we have a context object, and we have passed off control to the Jinja2 template rendering engine, we can look at the template Makefile, `tools/export/my_makefile/Makefile.tmpl`. 

Find documentation on what is available within a Jinja2 template [here](http://jinja.pocoo.org/docs/dev/templates/).

```make
###############################################################################
# Project settings

PROJECT := {{name}}

# Project settings
###############################################################################
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
###############################################################################
# Tools

AS      = arm_none_eabi_gcc -x assembler-with-cpp
CC      = arm_none_eabi_gcc -std=gnu99
CPP     = arm_none_eabi_gcc -std=gnu++98
LD      = arm_none_eabi_gcc

# Tools
###############################################################################
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
