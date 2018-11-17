### Example walkthrough

The quick start example blinks the LED on your platform on and off. The main thread additionally takes a snapshot of the device's runtime statistics and display them through serial to your PC. The snapshot includes:

- System information:
   - Mbed OS version: Defaults to 999999.
   - [Compiler ID](#compiler-id).
   - [CPUID register information](#cpuid-register-information).
   - [Compiler version](#compiler-version).
- CPU statistics:
   - Percentage of runtime the device has spent awake.
- Heap statistics:
   - Current heap size.
   - Maximum size the heap has ever grown.
- Thread statistics:
   - Provides information on all running threads in the OS including:
      - Thread ID.
      - Thread name.
      - Thread state.
      - Thread priority.
      - Thread stack size.
      - Thread stack space.

#### Compiler ID

| Compiler | Version tag |
| -------- | ----------- |
| ARM      | 1           |
| GCC_ARM  | 2           |
| IAR      | 3           |

#### Compiler version

| Compiler | Version layout |
| -------- | -------------- |
| ARM      | PVVbbbb (P = Major; VV = Minor; bbbb = build number) |
| GCC      | VVRRPP  (VV = Version; RR = Revision; PP = Patch)    |
| IAR      | VRRRPPP (V = Version; RRR = Revision; PPP = Patch)   |

#### CPUID register information

| Bit Field | Field Description | Values |
| --------- | ----------------- | ------ |
|[31:24]    | Implementer       | 0x41 = ARM |
|[23:20]    | Variant           | Major revision 0x0  =  Revision 0 |
|[19:16]    | Architecture      | 0xC  = Baseline Architecture |
|           |                   | 0xF  = Constant (Mainline Architecture) |
|[15:4]     | Part Number       | 0xC20 =  Cortex-M0 |
|           |                   | 0xC60 = Cortex-M0+ |
|           |                   | 0xC23 = Cortex-M3  |
|           |                   | 0xC24 = Cortex-M4  |
|           |                   | 0xC27 = Cortex-M7  |
|           |                   | 0xD20 = Cortex-M23 |
|           |                   | 0xD21 = Cortex-M33 |
|[3:0]      | Revision          | Minor revision: 0x1 = Patch 1 |

You can view individual examples and additional API information of the statistics collection tools at the bottom of the page in the [related links section](#related-links).

### Output

To view the serial output, you can use any terminal client, such as [PuTTY](http://www.putty.org/) or [CoolTerm](http://freeware.the-meiers.org/).

The default baud rate for this application is set to `115200`. You can modify it in the `mbed_app.json` file.

You can find more information on the Mbed OS configuration tools and serial communication in Mbed OS in the [related links section](#related-links).

The output contains the following block transmitted at the blinking LED frequency (actual values may vary depending on your target, build profile and toolchain):

```
=============================== SYSTEM INFO  ================================
Mbed OS Version: 999999
CPU ID: 0x410fc241
Compiler ID: 2
Compiler Version: 60300
================= CPU STATS =================
Idle: 98% Usage: 2%
================ HEAP STATS =================
Current heap: 1096
Max heap size: 1096
================ THREAD STATS ===============
ID: 0x20001eac
Name: main_thread
State: 2
Priority: 24
Stack Size: 4096
Stack Space: 3296

ID: 0x20000f5c
Name: idle_thread
State: 1
Priority: 1
Stack Size: 512
Stack Space: 352

ID: 0x20000f18
Name: timer_thread
State: 3
Priority: 40
Stack Size: 768
Stack Space: 664

```

#### Troubleshooting

If you have problems, you can review the [documentation](../tutorials/debugging.html) for suggestions on what could be wrong and how to fix it.

#### Related links

- [Mbed OS statistics API](../apis/mbed-statistics.html).
- [Mbed OS configuration](../reference/configuration.html).
- [Mbed OS serial communication](../tutorials/serial-communication.html).

