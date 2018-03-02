## Analyzing Mbed OS crash dump

This tutorial explains the crash dump generation in Mbed OS and how to analyze the crash dump data.

### Crash dump generation on fault exception

When the system crashes due to fault exceptions, the Mbed OS fault exception handler is invoked and generates a crash dump containing register context and current thread information. This information prints to your serial terminal. The register context generated is the state of registers at the instance when the exception was triggered. The following Cortex-M fault exceptions trigger the Mbed OS fault exception handler. 

1. HardFault Exception.
2. MemManage Exception.
3. BusFault Exception.
4. UsageFault Exception.

The exceptions supported on your platform depend on the specific Cortex-M core you have in your system. 

For example, Cortex-M0 (or any ARMv6M cores) cores do not have MemManage, BusFault and UsageFault exceptions implemented. In those cases, all exceptions are reported as HardFault exception. Please look at the **Technical Reference Manual** and **ARM Architecture Reference Manual** documents for more information on exceptions supported for the specific core you have in your system.

Below is an example of the crash dump the Mbed OS fault exception handler generate. 

```
++ MbedOS Fault Handler ++

FaultType: HardFault

Context:
R0   : 0000C158
R1   : 00000000
R2   : E000ED00
R3   : 0000AAA3
R4   : 0000C182
R5   : 00000000
R6   : 00000000
R7   : 00000000
R8   : 00000000
R9   : 00000000
R10  : 00000000
R11  : 00000000
R12  : FFFFFFFF
SP   : 20002E98
LR   : 00001799
PC   : 00001774
xPSR : 210F0000
PSP  : 20002E30
MSP  : 2002FFD8
CPUID: 410FC241
HFSR : 40000000
MMFSR: 00000000
BFSR : 00000000
UFSR : 00000100
DFSR : 00000008
AFSR : 00000000
SHCSR: 00000000

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
