# Alarm tutorial

This tutorial is for an alarm application that uses a simple countdown mechanism. It relies on two input buttons to set, activate and silence the alarm. During the countdown, the device is in sleep mode. When the countdown ends and the alarm triggers, an LED and a digital out pin go high. They go back to low when the alarm is reset.

The LEDs provides some feedback to the user: when setting the alarm, the LEDs blink to show the input was recognised. When the alarm is fully set, the LEDs blink the configured delay once, before letting the device go into sleep mode.

<span class="tips">**Tip:** You can complete this tutorial with the Mbed Online Compiler or [Mbed CLI](../tools/installation-and-setup.html).</span>

## Import the example application

If using Mbed CLI, use the `import` command:

```
mbed import mbed-os-example-alarm
cd mbed-os-example-alarm
```

If using the Online Compiler, click the **Import into Mbed IDE** button below:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Alarm/tree/v6.9)](https://github.com/ARMmbed/mbed-os-snippet-Alarm/blob/v6.9/main.cpp)

## Compile and flash to your board

1. To compile the application:

   - If using Mbed CLI, invoke `mbed compile`, and specify the name of your target and toolchain (`GCC_ARM`, `ARM`, `IAR`). For example, for the ARM Compiler 5 and FRDM-K64F:

   ```
   mbed compile -m K64F -t ARM
   ```

   - If using the Online Compiler, click the **Compile** button.

   Your PC may take a few minutes to compile your code.

1. Find the compiled binary:

   - If using the Online Compiler, the compiled binary will be downloaded to your default location.
   - If using Mbed CLI, the compiled binary will be next to the source code, in your local copy of the example.

1. Connect your Mbed device to the computer over USB.
1. Copy the binary file to the Mbed device.
1. Press the reset button to start the program.

## Use the alarm

The alarm isn't set to a timestamp; it counts down from the moment it's activated. So to set the alarm, specify the countdown duration:

1. Press **Button1** for the number of desired hours to delay.
1. Press **Button2** to cycle to minutes, and repeat the previous step for the number of desired minutes.
1. Press **Button2** again to start the alarm.
1. Press **Button2** again once the alarm triggers to silence it.

## Extending the application

You can set the alarm to a specific time by relying on either the board's RTC or the [time API](../apis/time.html). You will need to set the time on each reset, or rely on an internet connection and fetch the time.

## Troubleshooting

If you have problems, you can review the [documentation](../debug-test/troubleshooting-common-issues.html) for suggestions on what could be wrong and how to fix it.
