#Rapid Prototyping With mbed

If you have a [board](http://developer.mbed.org/platforms/) and a [user on the mbed compiler](https://developer.mbed.org/account/signup/), you can build your first prototype.

You can reuse a wealth of open source code and technical know-how from the official Handbook, community Cookbook and Components database as the foundation of your products.

You can also contribute back fixes, libraries and support for other developers to help everyone get things done even faster.

##Assemble components

The Components database contains community contributions for hundreds of popular components and peripherals. These include specifications, wiring diagrams, reusable libraries and “Hello World” examples on how to use each peripheral.

When you are deciding which components to use, browsing the components database can help narrow down to devices people have found success with and that are already supported.

There are also various existing domain-specific baseboards that pre-integrate useful components to help you prototype your software before designing the hardware.

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
See our [components page](http://developer.mbed.org/components/), [cookbook](http://developer.mbed.org/cookbook/Homepage) and [baseboards list](http://developer.mbed.org/cookbook/Homepage#baseboards). 
</span>

##Import libraries and get coding

Jump start your code by importing libraries and examples for components. Simply click “import” on any library or example you find around the site, and it can be imported in to your private compiler workspace.

After you’ve got your libraries, it’s time to get coding. The compiler includes full C/C++ error reporting, with each linked to a wiki page with help to you squish coding bugs faster.

You can use the built-in version control to keep track of working version of your code, and even publish your program to the community in a couple of clicks; this is excellent if you want help, as it makes it very easy for others to reproduce your problems quickly.

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
See our explanation on how to [import](/Getting_Started/Using_IDE/) or [publish](Development/Write_Publish/).
</span>

##Build on existing middleware

While lots of libraries are maintained by mbed users, we directly maintain certain important core libraries.

The mbed SDK is at the core of all programs and libraries on mbed, providing the high level object oriented library for the onboard interfaces and features of microcontrollers.

The mbed Networking stack provides a full Berkeley sockets layer TCP/IP implementation based on LwIP, and supports various transports such as Ethernet, WiFi and 3G Modems.

Other middleware includes libraries like Bluetooth Smart, HTTP, CoAP and other connectivity protocols essential for building connected products.

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
See our page on working [with the mbed community](Community/Intro/).
</span>

##Collaborate with other developers

Take some time to explore the tools we provide to help you collaborate with other developers. It can enable you to work on a your own projects and to help improve a public library.

If you fix a bug in a library you can contribute the fix back. Coding new libraries is simple, and you can add API documentation using the built-in Doxygen engine and publish it to the community for others to use in their projects.

We use Mercurial on the backend to support distributed version control; forking, pulling, merging and pushing all happen neatly from within the mbed Compiler. You can also grant developers access to your own repositories, so you can create a virtual team.

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
See our pages on working [with the mbed community](Community/Intro/) or [writing a library](Development/Write_Publish/).
</span>

##Going to production

<span style="float:right; display:block; padding:20px;">
<a href="http://www.youtube.com/watch?feature=player_embedded&v= XiR61Ecs5JU" target="_blank"><img src="http://img.youtube.com/vi/XiR61Ecs5JU/0.jpg" 
alt="The mbed compiler" width="480" height="360" border="10" /></a>
</span>

When your prototype proves a success, the mbed platform can also help support you as you develop it into a product.

The HDK is free for use in custom commercial designs, and the compiler can export to other professional toolchains if needed.

Choosing the mbed platform means you are in the company of tens of thousands of developers who know the tools and have the expertise to help you on the path to production.

###Manufacturing your own hardware

The mbed platform is designed to make it very fast to build and iterate prototypes, so you build the right product.

Once you have your final prototype you’ll likely want to build your own custom hardware. Both the mbed SDK and HDK are free for commercial use, so you can move to the production phase of your project with confidence.

Going to production can be daunting if you haven’t done it before. The prototype to production guide in the cookbook, board schematic / layout files in the HDK and the expertise in the mbed community can help with understanding the process of taking your prototype through to a manufacturable product.

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
See our page on the [mbed HDK](/Introduction/HDK/).
</span>

###Exporting to other professional tools

As you progress to production, you may want to perform rigorous optimisation and testing of your software, or hand-off to a contractor or engineer familiar with different tools.

The mbed Compiler is capable of exporting your projects to other professional toolchains. This export process packages up your code with any library dependencies and generates the tool specific project files to make the transition simple.

Combined with the CMSIS-DAP support built-in to the USB Onboard Interface, it is easy to move your project to full professional debugger tools without changing your hardware.

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
See our page on [exporting to other toolchains](/Going_Further/Export/).
</span>

###Support and Contracting

Once you have built a proof-of-concept that proves your product idea, it is worth considering how best to get it to production; finishing the last 10% is often 90% of the work.

You are lucky enough to be among thousands of highly skilled developers, all who know the platform you are working with, and each with expertise in different areas that could complement your own; reach out to them!

Whether you are looking for hardware or PCB design, low-level software, device drivers or even with your application, there are developers with the right skills and experience to help you with your project, and mbed.org is a great place to find them.

If you are a developer looking for contracting work, your profile and work history are a great way to advertise your skills and help you win challenging and interesting work.

###Finished products

The mbed platform is being used in companies across the world to develop new generations of products. Most companies that we enable are quietly working away on their designs, getting help from and contributing to the community to do amazing things.

We're always interested to hear your case studies so we can share details of products you have been creating, and help inform and inspire other developers that are earlier on in their journey to a finished product.

If you or your company have an advanced prototype or product success you’d be happy to share, please let us know! We love to cross post to our blog and social media to help get the word out. Also consider adding your product to our showcase at [hackster.io/mbed](http://www.hackster.io/mbed/).

###Prototype to hardware

If you want to read about moving from prototyping to hardware, see [here](http://developer.mbed.org/users/chris/notebook/prototype-to-hardware/).