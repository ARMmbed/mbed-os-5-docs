#The mbed Memory Model


This is a basic overview of the memory model used by mbed.

##Microcontroller Memory

A single-chip microcontroller contains two types of memory:

[FLASH](http://en.wikipedia.org/wiki/Flash_memory) - This is the [non-volatile](http://en.wikipedia.org/wiki/Non-volatile_memory) memory that primarily stores the program's instructions, and also any "constant" data values. In general, you only read from this memory, and it is only written when you download new code to the mbed.

[RAM](http://en.wikipedia.org/wiki/Static_random_access_memory) - This is the [volatile](http://en.wikipedia.org/wiki/Volatile_memory) memory that is the working data space for storing all variables whilst the program is running. In C, this is static variables, the heap, and the stack.

RAM is therefore much more scarce and valuable than FLASH, so it is worth understanding a little about the memory model to help make best use of the memory.

[EEPROM](http://en.wikipedia.org/wiki/EEPROM) - Some microcontrollers have special non-volatile memory that can be erased and written byte for byte rather than in blocks or sectors. This memory is typically used by the application to store special data or configuration. This memory requires special access by a peripheral and is not directly addressable.

##C Memory Model

The C runtime memory model can be divided in to three types; global/static memory, the heap, and the stack. These all share the RAM available on the microcontroller.

###Global/static memory 

Global and static memory are values that are allocated for the entire lifetime of the program. For example:

```c

	int x = 5;
	int main() {}
```

Here, "x" would be allocated a dedicated slot in RAM, that is never used by anything else. In this case it is initialised to 5, and it's value might be changed throughout the lifetime of the program.

If for some reason you have data that is fixed (such as a lookup table), you'd be much better off making sure the compiler can allocate it in FLASH to save valuable RAM space. In the previous example, we could use the C keyword "const" to tell the compiler the variable will never be changed:

```c

	const int x = 5;
	int main() {}
```

###The Stack

The [Stack](http://en.wikipedia.org/wiki/Stack_(data_structure)) is used to store types of variables that have a fixed lifetime based on how C programs run. It is a section of RAM that grows and shrinks as the program runs. When you call a function, its parameters and any variables you have defined in that function (which are not static) are stored on the stack. 

```c

	void foo() {
  		int x;
	}
	int main() {}
```

In this example, "x" will only exist for the duration of the call to foo(). As you start calling functions from within other functions, your stack grows downwards. As you return back up the call tree, your stack decreases in size.

###The Heap

The heap is used for [dynamic memory allocation](http://en.wikipedia.org/wiki/Dynamic_memory_allocation). When you create a new instance of an object using 'new', or if you allocate a block of memory using malloc and friends, you use memory in the heap. 

```c

	int *p;
	int main() {
    	p = new int;
	}
```

If there is a piece of unused memory in the heap which is big enough for what you need, then that is used. If there is not, then the heap grows upwards to fit the new instance/memory block. When you use delete or free, the memory it was using inside the heap is deallocated, ready for use again. However, unless the memory you released was at the very end of the heap, the heap does not shrink.

##Memory Sections

The information in your program is made up of several sorts based on the memory model:
  
* Executable code 
* Constants and other read-only data
* Initialised global/static variables
* Uninitialised global/static variables
* Local variables
* Dynamically created data

Each of these groups get allocated to a region of the memory space called a section. 

The executable code, constants and other read-only data get put in a section called "RO" (for read-only), which is stored in the FLASH memory of the device. Initialised static and global variables go into a section called "RW" (read-write), and the uninitialised ones in to one called "ZI" (Zero Initialise). I'll come on to the local and dynamic data in a bit, but these along with RW and ZI need to live in RAM.

On reset, the RAM is an undefined state and those initialised variables have to be setup for your program to work correctly. This setup is actually part of your program binary, as the compiler automatically inserts some housework code before main() as part of setting up the C environment which copies from FLASH to RAM what these variables should be initialised to; this becomes the runtime RW section. One of the other things it does is to zero fill the next section of RAM, which is where the ZI section lives.

<span style="text-align:center; display:block;">
![](/Going_Further/Images/Memory/Memory_Sections.png)
</span>

###Heap and Stack

The last two sorts of information are the local variables which will exist on the stack, and the dynamically created data which will exist in the heap. 

The sizes of these two regions vary during program execution, and only have fixed starting points. We use the single memory space shared stack/heap model which allows flexibility in the size of each, limited only by our available RAM. What this means is that the heap starts at the first address after the end of ZI, growing up into higher memory addresses, and the stack starts at the last memory address of RAM, and grows downwards into lower memory addresses:

<span style="text-align:center; display:block;">
![](/Going_Further/Images/Memory/Heap_Stack.png)
</span>

###Collisions

Obviously, looking at this, it is possible to for your heap and stack to collide, which is never going to end well! If that happens, you have hit the limit of your RAM, and need to find out ways to help ensure your program uses less memory.

To try and help you prevent detect when this would happen, the routines that allocate memory on the heap (new, malloc and friends) tell you when you don't have enough memory. Instead of passing you a pointer to the newly allocated block, they pass you the value NULL. 

If your stack and your heap do collide, despite your best efforts, then the results will be unpredictable. You may get data corruption, or you may get a hard fault. You can write a hard fault handler and/or implement a watchdog to recover from some of these faults, but you basically have to restart the system!

<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
Also see the [RTOS Memory Model](/Going_Further/RTOS_Mem/).
</span>