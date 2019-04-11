# Crash log parser tool

You can use this postprocessing tool to parse and analyze the crash dump generated when an exception happens.

## Capturing the crash log

When an exception happens, the Mbed OS exception handler prints the crash information to STDOUT, (which is usually your serial port). The crash information contains the register context at the time of the exception and the current threads in the system. Registers captured depend on the specific Cortex-M core you are using. For example, if your target is using Cortex-M0, some registers, such as MMFSR, BFSR and UFSR may not be available and do not appear in the crash log.

The information printed out to STDOUT will be similar to the following: 

```
++ MbedOS Fault Handler ++

FaultType: HardFault

Context:
R0   : 0000AAA3
R1   : 20002070
R2   : 00009558
R3   : 00412A02
R4   : E000ED14
R5   : 00000000
R6   : 00000000
R7   : 00000000
R8   : 00000000
R9   : 00000000
R10  : 00000000
R11  : 00000000
R12  : 0000BCE5
SP   : 20002070
LR   : 00009E75
PC   : 00009512
xPSR : 01000000
PSP  : 20002008
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
State: 00000002 EntryFn: 0000ADF5 Stack Size: 00001000 Mem: 20001070 SP: 20002030
Next:
State: 00000002 EntryFn: 0000ADF5 Stack Size: 00001000 Mem: 20001070 SP: 20002030
Wait Threads:
State: 00000083 EntryFn: 0000AA1D Stack Size: 00000300 Mem: 20000548 SP: 200007D8
Delay Threads:
Idle Thread:
State: 00000001 EntryFn: 00009F59 Stack Size: 00000200 Mem: 20000348 SP: 20000508

-- MbedOS Fault Handler --
```

To generate more information from this crash dump, copy and save this crash information to a text file, and run the `crash_log_parser.py` tool as below. 

<span class="notes">**Note:** Make sure you copy the section with the text `MbedOS Fault Handler` because the tool looks for that header.</span>

## Running the crash log parser

Run the tool as below with crash data file, map file and elf file as arguments.

**crash_log_parser.py \<Path to Crash log> \<Path to Elf or Axf file of the build> \<Path to Map file of the build>**

For example:

`crash_log_parser.py crash.log C:\MyProject\BUILD\k64f\arm\mbed-os-hf-handler.elf C:\MyProject\BUILD\k64f\arm\mbed-os-hf-handler.map`

Please see the example output from running `crash_log_parser` below. The information includes the location of the crash (crash location), stack pointer at the time of exception, cause of exception and so on.

```
Parsed Crash Info:
        Crash location = zero_div_test() [0000693E]
        Caller location = $Super$$main [00009E99]
        Stack Pointer at the time of crash = [20001CC0]
        Target/Fault Info:
                Processor Arch: ARM-V7M or above
                Processor Variant: C24
                Forced exception, a fault with configurable priority has been escalated to HardFault
                Divide by zero error has occurred

```
