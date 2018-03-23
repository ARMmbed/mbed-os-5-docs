## ConditionVariable

The ConditionVariable class provides a mechanism to safely wait for or signal state changes. A common scenario when writing multithreaded code is to protect shared resources with a mutex and then release that mutex to wait for a change of that data. If you do not do this carefully, this can lead to a race condition in the code. A condition variable provides a safe solution to this problem by handling the wait for a state change, along with releasing and acquiring the mutex automatically during this waiting period.

### ConditionVariable class reference

[![View code](https://www.mbed.com/embed/?type=library)](http://os-doc-builder.test.mbed.com/docs/v5.8/mbed-os-api-doxy/classrtos_1_1_condition_variable.html)

### ConditionVariable example

Below is an example of ConditionVariable usage, where one thread is generating events every 1s, and the second thread is waiting for the events and executing an action.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/ConditionVariable_Example_1/)](https://os.mbed.com/teams/mbed_example/code/ConditionVariable_Example_1/file/36d0e9449606/main.cpp)
