# Build tools

Mbed OS includes tools for building itself in the `tools` directory. These build tools include target-specific postbuild scripts. When adding a target, you may need to add a postbuild script. Use a postbuild script to modify a linked application binary in ways that the linker cannot, such as inserting a checksum at a specific offset. Postbuild scripts are rarely exportable, and you should use them only when you have exhausted all other options.

## Postbuild scripts

The tools include postbuild scripts for tasks that modify an application binary after it is linked. These tasks are written in Python as static methods of a class within the `tools.targets` module. The tasks are specified as `Class.method` in `targets.json`. 

The tools call the static method with 4 parameters:

 1) Toolchain object. You may use this object for logging.
 2) Resources object used for this build. This contains all of the C, C++ and ASM sources.
 3) Path to the `.elf` file the linker generates.
 4) Path to the binary file generated after link, or the `.elf` file if the code did not generate a binary.

## Implementation

To add a postbuild script, add a class with a single method into the `tools/targets/__init__.py` python file, such as:

```python
class LPCTargetCode(object):
    """General LPC Target patching"""
    @staticmethod
    def lpc_patch(t_self, resources, elf, binf):
        """Patch an elf file"""
        t_self.debug("LPC Patch: %s" % os.path.split(binf)[1])
        from .LPC import patch
        patch(binf)
```

A target that needs this postbuild script run must contain this snippet in `targets/targets.json`:

```JSON
"post_binary_hook": {"function": "LPCTargetCode.lpc_patch"}
```

When implementing a postbuild script, please be aware of the following considerations:

- You may use a `.` in a project name.
- You may change the output file type to any of binary, Intel Hex and `.elf`.
- The Arm compiler generates a directory containing a `.bin` file for each loadable section when there is more than one loadable section.
