# Lights of dead

![LPC1768 Lights of dead](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lights1.gif)    ![LPC11U24 Lights of dead](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lights2.gif)    ![FRMD-KL25Z Lights of dead](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lights3.gif)

*LPC1768, LPC11U24 and FRDM-KL25Z showing their distinctive lights of dead pattern*

When your development board shows the "lights of dead" it means the board ran into a runtime error. Runtime errors occur when code is correct but tries to do something that is invalid, or when malfunctioning hardware cannot be accessed.

A typical example is assigning the wrong function to a pin. For example, switching the `SDA` and `SCK` pins when accessing I2C or trying to use `PwmOut` on a pin that does not support pulse-width modulation.
