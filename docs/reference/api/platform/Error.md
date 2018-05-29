## Mbed OS Error Status Definitions and Error Handling
Mbed OS provides error code and error status definitions and error handling APIs for Error construction, reporting and retrieving previously reported errors. It also provides functions and macros to generate and define new error status values, extract information from error status values and to generate fatal system errors which terminates the application. Any software layer(Applications, Drivers, HAL, Protocol stacks etc) can use these error handling APIs. The error functions also facilitates emitting an error message through STDOUT. `mbed_error.h` declares the error functions provided by Mbed OS.

Conceptually, Error Handling is a platform service implemented by platform layer of Mbed OS and provides the following:
1. Provides System Defined Error Codes and Status values in `mbed_error.h`
1. Provides APIs for Error Construction, Reporting and Error history(see below sections), callable from anywhere in the system.
1. Provides ISR-safe and Thread-safe error handling APIs.
1. Provides mechanisms for extending the error status definitions.

### Error Status Usage
Mbed OS pre-defines a set of system errors and **Error Status** is defined as a 32-bit Signed Integer in **NEGATIVE space**. The error status values are represented by **mbed_error_status_t** type.

Error Status can be used  
- To indicate return status from function calls
  - Returning 0(=**MBED_SUCCESS**) or any positive number would be considered success.
  - A predefined status code named **MBED_SUCCESS**(=0) is available to indicate success.

- As system error codes
  - Used to report error conditions to the OS error handling sub-system.

### Error Status Types and Error Code Ranges
Mbed OS error status encoding defines three types of error status values. They are as below. Note that type of error status is encoded into the 32-bit signed integer.
- System Errors
- Posix Errors
- Custom Defined Errors

And for each error status type, we have defined a range of error codes which forms the least significant 16-bits of 32-bit error status values. Based on error code definitions below are the error code ranges for each error type.
- Posix Error Codes: 1 to 255 (see **Posix Error Codes Support** section below)
- System Error Codes: 256 to 4095
- Custom Error Codes: 4096 to 65535 

Its important to understand the difference between the terminologies "**Error Code**" and "**Error Status**". "**Error Status**" is the 32-bit signed integer in **NEGATIVE space** used by applications to report the error, and "**Error Code**" is the least significant 16-bits of 32-bit Error Status values indicating the error situation(For example, Out of memory). All pre-defined error status definitions start with **MBED_ERROR_** prefix and all pre-defined error code definitions start with **MBED_ERROR_CODE_**.
Error codes are not used by themselves, they are always encoded into error status values when reporting or representing errors in the system.

Accordingly, the Error Status Ranges are as below for each type:
- Posix Error Status  - 0xFFFFFFFF to 0xFFFFFF01 - This corresponds to Posix errors represented as negative.
- System Error Status - 0x80XX0100 to 0x80XX0FFF - This corresponds to System errors range(all values are negative). Bits 23-16 will capture the module type (marked with XX)
- Custom Error Status - 0xA0XX1000 to 0xA0XXFFFF - This corresponds to Custom errors range(all values are negative). Bits 23-16 will capture the module type (marked with XX)

Mbed OS system error status values can also capture the module reporting the error by encoding the module identifier in the error status depending on the type of error status. The error status values/ranges are provided here for information purposes but no implementation should assume or manipulate the bit fields in the encoding directly. Implementation using Mbed OS error handling and reporting APIs should deal with error status like an opaque object and should use Mbed OS provided macros and functions to manipulate or interpret the error status values.

