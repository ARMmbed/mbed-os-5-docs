<h2 id="mbed-studio">Arm Mbed Studio alpha</h2>

Arm Mbed Studio is a local development environment for Mbed OS projects. This document helps Mbed OS developers use Mbed Studio to code, run, and debug Mbed OS programs to supported Mbed Enabled devices. The Mbed Studio project is based on the Eclipse framework and extends Eclipse’s IDE capability to provide a more focused experience for developing with Mbed OS. In particular, it allows users to develop and run code offline. It also provides access to existing online resources.

### Current status and downloads

Mbed Studio is currently in closed alpha. You can [request access](https://os.mbed.com/studio/) if you're happy to provide feedback. During this phase, some features are still in progress, and there are frequent updates to the product. The user interface will also change during this phase, so the screenshots below will correspondingly change.

### Prerequisites

We currently support only DAPLink devices and use pyOCD for debug. This means that you need a supported development board with updated DAPLink firmware during the alpha phase.

### Getting started

This section shows the steps of creating, exploring, running and debugging an example project packaged with Mbed Studio. After reading it, you will have a better understanding of how you can use Mbed Studio to develop for Mbed OS. Start Mbed Studio, and follow the steps below.

#### On startup

When you launch Mbed Studio, you see a login screen (unless you're using an internal release), which requires you to sign in with your Mbed username and password. Sign in with your Mbed credentials. If you're an alpha user, you can continue through to the workspace.

#### Creating a new project based on an example

When you arrive in your workspace, it's empty - clean, white and lacking in programs. It's time to start populating it.

The first step is to create a project based on the included `mbed-os-example-blinky` example. You can do this using the Mbed Studio menu or using the context menu in the Mbed Projects view of Mbed Studio.

To use the context menu, right-click (Ctrl-click) inside the Mbed Projects or Mbed Projects view, and then select `New > Mbed OS Application`. To do the same through the menu, click `File > New > Mbed OS Application` to activate the New Project wizard.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Mbed-Studio-New-Application.png)<span>Create a new Mbed OS application.</span></span>

Now, create a new project through the activated New Project wizard. Select the `From Supplied Example` radio button, and then select the `mbed-os-example-blinky` example from the list of examples. Continue through the wizard by clicking the `Next` button.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Mbed-Studio-New-Project-Wizard.png)<span>Click through the new project wizard.</span></span>

Fill in the project name (you can be creative or just use the default example name), and update the location to match (`/path/to/project_name` for example: `/eclipse-ws/mbed-os-example-blinky`). Mbed Studio uses the project name, not the location name, to name created binaries. Once these steps are complete, click the `Finish` button in the lower part of the wizard window.

Additionally, you can create a blank project with the `Empty Project` radio button. As a result, you can click `Finish` without continuing, which creates a blank project.

Mbed Studio now begins to create the project in the workspace and shows its progress on the final screen of the wizard. Once complete, you can see the project in your workspace within the Mbed Projects view.

##### Active and inactive projects

Mbed Studio introduces the concept of an active project into Eclipse. The user interface updates automatically based on target selection and the active project, rather than requiring you as the user to create lots of different build and debug configurations. This creates behavior that is more consistent with our Online Compiler and adds default behavior to icons such as build, run and debug.

New projects become the active project by default, and you can make a project active by right-clicking and selecting `Set as active project`.

#### Explore or edit the project

Mbed Studio provides support for formatting, syntax highlighting, locating files, comparing files and navigating to lower level code, such as pin definitions for your target hardware. For a more general look at the features provided by Eclipse, consult the [Eclipse](http://help.eclipse.org/neon/index.jsp) online help documentation.

Now, there is a project located in the `Mbed Projects` view with the name `mbed-os-example-blinky` (or whatever project name you provided earlier). Clicking the triangle next to the project expands its contents and reveals the project’s current files and directories.

Double-click on the `main.cpp` file to open it in Mbed Studio’s editor. This file includes the code needed to blink an LED. 

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Mbed-Studio-Blinky-Main-CPP.png)<span>Explore your new project.</span></span>

#### Adding libraries to a project

Mbed Studio supports importing libraries from GitHub. To import a library, right-click on the `Mbed Projects` view, and select `Import`. Now click `Mbed > Import Mbed library into existing project`. Choose the program that you want to add the library to.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Mbed-Studio-Import-Library.png)<span>Import an Mbed library.</span></span>

Next, choose a library and copy the URL for the GitHub repository.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Mbed-Studio-GitHub-Library-URL.png)<span>Choose a library from GitHub.</span></span>

Click `Finish`, and Mbed Studio adds the library to your program of choice.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Mbed-Studio-ESP8266-Library.png)<span>The imported library in the workspace.</span></span>

### Connecting a board

