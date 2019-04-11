# Generating API Documentation

API documentation tells you what you need to know to use a library or work with a program. It details functions, classes, return types and more.

In Arm Mbed, API documentation for programs and libraries is fully supported both within the Arm Mbed Online Compiler and in the code listings on the public site.

## Browsing API documentation from within the Arm Mbed Online Compiler

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/docs_in_library_1.png)![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/docs_in_library_2.png)</span>

Each documentation group contains only the documented definitions for that group:

- Classes: classes and methods.

- Structs: struct and union data types.

- Files: functions, variables, enums, defines, references to struct and unions, but no namespaces and classes.

- Groups: defined by the author; grouped documentation elements such as files, namespaces, classes, functions, variables, enums, typedefs, defines and others for quick reference.

<span class="notes">**Note:** Undocumented classes, methods, functions and so on that exist in the source code won't appear in the documentation.</span>

## Viewing documentation

The documentation preview contains references presented as standard links that point to subsections of the document or to other documents. They open inside the Mbed Online Compiler when clicked:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/docs_preview1.png)</span>

Clicking one of the "Definition at line X of file source.c" links would open the definition source file in the Editor (see below). You can also open the definition source file with the "Go to definition" option in the context menu from the navigation tree:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/docs_preview2.png)</span>

<span class="notes">
**Note:** The documentation groups and individual documents **do not exist in your workspace**. They are meta navigation items that reflect the API documentation as present in the library's home page, so they cannot be moved, deleted, renamed and so on.
</span>

## New file from documentation example

Another notable feature of the API documentation in the Mbed Online Compiler is the ability to create new files from documentation examples, making it easier to try them. The Mbed Compiler prompts for file name and may suggest `main.cpp` if that file doesn't already exist in the program root:

## How to add documentation to your own programs and libraries

The documentation is created out of comment blocks in your code, usually located above declarations and definitions. Let's take the following example:

```c++
class HelloWorld {
	public:
		HelloWorld();
		void printIt(uint32_t delay = 0);
};
```

### Marking comments for documentation

The most important thing about code documentation is explicitly telling the system that a comment is intended for documenting (and isn't just an ordinary comment). To do that:

1. Put the comment block just above the definition.
1. Start the comment block with `/**` or `/*!` (as opposed to `/*`, which is a normal comment).


```c++
/** My HelloWorld class.
*  Used for printing "Hello World" on USB serial.
*/
class HelloWorld {
	public:
		/** Create HelloWorld instance */
		HelloWorld();

		/** Print the text */
		void printIt(uint32_t delay = 0);
};
```

You can also document single line comments, by starting them with `///` or `//!`:

```c++
//! My HelloWorld class. Used for printing "Hello World" on USB serial.
class HelloWorld {
	public:
	/// Create HelloWorld instance
	HelloWorld();

	/// Print the text
	void printIt(uint32_t delay = 0);
};
```

It requires almost no effort to translate scattered comments in code into well formatted documentation descriptions!

## Comment markup

Documentation has special markup to describe parameters, return values, notes, code examples and so on.

Doxygen accepts reserved words prefixed with `\` or `@`. Some of the commonly used ones are:

* `@param <name> text`

* `@return text (synonym @returns)`

* `@note text`

* `@group <name>`

* `@code example @endcode`

* `@see ref [, ref2...] (synonym @sa)`

Here is an example of advanced documentation:

```c++
/** My HelloWorld class.
*  Used for printing "Hello World" on USB serial.
*
* Example:
* @code
* #include "mbed.h"
* #include "HelloWorld.h"
*
* HelloWorld hw();
*
* int main() {
*     hw.printIt(2);
* }
* @endcode
*/
class HelloWorld {
	public:
		/** Create HelloWorld instance
		*/
		HelloWorld();

		/** Print the text
		*
		* @param delay Print delay in milliseconds
		* @returns
		*   1 on success,
		*   0 on serial error
		*/
		void printIt(uint32_t delay = 0);
};
```

To generate documentation for the example above, you have to click **Compile** > **Update Docs**:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/docs_update.png)</span>

Once the docs are generated, the navigation tree is refreshed, and you can see the formatted documentation:

<span class="images">![](images/docs_example.png)</span>

## Additional notes

Doxygen is the core of the documentation generation in the Arm Mbed ecosystem:

- Doxygen is compatible with Javadoc and other documentation styles. Refer to the [Doxygen manual](http://www.stack.nl/~dimitri/doxygen/manual.html) for more information.

- Doxygen won't process the `main.cpp` file unless referenced in another file using `/** @file main.cpp */` markup. It's generally a good idea to split definitions and defines into library (libraries) instead; do not rely on ``main.cpp`` file documentation.

- Doxygen can process comments located right next to definitions and declarations, and also at other places. Refer to [documentation at other places](http://www.stack.nl/~dimitri/doxygen/docblocks.html#structuralcommands) in the Doxygen manual.
