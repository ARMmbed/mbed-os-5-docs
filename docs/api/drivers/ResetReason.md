## ResetReason

Use the ResetReason interface to access hardware reset reason registers in a portable fashion.

### ResetReason class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/classmbed_1_1_resetreason.html)

### ResetReason example

```c++
#include "mbed.h"
#include "ResetReason.h"

#include <string>

std::string reset_reason_to_string(const reset_reason_t reason)
{
  switch (reason)
  {
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

int main() {
  const reset_reason_t reason = ResetReason::get();

  printf("Last system reset reason: %s\n", reset_reason_to_string(reason).c_str());
}
```