Connect an [Mbed Enabled development board](https://os.mbed.com/platforms/) to your machine, or select a target development board from the target dropdown. Mbed Studio detects the board, and a dialog asks to switch targets. Accept this, and you are ready to build and run the example.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Mbed-Studio-Target-Selection.png)<span>Select a target development board.</span></span>

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Mbed-Studio-Target-Auto-Detection.png)<span>Mbed Studio autodetects DAPLink-compatible boards that you have connected through USB.</span></span> 

#### Running the project

This section covers the necessary steps of building and running the project on a connected board. Mbed Studio must recognize the board for the instructions in the Run section to work.

### Build

Before you can run the program, Mbed Studio needs to build a binary using a compiler. For the alpha version of Mbed Studio this compiler is GCC. There are multiple ways to start a build, but the easiest is to click the build icon.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Mbed-Studio-Build-Button.png)<span>Build your project.</span></span>

Alternatively, you can right-click (Ctrl-click) on the project in the `Mbed Projects` view and then select `Build Project`. You can also use the menu by choosing `Project > Build Project`. Both build a binary that you can run on your board.

Alternatively, you can choose to build the project automatically through the menu by choosing `Project > Build Automatically`. This tells Mbed Studio to build the projects in the workspace whenever needed. After the build, an `mbed-os-example-blinky.bin` (or `<project name>.bin`) file is ready to run.

Once the build completes, the build artifacts, such as the .bin and .elf binaries, are in the `BUILD` folder under the active project. 

#### Further exploration

Once you have built a project for a given target board, Eclipse can also index the `mbed-os-example-blinky` project, which means that it creates the appropriate mappings for the selected target. You can refresh this index by right-clicking on the project and selecting `Index > Freshen all files`. After Eclipse completes the indexing process, you can use the `Open declaration` function, or `F3` as a shortcut while hovering over a pin name, such as `led1`. This allows you to look through the dependency tree of the application and explore the underlying Mbed OS library.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Mbed-Studio-Pin-Mapping.gif)<span>Press F3 to open a declaration, such as an IO pin name.</span></span> 

#### Building automatically

Mbed Studio uses the tools built into Mbed OS to determine what builds and where the output of a build goes. The build tools build on request or (if the `Project > Build Automatically` option is checked) when you change and save a source file. The build operation only builds components that have changed and does nothing if nothing changed. Mbed Studio regards all projects in the workspace as part of the same system, so it initially builds all projects. Pressing the build button also ensures that all workspace projects build (if required).

The aim is to maintain a system that is always in a built state, providing rapid error feedback to developers as they make changes.

Under some circumstances (in particularly large projects, or when the target device changes frequently), you may wish to turn off automatic builds and build individual projects on request. To do this, select Build from the project right-click menu.

### Run

Now that you have built the `mbed-os-example-blinky project`, you can run it on your target board. Running a project consists of several phases, which you can abstract if you click the green run icon.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Mbed-Studio-Run.png)<span>Run your project.</span></span>

The Mbed Studio run phases are:

- Locate or create a suitable binary.
- Flash the binary to the target.
- Reset target, causing the new program to run.

Although you manually built the project in the previous section and learned how to build a project in Mbed Studio, it wasn’t necessary before running. That’s because Mbed Studio checks that there is a binary for the currently selected target. If there isn’t one, Mbed Studio begins a compilation to create the binary. If there is a binary and there are no recent changes (build automatically option is on), Mbed Studio uses the existing binary to run the project.

Once Mbed Studio has a binary of the Mbed OS program, it flashes that binary to the currently selected development board and resets the board, so the program begins to run.

To make it happen, click the green run icon to launch the default run configuration for your connected development board.

Watch the primary LED on your connected target begin to blink!

### Debug

Now that you have learned the basics of Mbed Studio, it is time to learn how to debug projects within the IDE. There is a debug configuration specifically for debugging Mbed OS projects, which generates automatically. To launch a debug session on your development board, click the debug icon.

There are also additional configurations for more advanced debugging. This section covers the Mbed OS debug configuration, as well as the advanced PyOCD GDB debug configuration.

#### Simple debugging

To begin debugging, click the bug icon, which launches the default debug configuration. A prompt asks you to switch to the debug perspective. Click `Yes` to switch. The debug perspective opens additional views, including a Debugger console, Debug view (which shows active threads and where the debugger stops), Variables, Memory and your code editor, which stops on a breakpoint by default.

Additional icons are available in the menu bar for controlling the step debugger. Click these to advance the debugger, or click the green play/pause icon to resume execution.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/Mbed-Studio-Debug-Perspective.png)<span>Mbed Studio debug perspective, showing the debugger stopped on a breakpoint</span></span>

Alternatively, you can create the debug launch configuration and then begin debugging. To create a debug launch configuration, right-click on a project, and select `Debug As... > Debug Configurations` from the context menu.

Click `Choose...` next to the project textbox, and select the project you wish to debug if it isn’t already populated. After that, connect a board. The Mbed Debug launch configuration prepopulates the PyOCD GDB server and the GDB client to locations to the internal Mbed Studio tools. Select the Debug button in the lower right portion of the window to start debugging.

