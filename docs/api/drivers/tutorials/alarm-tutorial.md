# Alarm tutorial

This tutorial is for an alarm application that uses a simple countdown mechanism. It relies on two input buttons to set, activate and silence the alarm. During the countdown, the device is in sleep mode. When the countdown ends and the alarm triggers, a LED and a digital out pin go high. They go back to low when the alarm is reset.

The LEDs provide some feedback to the user: when setting the alarm, the LEDs blink to show the input was recognised. When the alarm is fully set, the LEDs blink the configured delay once, before letting the device go into sleep mode.

<span class="tips">**Tip:** You can complete this tutorial with Keil Studio or [Mbed CLI](../tools/installation-and-setup.html).</span>

## Import the example application

With Keil Studio, click the **Import into Keil Studio Cloud** button below:

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-snippet-Alarm/tree/v6.7)](https://github.com/ARMmbed/mbed-os-snippet-Alarm/blob/v6.7/main.cpp)

With Mbed CLI, use the `import` command:

```
mbed import mbed-os-example-alarm
cd mbed-os-example-alarm
```

## Compile and flash to your board

1. Compile the application:

   - With Keil Studio, click the **Build project** button.

   - With Mbed CLI, invoke `mbed compile`, and specify the name of your target and toolchain (`GCC_ARM`, `ARM`, `IAR`). For example, for the ARM Compiler 5 and FRDM-K64F:

   ```
   mbed compile -m K64F -t ARM
   ```

   Your PC may take a few minutes to compile your code.
   With Keil Studio, the compiled binary is automatically downloaded after a successful build. Check your **Downloads** folder.
   With Mbed CLI, the compiled binary is next to the source code, in your local copy of the example.

1. Connect your Mbed device to the computer over USB.

1. Flash the code:

  - With Keil Studio, click the **Run project** button to flash the code to your device and start the program.

  - With Mbed CLI:
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
