# Time

[![View code](https://www.mbed.com/embed/?url=https://developer.mbed.org/users/mbed_official/code/time_HelloWorld/)](https://developer.mbed.org/users/mbed_official/code/time_HelloWorld/file/b3b93997a0a6/main.cpp) 

```
/** Implementation of the C time.h functions
 *
 * Provides mechanisms to set and read the current time, based
 * on the microcontroller Real-Time Clock (RTC), plus some
 * standard C manipulation and formating functions.
 *
 * Example:
 * @code
 * #include "mbed.h"
 *
 * int main() {
 *     set_time(1256729737);  // Set RTC time to Wed, 28 Oct 2009 11:35:37
 *
 *     while(1) {
 *         time_t seconds = time(NULL);
 *
 *         printf("Time as seconds since January 1, 1970 = %d\n", seconds);
 *
 *         printf("Time as a basic string = %s", ctime(&seconds;));
 *
 *         char buffer[32];
 *         strftime(buffer, 32, "%I:%M %p\n", localtime(&seconds;));
 *         printf("Time as a custom formatted string = %s", buffer);
 *
 *         wait(1);
 *     }
 * }
 * @endcode
 */
 
/** Set the current time
 *
 * Initialises and sets the time of the microcontroller Real-Time Clock (RTC)
 * to the time represented by the number of seconds since January 1, 1970
 * (the UNIX timestamp).
 *
 * @param t Number of seconds since January 1, 1970 (the UNIX timestamp)
 *
 * Example:
 * @code
 * #include "mbed.h"
 *
 * int main() {
 *     set_time(1256729737); // Set time to Wed, 28 Oct 2009 11:35:37
 * }
 * @endcode
 */
``` 

<span class="warnings">**Warning:** Time with the FRDM-KL25Z </br>For the FRDM-KL25Z board, the on-board oscillator does not allow to use the RTC module. We instead **generate the RTC clock from the interface chip on the RTC_CLKIN pin** (PTC1). That is why the PTC1 pin is not available for other purpose. </span>
