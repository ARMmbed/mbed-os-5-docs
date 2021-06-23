# ResetReason

When the system restarts, the system registers contain the reason for the restart at boot time in a board specific manner. This API provides a generic method of fetching the reason for the restart.

You can use the ResetReason interface to determine the cause of the last system reset in a portable fashion.

## ResetReason class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/v6.12/mbed-os-api-doxy/classmbed_1_1_reset_reason.html)

## ResetReason example

Check the cause of the last system reset:

```c++
#include "mbed.h"
#include "ResetReason.h"

#include <string>

std::string reset_reason_to_string(const reset_reason_t reason)
{
    switch (reason) {
        case RESET_REASON_POWER_ON:
            return "Power On";
        case RESET_REASON_PIN_RESET:
            return "Hardware Pin";
        case RESET_REASON_SOFTWARE:
            return "Software Reset";
        case RESET_REASON_WATCHDOG:
            return "Watchdog";
        default:
            return "Other Reason";
    }
}

int main()
{
    const reset_reason_t reason = ResetReason::get();

    printf("Last system reset reason: %s\r\n", reset_reason_to_string(reason).c_str());
}
```