Mbed Studio automatically switches into the Mbed Debug perspective when debugging with the Mbed Debug launch configuration. The project also brakes on a default break point.

#### Advanced debugging

If you want more control over the options regarding debugging, this section is for you. This section describes how to create a PyOCD GDB debug configuration. This configuration allows you to change more settings, such as ports and executable locations for the GDB client and server.

To begin debugging, create the debug launch configuration and set some variables. (You may use your own values if you don’t want to use the default provided here.) To create a debug launch configuration, as before, right-click on a project, and select `Debug As... > Debug Configurations` from the context menu.

A window for the debug configurations appears. Select the `GDB PyOCD Debugging` category, and create a new launch configuration. You can click the new icon (a page with a `+` in the upper right corner), or right-click on the category and select `New`.

Next, configure the binary you want to use for debugging. This is the `.elf` file located within the project directory and inside `BUILD/<target>/GCC_ARM`. Currently, this is configured manually, so switching to a different target to run the same project requires you to update this field in the debug configuration.

The next step is to configure the location of the executables for the PyOCD GDB Server and the GDB Client on the Debugger tab within the debug configuration. These should be set to the executables located within Mbed Studio’s tools directory which is located at:

`/eclipse-ws/mbed-studio-ws/tools`

Alternatively, and at your own risk, you may select executables from locations elsewhere on your machine.

On *nix machines, the two bundled executables are located at:

`/eclipse-ws/mbed-studio-ws/tools/python/bin/pyocd-gdbserver`
`/eclipse-ws/mbed-studio-ws/tools/gcc-arm/bin/gcc-arm-none-eabi-gdb`

On Windows machines, the two bundled executables are located at:

`\eclipse-ws\mbed-studio-ws\tools\python\Scripts\pyocd-gdbserver.exe`
`\eclipse-ws\mbed-studio-ws\tools\gcc-arm\bin\gcc-arm-none-eabi-gdb.exe`

When you have configured everything, select `Apply` in the lower right side of the panel, and the click the blue Debug button just below that.

### Help

This section outlines known issues and provides answers to common questions.

#### Glossary

##### Workspace

Mbed Studio automatically sets up the workspace. Use it to keep track of settings and user preferences for all of the projects you open in Mbed Studio.

##### Project

A project is a group of associated files, directories and settings. The `Mbed Projects` view lists these projects. In Mbed Studio, each project represents an Mbed OS program or an Mbed OS library. An Mbed Studio project can also represent a program that includes libraries, as well.

##### View

In Mbed Studio, a view is a window that has a label, and sometimes options, specific to that window. Examples are the editor, Mbed Projects, Console and Outline.

##### Perspective

A perspective is a collection of views, which group functionally in Eclipse. An example of a perspective is the debug perspective.

##### Program

This term denotes a project that contains code that runs on an Mbed Enabled device.

##### Library

This term denotes a project that contains code meant to be included in other Mbed OS programs.

### Known issues

This section lists known issues that currently exist in Mbed Studio.

#### General

Currently, Mbed Studio does not communicate with ST boards because they don’t use DAPLink by default.
Workaround: None

#### Mac

The `Eclipse.app` distributed for Mac is not yet signed. Mac OS X may show errors about unknown developers when you double-click to launch.
Workaround: To launch, Ctrl-click on `Eclipse.app`, and choose `Open`. Then, approve the open action on subsequent warning dialogs.

When CDT (C/C++ Developer Tooling) performs a build, it tries to use the system GCC. If it is not present, Mac OS X prompts to install the Xcode command-line tools.
Workaround: None. Follow the prompts to install the command-line tools, and restart Mbed Studio.

#### Linux

Mbed Studio does not currently pick up target boards in the Linux version. This is an issue with the detection of USB. Interacting with boards is not possible currently.
Workaround: None

#### Windows

GCC builds are slower in Windows than Mac or Linux.
Workaround: None, this is also the case when using GCC from the command-line.

### FAQ

This section includes common questions and answers.

Q: How can I tell if I already have a working Java install?
A: From the command-line, run: `java -version`. You have a working Java install if you see something similar to the following:

`java version "1.8.0_141"`
`Java(TM) SE Runtime Environment (build 1.8.0_141-b15)`
`Java HotSpot(TM) 64-Bit Server VM (build 25.141-b15, mixed mode)`

If not, follow the instructions earlier in this document to install Java.

Q: I have Java installed. Why won’t Mbed Studio launch?
A: Mbed Studio is a 64-bit only application, which requires not only a 64-bit OS, but also a 64-bit Java JDK/JRE installed on the OS.
The 64-bit JDK/JRE needs to be the system default, or you may have to manually configure internal Mbed Studio initialization files to use the 64-bit JDK/JRE.

Q: Will Mbed Studio work with Java 9?
A: Currently, Mbed Studio does not work with Java 9, but later versions will.
