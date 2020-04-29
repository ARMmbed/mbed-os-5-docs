# Mbed OS bare metal profile

<img src="../../images/bare_metal_block_diagram.png" width="35%" align="right" />


Bare metal is a profile of Mbed OS for ultraconstrained devices. Unlike the full Mbed OS, which by default includes all APIs, the bare metal profile starts with a minimal set of APIs to which you can add only the APIs your application or hardware demand. This helps you control the size of your final binary.<!--not sure that's a good term-->

Bare metal doesn't use the RTOS APIs. Instead, it relies on timers to control the workflow.
<!--not sure I get it - I looked at both Blinky examples and they both use thread_sleep_for, even though the bare metal one doesn't include mbed_thread.h-->
<!--what other APIs does it have or not have by default?-->

The Mbed OS tools - Mbed CLI, Mbed Online Compiler and Mbed Studio all support working with the bare metal profile.

Note that Mbed TLS and Mbed Crypto are not supported for bare metal.

<span class="images">![Mbed OS bare metal profile block diagram]()<span>Mbed OS bare metal profile block digram</span></span>


## Features

For a breakdown of supported APIs, please see [the full API list](../apis/index.html).

<table>
    <thead>
        <tr>
            <th colspan="2">Features</th>
            <th>Mbed OS bare metal profile</th>
            <th> Mbed OS full profile</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="8">Core</td>
            <td>Drivers</td>
            <td>Available <br>(Except the class `USBCDC_ECM`)</td>
            <td>Available</td>
        </tr>
        <tr>        
            <td >Events</td>
            <td>Available</span></td>
            <td>Available</td>
        </tr>
        <tr>        
            <td >HAL</td>
            <td>Available</span></td>
            <td>Available</td>
        </tr>
        <tr>        
            <td >Platform</td>
            <td>Available</span></td>
            <td>Available</td>
        </tr>
        <tr>        
            <td>RTOS</td>
            <td><span>Not Available</span></span></td>
            <td>Available</td>
        </tr>  
                <tr>        
            <td>RTOS APIs <br> (Semaphore, Mutex, EventFlags, ThisThread)</td>
            <td>Available</td>
            <td>Available</td>
        </tr>
        <tr>        
            <td>Storage</td>
            <td>Available</td>
            <td>Available</td>
        </tr>
        <tr>        
            <td>Development tools<br> (Mbed CLI, Mbed Studio, Mbed Online Compiler)</td>
            <td>Available</td>
            <td>Available</td>
        </tr>      
        <tr>
            <td rowspan="9">Connectivity</td>
            <td>802.15.4_RF</td>
            <td><span  >Not Available</span></td>
            <td>Available</td>
        </tr>
        <tr>
            <td>Wifi</td>
            <td><span>Not Available</span></td>
            <td>Available</td>
        </tr>
        <tr>
            <td>Cellular</td>
            <td><span>Not Available</span></td>
            <td>Available</td>
        </tr>
        <tr>
            <td>LWIP stack</td>
            <td><span>Not Available</span></td>
            <td>Available</td>
        </tr>
        <tr>
            <td>Nanostack</td>
            <td><span>Not Available</span></td>
            <td>Available</td>
        </tr>
        <tr>
            <td>Network Socket</td>
            <td><span>Not Available</span></td>
            <td>Available</td>
        </tr>
        </tr>
        <tr>
            <td>BLE</td>
            <td>Available<br>(Except on `TARGET_NORDIC_CORDIO`)</td>
            <td>Available</td>
        </tr>    
        <tr>
            <td>LoRaWAN</td>
            <td>Available</td>
            <td>Available</td>
        </tr>  
        <tr>
            <td>NFC</td>
            <td>Available</td>
            <td>Available</td>
        </tr>
        <tr>
            <td rowspan="4">Security</td>
            <td>PSA</td>
            <td><span>Not Available</span></td>
            <td>Available</td>
        </tr>
        <tr>
            <td>Mbed Crypto</td>
            <td>Available</td>
            <td>Available</td>
        </tr>
        <tr>
            <td>Devicekey</td>
            <td>Available</td>
            <td>Available</td>
        </tr>  
        <tr>
            <td>Mbed TLS</td>
            <td>Available</td>
            <td>Available</td>
        </tr>
    </tbody>
</table>

## Documentation

- To see how to enable the profile, or to try the bare metal Blinky, see [our example page]().
- To learn how to add APIs, [see the bare metal API page]().
- If you're an Mbed OS 2 user, migrate to the Mbed OS 6 bare metal profile by following [our migration guide]().<!--that's not application develoeprs though, right? it's for hardware people?-->
