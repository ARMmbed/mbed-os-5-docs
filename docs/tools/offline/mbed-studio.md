<h2 id="mbed-studio">Arm Mbed Studio</h2>

Arm Mbed Studio is a local development environment for Mbed OS projects. This document helps Mbed OS developers use Mbed Studio to code, run, debug and deploy Mbed OS programs to Mbed Enabled devices. The Mbed Studio project is based on the Eclipse framework and extends Eclipse’s IDE capability to provide a more focused experience for developing with Mbed OS. In particular, it allows users to develop and deploy code offline. It also provides access to existing online resources.

### Current status and downloads

Mbed Studio is currently in closed alpha. You can request access here if you're happy to provide feedback. During this phase, some features are still in progress, and there are frequent updates to the product.

### Getting started

This section shows the steps of creating, exploring, running and debugging an example project packaged with Mbed Studio. After reading it, you will have a better understanding of how you cna use Mbed Studio to develop for Mbed OS. Start Mbed Studio, and follow the steps below.

#### On startup

When you launch Mbed Studio, you see a login screen (unless you're using an internal release), which requires you to sign in with your Mbed username and password. Sign in with your Mbed credentials. If you're an alpha user, you can continue through to the workspace.

#### Creating a new project based on an example

When you arrive in your workspace, it's empty - clean, white and lacking in programs. It's time to start populating it.

The first step is to create a project based on the included `mbed-os-example-blinky` example. You can do this using the Mbed Studio menu or using the context menu in the C++ Projects view of Mbed Studio. To use the context menu, right-click (Ctrl-click) inside the Mbed Projects or C++ Projects view, and then select `New > Mbed OS Application`. To do the same through the menu, click `File > New > Mbed OS Application` to activate the New Project wizard. Now, create a new project through the activated New Project wizard. Select the `From Supplied Example` radio button, and then select the `mbed-os-example-blinky` example from the list of examples. Continue through the wizard by clicking the `Next` button. Fill in the project name (you can be creative or just use the default example name), and update the location to match (`/path/to/project_name` for example: `/eclipse-ws/mbed-os-example-blinky`). Mbed Studio uses the project name, not the location name, to name created binaries. Once these steps are complete, click the `Finish` button in the lower part of the wizard window. Additionally, you can create a blank project with the `Empty Project` radio button. As a result, you can click `Finish` without continuing, which creates a blank project.

Mbed Studio now begins to create the project in the workspace and shows its progress on the final screen of the wizard. Once complete, you can see the project in your workspace within the Mbed Projects view.

#### Explore or edit the project

Mbed Studio provides support for formatting, syntax highlighting, locating files, comparing files, and navigating through to lower level code, such as pin definitions for your target hardware. For a more general look at the features provided by Eclipse, consult the [Eclipse](http://help.eclipse.org/neon/index.jsp) on-line help documentation.
There should now be a project located in the “C++ Projects” with the name “mbed-os-example-blinky” (or whatever project name you provided earlier). Clicking the triangle next to the project should expand its contents, revealing the project’s current files and directories.
Double-click on the `main.cpp` file to open it in Mbed Studio’s editor area. This file includes the code needed to blink an LED. If you haven’t done so already, connect an Mbed Enabled board (such as the FRDM-K64F) to your machine. Mbed Studio should detect the board and prompt you with a dialog asking to switch targets. Accept this and you will be ready to run the example!

#### Running the project

This section covers the necessary steps of building and running the project, so the program deploys and runs a connected board. Mbed Studio must recognize the board for the instructions in the Run section to work. This documentation uses the FRDM-K64F throughout.

##### Build

Before the program can be run, a binary needs to be built by Mbed Studio. There are multiple ways of starting a build, but the easiest is to click the build icon.
Alternatively, you can right-click (Ctrl-click) on the project in the “C++ Projects” view and then select Build Project. You can also use the menu by choosing: `Project > Build Project`. Both will begin to build a binary that can be deployed.
Alternatively, you can choose to have the project built automatically through the menu by choosing: `Project > Build Automatically`. This tells Mbed Studio to build the projects in the workspace whenever it is needed. After the build, there should be a `mbed-os-example-blinky.bin` (or `<project name>.bin`) file ready to deploy.

##### Building within Mbed Studio

Mbed Studio uses the tools built in to the Mbed OS to decide what should be built and where the output of a build should go. The build tools will build on request or (if the `Project > Build Automatically` option is checked) when a source file is changed and saved. The build operation will only build those components that have changed and will do nothing if nothing has changed. All projects in the workspace are regarded as part of the same system, so initially all projects will be built. Pressing the build button will also ensure that all workspace projects are built (if required).
The aim is to maintain a system that is always in a built state, providing rapid error feedback to developers as changes are made.
Under some circumstances (in particularly large projects, or where the target device is changing frequently) you may wish to turn off automatic builds and build individual projects on request. To do this, select Build from the project right-click menu.

##### Run

Now that you have built the `mbed-os-example-blinky project`, we can run it. Running a project consists of several phases, which are abstracted if you click the green run icon.
We will go through the run phases here, as well as, explain how to run a project from within Mbed Studio.
The Mbed Studio run phases are:
- Locate/Create a suitable binary
- Deploy the binary to the target
- Reset target, causing the deployed program to run
While we manually built the project in the previous section, which was meant to show how building a project can be done in Mbed Studio, it wasn’t absolutely necessary before running. That’s because Mbed Studio checks that there is a binary for the currently selected target. If there isn’t one, Mbed Studio will begin a compilation to create the binary. If there is a binary and there are no recent changes (build automatically option is on), the existing binary will be used for running the project.
Once Mbed Studio has a binary of the Mbed OS program, it will deploy that binary to the currently selected target and reset the target so that the program will begin to run.
Let’s make it happen. Click the green run icon to launch the default run configuration for your connected development board.
Alternatively, open the context menu (right-click, ctrl-click) on the `mbed-os-example-blinky` project and select `Run As > Run Configurations...` from the menu. You can also use the menu by selecting `Run > Run Configurations` (both ways shown below).
In the “Run Configurations” window, right-click on Mbed Deploy and select New to create a “Mbed Deploy” run configuration. This will create the run configuration we need to populate with details of our project and target. For project (if everything isn’t already populated), click `Choose` and select the `mbed-os-example-blinky` project. The binary built by Mbed Studio will fill in automatically. If you used a different project name, remember that the binary name will reflect that. Finally, click the Refresh button to ensure that the current target board’s ID is updated if it isn’t already.
After everything is configured properly, click on the Apply button, and then on the Run button.
Now the primary LED on your connected target should begin to blink!

#### Debugging

Now that the basics of Mbed Studio have been covered, it is time to detail how to debug projects within the IDE. There is a simplified debug configuration specifically for easy debugging of Mbed OS projects. There are also additional configurations for more advanced debugging as well. This section will cover the Mbed OS Debug configuration as well as the advanced PyOCD GDB Debug configuration.

##### Simple debugging

To begin debugging, click the bug icon, which will launch the default debug configuration.
Alternatively, we can create the debug launch configuration and then begin debugging. To create a debug launch configuration right click on a project and select `Debug As... > Debug Configurations` from the context menu (you can also use the menu bar as shown below).
Once created, the configuration will pre-populate all the values that can readily be inferred. Click Choose... next to the project textbox and select the project you wish to debug (if it isn’t already populated). After that, and when there is a board connected, the project will be ready to debug. The Mbed Debug launch configuration pre-populates the PyOCD GDB server and the GDB client to locations to the internal Mbed Studio tools. Select the Debug button in the lower right-hand portion of the window to start the Debugging.
Mbed Studio will automatically switch into the Mbed Debug perspective when debugging with the Mbed Debug launch configuration. The project will also break on a default break point, the resulting workspace should look like the image below.

##### Advanced debugging

If you want to have more control over the options regarding debugging, this section is for you. This section will describe how to create a PyOCD GDB debug configuration. This configuration allows you to change more settings like ports and executable locations for the GDB client and server.
To begin debugging, we will create the debug launch configuration and set some variables (you may use your own values if you don’t want to use the default provided here). To create a debug launch configuration, as before, right click on a project and select Debug As... > Debug Configurations from the context menu.
You should now see a window for the debug configurations. Select the GDB PyOCD Debugging category and create a new launch configuration. The new icon (a page with a + in the upper right hand corner) can be clicked, or right click on the category and select New. See the screenshot above, on the right hand side.
Next, configure the binary to be used for debugging. This is the .elf file located within the project directory and inside `BUILD/<target>/GCC_ARM` (for this example it is BUILD/K64F/GCC_ARM). Currently this is configured manually, so switching to a different target to run the same project requires this field to be updated in the debug configuration. See the below, left screenshot.
The next step is to configure the location of the executables for the PyOCD GDB Server and the GDB Client on the Debugger tab within the debug configuration. These should be set to the executables located within Mbed Studio’s tools directory which is located at:
`/eclipse-ws/mbed-studio-ws/tools`
Alternatively, and at your own risk, you may select executables from locations elsewhere on your machine.
On *nix machines the two bundled executables are located at:
`/eclipse-ws/mbed-studio-ws/tools/python/bin/pyocd-gdbserver`
`/eclipse-ws/mbed-studio-ws/tools/gcc-arm/bin/gcc-arm-none-eabi-gdb`
On Windows machines, the two bundled executables are located at:
`\eclipse-ws\mbed-studio-ws\tools\python\Scripts\pyocd-gdbserver.exe`
`\eclipse-ws\mbed-studio-ws\tools\gcc-arm\bin\gcc-arm-none-eabi-gdb.exe`
If everything is configured correctly, select Apply in the lower right hand side of the panel and the click the blue Debug button just below that. Debugging should now commence.

### Help

This section outlines known issues and provides answers to common questions.

#### Glossary

##### Workspace

Mbed Studio automatically sets up the workspace. Use it to keep track of settings and user preferences for all of the projects you open in Mbed Studio.

##### Project

A project is a group of associated files, directories and settings. The `C++ Projects` view lists these projects. In Mbed Studio, each project represents an Mbed OS program or an Mbed OS library. An Mbed Studio project can also represent a program that includes libraries, as well.

##### View

In Mbed Studio, a view is a window that has a label, and sometimes options, specific to that window. Examples are the editor, C++ Projects, Console and Outline.

##### Perspective

A perspective is a collection of views, which group functionality in Eclipse. An example of a perspective is the debug perspective.

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

Using the product update functionality in Eclipse returns a timestamp error.
Workaround: This error does not prevent the product from successfully updating.

#### FAQ

This section includes common questions and answers.

Q: How can I tell if I already have a working Java install?
A: From the command-line, run: java -version. You have a working Java install if you see something similar to the following:
`java version "1.8.0_141"`
`Java(TM) SE Runtime Environment (build 1.8.0_141-b15)`
`Java HotSpot(TM) 64-Bit Server VM (build 25.141-b15, mixed mode)`
If not, follow the instructions earlier in this document to install Java.

Q: I have Java installed. Why won’t Mbed Studio launch?
A: Mbed Studio is a 64-bit only application, which requires not only a 64-bit OS, but also a 64-bit Java JDK/JRE installed on the OS.
The 64-bit JDK/JRE needs to be the system default, or you may have to manually configure internal Mbed Studio initialization files to use the 64-bit JDK/JRE.

Q: Will Mbed Studio work with Java 9?
A: Currently, Mbed Studio does not work with Java 9, but later versions will.
