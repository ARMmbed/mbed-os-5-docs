## Logger

Mbed OS provides a set of API's that you can use to output different log level messages to STDIO at runtime. mbed_logger.h declares these functions, which are available only in debug builds.
API's in logging module are printf-style API's which take module name and format string followed by arguments.

By default all messages till LOG_LEVEL_DEBUG are enabled. If you want to enable Trace and Info level messages, then set `MBED_CONF_MAX_LOG_LEVEL` accordingly.

### Debug Log Levels
Below are various log levels supported and recommended usage.

#### LOG_LEVEL_ERR_CRITICAL
In case of critical errors when system recovery is not possible, you should use `MBED_CRIT` API. `MBED_CRIT` is equivalent to `ASSERT`, it will dump previous debug log and application will terminate. 

Usage:
```C
uint8_t serial_tx_active(serial_t *obj) {
    MBED_ASSERT(obj);
    ...
}
Is Equivalent to 
uint8_t serial_tx_active(serial_t *obj) {
    if (NULL == obj) {
        MBED_CRIT("UART", "NULL object passed %s" __FUNCTION__);
    }
    ...
}
```

#### LOG_LEVEL_ERR
You should use error level in OS, HAL, library, application, etc to report all the errors. Errors are not considered fatal by OS, library and will not terminate the application.

Usage:
```C
Funcitons returns NULL and does not terminate the application. If error is categorized as fatal, use `MBED_CRIT` instead.
void *operator new(std::size_t count) {
    void *buffer = malloc(count);
    if (NULL == buffer) {
        MBED_ERR("OS", "Operator new out of memory");
    }
    return buffer;
}

Fatal error, will terminate the application if memory is not available.
void *operator new(std::size_t count) {
    void *buffer = malloc(count);
    if (NULL == buffer) {
        MBED_CRIT("OS", "Operator new out of memory");
    }
    return buffer;
}
```

#### LOG_LEVEL_WARN
You should use warning level in OS, HAL, library, application, etc to log all the warning messages.

Usage:
```C
void dev_init() {
    ...
    if (DEV_ID != id) {
        MBED_WARN ("Driver", "Incorrect Device ID: Expected %d Actual %d", DEV_ID, id);
    }
    ...
}
```

#### LOG_LEVEL_DEBUG
You should use debug level in user application for adding debug level messages. You should not use debug level in OS, HAL and libraries instead trace level should be used. 

Usage:
```C
void main() {
    ...
    int err = dev_init();
    if (SUCCESS == err) {
        MBED_DBG("Main", "Init successful");
    }
    ...
}
```
You can alse use `MBED_DBG_IF` function for debug level logs. It is similar to `MBED_DBG` except that it takes an additional argument for condition, the message is logged only if condition evaluates to true.

Usage:
```C
void main() {
    ...
    int err = dev_init();
    MBED_DBG_IF("Main", (SUCCESS == err), "Init successful");
    ...
}
```

#### LOG_LEVEL_INFO
You can use info level messages to log any additional information. 

Usage:
```C
void main() {
    ...
    case STATE_DISCONNECTED:
        MBED_INFO("Main", "Disconnected");
        break;
    ...
}
```
You can alse use `MBED_INFO_IF` function for info level logs. It is similar to `MBED_INFO` except that it takes an additional argument for condition, the message is logged only if condition evaluates to true.

Usage:
```C
void main() {
    ...
    case STATE_DISCONNECTED:
        MBED_INFO_IF("Main", (true == wasRequested), "Disconnect successful");
        MBED_INFO_IF("Main", (false == wasRequested), "Disconnect event occurred");
        break;
    ...
}
```

#### LOG_LEVEL_TRACE
You should use trace level in HAL, OS and libraries for adding debug logs. Trace level messsages are by default disabled, you can set `MBED_CONF_MAX_LOG_LEVEL` as `LOG_LEVEL_TRACE` to enable all trace logs.

Usage:
```C
int dev_init() {
    ...
    MBED_TRACE("Driver", "Init successful");
    return SUCCESS;
}
```
You can alse use `MBED_TRACE_IF` function for trace level logs. It is similar to `MBED_TRACE` except that it takes an additional argument for condition, the message is logged only if condition evaluates to true.

Usage:
```C
#define ENABLE_DRIVER_MSG   0
int dev_init() {
    ...
    MBED_TRACE_IF("Main", ENABLE_DRIVER_MSG, "Init successful");
    return SUCCESS;
    ...
}
```
Note: We recommend modules to have additional macro for enabling driver specific messages, default set as false and use `MBED_TRACE_IF` for all trace messages. This will help in enabling trace level debugs for particular driver or module without enabling all messages of trace level. This will be effective only if all modules, drivers, hal interfaces and libraries implement it.

### MBED_LOG API
`MBED_LOG` API is general trace API which is always enabled and can be used to log messages of all levels. You can use it to create a wrapper/frontend for any other logging system using mbed logging module as backend.

Usage:
```C
#define tr_warn(...)        MBED_LOG(TRACE_LEVEL_WARN, TRACE_GROUP, ##__VA_ARGS__)
#define tr_cmdline(...)     MBED_LOG(TRACE_LEVEL_CMD, TRACE_GROUP, ##__VA_ARGS__)
```

Note: 
1. Old Mbed OS logging APIs `mbed_trace`, `error`, `debug`, `debug_if`, are deprecated.
2. All API's are available in the debug and develop build profiles but not in the release build profile.

### Logger class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/development/mbed-os-api-doxy/<TODO>)

### Log example

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/logging/)](https://os.mbed.com/teams/mbed_example/code/logging/file/10b2ce72c7ac/main.cpp/)
