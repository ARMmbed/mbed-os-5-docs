<h1 id="error-handling">Error handling</h1>

Mbed OS provides error status definitions and APIs for error construction, reporting and retrieving previously reported errors. Mbed OS also provides functions and macros to generate and define new error status values, extract information from error status values and to report errors into the system. Any software layer, such as applications, drivers, HAL and protocol stacks, can use these error handling APIs. The error functions also facilitate emitting an error message through STDOUT. `mbed_error.h` declares the error functions that Mbed OS provides.

Conceptually, error handling is a platform service that the Mbed OS platform layer implements. Error handling provides the following:

1. Provides system defined error codes and status values in `mbed_error.h`
1. Provides APIs for error construction, reporting and error history management.
1. Provides ISR-safe and Thread-safe error handling APIs.
1. Provides mechanisms for extending the error status definitions.

## Error status usage

Mbed OS predefines a set of system errors, and it defines **Error Status** as a 32-bit signed integer in **NEGATIVE space**. The **mbed_error_status_t** type represents the error status values.

You can use error status:

- To indicate return status from function calls.
  - Returning 0 (=**MBED_SUCCESS**) or any positive number is success.
  - A predefined status code named **MBED_SUCCESS** (=0) is available to indicate success.

- As system error codes
  - Used to report error conditions to the OS error handling subsystem.

## Error status types

Mbed OS error status encoding defines three types of error status values. Note that type of error status is encoded into the 32-bit signed integer.