### Posix Error Codes Support
Presently many modules(like filesystems) under Mbed-OS use Posix error codes. For this reason, Mbed OS error status definitions captures Posix error codes as well
under the new error encoding scheme. Error code defintions also ensures that Posix error code values doesn’t overlap with Mbed Error code values and thus make it easier for developers to report Posix error codes into Mbed OS error handling system if required.
To incorporate Posix error code representation into Mbed-OS, a portion of error space is allocated for Posix error codes. Since Mbed-OS error codes will always be negative, we will capture the negative of the actual Posix error code in the error code defintions. For example, the Posix error code EPERM in Mbed-OS error code space would be represented as ngeative of actual EPERM value. This aligns with Mbed-OS error encoding convention of using negative values, but the numerical(or absolute) value will be same as the Posix error code. Also note that, since Posix error codes are represented as negative of Posix error codes, they cannot capture module information as in Mbed OS system error codes.
**Although we support Posix error codes for compatibility reasons, its highly encouraged that all future Mbed-OS focussed implementations use Mbed-OS error definitions so that errors reported works seamlessly with error reporting and handling implementation in Mbed-OS.**

### Error Context Capture
Error handling system in Mbed OS automatically captures the thread context for each error reported into the system. The context captured includes following information:

- Error Status Code – Status code
- Error Address – Captures return address of set error calls.
- Error Value – A context specific value set by the caller in MBED_ERROR()/MBED_WARNING() calls
- Thread ID – ID of the current thread - This information is captured only if the system is built with RTOS support.
- Thread Entry Address – Entry function for the current thread - This information is captured only if the system is built with RTOS support.
- Thread Stack Size – Size of stack - This information is captured only if the system is built with RTOS support.
- Thread Stack Mem - Top of stack - This information is captured only if the system is built with RTOS support.
- Thread Current SP – SP value (PSP or MSP based on what’s active) - This information is captured only if the system is built with RTOS support.
- Filename and Line number - By default capturing of filename, line number is disabled. If you need this information to be captured it needs to be enabled using **MBED_CONF_ERROR_FILENAME_CAPTURE_ENABLED** macro.

This captured context will be emitted through STDOUT in the case of fatal errors and in the case of warnings it will be recorded by the system and can be retrieved later for system diagnostics, external reporting and for debugging purposes.

### Error Reporting
Mbed OS provides mainly three ways to report an error using the error handling implementation - 
1. Using **error()** function to report a fatal error condition - This is the legacy function used for reporting a fatal error. It has been modified to capture the context information. But, it will not capture the address of the caller, module information and also doesn't support reporting specific error codes. Any implementation using this API to report an error will use the error status **MBED_ERROR_UNKNOWN**. Its highly encouraged that all future Mbed-OS focussed implementations use MBED_ERROR()/MBED_ERROR1() or MBED_WARNING()/MBED_WARNING() macros for reporting errors.**
1. Using **MBED_ERROR()/MBED_ERROR()** macros to report a fatal error with enhanced capability for capturing module reporting the error.
1. Using **MBED_WARNING()/MBED_WARNING1()** macros to report a non-fatal error with enhanced capability for capturing module reporting the error.

When you report an error using MBED_ERROR()/MBED_ERROR1() macros, the error will be recorded in the error history(see **Error History** section below) with the context, the error information will be printed out to STDOUT and the application will be terminated.
Note that the error functions outputs the error message or the filename in debug and develop builds only.

Below is an example of terminal output created by MBED_ERROR1() call. Note that filename capture is disabled by default.

```
++ MbedOS Error Info ++
Error Status: 0x80000110 Code: 272 Entity: 0
Error Message: System type error
Location: 0xab59
File:main.cpp+222
Error Value: 0xdeaddead
Current Thread: Id: 0x200020e0 Entry: 0xcb31 StackSize: 0x1000 StackMem: 0x200010e0 SP: 0x20002020
-- MbedOS Error Info --
```

