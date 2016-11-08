This is a guide for adding exporters to the mbed-os tools. 
It will cover the structure of the export subsystem and how an individual exporter is structured.


## Structure of the export Subsystem

The export subsystem is organized as a group of common code and a group of IDE or toolchain specific plugins.
The common code is contained in four files: 
 * `tools/project.py` contains the command line interface and handles the differences between mbed classic tests and mbed-os projects
 * `tools/project_api.py` contains a high-level API for use by the online IDE and the command line and is responsible for doing boilerplate-like things such as scanning for resources
 * `tools/export/__init__.py` contains the map of exporter names to plugin classes and handles printing of support
 * `tools/export/exporters.py` contains the base class for all plugins that further acts as a library of useful exporter-specific actions

A IDE or Toolchain specific plugin is a python class that inherits from the `Exporter` class and is listed in the `tools/export/__init__.py` exporter map.

### Common code

The common code is geared towards two things: setting things up for the plugins, and providing a library of useful tools for plugins to use.

The setup code takes care of scanning for the resources used in the export process and collecting the configuration required to build the project at hand.
These steps construct an object of one of the exporter plugin classes listed in the exporter map and populate the object with useful attributes.
The attributes include:
 * `toolchain` a mbedToolchain object that may be used to query the configuration of the toolchain
   * `toolchain.target` a Target object that may be use to query target configuration
 * `project_name` the name of the project
 * `flags` the flags that the mbedToolchain instance would use to compile the c/cpp/asm files if invoked
 * `resources` a Resources object that contains many lists of files that an exporter would find useful, like C and Cpp sources or header search paths

The other half of the common code is a library for use by a plugin.
This API includes:
 * `gen_file` use Jinja2 to generate a file from a template
 * `get_source_files` get all asembly, C, C++, and so on files as one list
 * `group_project_files` Group all files passed in into groups sutable for an IDE

### Plugin code

Plugin code is contained within a sub-directory of the `tools/export` directory named after the IDE or Toolchain that the plugin is exporting for.
For example, the Uvision exporter's templates and python code is contained within the directory `tools/export/uvision` and the Makefile exporter's code and templates within `tools/export/makefile`.
The python code for the Plugin should be placed into an `__init__.py` file and should be imported into `tools/export/__init__.py` and added to the exporter map to be enabled.

Each exporter is expected to implement one method, `generate`, which is responsible for creating all of the required project files for the IDE or Toolchain that the plugin targets and provide their supported Targets in a `TARGETS` class variable.
This `generate` method may use any of the attributes and APIs included by the common code to accomplish its goal.

Further, a plugin that would like to be tested by CI may implement the `build` method. 
This method is expected to be run after `generate` on an object that inherits from `Exporter`, and is responsible for invoking the build tools that the IDE or Toolchain would when a user instructs it to compile.

## Implementing an example Plugin
In this section, we walk through implementing a simple exporter, `my_makefile`.
This exporter is a simplified Makefile that will use one template.
As this plugin is named `my_makefile`, all of the support code will be placed into `tools/export/my_makefile`
We will create two files and discuss the contents: `__init__.py` with the python plugin code, and `Makefile.tmpl` with the template.

### Python code

To generate our makefile, we need a list of object files that are needed by the executable. 
This can be constructed from the sources if we replace the extensions with `.o`.
To do this we use the following python code:
```python
to_be_compiled = [splitext(src)[0] + ".o" for src in
                  self.resources.s_sources +
                  self.resources.c_sources +
                  self.resources.cpp_sources]
```

Further, we may need to link against some libraries.
We use the `-l:` gcc command line syntax to specify the libraries.
```python
libraries = ["-l:" + lib for lib in self.resources.libraries]
```

Now we construct a context for the Jinja2 template rendering engine, filling in the less complicated resources.

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

Next we simply pass this context to the library provided `gen_file` method to render our template, passing it the template filename, the context, and the destination location within the exported project.
```python
self.gen_file('my_makefile/Makefile.tmpl', ctx, 'Makefile')
```

All that is left is providing the Target compatibility.
We could claim to support all targets that support `GCC_ARM` as follows.
```python
TARGETS = [target for target, obj in TARGET_MAP.iteritems()
           if "GCC_ARM" in obj.supported_toolchains]
```

### Template

Now that we have a context object and we have passed off control to the Jinja2 template rendering engine, we can look at the template Makefile, `tools/export/my_makefile/Makefile.tmpl`. 
Documentation on what is available within a jinja2 template is available [here](http://jinja.pocoo.org/docs/dev/templates/).
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
