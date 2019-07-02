## ResetReason

Use the ResetReason interface to determine the cause of the last system reset in a portable fashion.

When the system restarts, the reason for the restart is contained in the system registers at boot time in a platform specific manner. This API provides a generic method of fetching the reason for the restart.

### ResetReason class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/classmbed_1_1_resetreason.html)

### ResetReason example

Check the cause of the last system reset.

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
