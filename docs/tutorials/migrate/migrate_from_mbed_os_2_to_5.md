### Mbed OS 2 to 5 migration guide

This guide is to assist you in the process of updating an existing [component](https://os.mbed.com/components/), library or program from Mbed OS 2 to Mbed OS 5.

#### Prerequisites

- [Mbed CLI](/docs/v5.7/tools/arm-mbed-cli.html).
- An [offline compiler](/docs/latest/tools/index.html#compiler-versions).

### Identifying old versions of Mbed OS

This guide uses the Grove temperature and humidity sensor as an example: [Grove-TempHumi-Sensor](https://os.mbed.com/components/Grove-TempHumi-Sensor/).

First, navigate to the Hello World repository for the component.

<span class="images">![](https://os.mbed.com/media/uploads/jplunkett/1-helloworld.png)</span>

Next, view the files in the Hello World repository. The presence of an `mbed.bld` or `mbed-rtos.lib` file signifies that this program uses an older version of Mbed OS (older than Mbed OS 5).

<span class="images">![](https://os.mbed.com/media/uploads/jplunkett/2-oldmbed.png)</span>

A program that uses and has been tested with Mbed OS 5 or later has an `mbed-os.lib` file.

<span class="images">![](https://os.mbed.com/media/uploads/jplunkett/3-newmbed.png)</span>

Some repositories may have both an `mbed.bld` file and a `mbed-rtos.lib` file present. Mbed-RTOS is the precursor to Mbed OS 5, which combines the older Mbed OS 2 library with Mbed-RTOS. So, Mbed OS 5 can replace BOTH `mbed.bld` and `mbed-rtos.lib`.

### Migrating to Mbed OS 5

There are two possible outcomes when migrating to Mbed OS 5:

1. Replacing the old Mbed library with Mbed OS is successful because the APIs in the library have not changed. In this instance, you're finished.
2. Replacing the old Mbed library with Mbed OS produces some compilation errors. These errors can occur in the library or application code for the following two reasons:
  - The Mbed OS API calls are out of date, and you need to migrate to the updated Mbed OS API syntax.
  - There is target specific code, and you need to migrate it to use code for the specific target you are compiling for.

The general outline for updating to Mbed OS 5 is:

```
mbed import [URL of Hello World]
cd [Project Name]
mbed remove mbed
mbed remove mbed-rtos
mbed add mbed-os
```

To determine the success of migration, run:

`mbed compile -m [platform] -t [toolchain]`

### Example component No. 1 - successful initial migration

Repositories used in this example:

- Component: [Grove - Buzzer](https://os.mbed.com/components/Grove-Buzzer/).
- Hello World repo: [Seeed_Grove_Buzzer](https://os.mbed.com/teams/Seeed/code/Seeed_Grove_Buzzer/).

Compile configuration used in this example:

- Platform: [u-blox EVK-ODIN-W2](https://os.mbed.com/platforms/ublox-EVK-ODIN-W2/).
- Toolchain: [GCC ARM](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads).

In the command-line, run:

```
mbed import https://os.mbed.com/teams/Seeed/code/Seeed_Grove_Buzzer/
cd Seeed_Grove_Buzzer
mbed remove mbed
mbed remove mbed-rtos
mbed add mbed-os
mbed compile -m ublox_evk_odin_w2 -t gcc_arm
```

It successfully compiles, so no changes are necessary to the `Grove - Buzzer` library or `Hello World` program.

### Example component No. 2 - application fails to compile

Repositories used in this example:

- Component: [SRF08-Ultrasonic-Range-Finder](https://os.mbed.com/components/SRF08-Ultrasonic-Range-Finder/).
- Hello World repo: [SRF08HelloWorld](https://os.mbed.com/users/melse/code/SRF08HelloWorld/).

Compile configuration used in this example:

- Platform: [FRDM-K64F](https://os.mbed.com/platforms/FRDM-K64F/).
- Toolchain: [GCC ARM](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads).

In the command-line, run:

```
mbed import https://os.mbed.com/users/melse/code/SRF08HelloWorld/
cd SRF08HelloWorld
mbed remove mbed
mbed remove mbed-rtos
mbed add mbed-os
mbed compile -m k64f -t gcc_arm
```

#### Compilation errors

After you have cloned the repository to your computer and deployed the latest version of Mbed OS, check whether any compilation errors already exist.

Here is the output produced from `mbed compile`:

```
Building project SRF08HelloWorld (K64F, GCC_ARM)
Scan: .
Scan: env
Scan: mbed
Scan: FEATURE_LWIP
Scan: FEATURE_STORAGE
Compile [  0.3%]: AnalogIn.cpp
Compile [  0.6%]: BusIn.cpp
Compile [  0.8%]: main.cpp
[Error] main.cpp@4,13: 'p9' was not declared in this scope
[Error] main.cpp@4,17: 'p10' was not declared in this scope
[ERROR] .\main.cpp:4:13: error: 'p9' was not declared in this scope
 SRF08 srf08(p9, p10, 0xE0);      // Define SDA, SCL pin and I2C address
             ^~
.\main.cpp:4:17: error: 'p10' was not declared in this scope
 SRF08 srf08(p9, p10, 0xE0);      // Define SDA, SCL pin and I2C address
                 ^~~

[mbed] ERROR: "c:\python27\python.exe" returned error code 1.
[mbed] ERROR: Command "c:\python27\python.exe -u C:\Repos\SRF08HelloWorld\mbed-os\tools\make.py -t gcc_arm -m k64f --source . --build .\BUILD\k64f\gcc_arm" in "C:\Repos\SRF08HelloWorld"
```

This is a target-specific error. The pins in the `Hello World` application do not exist on this target, K64F. To fix this, replace the SDA/SCL pins with ones present on the K64F. Use the [K64F platform page](https://os.mbed.com/platforms/FRDM-K64F/) to find the correct pins. D14/D15 work. So, `main.cpp` now looks like this:

```
#include "mbed.h"
#include "SRF08.h"

SRF08 srf08(D14, D15, 0xE0);      // Define SDA, SCL pin and I2C address

int main() {

    while (1) {
       printf("Measured range : %.2f cm\n",srf08.read());
       wait(0.1);
    }

}
```

Now, the program successfully compiles.

### Example component #3 - library fails to compile

Repositories used in this example:

- Component: [CN0357 - Toxic gas measurement](https://os.mbed.com/components/CN0357-Toxic-gas-measurement/).
- Hello World repo: [CN0357-helloworld](https://os.mbed.com/teams/AnalogDevices/code/CN0357-helloworld/).

Compile configuration used in this example:

- Platform: [FRDM-K64F](https://os.mbed.com/platforms/FRDM-K64F/).
- Toolchain: [GCC ARM](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads).

In the command-line, run:

```
mbed import http://mbed.org/teams/AnalogDevices/code/CN0357-helloworld/
cd CN0357-helloworld
mbed remove mbed
mbed remove mbed-rtos
mbed add mbed-os
mbed compile -m k64f -t gcc_arm
```

#### Compilation errors

After you have cloned the repository to your computer and deployed the latest version of Mbed OS, check whether any compilation errors already exist.

Here is the output produced from `mbed compile`:

```
Building project CN0357-helloworld (K64F, GCC_ARM)
Scan: .
Scan: mbed
Scan: env
Scan: FEATURE_LWIP
Scan: FEATURE_STORAGE
Compile [  0.3%]: AD5270.cpp
[Error] AD5270.h@91,25: 'SPI_CS' was not declared in this scope
[Error] AD5270.h@91,80: 'SPI_MOSI' was not declared in this scope
[Error] AD5270.h@91,105: 'SPI_MISO' was not declared in this scope
[Error] AD5270.h@91,129: 'SPI_SCK' was not declared in this scope
[ERROR] In file included from ./CN0357/AD5270/AD5270.cpp:50:0:
./CN0357/AD5270/AD5270.h:91:25: error: 'SPI_CS' was not declared in this scope
     AD5270(PinName CS = SPI_CS, float max_resistance = 20000.0, PinName MOSI = SPI_MOSI, PinName MISO = SPI_MISO, PinName SCK = SPI_SCK);
                         ^~~~~~
./CN0357/AD5270/AD5270.h:91:80: error: 'SPI_MOSI' was not declared in this scope
     AD5270(PinName CS = SPI_CS, float max_resistance = 20000.0, PinName MOSI = SPI_MOSI, PinName MISO = SPI_MISO, PinName SCK = SPI_SCK);
                                                                                ^~~~~~~~
./CN0357/AD5270/AD5270.h:91:105: error: 'SPI_MISO' was not declared in this scope
     AD5270(PinName CS = SPI_CS, float max_resistance = 20000.0, PinName MOSI = SPI_MOSI, PinName MISO = SPI_MISO, PinName SCK = SPI_SCK);
                                                                                                         ^~~~~~~~
In file included from ./CN0357/AD5270/AD5270.cpp:50:0:
./CN0357/AD5270/AD5270.h:91:129: error: 'SPI_SCK' was not declared in this scope
     AD5270(PinName CS = SPI_CS, float max_resistance = 20000.0, PinName MOSI = SPI_MOSI, PinName MISO = SPI_MISO, PinName SCK = SPI_SCK);
                                                                                                                                 ^~~~~~~

[mbed] ERROR: "/usr/local/opt/python/bin/python2.7" returned error code 1.
[mbed] ERROR: Command "/usr/local/opt/python/bin/python2.7 -u /Users/jenplu01/Repos/CN0357-helloworld/mbed-os/tools/make.py -t gcc_arm -m k64f --source . --build ./BUILD/k64f/gcc_arm" in "/Users/jenplu01/Repos/CN0357-helloworld"
---
```

The errors relating to "was not declared in this scope" are library-specific errors. To fix this, go into the `./CN0357/AD5270/AD5270.h` header file and remove the constructor's default arguments. Line 91 of the `AD5270.h` header file now looks like this:

```
AD5270(PinName CS, float max_resistance, PinName MOSI, PinName MISO, PinName SCK);
```

Run `mbed compile` again:

```
Building project CN0357-helloworld (K64F, GCC_ARM)
Scan: .
Scan: mbed
Scan: env
Scan: FEATURE_LWIP
Scan: FEATURE_STORAGE
Compile [  2.5%]: main.cpp
[Error] AD7790.h@114,51: 'SPI_CS' was not declared in this scope
[Error] AD7790.h@114,74: 'SPI_MOSI' was not declared in this scope
[Error] AD7790.h@114,99: 'SPI_MISO' was not declared in this scope
[Error] AD7790.h@114,123: 'SPI_SCK' was not declared in this scope
[Error] CN0357.h@77,73: 'SPI_MOSI' was not declared in this scope
[Error] CN0357.h@77,98: 'SPI_MISO' was not declared in this scope
[Error] CN0357.h@77,122: 'SPI_SCK' was not declared in this scope
[Error] main.cpp@111,12: call to 'CN0357::CN0357(PinName, PinName, PinName, PinName, PinName)' uses the default argument for parameter 3, which is not yet defined
[Error] main.cpp@111,0: call to 'CN0357::CN0357(PinName, PinName, PinName, PinName, PinName)' uses the default argument for parameter 4, which is not yet defined
[Error] main.cpp@111,0: call to 'CN0357::CN0357(PinName, PinName, PinName, PinName, PinName)' uses the default argument for parameter 5, which is not yet defined
[ERROR] In file included from ./CN0357/CN0357.h:52:0,
                 from ./main.cpp:48:
./CN0357/AD7790/AD7790.h:114:51: error: 'SPI_CS' was not declared in this scope
     AD7790( float reference_voltage, PinName CS = SPI_CS, PinName MOSI = SPI_MOSI, PinName MISO = SPI_MISO, PinName SCK = SPI_SCK);
                                                   ^~~~~~
./CN0357/AD7790/AD7790.h:114:74: error: 'SPI_MOSI' was not declared in this scope
     AD7790( float reference_voltage, PinName CS = SPI_CS, PinName MOSI = SPI_MOSI, PinName MISO = SPI_MISO, PinName SCK = SPI_SCK);
                                                                          ^~~~~~~~
./CN0357/AD7790/AD7790.h:114:99: error: 'SPI_MISO' was not declared in this scope
     AD7790( float reference_voltage, PinName CS = SPI_CS, PinName MOSI = SPI_MOSI, PinName MISO = SPI_MISO, PinName SCK = SPI_SCK);
                                                                                                   ^~~~~~~~
./CN0357/AD7790/AD7790.h:114:123: error: 'SPI_SCK' was not declared in this scope
     AD7790( float reference_voltage, PinName CS = SPI_CS, PinName MOSI = SPI_MOSI, PinName MISO = SPI_MISO, PinName SCK = SPI_SCK);
                                                                                                                           ^~~~~~~
In file included from ./main.cpp:48:0:
./CN0357/CN0357.h:77:73: error: 'SPI_MOSI' was not declared in this scope
     CN0357(PinName CSAD7790 = D8, PinName CSAD5270 = D6, PinName MOSI = SPI_MOSI, PinName MISO = SPI_MISO, PinName SCK = SPI_SCK);
                                                                         ^~~~~~~~
./CN0357/CN0357.h:77:98: error: 'SPI_MISO' was not declared in this scope
     CN0357(PinName CSAD7790 = D8, PinName CSAD5270 = D6, PinName MOSI = SPI_MOSI, PinName MISO = SPI_MISO, PinName SCK = SPI_SCK);
                                                                                                  ^~~~~~~~
./CN0357/CN0357.h:77:122: error: 'SPI_SCK' was not declared in this scope
     CN0357(PinName CSAD7790 = D8, PinName CSAD5270 = D6, PinName MOSI = SPI_MOSI, PinName MISO = SPI_MISO, PinName SCK = SPI_SCK);
                                                                                                                          ^~~~~~~
./main.cpp: In function 'int main()':
./main.cpp:111:12: error: call to 'CN0357::CN0357(PinName, PinName, PinName, PinName, PinName)' uses the default argument for parameter 3, which is not yet defined
     CN0357 cn0357;
            ^~~~~~
./main.cpp:111:12: error: call to 'CN0357::CN0357(PinName, PinName, PinName, PinName, PinName)' uses the default argument for parameter 4, which is not yet defined
./main.cpp:111:12: error: call to 'CN0357::CN0357(PinName, PinName, PinName, PinName, PinName)' uses the default argument for parameter 5, which is not yet defined

[mbed] ERROR: "/usr/local/opt/python/bin/python2.7" returned error code 1.
[mbed] ERROR: Command "/usr/local/opt/python/bin/python2.7 -u /Users/jenplu01/Repos/temp/CN0357-helloworld/mbed-os/tools/make.py -t gcc_arm -m k64f --source . --build ./BUILD/k64f/gcc_arm" in "/Users/jenplu01/Repos/temp/CN0357-helloworld"
---
```

Notice that the `./CN0357/AD7790/AD7790.h` and `./CN0357/CN0357.h` header files also have similar "was not declared in this scope" errors. You need to remove the constructor's default arguments again in both files.

Line 114 of the `AD7790.h` header file now looks like this:

```
AD7790( float reference_voltage, PinName CS, PinName MOSI, PinName MISO, PinName SCK);
```

Line 77 of the `CN0357.h` header file now looks like this:

```
CN0357(PinName CSAD7790, PinName CSAD5270, PinName MOSI, PinName MISO, PinName SCK);
```

Run `mbed compile` once again. You now have the following errors:

```
Building project CN0357-helloworld (K64F, GCC_ARM)
Scan: .
Scan: mbed
Scan: env
Scan: FEATURE_LWIP
Scan: FEATURE_STORAGE
Compile [  5.1%]: Ticker.cpp
Compile [  5.4%]: Timeout.cpp
Compile [  5.6%]: main.cpp
[Error] main.cpp@111,12: no matching function for call to 'CN0357::CN0357()'
[ERROR] ./main.cpp: In function 'int main()':
./main.cpp:111:12: error: no matching function for call to 'CN0357::CN0357()'
     CN0357 cn0357;
            ^~~~~~
In file included from ./main.cpp:48:0:
./CN0357/CN0357.h:77:5: note: candidate: CN0357::CN0357(PinName, PinName, PinName, PinName, PinName)
     CN0357(PinName CSAD7790, PinName CSAD5270, PinName MOSI, PinName MISO, PinName SCK);
     ^~~~~~
./CN0357/CN0357.h:77:5: note:   candidate expects 5 arguments, 0 provided
./CN0357/CN0357.h:58:7: note: candidate: CN0357::CN0357(const CN0357&)
 class CN0357
       ^~~~~~
./CN0357/CN0357.h:58:7: note:   candidate expects 1 argument, 0 provided

[mbed] ERROR: "/usr/local/opt/python/bin/python2.7" returned error code 1.
[mbed] ERROR: Command "/usr/local/opt/python/bin/python2.7 -u /Users/jenplu01/Repos/temp/CN0357-helloworld/mbed-os/tools/make.py -t gcc_arm -m k64f --source . --build ./BUILD/k64f/gcc_arm" in "/Users/jenplu01/Repos/temp/CN0357-helloworld"
---
```

These errors are now due to the CN0357 variable in `main.cpp` no longer having sufficient arguments. Go into `main.cpp`, and modify the initialization of the `CN0357 cn0357;` variable on line 111 to include the K64F's pin names. Line 111 now looks like this:

```
CN0357 cn0357(D8, D6, D11, D12, D13); // CSAD7790, CSAD5270, MOSI, MISO, SCK
```

Now, the program successfully compiles.

### Runtime errors

Although the program or library now compiles successfully, runtime errors may still be present. Please visit the [compile-time errors tutorial](/docs/latest/tutorials/compile-time-errors.html#runtime-errors-and-lights-of-the-dead) for further debugging tips about common errors.
