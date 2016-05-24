#RTOS Memory Model

This is a basic overview of the memory model used by the mbed RTOS.

##Threads

Each thread of execution in the RTOS has its separate stack.

When you use the RTOS, before explicitly initializing any additional thread, you will have 4 separate stacks:

* The stack of the ``Main Thread`` (executing the ``main`` function).
* The ``Idle Thread`` executed each time all the other threads are waiting for external, or scheduled events. This is particularly useful to implement energy saving strategies. (ie ``sleep``).
* The ``Timer Thread`` that executes all the time scheduled tasks (periodic and non periodic).
* The stack of ``OS Scheduler`` itself (also used by the ISRs).

<span style="text-align:center; display:block;">
![](/Going_Further/Images/Memory/RTOS.png)
</span>


<span style="background-color:lightgray; color:purple; display:block; height:100%; padding:10px">
Also see the [the mbed Memory Model](/Going_Further/Mem_Mo/).
</span>

