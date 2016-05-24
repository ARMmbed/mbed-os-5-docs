#Terminal Applications

Terminal applications run on your host PC, and provide a window for your mbed Microcontroller to print to, and a means for you to type characters back to your mbed Microcontroller. 

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">**Serial configuration:** The standard setup for the USB Serial Port is 9600 baud, 8 bits, 1 stop bit, no parity (aka 9600-8-N-1)
</span>

##Windows users

###Install a Terminal Application

Download and install a Terminal application. 

In this example we recommend the latest version of [Teraterm](http://sourceforge.jp/projects/ttssh2/files).

Other terminal applications are available:
   
* [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/)
* [Terminal by Bray](http://sites.google.com/site/braypp/terminal)

Some Windows PCs come with ''Hyperterminal'' installed; you can use this too, but we have found Tera Term is just a bit more friendly to use.

###Configure the Connection

Open and Setup Teraterm 
 
* File -> New Connection (or just press Alt+N) 
* Select the ''Serial'' radio button and choose the ''mbed Serial Port'' from the drop down menu.
* Click ''OK''

Setup New-line format (to print out new line characters correctly)
 
* Setup -> Terminal...
* Under "New-line", set Receive to "LF"

Your terminal program is now configured and connected. 

To change the baud rate, go to Setup -> Serial Port...

##Mac/Linux Users

###Install a Terminal Application

If you do not already have it, install [GNU Screen](http://en.wikipedia.org/wiki/GNU_Screen).

###Setup the Connection
  
* Connect using screen by typing the command ``screen /dev/<devicename>`` in your console window
* To find the device name of your mbed Serial Port, see the [SerialPC](/Going_Further/PC_Com/) *Host Interface* section
* To exit screen, press Ctrl-A, then ":quit"

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
**Troubleshooting:**
</br><br />
You can check the connection is working by typing keys in the terminal application; nothing useful will happen, but the Status light on the mbed Microcontroller should flicker as the characters are received.
<br /><br />
**If you have any problems, or think this tutorial could be improved, please tell us in the [Forum](http://developer.mbed.org/forum)**
</span>




