# Compile time errors

Compile time errors and warnings that incorrect syntax, or misuse of variables or functions, causes. An error prevents the compile process from completing (and therefore no binary file will be created). A warning does not prevent the binary from being created, but you should still review the warning because it may mean that your code is not going to do what you had intended.

Common errors are:

* Missing declarations of variables and interfaces, leading to `Identifier undefined` errors.
* Missing semicolons (`;`). Semicolons are required at the end of each line.
* Missing quotes or brackets (`""`, `()`, `[]` or `{}`). These are used in pairs to contain various types of statement. The compiler reports an error if you have not used them in correct pairings.
* Always tackle the first reported error because later errors may be as a result of the first one and will disappear you correct the first one.

If you see a compile time error or warning that you do not understand, you can usually find explanations of the error message on Google, or post to the [mbed forums](https://developer.mbed.org/questions/).