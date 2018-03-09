## Analyzing Mbed OS crash dump

This tutorial explains the crash dump generation in Mbed OS and how to analyze the crash dump data.

### Crash dump generation on fault exception

When the system crashes due to fault exceptions, the Mbed OS fault exception handler is invoked and generates a crash dump containing register context and current thread information. This information prints to your serial terminal. The register context generated is the state of registers at the instance when the exception was triggered. The following Cortex-M fault exceptions trigger the Mbed OS fault exception handler.

1. HardFault Exception.
2. MemManage Exception.
3. BusFault Exception.
4. UsageFault Exception.

The exceptions supported on your platform depend on the specific Cortex-M core you have in your system.

For example, Cortex-M0 cores (or any ARMv6M cores) do not have MemManage, BusFault and UsageFault exceptions implemented. In those cases, all exceptions are reported as HardFault exception. Please look at the **Technical Reference Manual** and **ARM Architecture Reference Manual** documents for more information on exceptions supported for the specific core you have in your system.

Below is an example of the crash dump (with a description of registers) that the Mbed OS fault exception handler generates.

```
++ MbedOS Fault Handler ++

FaultType: HardFault

Context:
R0   : 0000C158     - R0 at the time of exception
R1   : 00000000     - R1 at the time of exception
R2   : E000ED00     - R2 at the time of exception
R3   : 0000AAA3     - R3 at the time of exception
R4   : 0000C182     - R4 at the time of exception
R5   : 00000000     - R5 at the time of exception
R6   : 00000000     - R6 at the time of exception
R7   : 00000000     - R7 at the time of exception
R8   : 00000000     - R8 at the time of exception
R9   : 00000000     - R9 at the time of exception
R10  : 00000000     - R10 at the time of exception
R11  : 00000000     - R11 at the time of exception
R12  : FFFFFFFF     - R12 at the time of exception
SP   : 20002E98     - SP/R13 at the time of exception
LR   : 00001799     - LR/R14 at the time of exception
PC   : 00001774     - PC at the time of exception
xPSR : 210F0000     - xPSR at the time of exception
PSP  : 20002E30     - PSP value after the exception happened
MSP  : 2002FFD8     - MSP value after the exception happened
CPUID: 410FC241     - CPUID Register Value
HFSR : 40000000     - HFSR value after the exception happened
MMFSR: 00000000     - MMFSR value after the exception happened
BFSR : 00000000     - BFSR value after the exception happened
UFSR : 00000100     - UFSR value after the exception happened
DFSR : 00000008     - DFSR value after the exception happened
AFSR : 00000000     - AFSR value after the exception happened
SHCSR: 00000000     - SHCSR value after the exception happened
Mode : Thread       - Processor mode at the time of exception
Priv : Privileged   - Privilege level at the time of exception
Stack: PSP          - Stack pointer in use at the time of exception

Thread Info:
Current:
State: 00000002 EntryFn: 00002595 Stack Size: 00001000 Mem: 20001EA0 SP: 20002E60
Next:
State: 00000002 EntryFn: 00002595 Stack Size: 00001000 Mem: 20001EA0 SP: 20002E60
Wait Threads:
State: 00000083 EntryFn: 00004205 Stack Size: 00000300 Mem: 20000E18 SP: 200010B0
Delay Threads:
Idle Thread:
State: 00000001 EntryFn: 00002715 Stack Size: 00000200 Mem: 20001118 SP: 200012D8

-- MbedOS Fault Handler --
```

### Analyzing crash dump

In the example above, you can see that the crash dump indicates the fault exception type (see **FaultType**), the register context (see **Context**) at the time of exception and the current threads (see **Thread Info**) in the system, along with their stack information.

The register context contains key information to determine the cause and location of crash. For example, you can use **PC** value to find the location of the crash and **LR** to find the caller of the function where the crash occurred.

Note that the **LR** value may not reflect the actual caller, depending on the invocation of the function. You can use the linker address map generated during the build to find the name of the function from the **PC** value. The other key information in the register context is fault status register values (**HFSR, MMFSR, UFSR and BFSR**). The values in these registers indicate the cause of the exception. Please look at the **Technical Reference Manual** and **ARM Architecture Reference Manual** documents for more information on how to interpret these registers.

The thread information section is split into five subsections corresponding to the state of the thread. For each thread: state of the thread (**State**), entry function address (**EntryFn**), stack size (**Stack Size**), stack top (**Mem**) and current stack pointer (**SP**) are reported. You can use the linker address map to find the thread entry function from the **EntryFn** value. You can also use the stack size (**Stack Size**), stack top (**Mem**) and current stack pointer (**SP**) value to determine if there is thread stack overflow. For example, if the **SP** value is smaller than the **Mem** value, it indicates stack overflow for that thread.

### Crash dump analyzer script

Mbed OS provides a convenience script, named **crash_log_parser**, to help analyze crash data. Please look at the [documentation for crash_log_parser](/docs/v5.8/tools/debug/crash-log-parser-tool.html) for more information.
