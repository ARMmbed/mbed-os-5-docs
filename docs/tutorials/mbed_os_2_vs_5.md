## Arm Mbed OS 2 vs. Arm Mbed OS 5

Arm Mbed OS 5 is a superset of Arm Mbed OS 2. This means that Mbed OS 5 *is* Mbed OS 2 but with more features, such as an RTOS.

### Overview

- Mbed OS 5 is a *superset* of Mbed OS 2.
- Mbed OS 5 is a combination of both Mbed OS 2 and Mbed-RTOS.
- Mbed OS 2 and Mbed OS 5 both use the same `.h` file.

### FAQs

**Do Mbed OS 2 and Mbed OS 5 use the same header file?**

   Inside the `mbed.h` file in your Mbed OS project, you can see `if` statements that look at `MBED_CONF` variables. These variables are defined in `mbed_lib.json` files located in their respective Mbed OS directory. For example, in `mbed.h` you can find the following lines:

   ```
   #if MBED_CONF_RTOS_PRESENT
   #include "rtos/rtos.h"
   #endif
   ```

   Because RTOS is only present in Mbed OS 5, when this line is encountered by the compiler, and if you are using Mbed OS 5, it will find the following "present" value in the `/mbed-os/rtos/` directory:

   ```
   {
       "name": "rtos",
       "config": {
           "present": 1
       }
   }
   ```

   So, the `if` statement in the `mbed.h` file is evaluated to `True` and the RTOS header file is included (in other words, it is present). If you were running an Mbed OS 2 program, this `if` statement in `mbed.h` would evaluate to `False`, and thus the RTOS is not present in your Mbed OS 2 program.

   If you want to learn more about how these configuration files work, see [our configuration documentation](https://os.mbed.com/docs/latest/tools/configuring-tools.html).

**How can I tell which platforms support Mbed OS 2 and/or Mbed OS 5?**

   Visit the platform page for the board on [os.mbed.com/platforms](https://os.mbed.com/platforms/). For example, if you would like to use the Mbed LPC1768 board for your project, visit its [platform page](https://os.mbed.com/platforms/mbed-LPC1768/). Then, scroll down the page. On the right-hand sidebar under the green "Follow" button is a list of Mbed OS versions that the board supports (signifying that the board is "Mbed Enabled"):

   <span class="images">![](https://os.mbed.com/media/uploads/jplunkett/mbedenabled.png)</span>

**Do Mbed OS 2 and Mbed OS 5 use the same documentation?**

   No. Please see the corresponding documentation pages for Mbed OS 2 and Mbed OS 5:

   - [Mbed OS 5 Documentation](https://os.mbed.com/docs/latest).
   - [Mbed OS 5 GitHub Repository](https://github.com/armmbed/mbed-os).
   - [Mbed OS 2 Handbook](https://os.mbed.com/handbook/Homepage).
   - [Mbed OS 2 Library](https://os.mbed.com/users/mbed_official/code/mbed/).

   If you come across a documentation page for Mbed OS 2, and you would like to see if there is an updated version of this page for Mbed OS 5, from the Handbook page click on the link provided in the top yellow box. For example, you can see the yellow box at the top of the [LocalFileSystem page](https://os.mbed.com/handbook/LocalFileSystem) for Mbed OS 2.

   <span class="images">![](https://os.mbed.com/media/uploads/jplunkett/mbedhandbookbox.png)</span>

   Click on "the file system API" link to navigate to the updated documentation regarding this API for Mbed OS 5.

**How do I know if my project uses Mbed OS 2 or Mbed OS 5?**

   The presence of an `mbed.bld` or `mbed-rtos.lib` file signifies that the project uses a version of Mbed OS earlier than version 5.

   Here is an example of an Mbed OS 2 project as viewed on [os.mbed.com](https://os.mbed.com):

   <span class="images">![](https://os.mbed.com/media/uploads/jplunkett/2-oldmbed.png)</span>
