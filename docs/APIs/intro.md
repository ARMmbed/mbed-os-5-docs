# Writing applications with the mbed OS APIs

You can think of mbed OS as a collection of application programming interfaces (APIs). You use these APIs to control the hardware, and mbed OS provides the "glue" that makes the APIs work together. 

## Hardware agnosticism

mbed OS exposes the same APIs to you, irrespective of the hardware on which you're working. The job of making the standard APIs work with different hardware is conducted behind the scenes; this means that your application code can run on any hardware without any deliberate changes on your part.

