# Compile time errors

Compile time errors and warnings that incorrect syntax, or misuse of variables or functions, causes. An error prevents the compile process from completing (and therefore no binary file will be created). A warning does not prevent the binary from being created, but you should still review the warning because it may mean that your code is not going to do what you had intended.

Common errors are:

- Missing declarations of variables and interfaces, leading to `Identifier undefined` errors.
- Missing semicolons (`;`). Semicolons are required at the end of each line.
- Missing quotes or brackets (`""`, `()`, `[]` or `{}`). These are used in pairs to contain various types of statement. The compiler reports an error if you have not used them in correct pairings.
- Always tackle the first reported error because later errors may be as a result of the first one and will disappear you correct the first one.

For more information about compile time errors or warning, please see [the list of Mbed OS defined error codes and descriptions](../apis/error-handling.html#list-of-mbed-os-defined-error-codes-and-descriptions). If you have questions about a compile time error or warning that you do not understand, please post to the [Arm Mbed forums](https://os.mbed.com/questions/).

## Runtime errors and siren lights

<span class="images">![LPC1768 siren lights](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lights1.gif)</span>

<span class="images">![LPC11U24 siren lights](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lights2.gif)</span>

<span class="images">![FRMD-KL25Z siren lights](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/lights3.gif)</span>

*LPC1768, LPC11U24 and FRDM-KL25Z showing their distinctive pattern of siren lights*

When your development board shows the siren lights, it means the board ran into a runtime error. Runtime errors occur when code is correct but tries to do something that is invalid, or when malfunctioning hardware cannot be accessed.

A typical example is assigning the wrong function to a pin. For example, switching the `SDA` and `SCK` pins when accessing I2C or trying to use `PwmOut` on a pin that does not support pulse-width modulation.
