## Arm Mbed OS

### Problem statement

Writing software for deeply embedded or connected devices continues to increase in complexity. This complexity is commonly known as “The Internet of Things” (IoT) and is changing the expectations of device capabilities, be it security, robustness, power consumption or device management. Arm Mbed OS is a free, open-source embedded operating system designed specifically for the "things" in the Internet of Things. It includes all the capabilities needed to develop a connected product based on an Arm Cortex-M microcontroller, including security, wired and wireless connectivity, a preemptive RTOS kernel and peripheral drivers for sensors and I/O devices.

### Promise

As software integration complexities increase and demands on the time to market decrease for embedded devices, the ability to prototype and prove concepts quickly is crucial. Mbed OS uses USB drag and drop programming to allow you to rapidly protoype without expensive debug hardware. Basing development efforts on an operating system that is well tested and released on a regular cadence (quarterly [feature releases](https://os.mbed.com/releases/) and biweekly patch releases) allows you to focus on the application and differentiation rather than investing software integration and tooling compatibilities. This effectively multiplies team effectiveness by picking up bug fixes and new target support in patch releases while getting new capabilities in feature releases. That, combined with low power and a small footprint, makes moving from concept to production very low risk.

### Principles

Mbed OS is an open-source operating system actively developed by Arm, in partnership with over 60 partners and the Arm Mbed community of over 340,000 developers throughout the world. Everyone is encouraged to contribute and make Mbed OS even better, and our community has contributed to many of our components and projects. Our developer community is a valuable part of Mbed OS and adds an important layer of transparency.

Because we release Mbed OS under an Apache 2.0 license, you can confidently use it in commercial and personal projects. You can ask questions about hardware availability and software compatibility on the developer website, forums and question pages. You can contribute software issues and fixes to the development repository on GitHub. For private inquiries that may not be suitable to share in public, please email [support](support@mbed.org). You can find more information about licensing and how to contribute, as well as our code of conduct, on our [contributing page](https://os.mbed.com/contributing/).

### Architecture

Three principals form the basis of Mbed OS: modular, secure and connected. With a large contributor base, it’s important to have visibility of where and how changes should be made.

#### Modular

The Hardware Abstraction Layer (HAL) allows support for the basic and most common parts of a microcontroller, such as timers, analog and digital interfaces. A HAL is the foundation of allowing applications to be written against a common set of application programming interfaces (APIs) and where to start from when adding support for a new target.

With the HAL, we can create new features on feature branches, and silicon Partners can then port them to Mbed Enabled development boards. Please see more information about HAL APIs in our documentation about [contributing targets](/docs/development/porting/index.html).

Mbed OS has an RTOS core based on the widely used open-source CMSIS-RTOS RTX. Because of this, Mbed OS supports deterministic, multithreaded, real-time software execution. The RTOS primitives are always available, allowing drivers and applications to rely on features, such as threads, semaphores and mutexes.

Other features include more complex software components, such as file systems and networking stacks, which may require complex synchronization primitives to ensure deterministic and safe execution or might have multiple compatible drivers. The modular design allows application level composition of storage systems, for instance where the block level storage options vary and are application dependent.

The modular design of Mbed OS means your device automatically includes necessary libraries. It also includes driver support for standard MCU peripherals, such as I2C, serial and SPI. This allows you to concentrate on writing application code.

#### Secure

We implement our security strategy throughout the device life cycle. Mbed OS security begin with isolated security domains and continue through secure communication. For example, with Mbed OS, you can include SSL and TLS in your projects for secure communications.

#### Connected

Mbed OS supports many connectivity options. These include [network sockets](/docs/development/apis/network-socket.html), [Bluetooth](/docs/development/apis/bluetooth.html) and [LoRaWAN](/docs/development/apis/lorawan.html). They also include network interfaces, such as Ethernet, Wi-Fi and 6LoWPAN. Mbed OS is also a Thread-certified component.

For each connectivity option, Mbed OS provides API class references, reference material and examples.

#### Architecture diagram

This is the basic architecture of an Mbed board:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/MbedOS_002.png)<span>A sketch of a typical Mbed board's hardware architecture</span></span>

### Compatibility

Mbed OS [includes the tools](/docs/development/tools/index.html) needed for developers of all skill levels. Many experienced developers prefer to work offline using Arm Mbed CLI, our offline command-line tool based on Python. This requires having a toolchain installed on your computer. You can use Mbed CLI to build projects using out three supported toolchains: Arm Compiler 6, GCC and IAR. You can also [export projects](/docs/development/tools/exporting.html) for use in other IDEs, such as Keil MDK.

Developers who do not have a dedicated desktop setup or prefer to work online use the Arm Mbed Online Compiler, our online development tool, which lets you write and build applications using a web browser. This online IDE requires no setup.

Other tools included as part of Mbed OS work well for developers of all skill sets. For example, you can use our debugging tools, DAPLink and pyOCD, to program and debug their many devices. Mbed OS also includes build tools and supported toolchains and the C libraries of each supported toolchain, including implementation of thread safety support. At the end of the development cycle, you can us the Mbed OS validation tools to test your project. All of these tools make it easy for you to use Mbed OS for your projects throughout the development cycle.

### Conclusion

Mbed OS is a secure, connected, production-ready operating system with a modular design that includes all the tools you need, whatever your skillset. For businesses entering the IoT space requiring an open source industry agnostic OS solution. Using our heritage in architecture, we have built our device software to create a forward-looking yet robust chip to cloud solution.

This operating system is the core of Arm's Mbed IoT Device Platform. By using Mbed OS, you can create application code that remains clean and portable while taking advantage of security and communication. Use our quick start guide to get started with Mbed OS today.
