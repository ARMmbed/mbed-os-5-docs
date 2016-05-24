#The mbed Compiler

**Instant access to your lightweight C/C++ microcontroller development environment**

<span style="display:block; float:right;">
![](/Getting_Started/Images/Compiler/Compiler1.png)
</span>

The mbed Compiler provides a lightweight online C/C++ IDE that is pre-configured to let you quickly write programs, compile and download them to run on your mbed Microcontroller. In fact, you don't have to install or set up anything to get running with mbed. Because it is a web app, you can log in from anywhere and carry on where you left off, and you are free to work on Windows, Mac, iOS, Android, Linux, or all of them.

Watch a demonstration: 

<span style="text-align:center; display:block; padding:20px;">
<a href="http://www.youtube.com/watch?feature=player_embedded&v=7N2RxktXwE4" target="_blank"><img src="http://img.youtube.com/vi/7N2RxktXwE4/0.jpg" 
alt="The mbed compiler" width="480" height="360" border="10" /></a>
</span>

**It is online and lightweight, but it is also powerful.**

The compiler uses the professional ARMCC compiler engine, so it produces efficient code that can be used free-of-charge, even in commercial applications. The IDE includes [workspace version control](/Going_Further/Comp_Ver_Cont/), code formatting and [auto-generation](/Going_Further/Docu/) of documentation for published libraries. The mbed tools are focused on prototyping and are designed for fast experimentation, and complement other professional production-level tools; you can even export directly to [other toolchains](/Going_Further/Export/) if you choose, as you progress to productise your design.

You can [publish projects](/Development/Write_Publish/) directly from your Compiler workspace to the mbed.org website to [share code](http://developer.mbed.org/code/) with others, and pull existing libraries in to your workspace to get a head start.

##Feature Highlights 

###Online Compiler IDE

Every mbed user account gets their own private Compiler workspace which contains their programs. This is private to you, and available wherever you login to mbed.

The IDE includes a full code editor including syntax highlighting, standard editor keyboard shortcuts, undo/redo, cut/copy/paste, tabs, block/line comment, and even a code auto-formater. This is where you work on your personal workspace, with multiple files, folders, programs, including a drag and drop folder interface:

<span style="text-align:center; display:block;">
![](/Getting_Started/Images/Compiler/Compiler2.png)
</span>

The editor also includes features like find and searching across multiple files and filetypes; for example, searching across your whole program. When you search, the results will appear as a list in the compiler output window where you can jump to any of them with a click:

<span style="text-align:center; display:block;">
![](/Getting_Started/Images/Compiler/Compiler3.png)
</span>
<span style="text-align:center; display:block; padding:20px">
![](/Getting_Started/Images/Compiler/Compiler4.png)
</span>

###Integrated Version Control

You can use the built-in version control features to let you version, branch and merge code, with a nice representation of the state of your project history:

<span style="text-align:center; display:block;">
![](/Getting_Started/Images/Compiler/Compiler5.png)
</span>

The approach should be familiar to those of you with experience of distributed version control models (as used by mercurial/git); each program has its own local repository, so you can commit and perform actions on it within your own workspace (such as updating, branching and showing changes).

The main things you can do include:

* Commit a version of your project, and view the revision history

* View changes a version made, and compare changes between versions

* Update or revert to a different version

* Branch and merge

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
See also [Version Control](/Going_Further/Comp_Ver_Cont/).
</span>

###Importing Libraries or Example Programs

The Import Wizard allows you to import programs and libraries published by mbed users. This is useful for importing code that has been packaged as a reusable library component (e.g. a class for a peripheral), so you can quickly pull in the building blocks for your project.

<span style="text-align:center; display:block;">
![](/Getting_Started/Images/Compiler/Compiler6.png)
</span>

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
See also [Importing code](/Getting_Started/Using_IDE/).
</span>

###Compilation

To perform the actual compilation the mbed Compiler uses the industry standard [ARM RVDS 4.1](http://www.arm.com/products/tools/software-tools/rvds/arm-compiler.php) compiler engine, in the default configuration, to give excellent code size and performance. There are no limitations on code size (apart from the limits of the device itself!), and the generated code can be used freely for commercial and non-commercial use.

When you compile a program, you'll get a display of the memory usage. This shows the size of program code and any constant (const) variables that will end up in FLASH, and size of data variables that end up in main RAM. 

<span style="text-align:center; display:block;">
![](/Getting_Started/Images/Compiler/Compiler7.png)
</span>

Note, this doesn't include the runtime allocated variables (i.e. the heap and stack), which live in any remaining RAM.
 
<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
See also the mbed [Memory Model](/Going_Further/Mem_Mo/).
</span>

###Export to Offline Toolchains

The [mbed C/C++ SDK](/Introduction/SDK/) used with the mbed Online Compiler is also compatible with a number of other popular ARM microcontroller toolchains, so we've also built in the ability to export directly to these toolchains! For example, if you'd like to migrate to a different toolchain as your project develops past prototype, you can choose to export an mbed project by right-clicking on it:

<span style="text-align:center; display:block;">
![](/Getting_Started/Images/Compiler/Compiler8.png)
</span>

 <span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
See also the [SDK](/Introduction/SDK/) and [Exporting to offline toolchains](/Going_Further/Export).
</span>

##Feature Overview

Code IDE

* All the core features you expect from a code editor including syntax highlighting, standard [editor keyboard shortcuts](/Getting_Started/IDE_Shortcuts/), copy/paste, etc.

* Personal workspace with multiple files, folders, programs, including drag and drop folder interface.

* Code auto-formatter, print-friendly code preview.

Compile Engine

* Pre-configured compile engine that "just works", delivering .bin binary file to save to mbed microcontroller.

* Switch between different mbed targets with a drop-down selector.
 
* Output of compile-time messages, including click to go to error and error message wiki.
 
* Build information including graphical display of code size and RAM usage.

Built-in Version Control and Collaboration tools
 
* [Built-in version control](/Going_Further/Comp_Ver_Cont/) (DVCS).
 
* Publish, fork, push and pull code in [collaboration-enabled environment](/Community/Collab/).
 
* View graphs, diffs, change sets.

Importing and Exporting
 
* Import programs from online catalogue of [published programs](http://developer.mbed.org/code/).
 
* Publish your code directly from the mbed Compiler to the mbed Developer Website.
 
* Import from and export to local source files and zip archives.
 
* [Export directly](/Going_Further/Export) to other popular ARM toolchains.

Accessibility
 
* Access the mbed Compiler on all major browsers, on all modern operating systems.
 
* Develop and prototype right on your [tablet device](http://developer.mbed.org/handbook/Guide-to-mbed-Compiler-on-tablet-device) (Android, iOS) with the integrated [touch support](http://developer.mbed.org/blog/entry/compiler-touch-support/).
 
* Backward compatible up to Internet Explorer 6.