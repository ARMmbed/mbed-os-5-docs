## Example walkthrough

The quick start example blinks the LED on your board on and off. The main thread also takes a snapshot of the device's runtime statistics and displays them over a serial connection to your PC.

### Viewing the output

To view the serial output use any terminal client, such as [PuTTY](http://www.putty.org/) or [CoolTerm](http://freeware.the-meiers.org/).

The default baud rate, or speed, for this application is set to `9600`. You can modify it in the `mbed_app.json` file. To configure your terminal client to this baud rate, change the speed option when selecting the port.

<span class="tips">**Tip:** You can find more information on the Mbed OS configuration tools and serial communication in Mbed OS in the [related links section](#related-links).</span>

The output transmits the system, CPU, heap and thread information. 

<span class="notes">**Note:** If you are building with the Mbed OS bare metal profile, you will not get thread information.</span>

### Understanding the output

#### System information

**Mbed OS version:** Tip of master is represented by 999999. If you are using a tagged release of Mbed OS, the version will be configured by the OS. For custom releases, you can modify the version manually in `platform/mbed_version.h`.

**CPUID register information:**

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

**Compiler ID and version:**

| Compiler | Version tag | Version layout |
| -------- | ----------- | -------------- |
| ARM      | 1           | PVVbbbb (P = Major; VV = Minor; bbbb = build number) |
| GCC_ARM  | 2           | VVRRPP  (VV = Version; RR = Revision; PP = Patch)    |
| IAR      | 3           | VRRRPPP (V = Version; RRR = Revision; PPP = Patch)   |


#### CPU statistics

Percentage of runtime the device has spent awake.

#### Heap statistics

- Current heap size.
- Maximum size the heap has ever reached (*not* the maximum size it can reach).

#### Thread statistics

Provides information on all running threads in the OS:

- ID.
- Name.
- State.
- Priority.
- Stack size.
- Stack space.

### Related links

- [Mbed OS statistics API](../apis/mbed-statistics.html).
- [Mbed OS configuration](../reference/configuration.html).
- [Mbed OS serial communication](../tutorials/serial-communication.html).
