#API Documentation

##What is API documentation?

API documentation is a quick and concise reference containing what you need to know to use a library or work with a program. It details functions, classes, return types, and more.

In mbed, API documentation for programs and libraries is fully supported both within the Compiler and in the code listings on the public site. 

##Browsing API documentation from within the mbed Compiler

<span style="text-align:center; display:block;">
![](/Going_Further/Images/API_Docs/APIDOCS1.png)
</span>

Each documentation group contains only the documented definitions for that group as follows:

* Classes - documented classes and methods

* Structs - documented struct and union data types

* Files - documented functions, variables, enums, defines, also references to struct and unions, but no namespaces and classes

* Groups - defined by the author, grouped documentation elements like files, namespaces, classes, functions, variables, enums, typedefs, defines and other groups for quick reference - e.g. [mbed library Device Peripheral Registers](http://developer.mbed.org/users/mbed_official/code/mbed/).

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
**Note:** Classes, methods, functions, etc which exist in the source code but aren't documented won't appear in the documentation.
</span>

The documentation preview contains references presented as standard links (default in blue) that point to sub-sections of the document or point to other documents, and which once activated would open inside the mbed Compiler.

<span style="text-align:center; display:block;">
![](/Going_Further/Images/API_Docs/APIDOCS2.png)
</span>

Clicking one of the "Definition at line of file source.c" links would open the definition source file in the Editor (see below). The definition source file can also be opened with "Go to definition" option in the context menu from the navigation tree.

<span style="text-align:center; display:block;">
![](/Going_Further/Images/API_Docs/APIDOCS3.png)
</span>

Another notable feature of the API documentation in the mbed Compiler is the ability to create new files from documentation examples, making it easier to try them. The mbed Compiler would prompt for file name and may suggest main.cpp as name if it doesn't exist in the program root.

<span style="background-color:lightyellow; color:black; display:block; height:100%; padding:10px">
**Warning:** The documentation groups and individual documents **do not exist in your workspace**. They are meta navigation items that reflect the API documentation as present in the library home page, and as such they cannot be moved, deleted, renamed, etc.
</span>

##How to add documentation to your own programs and libraries

The documentation is created out of comment blocks in your code, usually located above declarations and definitions. Let's take the following example:

```c

	class HelloWorld {
		public:
			HelloWorld();
			printIt(uint32_t delay = 0);
	};
```

**First** important thing about documenting a code is to give hint to the documentation system that a comment is intended for documenting, that it's not an ordinary comment. To do that a comment block should start with ``/**`` or ``/*!`` sequences (as opposed to ``/*``), and that comment block should be just above the definition:

```c

	/** My HelloWorld class.
	*  Used for printing "Hello World" on USB serial.
	*/
	class HelloWorld {
		public:
			/** Create HelloWorld instance */
			HelloWorld();

			/** Print the text */
			printIt(uint32_t delay = 0);
	};
```

It's also possible to use single line comments starting with ``///`` or ``//!``.

```c

	//! My HelloWorld class. Used for printing "Hello World" on USB serial.
	class HelloWorld {
		public:
		/// Create HelloWorld instance
		HelloWorld();

		/// Print the text
		printIt(uint32_t delay = 0);
	};
```

It requires almost no effort to translate scattered comments in code into well formatted documentation descriptions!

**Second** important thing about the documentation process is the documentation markup to describe parameters and return values, but also to notes, groups, code examples and more.
Doxygen accepts reserved words prefixed with ``\`` or ``@``, where some of the commonly used are:

* @param <name> text

* @return text (synonym @returns)

* @note text

* @group <name>

* @code example @endcode

* @see ref [, ref2...] (synonym @sa)

Here is an example of advanced documentation:

```c

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
			printIt(uint32_t delay = 0);
	};
```

To generate documentation for the example above, you have to click the **Update Docs** menu item in the **Compile** dropdown:

<span style="text-align:center; display:block;">
![](/Going_Further/Images/API_Docs/APIDOCS5.png)
</span>

Once generated the navigation tree would refresh and the formatted documentation would look like this:

<span style="text-align:center; display:block;">
![](/Going_Further/Images/API_Docs/APIDOCS4.png)
</span>

Congratulations! You now know how to document a library.

##Extra Features

Not only do you get the API documentation, but you can insert code and API documentation in to your wiki pages, notebook pages, questions, forum posts, etc.

##Example

<div class="flashbox flibrary"><span style="background-color:lightyellow; color:gray; display:block; height:100%; padding:10px"><h4 class="ftitle"><a class="button small radius" style="font-weight: bold; position: relative; float: right;" href="https://developer.mbed.org/compiler/#import:/users/simon/code/Servo/;mode:lib" target="compiler">Import library</a><a href="http://mbed.org/users/simon/code/Servo/docs/tip/classServo.html"><span></span></a><div class="wiki-api-header"><a href="http://mbed.org/users/simon/code/Servo/docs/tip/classServo.html"></a><a href="http://developer.mbed.org/users/simon/code/Servo/docs/36b69a7ced07//classServo.html">Servo - Servo Class Reference</a></div></h4><div><div class="wiki-api-snippet"><table class="memberdecls">
<tbody>
 
<table style="width:100%" border="1">
<tr style="background-color:white">
  <td colspan="2">
   <h2>
    <a name="pub-methods">
    </a>
    Public Member Functions
   </h2>
  </td>
 </tr>
 <tr>
  <td align="right" class="memItemLeft" valign="top">
   &nbsp;
  </td>
  <td class="memItemRight" valign="bottom" >
   <a class="el" href="http://developer.mbed.org/users/simon/code/Servo/docs/36b69a7ced07/classServo.html#a550914ccdb13d817f6460dd80aec23c3">
    Servo
   </a>
   (PinName pin)
	<br />
   Create a servo object connected to the specified PwmOut pin.
   <a href="http://developer.mbed.org/users/simon/code/Servo/docs/36b69a7ced07/#a550914ccdb13d817f6460dd80aec23c3">
   </a>
   <br>
  </td>
 </tr>
 <tr>
  <td align="right" class="memItemLeft" valign="top">
   void&nbsp;
  </td>
  <td class="memItemRight" valign="bottom">
   <a class="el" href="http://developer.mbed.org/users/simon/code/Servo/docs/36b69a7ced07/classServo.html#adf6f102a108f8093b48c08b1f72d5413">
    write
   </a>
   (float percent)
  <br />
   Set the servo position, normalised to it's full range.
   <a href="http://developer.mbed.org/users/simon/code/Servo/docs/36b69a7ced07/#adf6f102a108f8093b48c08b1f72d5413">
   </a>
   <br>
  </td>
 </tr>
 <tr>
  <td align="right" class="memItemLeft" valign="top">
   float&nbsp;
  </td>
  <td class="memItemRight" valign="bottom">
   <a class="el" href="http://developer.mbed.org/users/simon/code/Servo/docs/36b69a7ced07/classServo.html#a868d9d1513fbaf34c4d5d15a7fa4baa8">
    read
   </a>
<br/ >
   Read the servo motors current position.
   <a href="http://developer.mbed.org/users/simon/code/Servo/docs/36b69a7ced07/#a868d9d1513fbaf34c4d5d15a7fa4baa8">
   </a>
   <br>
  </td>
 </tr>
 <tr>
  <td align="right" class="memItemLeft" valign="top">
   void&nbsp;
  </td>
  <td class="memItemRight" valign="bottom">
   <a class="el" href="http://developer.mbed.org/users/simon/code/Servo/docs/36b69a7ced07/classServo.html#a9c41903bf587e02b4f57eb957ae82341">
    position
   </a>
   (float degrees)
<br />
   Set the servo position.
   <a href="http://developer.mbed.org/users/simon/code/Servo/docs/36b69a7ced07/#a9c41903bf587e02b4f57eb957ae82341">
   </a>
   <br>
  </td>
 </tr>
 <tr>
  <td align="right" class="memItemLeft" valign="top">
   void&nbsp;
  </td>
  <td class="memItemRight" valign="bottom">
   <a class="el" href="http://developer.mbed.org/users/simon/code/Servo/docs/36b69a7ced07/classServo.html#ab9876359dc71baa008846bef055cbaaf">
    calibrate
   </a>
   (float range=0.0005, float degrees=45.0)
<br />
   Allows calibration of the range and angles for a particular servo.
   <a href="http://developer.mbed.org/users/simon/code/Servo/docs/36b69a7ced07/#ab9876359dc71baa008846bef055cbaaf">
   </a>
   <br>
  </td>
 </tr>
 <tr>
  <td align="right" class="memItemLeft" valign="top">
   <a class="el" href="http://developer.mbed.org/users/simon/code/Servo/docs/36b69a7ced07/classServo.html">
    Servo
   </a>
   &amp;&nbsp;
  </td>
  <td class="memItemRight" valign="bottom">
   <a class="el" href="http://developer.mbed.org/users/simon/code/Servo/docs/36b69a7ced07/classServo.html#a99dd298eb7dad01cf06fa65b7761b149">
    operator=
   </a>
   (float percent)
<br />
   Shorthand for the write and read functions.
   <a href="http://developer.mbed.org/users/simon/code/Servo/docs/36b69a7ced07/#a99dd298eb7dad01cf06fa65b7761b149">
   </a>
   <br>
  </td>
 </tr>
</tbody>
</table>
</div></div></span></div>


These are done using the ``library``  macro and the URLs of the documentation you wish to pull in:

```

	<<library http://mbed.org/users/simon/code/Servo/docs/36b69a7ced07/classServo.html>>
	
	<<library http://mbed.org/users/simon/code/Servo/docs/tip/classServo.html>>
	
	<<library http://mbed.org/users/simon/code/Servo/>>
```

Each public documentation page has a handy Embed code box which you can copy and paste into your wikipage.

Note the difference URL above with 'tip' and the one with a mercurial revision hash. Linking to documentation with a 'tip' URL will mean that the page will always show the latest documentation for your library.

See [Wiki syntax](http://mbed.org/cookbook/Wiki-Syntax) for more details.

##Additional notes

Last but not least, a few notes about Doxygen as being the core of the documentation generation in the mbed ecosystem:

* Doxygen is compatible with Javadoc and other documentation styles. Refer to the [Doxygen manual](http://www.stack.nl/~dimitri/doxygen/manual.html) for more information.

* Doxygen won't process the ``main.cpp`` file unless referenced in another file using ```/** @file main.cpp */``` markup. It's generally good idea to split definitions and defines into library (libraries) instead and do not rely on ``main.cpp`` file documentation.

* Doxygen can process comments located right next to definitions and declarations, and also at other places. Refer to [documentation at other places](http://www.stack.nl/~dimitri/doxygen/docblocks.html#structuralcommands) in the Doxygen manual.

##Final words

There is so much more to be said about API documentation that isn't covered by this guide. How it improves direct and indirect collaborative development of complex programs and libraries. How the documentation preview can improved even further with groups, brief descriptions, etc. No doubt that documenting a code is an added effort on top of the code development. But if that extra effort could enable everyone to efficiently utilize the code and its features, then may be that effort is as important as the code itself. 

For further information about the Doxygen markup and more examples you can visit the [Doxygen manual](http://www.stack.nl/~dimitri/doxygen/manual/index.html) on their website.