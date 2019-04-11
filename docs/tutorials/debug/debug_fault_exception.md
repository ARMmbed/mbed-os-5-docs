# Analyzing Mbed OS crash dump

This tutorial explains the crash dump generation in Mbed OS and how to analyze the crash dump data.

## Crash dump generation on fault exception

When the system crashes due to fault exceptions, the Mbed OS fault exception handler is invoked and generates a crash dump containing register context and current thread information. This information prints to your serial (STDOUT) terminal. The register context generated is the state of registers at the instance when the exception triggers. The following Cortex-M fault exceptions trigger the Mbed OS fault exception handler.

- MemManage Exception - Memory accesses that violate the setup in the MPU and certain illegal memory accesses trigger memory management faults.
- BusFault Exception - When an error response is received during a transfer on the AHB interfaces, it produces bus faults.
- UsageFault Exception - Division by zero, unaligned accesses and trying to execute coprocessor instructions can cause usage faults.
- HardFault Exception - Triggered on all fault conditions or if the corresponding fault handler (one of the above) is not enabled.

Please look at the **Technical Reference Manual** and **Arm Architecture Reference Manual** documents for more information on these exceptions and the exceptions implemented for the specific core in your system.

For example, Cortex-M0/M0+ processors (or any ARMv6M processors) do not have MemManage, BusFault and UsageFault exceptions implemented. In those cases, all exceptions are reported as HardFault exception. For ARMv7M processors, MemManage, BusFault and UsageFault exceptions trigger only if they are enabled in System Handler Control and State Register (**SHCSR**).

Below is an example of the crash dump (with a description of registers) that the Mbed OS fault exception handler generates. Note that the system also invokes the Mbed OS error handler when an exception happens and prints out the error information, as well.

Please see the [Error API reference](../apis/error-handling.html) for more about error information. 

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

-- MbedOS Fault Handler --


++ MbedOS Error Info ++
Error Status: 0x80FF013D Code: 317 Module: 255
Error Message: Fault exception
Location: 0x5B25
Error Value: 0x5946
Current Thread: Id: 0x20001E80 Entry: 0x5D05 StackSize: 0x1000 StackMem: 0x20000E80 SP: 0x2002FF90
For more info, visit: https://armmbed.github.io/mbedos-error/?error=0x80FF013D
-- MbedOS Error Info --

```

## Analyzing crash dump

In the example above, you can see that the crash dump indicates the fault exception type (see **FaultType**), the register context (see **Context**) at the time of exception and the current threads (see **Thread Info**) in the system, along with their stack information.

The register context contains key information to determine the cause and location of crash. For example, you can use **PC** value to find the location of the crash and **LR** to find the caller of the function where the crash occurred.

Note that the **LR** value may not reflect the actual caller, depending on the invocation of the function. You can use the linker address map generated during the build to find the name of the function from the **PC** value. The other key information in the register context is fault status register values (**HFSR, MMFSR, UFSR and BFSR**). The values in these registers indicate the cause of the exception. Please look at the **Technical Reference Manual** and **Arm Architecture Reference Manual** documents for more information on how to interpret these registers.

The thread information section is split into five subsections corresponding to the state of the thread. For each thread: state of the thread (**State**), entry function address (**EntryFn**), stack size (**Stack Size**), stack top (**Mem**) and current stack pointer (**SP**) are reported. You can use the linker address map to find the thread entry function from the **EntryFn** value. You can also use the stack size (**Stack Size**), stack top (**Mem**) and current stack pointer (**SP**) value to determine if there is thread stack overflow. For example, if the **SP** value is smaller than the **Mem** value, it indicates stack overflow for that thread.

## Debugging imprecise bus faults

Cortex-M3 and Cortex-M4 processors have write buffers, which are high-speed memory between the processor and main memory whose purpose is to optimize stores to main memory. This is great for performance because the processor can proceed to the next instruction without having to wait for the write transaction to complete. However, this can cause imprecise bus faults in which the processor could have executed instructions, including branch instructions, by the time bus fault triggers. This makes it harder to debug imprecise faults because you cannot tell which instruction caused the fault because the **PC** value reported points to the current instruction being executed, which may not be the instruction that triggered the fault.

You can verify if you are encountering an imprecise fault by looking at the **BFSR.IMPRECISERR** (bit 2 of **BFSR**) status bit. To help debugging such situations, you can disable the write buffer by setting **DISDEFWBUF** bit in the Auxiliary Control Register (**ACTLR**), which makes those exceptions precise.

Please look at the **Technical Reference Manual** and **Arm Architecture Reference Manual** documents for more information on fault exception types and information on these registers. Note that disabling the write buffer affects performance, so you probably don't want to do that in production code.