- System errors - Mbed-OS defined error codes (see [error code and error status ranges](#error-code-and-error-status-ranges)).
- Posix errors - See [Posix error codes support](#posix-error-codes-support).
- Custom defined errors - See [extending error codes](#extending-error-codes).

## Error code and error status ranges

For each error status type, we have defined a range of error codes, which forms the least significant 16-bits of 32-bit error status values. Based on error code definitions below are the error code ranges for each error type:

- Posix error codes: 1 to 255 (Please see the [Posix error codes support](#posix-error-codes-support) section for more details).
- System error codes: 256 to 4095.
- Custom error codes: 4096 to 65535.

Accordingly, the error status ranges for each type are:

- Posix error status  - 0xFFFFFFFF to 0xFFFFFF01 - This corresponds to Posix errors represented as negative.
- System error status - 0x80XX0100 to 0x80XX0FFF - This corresponds to system errors range (all values are negative). Bits 23-16 capture the module type (marked with XX).
- Custom error status - 0xA0XX1000 to 0xA0XXFFFF - This corresponds to custom errors range (all values are negative). Bits 23-16 capture the module type (marked with XX).

It's important to understand the difference between the terminologies "**Error Code**" and "**Error Status**". "**Error Status**" is the 32-bit signed integer in **NEGATIVE space** that the applications use to report the error, and "**Error Code**" is the least significant 16-bits of 32-bit error status values indicating the error situation, for example, out of memory. All predefined error status definitions start with **MBED_ERROR_**, and all predefined error code definitions start with **MBED_ERROR_CODE_**.
Note that error codes are always encoded into error status values when reporting or representing errors in the system.

Mbed OS system error status values can also capture the module reporting the error by encoding the module identifier in the error status, depending on the type of error status. The module information prints to the terminal as part of the [error report](#error-reporting). We provide the error status values and ranges for information purposes, but no implementation should assume or manipulate the bit fields in the encoding directly. Implementation using Mbed OS error handling and reporting APIs should deal with error status, such as an opaque object, and should use Mbed OS provided macros and functions to manipulate or interpret the error status values.

## Posix error codes support

Many modules (such as file systems) under Mbed OS use Posix error codes. For this reason, Mbed OS error status definitions capture Posix error codes, as well, under the new error encoding scheme. Error code definitions also ensure that Posix error code values don’t overlap with Mbed error code values. This makes it easier for developers to report Posix error codes into the Mbed OS error handling system.

To incorporate Posix error code representation into Mbed OS, a portion of error space is allocated for Posix error codes. Because Mbed OS error codes are always negative, we capture the negative of the actual Posix error code in the error code definitions. For example, the Posix error code `EPERM` in the Mbed OS error code space would be represented as negative of the actual `EPERM` value. This aligns with the Mbed OS error encoding convention of using negative values, but the numerical (or absolute) value is same as the Posix error code. Also note that, because Posix error codes are represented as negative of Posix error codes, they cannot capture module information as in Mbed OS system error codes.

**Although we support Posix error codes for compatibility reasons, we highly encourage all future Mbed OS focused implementations to use Mbed OS error definitions, so errors reported work seamlessly with error reporting and handling implementation in Mbed OS.**

## Error context capture

The error handling system in Mbed OS automatically captures the thread context for each error reported into the system. The context captured includes the following information:

- Error status code – Status code.
- Error address – Captures return address of set error calls.
- Error value – A context-specific value the caller sets in `MBED_ERROR()/MBED_WARNING()` calls.
- Thread ID – ID of the current thread; this information is captured only if the system is built with RTOS support.
- Thread entry address – Entry function for the current thread; this information is captured only if the system is built with RTOS support.
- Thread stack size – Size of stack; this information is captured only if the system is built with RTOS support.
- Thread stack mem - Top of stack; this information is captured only if the system is built with RTOS support.
- Thread current SP – SP value (PSP or MSP based on what’s active); this information is captured only if the system is built with RTOS support.
- File name and line number - By default, capturing of file name and line number is disabled. If you need this information to be captured, you need to set the configuration option **MBED_CONF_PLATFORM_ERROR_FILENAME_CAPTURE_ENABLED** to true.

STDOUT emits this captured context in the case of fatal errors. In the case of warnings, it is recorded by the system, and you can retrieve it later for system diagnostics, external reporting and debugging purposes. See the [error history](#error-history) section for information on how the error history feature works in Mbed OS. The [error handling API examples](#error-handling-api-examples) also include more information on how to use error retrieval APIs.

## Error reporting

Mbed OS provides three ways to report an error using the error handling implementation:

1. Using the **error()** function to report a fatal error condition - This is the legacy function used for reporting a fatal error. It has been modified to capture the context information, but it does not capture the address of the caller or module information. It also doesn't support reporting specific error codes. Any implementation using this API to report an error uses the error status **MBED_ERROR_UNKNOWN**. We highly encourage all future Mbed OS focused implementations to use `MBED_ERROR()`/`MBED_ERROR1()` or `MBED_WARNING()`/`MBED_WARNING1()` macros for reporting errors.
1. Using **MBED_ERROR()/MBED_ERROR1()** macros (see the [error handling API examples](#error-handling-api-examples)) to report a fatal error with enhanced capability for capturing the module reporting the error.
1. Using **MBED_WARNING()/MBED_WARNING1()** macros (see the [Error handling API examples](#error-handling-api-examples)) to report a nonfatal error with enhanced capability for capturing the module reporting the error.

When you report an error using `MBED_ERROR()` or `MBED_ERROR1()` macros, the error is recorded in the [error history](#error-history) with the context. The error information prints to STDOUT, and the application is terminated.

Note that the error functions output the error message or the file name in debug and develop builds only.

Below is an example of terminal output the `MBED_ERROR1()` call created. Note that file name capture is disabled by default, even for debug and develop builds. You can enable the file name capture by setting the configuration option **MBED_CONF_PLATFORM_ERROR_FILENAME_CAPTURE_ENABLED** to true.

```
++ MbedOS Error Info ++
Error Status: 0x80FF013D Code: 317 Module: 255
Error Message: Fault exception
Location: 0x5CD1
Error Value: 0x4A2A
Current Thread: Id: 0x20001E80 Entry: 0x5EB1 StackSize: 0x1000 StackMem: 0x20000E80 SP: 0x2002FF90
For more info, visit: https://mbed.com/s/error?error=0x80FF013D
-- MbedOS Error Info --
```

## Constructing error status values in your implementation

Mbed OS provides the necessary functions and macros for implementations to construct error status values. There are a few ways you can construct error status values.

If you know the module reporting the error you can use the **MBED_MAKE_ERROR()** macro to construct an error status with the module information. For example, if you want to report an unsupported configuration error from the serial driver, you may construct the error status as follows to capture the module information along with a specific error code. The below example constructs an error status value with the error code set to `MBED_ERROR_CODE_CONFIG_UNSUPPORTED` from the serial driver, indicated by module information set to `MBED_MODULE_DRIVER_SERIAL`.

```
mbed_error_status_t error = MBED_MAKE_ERROR(MBED_MODULE_DRIVER_SERIAL, MBED_ERROR_CODE_CONFIG_UNSUPPORTED)
```

There may be scenarios in which the module might have called an API exported from other modules, such as protocol stacks, but has received an error status in return. In those cases, the calling module doesn't know which of the lower layers raised the error, but you may still want to report the error. In those cases, the module can use the predefined error status, such as `MBED_ERROR_CONFIG_UNSUPPORTED`, with the module value already set to `MBED_MODULE_UNKNOWN`.

This is equivalent to defining an error status with `MODULE_UNKNOWN`. However, using predefined values, such as `MBED_ERROR_CONFIG_UNSUPPORTED`, makes it more convenient and easier to read the implementation.

```
mbed_error_status_t error = MBED_MAKE_ERROR(MBED_MODULE_UNKNOWN, MBED_ERROR_CODE_CONFIG_UNSUPPORTED)
```

## Error history

Error handling implementation in Mbed OS keeps track of previous errors in the system. This feature is called **Error history** and is configurable using the configuration value **MBED_CONF_PLATFORM_ERROR_HIST_ENABLED**.

`MBED_CONF_PLATFORM_ERROR_HIST_SIZE` configures the number of previous errors the system keeps in its error history. You can enable the error history by setting the configuration option `MBED_CONF_PLATFORM_ERROR_HIST_ENABLED` to true. By default, it keeps track of the past four errors, if enabled. Whether error history is enabled or not, the system always records the first and last errors that happened in the system. We provide APIs to retrieve errors or warnings from the **Error history** and the first and last errors. (Please see the [error handling API examples](#error-handling-api-examples) section for API usage examples.) In most cases, calling **MBED_ERROR()/MBED_ERROR1()** halts the system. Therefore, the error history APIs retrieve the warnings, unless you are calling these APIs from the [error hook](#error-hook-for-applications) function.

See the below link to learn more about the APIs related to error history:

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/mbed__error_8h_source.html)

## Extending error codes

Mbed OS application and system developers may need to define error codes specific to their the applications. However, these error codes may not be applicable to the broader system to be defined as system error codes. In those cases, applications can predefine custom error codes using the **MBED_DEFINE_CUSTOM_ERROR()** macro. **MBED_DEFINE_CUSTOM_ERROR()** macro specifically defines error status values whose type will be of **Custom Defined Errors** as mentioned above in the [error status types and error code ranges](#error-status-types-and-error-code-ranges) section. If you are defining custom error codes, we advise to capture those definitions in `mbed_error.h` under custom error codes definitions.

## Error hook for applications

Some applications may want to do custom error handling when an error is reported using `MBED_ERROR()` or `MBED_WARNING()`. Applications can accomplish this by registering an error hook function with the Mbed OS error handling system using the **mbed_set_error_hook()** API. This function is called with error context information whenever the system handles an **MBED_ERROR()** or **MBED_WARNING()** invocation. This function should be implemented for re-entrancy because multiple threads may invoke `MBED_ERROR()` or `MBED_WARNING()`, which may cause the error hook to be called in parallel.

## Crash reporting and auto-reboot

Whenever a fatal error happens in the system, the Mbed OS error handling system collects key information such as error code, error location, register context (in the case of fault exceptions) and so on. The error handing system stores that information in a reserved RAM region called Crash-data-RAM. The error information stored in Crash-data-RAM is in binary format and follows the `mbed_error_ctx` structure defined in `mbed_error.h`. The system then triggers a warm-reset without losing the RAM contents that store the error information. After the system reboots, during Mbed OS initialization, the Crash-data-RAM region is checked to find if there is valid error information captured. This is done by using a CRC value calculated over the stored error information and is appended as part of information stored in Crash-data-RAM. If the system detects that the reboot was triggered by a fatal error, it will invoke a callback function with a pointer to the error context structure stored in Crash-data-RAM. The default callback function is defined with the `WEAK` attribute, which the application can override. Below is the signature for the callback:

```
void mbed_error_reboot_callback(mbed_error_ctx *error_context);
```

<span class="notes">**Note:** This callback is invoked before the system starts executing the application `main()`. The implementation of callback should be aware any resource limitations or availability. Also, the callback is invoked only when there is a new error.</span>

### Adding the Crash-data-RAM region for crash reporting

The crash reporting feature requires a special memory region, called Crash-data-RAM, to work. This region is 256 bytes and is allocated using linker scripts for the target for each toolchain. Although all platforms support crash reporting feature, not all targets are currently modified to allocate this Crash-data-RAM region.

See `mbed_lib.json` in the platform directory to see which targets are currently enabled with crash reporting. To enable crash reporting in other targets, you must modify the linker scripts for those targets to allocate the Crash-data-RAM region. You can refer to the linker scripts for one of the targets already enabled with crash reporting to understand how the Crash-data-RAM region is allocated. Below are some guidelines to make the linker script changes:

- The region size should be 256 bytes and aligned at 8-byte offset.
- If you are enabling the Crash-data-RAM for the *ARM compiler*, linker scripts must export the following symbols:

   __Image$$RW_m_crash_data$$ZI$$Base__ - Indicates start address of Crash-data-RAM region.
   __Image$$RW_m_crash_data$$ZI$$Size__ - Indicates size of Crash-data-RAM region.

- If you are enabling the Crash-data-RAM for the *GCC ARM compiler* or *IAR Compiler*, linker scripts must export the following symbols:

   __\_\_CRASH_DATA_RAM_START\_\___ - Indicates start address of Crash-data-RAM region.
   __\_\_CRASH_DATA_RAM_END\_\___ - Indicates end address of Crash-data-RAM region.

It's important that this region is marked with the appropriate attributes (based on the toolchain) to mark it as an uninitialized region. For example, you can mark the ARM Compiler Crash-data-RAM with the attribute *EMPTY*. The only requirement about the placement of this region is that no other entity can overwrite this region during reboot or at runtime. However, to avoid fragmentation, it's best if you place this region just after the vector table region, or if there is no vector table region, iat the bottom of RAM (lowest address).

See [memory model](../reference/memory.html) for more info on the placement of this region.

### Configuring crash reporting and autoreboot

The Mbed OS crash reporting implementation provides many options to configure the crash reporting behavior. Below is the list of configuration options available to configure crash reporting functionality. These configuration options are defined in `mbed_lib.json` under the platform directory:

- `crash-capture-enabled` - Enables crash context capture when the system enters a fatal error or crash. When this is disabled, it also disables other dependent options mentioned below.
- `fatal-error-auto-reboot-enabled` - Setting this to true enables autoreboot on fatal errors.
- `error-reboot-max` - Maximum number of auto-reboots(warm-resets) permitted on fatal errors. The system stop auto-rebooting once it reaches the maximum limit. Setting this value to 0 disable auto-reboot.

Crash reporting feature also provides APIs to read and clear error context information captured in Crash-data-RAM region. Please see the API reference below for [crash reporting related APIs](#crash-reporting-api).

## Error handling functions reference

The below link provides the documentation for all the APIs that Mbed OS provides for error definitions and handling:

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/mbed__error_8h_source.html)

## Error handling API examples

### Using the `error()` function

The code below uses error function to print a fatal error indicating an out-of-memory condition.

```CPP TODO
void *operator new(std::size_t count) {
    void *buffer = malloc(count);
    if (NULL == buffer) {
        error("Operator new out of memory\r\n");
    }
    return buffer;
}
```

### Using the `MBED_ERROR()` macro with module information

The code below uses an `MBED_ERROR` macro to print a fatal error indicating an invalid argument with the module name specified as `MODULE_APPLICATION`:

```CPP
void receive_data(unsigned char *buffer) {
    if (NULL == buffer) {
        MBED_ERROR( MBED_MAKE_ERROR(MBED_MODULE_APPLICATION, MBED_ERROR_CODE_INVALID_ARGUMENT), "Buffer pointer is Null" );
    }
    // read the data into given buffer

}
```

### Using the `MBED_WARNING()` macro with module information and return with Mbed error status

The code below uses an `MBED_WARNING` macro to report a invalid configuration attempt with the module name specified as `MBED_MODULE_PLATFORM`:

```CPP
mbed_error_status_t configure(int config_value) {
    if (config_value > 10) {
        //Log the fact that a invalid configuration attempt was made and return with error code
        MBED_WARNING( MBED_MAKE_ERROR(MBED_MODULE_PLATFORM, MBED_ERROR_CODE_UNSUPPORTED), "Invalid config parameter" );
        return MBED_ERROR_CODE_UNSUPPORTED;
    }

    //configure whatever

    return MBED_SUCCESS;
}
```

### Using the `MBED_ERROR1()` macro

The `MBED_ERROR1` macro is similar to `MBED_ERROR` macro, but it can take an additional context-specific argument. The error handling system also records this value as part of the context capture. The code below uses the `MBED_ERROR1` macro to print a fatal error indicating an out-of-memory condition with a context specific value as the last argument to `MBED_ERROR1` macro:

```CPP
void receive_data(unsigned char *buffer) {
    if (NULL == buffer) {
        MBED_ERROR1(MBED_MAKE_ERROR(MBED_MODULE_APPLICATION, MBED_ERROR_CODE_INVALID_ARGUMENT), "Buffer pointer is Null", 1024/* Size of allocation which failed */ );
    }
    // read the data into given buffer

}
```

### Using the `MBED_WARNING1()` macro

The `MBED_WARNING1` macro is similar to the `MBED_WARNING` macro, but it can take an additional context-specific argument. The error handling system also records this value as part of the context capture. The code below uses the `MBED_WARNING1` macro to report a warning with a context specific value as the last argument to `MBED_WARNING1` macro:

```CPP
mbed_error_status_t configure(int config_value) {
    if (config_value > 10) {
        //Log the fact that a invalid configuration attempt was made and return with error code
        MBED_WARNING1(MBED_MAKE_ERROR(MBED_MODULE_PLATFORM, MBED_ERROR_CODE_UNSUPPORTED), "Invalid config parameter", config_value /* Invalid config value */ );
        return MBED_ERROR_CODE_UNSUPPORTED;
    }

    //configure whatever

    return MBED_SUCCESS;
}
```

### Using `MBED_WARNING()` macro without module information

The code below uses an `MBED_WARNING` macro to report a invalid configuration attempt without module name:

```CPP
mbed_error_status_t configure(int config_value) {
    if (config_value > 10) {
        //Log the fact that a invalid configuration attempt was made and return with error code
        MBED_WARNING1(MBED_ERROR_UNSUPPORTED, "Invalid config value", 0 );
        return MBED_ERROR_UNSUPPORTED;
    }

    //configure whatever

    return MBED_SUCCESS;
}
```

### Using `mbed_get_first_error()` and `mbed_get_first_error_info()` functions to retrieve the first error or first warning logged in the system

The code below uses the `mbed_get_first_error()` and `mbed_get_first_error_info()` functions to retrieve the first error or first warning logged in the system using `MBED_WARNING()/MBED_ERROR()` calls:

```CPP
void get_first_error_info() {
    mbed_error_status_t first_error_status = mbed_get_first_error();
    printf("\nFirst error code = %d", MBED_GET_ERROR_CODE(first_error_status));

    //Now retrieve more information associated with this error
    mbed_error_ctx first_error_ctx;
    mbed_error_status_t first_error = mbed_get_first_error_info(&first_error_ctx);
}
```

### Using `mbed_get_last_error()` and `mbed_get_last_error_info()` functions to retrieve the last error or last warning logged in the system

Use the functions `mbed_get_last_error()` and `mbed_get_last_error_info()` to retrieve the last error or last warning logged in the system using `MBED_WARNING()/MBED_ERROR()` calls. Note that these are similar to `mbed_get_first_error()` and `mbed_get_first_error_info()` calls, except that they retrieve the last error or last warning in this case:

```CPP
void get_last_error_info() {
    mbed_error_status_t last_error_status = mbed_get_last_error();
    printf("\nLast error code = %d", MBED_GET_ERROR_CODE(last_error_status));

    //Now retrieve more information associated with this error
    mbed_error_ctx last_error_ctx;
    mbed_error_status_t last_error = mbed_get_last_error_info(&last_error_ctx);
}
```

### Using `mbed_get_error_hist_info()` and `mbed_get_error_hist_count()` to retrieve the error or warning information from the error history

You can use the function `mbed_get_error_hist_info()` to retrieve the error or warning information from the [error history](#error-history):

```CPP TODO
void get_error_info_from_hist() {
    //Retrieve error information from error history
    mbed_error_ctx hist_error_ctx;

    int num_entries_in_hist = mbed_get_error_hist_count();
    for(int i=0; i<num_entries_in_hist; i++) {
        //Reads the error context information for a specific error from error history, specified by an index(first arg to mbed_get_error_hist_info).
        //index of the error context entry in the history to be retrieved.
        //The number of entries in the error history is configured during build and the max index depends on max depth of error history.
        //index = 0 points to the oldest entry in the history, and index = (max history depth - 1) points to the latest entry in the error history.
        mbed_get_error_hist_info( i, &hist_error_ctx );
        printf("\nError code[%d] = %d", i, MBED_GET_ERROR_CODE(last_error_status))
    }
}
```

### Using `mbed_clear_all_errors()` to clear the error history

You can use the function `mbed_clear_all_errors()` to clear all currently logged errors from the [error history](#error-history). You can use this if you have already backed up all the currently logged errors (for example, to a file system or cloud) and want to capture new errors:

```CPP
void save_all_errors() {
    //Save the errors first
    save_all_errors();

    //We have sent all the current errors to Mbed Cloud. So clear the history so that you can capture next set of warnings or errors.
    mbed_clear_all_errors();
}
```

### Using `mbed_get_reboot_error_info()` to retrieve the reboot error info

In the example below, status variable `reboot_error_detected` is set to 1 when the callback is invoked. Then, the `main()`
function reads the reboot error information using `mbed_get_reboot_error_info()`.

```CPP TODO
mbed_error_ctx error_ctx;
int reboot_error_detected = 0;

//Callback during reboot
void mbed_error_reboot_callback(mbed_error_ctx *error_context)
{
    printf("error callback received");
    reboot_error_detected = 1;
}

// main() runs in its own thread in the OS
int main()
{
    if (reboot_error_detected == 1) {
        if (MBED_SUCCESS == mbed_get_reboot_error_info(&error_ctx)) {
            printf("\nSuccessfully read error context\n");
        }
    }
    //main continues...
}
```

### Using `mbed_get_reboot_fault_context()` to retrieve the fault context info

The example code below checks for the exception error (`MBED_ERROR_HARDFAULT_EXCEPTION`) using `error_status` in the error context
and then retrieves the fault context using `mbed_get_reboot_fault_context()`:

```CPP TODO
mbed_error_ctx error_ctx;
mbed_fault_context_t fault_ctx;
int reboot_error_detected = 0;

//Callback during reboot
void mbed_error_reboot_callback(mbed_error_ctx * error_context)
{
    printf("error callback received");
    reboot_error_detected = 1;
}

// main() runs in its own thread in the OS
int main()
{
    if (reboot_error_detected == 1) {
        if (MBED_SUCCESS == mbed_get_reboot_error_info(&error_ctx)) {
            printf("\nRead in reboot info\n");
            if (error_ctx.error_status == MBED_ERROR_HARDFAULT_EXCEPTION) {
               if (MBED_SUCCESS == mbed_get_reboot_fault_context(&fault_ctx)) {
                   printf("\nRead in fault context info\n");
               }
            }
        }
    }
    //main continues...
}
```

### Using `mbed_reset_reboot_error_info()` to clear the reboot error info

You can use `mbed_reset_reboot_error_info()` to clear the reboot error information:

```CPP TODO
void clear_reboot_errors() {

    //Clear the currently stored error info in Crash-data-RAM
    mbed_reset_reboot_error_info();
}
```

### Using `mbed_reset_reboot_count()` to reset the reboot count

You can use `mbed_reset_reboot_error_info()` to specifically reset the reboot count stored in Crash-data-RAM. Calling this function sets the reboot count to 0:

```CPP TODO
void clear_reboot_count() {

    //Clear the currently stored error info in Crash-data-RAM
    mbed_reset_reboot_count();
}
```

## Error handling example

The example application below demonstrates usage of error handling APIs:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-error-handling)](https://github.com/ARMmbed/mbed-os-example-error-handling/blob/mbed-os-5.14/main.cpp)

## Crash reporting example

The example application below demonstrates the crash reporting feature:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-crash-reporting)](https://github.com/ARMmbed/mbed-os-example-crash-reporting/blob/mbed-os-5.14/main.cpp)

## List of Mbed OS defined error codes and descriptions

Below are the predefined Mbed system error codes and their descriptions:

    MBED_ERROR_CODE_UNKNOWN                         Unknown error
    MBED_ERROR_CODE_INVALID_ARGUMENT                Invalid Argument
    MBED_ERROR_CODE_INVALID_DATA                    Invalid data
    MBED_ERROR_CODE_INVALID_FORMAT                  Invalid format
    MBED_ERROR_CODE_INVALID_INDEX                   Invalid Index
    MBED_ERROR_CODE_INVALID_SIZE                    Invalid Size
    MBED_ERROR_CODE_INVALID_OPERATION               Invalid Operation
    MBED_ERROR_CODE_NOT_FOUND                       Not Found
    MBED_ERROR_CODE_ACCESS_DENIED                   Access Denied
    MBED_ERROR_CODE_NOT_SUPPORTED                   Not supported
    MBED_ERROR_CODE_BUFFER_FULL                     Buffer Full
    MBED_ERROR_CODE_MEDIA_FULL                      Media/Disk Full
    MBED_ERROR_CODE_ALREADY_IN_USE                  Already in use
    MBED_ERROR_CODE_TIMEOUT                         Timeout error
    MBED_ERROR_CODE_NOT_READY                       Not Ready
    MBED_ERROR_CODE_FAILED_OPERATION                Requested Operation failed
    MBED_ERROR_CODE_OPERATION_PROHIBITED            Operation prohibited
    MBED_ERROR_CODE_OPERATION_ABORTED               Operation failed
    MBED_ERROR_CODE_WRITE_PROTECTED                 Attempt to write to write-protected resource
    MBED_ERROR_CODE_NO_RESPONSE                     No response
    MBED_ERROR_CODE_SEMAPHORE_LOCK_FAILED           Semaphore lock failed
    MBED_ERROR_CODE_MUTEX_LOCK_FAILED               Mutex lock failed
    MBED_ERROR_CODE_SEMAPHORE_UNLOCK_FAILED         Semaphore unlock failed
    MBED_ERROR_CODE_MUTEX_UNLOCK_FAILED             Mutex unlock failed
    MBED_ERROR_CODE_CRC_ERROR                       CRC error or mismatch
    MBED_ERROR_CODE_OPEN_FAILED                     Open failed
    MBED_ERROR_CODE_CLOSE_FAILED                    Close failed
    MBED_ERROR_CODE_READ_FAILED                     Read failed
    MBED_ERROR_CODE_WRITE_FAILED                    Write failed
    MBED_ERROR_CODE_INITIALIZATION_FAILED           Initialization failed
    MBED_ERROR_CODE_BOOT_FAILURE                    Boot failure
    MBED_ERROR_CODE_OUT_OF_MEMORY                   Out of memory
    MBED_ERROR_CODE_OUT_OF_RESOURCES                Out of resources
    MBED_ERROR_CODE_ALLOC_FAILED                    Alloc failed
    MBED_ERROR_CODE_FREE_FAILED                     Free failed
    MBED_ERROR_CODE_OVERFLOW                        Overflow error
    MBED_ERROR_CODE_UNDERFLOW                       Underflow error
    MBED_ERROR_CODE_STACK_OVERFLOW                  Stack overflow error
    MBED_ERROR_CODE_ISR_QUEUE_OVERFLOW              ISR queue overflow
    MBED_ERROR_CODE_TIMER_QUEUE_OVERFLOW            Timer Queue overflow
    MBED_ERROR_CODE_CLIB_SPACE_UNAVAILABLE          Standard library error - Space unavailable
    MBED_ERROR_CODE_CLIB_EXCEPTION                  Standard library error - Exception
    MBED_ERROR_CODE_CLIB_MUTEX_INIT_FAILURE         Standard library error - Mutex Init failure
    MBED_ERROR_CODE_CREATE_FAILED                   Create failed
    MBED_ERROR_CODE_DELETE_FAILED                   Delete failed
    MBED_ERROR_CODE_THREAD_CREATE_FAILED            Thread Create failed
    MBED_ERROR_CODE_THREAD_DELETE_FAILED            Thread Delete failed
    MBED_ERROR_CODE_PROHIBITED_IN_ISR_CONTEXT       Operation Prohibited in ISR context
    MBED_ERROR_CODE_PINMAP_INVALID                  Pinmap Invalid
    MBED_ERROR_CODE_RTOS_EVENT                      Unknown Rtos Error
    MBED_ERROR_CODE_RTOS_THREAD_EVENT               Rtos Thread Error
    MBED_ERROR_CODE_RTOS_MUTEX_EVENT                Rtos Mutex Error
    MBED_ERROR_CODE_RTOS_SEMAPHORE_EVENT            Rtos Semaphore Error
    MBED_ERROR_CODE_RTOS_MEMORY_POOL_EVENT          Rtos Memory Pool Error
    MBED_ERROR_CODE_RTOS_TIMER_EVENT                Rtos Timer Error
    MBED_ERROR_CODE_RTOS_EVENT_FLAGS_EVENT          Rtos Event flags Error
    MBED_ERROR_CODE_RTOS_MESSAGE_QUEUE_EVENT        Rtos Message queue Error
    MBED_ERROR_CODE_DEVICE_BUSY                     Device Busy
    MBED_ERROR_CODE_CONFIG_UNSUPPORTED              Configuration not supported
    MBED_ERROR_CODE_CONFIG_MISMATCH                 Configuration mismatch
    MBED_ERROR_CODE_ALREADY_INITIALIZED             Already initialized
    MBED_ERROR_CODE_HARDFAULT_EXCEPTION             HardFault exception
    MBED_ERROR_CODE_MEMMANAGE_EXCEPTION             MemManage exception
    MBED_ERROR_CODE_BUSFAULT_EXCEPTION              BusFault exception
    MBED_ERROR_CODE_USAGEFAULT_EXCEPTION            UsageFault exception
    MBED_ERROR_CODE_BLE_NO_FRAME_INITIALIZED        BLE No frame initialized
    MBED_ERROR_CODE_BLE_BACKEND_CREATION_FAILED     BLE Backend creation failed
    MBED_ERROR_CODE_BLE_BACKEND_NOT_INITIALIZED     BLE Backend not initialized

Note that the system defined error codes can potentially expand in the future as new error scenarios are identified and incorporated into the Mbed OS error handling system.

For each of the above mentioned error codes, a corresponding system error status value with module information set to `MBED_MODULE_UNKNOWN` has been predefined for convenience and implementations to report errors when the module information is unknown (for example, from exceptions handlers where the module is unknown).

See the below Doxygen file for additional information regarding error code definitions:

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/mbed__error_8h_source.html)

## Related content

- Debug and develop [build profiles](../tools/build-profiles.html).
- Mbed OS [error decoder](https://mbed.com/s/error).
- [Office Hours video about Crash Reporting](https://www.youtube.com/watch?v=SdC_aM-aZNc).
- [Office Hours video about Crash Dump Analysis](https://www.youtube.com/watch?v=7xKWFSnUye8).

