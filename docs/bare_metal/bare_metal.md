# Mbed OS bare metal profile

Bare metal is a profile of Mbed OS for ultraconstrained hardware: compact and without an RTOS. It represents a different way of working with Mbed OS: Instead of enabling all features by default, as the full profile does, bare metal mandates only the smallest set of APIs that applications require - driver APIs, platform APIs and a subset of the RTOS APIs. All other supported APIs are optional, so you can better control your application's final size.

The bare metal profile implements a subset of Mbed OS's RTOS APIs that are useful in non-threaded applications, for example semaphores (with release from interrupts) <!--what does "with" mean?-->and tickers (to set up a recurring interupt). It is not a full RTOS, and is therefore suitable for applications that do not require complex thread management. This not only simplifies your application code, it also means you can use APIs that are not thread safe. Just as important, you can use the code-optimized versions of the C standard libraries, `microlib` and `newlib-nano`, which are much smaller than the thread safe equivalents the full profile requires.

The bare metal profile is determined at build time - your working environment includes the full Mbed OS library, but only the bare metal APIs are compiled.

## Features

For a breakdown of supported APIs, please see [the full API list](../apis/index.html).

The Mbed OS build tools - Mbed CLI, Mbed Online Compiler and Mbed Studio - all support working with the bare metal profile.

<span class="notes">**Note:** Because bare metal uses some APIs that Mbed OS classifies as RTOS APIs, some class names that traditionally belong in RTOS programming are used in bare metal. For example, bare metal uses the class `ThisThread` despite not using threads.</span>

<table>
    <thead>
        <tr>
            <th colspan="2">Features</th>
            <th>Support details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="6">Core</td>
            <td>Drivers</td>
            <td>Available; enabled by default</td>
        </tr>
        <tr>        
            <td>Events</td>
            <td>Available</td>
        </tr>
        <tr>        
            <td>HAL</td>
            <td>Available</td>
        </tr>
        <tr>        
            <td>Platform</td>
            <td>Available; enabled by default</td>
        </tr>
            <tr>        
            <td>RTOS APIs</td>
            <td>Semaphore, Mutex, EventFlags, ThisThread: Available; enabled by default.<br><br> All other APIs<!--I think we say "api" for the collective and class for the individual - I'll look into it--> not supported.</td>
        </tr>
        <tr>        
            <td>Storage</td>
            <td>Available</td>
        <tr>
            <td rowspan="9">Connectivity</td>
            <td>802.15.4_RF</td>
            <td>Not Available</td>
        </tr>
        <tr>
            <td>Wifi</td>
            <td>Not Available</td>
        </tr>
        <tr>
            <td>Cellular</td>
            <td>Not Available</td>
        </tr>
        <tr>
            <td>LWIP stack</td>
            <td>Not Available</td>
        </tr>
        <tr>
            <td>Nanostack</td>
            <td>Not Available</td>
        </tr>
        <tr>
            <td>Network Socket</td>
            <td>Not Available</td>
        </tr>
        </tr>
        <tr>
            <td>BLE</td>
            <td>Available<br>(Except on `TARGET_NORDIC_CORDIO`)</td>
        </tr>    
        <tr>
            <td>LoRaWAN</td>
            <td>Available</td>
        </tr>  
        <tr>
            <td>NFC</td>
            <td>Available</td>
        </tr>
        <tr>
            <td rowspan="4">Security</td>
            <td>PSA</td>
            <td>Not Available</td>
        </tr>
        <tr>
            <td>Mbed Crypto</td>
            <td>Available</td>
        </tr>
        <tr>
            <td>Devicekey</td>
            <td>Available</td>
        </tr>  
        <tr>
            <td>Mbed TLS</td>
            <td>Available</td>
        </tr>
    </tbody>
</table>

## Documentation

The bare metal documentation covers:

- [A bare metal version of our standard Blinky example](../bare-metal/bare-metal-example.html).
- A [bare metal usage guide](../bare-metal/using-the-bare-metal-profile.html) that shows how to set up a bare metal application, add optional APIs and use Greentea to test the application.
- [A short review of small C libraries](../bare-metal/using-small-c-libraries.html).
- [A porting guide for Mbed OS 2 targets](../bare-metal/porting-a-target-from-mbed-os-2-to-mbed-os-6-bare-metal.html).

<!--
<table>
    <thead>
        <tr>
            <th colspan="2">Features</th>
            <th>Bare metal profile</th>
            <th>Full profile</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="7">Core</td>
            <td>Drivers</td>
            <td>Available <br>(Except the class `USBCDC_ECM`)</td>
            <td>Available</td>
        </tr>
        <tr>        
            <td >Events</td>
            <td>Available</td>
            <td>Available</td>
        </tr>
        <tr>        
            <td >HAL</td>
            <td>Available</td>
            <td>Available</td>
        </tr>
        <tr>        
            <td >Platform</td>
            <td>Available</td>
            <td>Available</td>
        </tr>
        <tr>        
            <td>RTOS</td>
            <td>Not Available</td>
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
        <tr>
            <td rowspan="9">Connectivity</td>
            <td>802.15.4_RF</td>
            <td>Not Available</td>
            <td>Available</td>
        </tr>
        <tr>
            <td>Wifi</td>
            <td>Not Available</td>
            <td>Available</td>
        </tr>
        <tr>
            <td>Cellular</td>
            <td>Not Available</td>
            <td>Available</td>
        </tr>
        <tr>
            <td>LWIP stack</td>
            <td>Not Available</td>
            <td>Available</td>
        </tr>
        <tr>
            <td>Nanostack</td>
            <td>Not Available</td>
            <td>Available</td>
        </tr>
        <tr>
            <td>Network Socket</td>
            <td>Not Available></td>
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
            <td>Not Available</td>
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
-->