### Constructing Error Status values in your implementation
Mbed OS provides necessary functions and macros for implementations to construct error status values. There are few ways you can construct error status values. 
If you know the module reporting the error you can use the **MBED_MAKE_ERROR()** macro to construct an error status with the module information. For example, if you want to report 
an unsupported configuration from serial driver you may construct the error status as follows to capture the module information along with specific error code. In the below example,
we are constructing an error status value with error code set to MBED_ERROR_CODE_CONFIG_UNSUPPORTED from serial driver indicated by module info set to MBED_MODULE_DRIVER_SERIAL.
```mbed_error_status_t error = MBED_MAKE_ERROR(MBED_MODULE_DRIVER_SERIAL, MBED_ERROR_CODE_CONFIG_UNSUPPORTED)```

There may be scenarios when the module might have called an API exported from other modules like protocol stacks but have received an error status in return. In those cases, it doesn't know which of the lower layers raised the
error but we may still want to report the error without the module information. In those cases, it can use the predefined error status such as MBED_ERROR_CONFIG_UNSUPPORTED with the module value already set to MBED_MODULE_UNKNOWN.
This is equivalent to defining an error status with MODULE_UNKNOWN as below. Although, using predefined values like MBED_ERROR_CONFIG_UNSUPPORTED makes it more convenient and easier to read the implementation.
```mbed_error_status_t error = MBED_MAKE_ERROR(MBED_MODULE_UNKNOWN, MBED_ERROR_CODE_CONFIG_UNSUPPORTED)```

### Error History
Error handling implementation in Mbed OS also keeps track of previous errors in the system. This feature is called **Error history** and is configurable using the configuration value **MBED_CONF_ERROR_HIST_SIZE**.
MBED_CONF_ERROR_HIST_SIZE configures the number of previous errors the system keeps in its error history. You can disable the history feature by setting MBED_CONF_ERROR_HIST_SIZE to 0 if required. By default, 
it keeps track of last four errors. Irrespective of whether error history is enabled or not, the system always records the first and last error happened in the system. See
[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/mbed__error_8h_source.html) 
to learn more about the APIs related to error history.

### Extending Error Codes
Mbed OS application and system developers may need to define error codes specific to their the application. But they may not be applicable to the broader system to be defined as system error codes. In those cases,
application can pre-define custom error codes using **MBED_DEFINE_CUSTOM_ERROR()** macro. This macro specifically defines error status values whole type will be of **Custom Defned Errors** as mentioned above in
**Error Status Types** section. If you are defining custom error codes, it's advised to capture those definition in `mbed_error.h` in custom error codes section. Please review documentation at 
[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/mbed__error_8h_source.html)

### Error Hook for applications
Some applications may want to do custom error handling when an error is reported using MBED_ERROR()/MBED_WARNING() APIs. Applications can accomplish this by registering an error hook function with Mbed OS
error handling system using **mbed_set_error_hook()** API. This function will be called with error context information whenever system handles a **MBED_ERROR()/MBED_WARNING()** call. This function should be implemented for re-entrancy as multiple threads may invoke MBED_ERROR()/MBED_WARNING() which may cause error hook to be called in parallel. 

### Error Handling functions reference
Below link provides the documentation on all the APIs provided by Mbed OS for Error Definitions and Handling.
[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/mbed__error_8h_source.html)

### Error Handling API examples
#### Using error() function
The code below uses error function to print a fatal error indicating an out-of-memory condition.

```C
void *operator new(std::size_t count) {
    void *buffer = malloc(count);
    if (NULL == buffer) {
        error("Operator new out of memory\r\n");
    }
    return buffer;
}
```

#### Using MBED_ERROR() function with module information
The code below uses an MBED_ERROR function to print a fatal error indicating an out-of-memory condition with module name specified as MODULE_APPLCIATION.
```C
void receive_data(unsigned char *buffer) {
    if (NULL == buffer) {
        MBED_ERROR1(MBED_MAKE_ERROR(MBED_MODULE_APPLICATION, MBED_ERROR_CODE_INVALID_ARGUMENT), "Buffer pointer is Null", 0 );
    }
    // read the data into given buffer
    
}
```

