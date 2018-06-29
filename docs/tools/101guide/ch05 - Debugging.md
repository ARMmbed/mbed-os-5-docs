## Debugging

### printf() 

For basic debugging, checking variables and confirming logic the `prinft` command is extremely useful. By default the printf in mbed is set to 9600 8-N-1 . You can change this in the mbed_app.json file if you like. 

For example in the following code we will print the value of x. 

```C
#include "mbed.h"

int main(){
	int x = 10;
	printf("\r\n the value of x = %d \r\n", x)
}
```

The suggested use is to use one of the following program, or the serial terminal built into Mbed CLI `mbed sterm`

- Windows : [PuTTY](https://putty.org/), [CoolTerm](http://freeware.the-meiers.org/CoolTermWin.zip), [TeraTerm](https://osdn.net/projects/ttssh2/releases/)
- OSX : [CoolTerm](http://freeware.the-meiers.org/CoolTermMac.zip), or use `screen`
- Linux : screen or minicom

### External IDE

When you need more advanced debugging we reccomend exporting your project to a 3rd party IDE and debugging it there. All mbed boards support Keil, IAR and GCC_ARM and typically also Eclipse projects.

![](images/exporter_online.gif)

To see a complete list of all available exporters either select export from the online compiler or run the `mbed export --supported` command. 

For example: To export with Mbed CLI run a command similar to `mbed export --IDE UVISION5 --target <target_name>`