#### Using MBED_WARNING() function with module information and return with Mbed Error status
The code below uses an MBED_WARNING function to report a invalid configuration attempt with module name specified as MBED_MODULE_PLATFORM.
```C
mbed_error_status_t configure(int config_value) {
    if (config_value > 10) {
        //Log the fact that a invalid configuration attempt was made and return with error code
        MBED_WARNING1(MBED_MAKE_ERROR(MBED_MODULE_PLATFORM, MBED_ERROR_CODE_UNSUPPORTED), "Buffer pointer is Null", 0 );
        return MBED_ERROR_CODE_UNSUPPORTED;
    }
    
    //configure whatever

    return MBED_SUCCESS;
}
```

#### Using MBED_WARNING() function without module information
The code below uses an MBED_WARNING function to report a invalid configuration attempt without module name.
```C
mbed_error_status_t configure(int config_value) {
    if (config_value > 10) {
        //Log the fact that a invalid configuration attempt was made and return with error code
        MBED_WARNING1(MBED_ERROR_UNSUPPORTED, "Buffer pointer is Null", 0 );
        return MBED_ERROR_UNSUPPORTED;
    }
    
    //configure whatever

    return MBED_SUCCESS;
}
```

### List of Mbed OS Defined Error Codes and Description

Below are the pre-defined Mbed System error codes and their description. Also look at 
[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/mbed__error_8h_source.html)
for additional information.

    MBED_ERROR_CODE_UNKNOWN                    Unknown error
    MBED_ERROR_CODE_INVALID_ARGUMENT           Invalid Argument
    MBED_ERROR_CODE_INVALID_DATA               Invalid data
    MBED_ERROR_CODE_INVALID_FORMAT             Invalid format
    MBED_ERROR_CODE_INVALID_INDEX              Invalid Index
    MBED_ERROR_CODE_INVALID_SIZE               Inavlid Size 
    MBED_ERROR_CODE_INVALID_OPERATION          Invalid Operation 
    MBED_ERROR_CODE_NOT_FOUND                  Not Found 
    MBED_ERROR_CODE_ACCESS_DENIED              Access Denied 
    MBED_ERROR_CODE_NOT_SUPPORTED              Not supported 
    MBED_ERROR_CODE_BUFFER_FULL                Buffer Full 
    MBED_ERROR_CODE_MEDIA_FULL                 Media/Disk Full 
    MBED_ERROR_CODE_ALREADY_IN_USE             Already in use 
    MBED_ERROR_CODE_TIMEOUT                    Timeout error 
    MBED_ERROR_CODE_NOT_READY                  Not Ready 
    MBED_ERROR_CODE_FAILED_OPERATION           Requested Operation failed 
    MBED_ERROR_CODE_OPERATION_PROHIBITED       Operation prohibited 
    MBED_ERROR_CODE_OPERATION_ABORTED          Operation failed 
    MBED_ERROR_CODE_WRITE_PROTECTED            Attempt to write to write-protected resource 
    MBED_ERROR_CODE_NO_RESPONSE                No response 
    MBED_ERROR_CODE_SEMAPHORE_LOCK_FAILED      Sempahore lock failed 
    MBED_ERROR_CODE_MUTEX_LOCK_FAILED          Mutex lock failed 
    MBED_ERROR_CODE_SEMAPHORE_UNLOCK_FAILED    Sempahore unlock failed 
    MBED_ERROR_CODE_MUTEX_UNLOCK_FAILED        Mutex unlock failed 
    MBED_ERROR_CODE_CRC_ERROR                  CRC error or mismatch 
    MBED_ERROR_CODE_OPEN_FAILED                Open failed 
    MBED_ERROR_CODE_CLOSE_FAILED               Close failed 
    MBED_ERROR_CODE_READ_FAILED                Read failed 
    MBED_ERROR_CODE_WRITE_FAILED               Write failed 
    MBED_ERROR_CODE_INITIALIZATION_FAILED      Initialization failed 
    MBED_ERROR_CODE_BOOT_FAILURE               Boot failure 
    MBED_ERROR_CODE_OUT_OF_MEMORY              Out of memory 
    MBED_ERROR_CODE_OUT_OF_RESOURCES           Out of resources 
    MBED_ERROR_CODE_ALLOC_FAILED               Alloc failed 
    MBED_ERROR_CODE_FREE_FAILED                Free failed 
    MBED_ERROR_CODE_OVERFLOW                   Overflow error 
    MBED_ERROR_CODE_UNDERFLOW                  Underflow error 
    MBED_ERROR_CODE_STACK_OVERFLOW             Stack overflow error 
    MBED_ERROR_CODE_ISR_QUEUE_OVERFLOW         ISR queue overflow 
    MBED_ERROR_CODE_TIMER_QUEUE_OVERFLOW       Timer Queue overflow 
    MBED_ERROR_CODE_CLIB_SPACE_UNAVAILABLE     Standard library error - Space unavailable 
    MBED_ERROR_CODE_CLIB_EXCEPTION             Standard library error - Exception 
    MBED_ERROR_CODE_CLIB_MUTEX_INIT_FAILURE    Standard library error - Mutex Init failure 
    MBED_ERROR_CODE_CREATE_FAILED              Create failed 
    MBED_ERROR_CODE_DELETE_FAILED              Delete failed 
    MBED_ERROR_CODE_THREAD_CREATE_FAILED       Thread Create failed 
    MBED_ERROR_CODE_THREAD_DELETE_FAILED       Thread Delete failed 
    MBED_ERROR_CODE_PROHIBITED_IN_ISR_CONTEXT  Operation Prohibited in ISR context 
    MBED_ERROR_CODE_PINMAP_INVALID             Pinmap Invalid 
    MBED_ERROR_CODE_RTOS_EVENT                 Unknown Rtos Error 
    MBED_ERROR_CODE_RTOS_THREAD_EVENT          Rtos Thread Error 
    MBED_ERROR_CODE_RTOS_MUTEX_EVENT           Rtos Mutex Error 
    MBED_ERROR_CODE_RTOS_SEMAPHORE_EVENT       Rtos Semaphore Error 
    MBED_ERROR_CODE_RTOS_MEMORY_POOL_EVENT     Rtos Memory Pool Error 
    MBED_ERROR_CODE_RTOS_TIMER_EVENT           Rtos Timer Error 
    MBED_ERROR_CODE_RTOS_EVENT_FLAGS_EVENT     Rtos Event flags Error 
    MBED_ERROR_CODE_RTOS_MESSAGE_QUEUE_EVENT   Rtos Message queue Error 
    MBED_ERROR_CODE_DEVICE_BUSY                Device Busy 
    MBED_ERROR_CODE_CONFIG_UNSUPPORTED         Configuration not supported 
    MBED_ERROR_CODE_CONFIG_MISMATCH            Configuration mismatch 
    MBED_ERROR_CODE_ALREADY_INITIALIZED        Already initialzied 
    MBED_ERROR_CODE_HARDFAULT_EXCEPTION        HardFault exception 
    MBED_ERROR_CODE_MEMMANAGE_EXCEPTION        MemManage exception 
    MBED_ERROR_CODE_BUSFAULT_EXCEPTION         BusFault exception 
    MBED_ERROR_CODE_USAGEFAULT_EXCEPTION       UsageFault exception
    
Note that the system defined error codes can potentially expand in future as new error scenarios are identified and incorporated into Mbed OS error handling system.
And for each of the above mentioned error codes, a corresponding system error status value with module information set to MBED_MODULE_UNKNOWN has been pre-defined 
for convenience and implementations to report errors when the module info is unknown(For example:- from exceptions handlers where the module is unknown).

### Related content
- Debug and develop [build profiles](/docs/development/tools/build-profiles.html).

