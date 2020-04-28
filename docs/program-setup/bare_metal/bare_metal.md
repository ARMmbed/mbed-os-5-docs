# Mbed OS bare metal profile

There are many use cases for IoT devices. Different use cases require different configurations, connectivity and security. They also have different requirements for resource consumption. Many products must operate in ultraconstrained environments on tiny MCUs with low memory and compute power available. We created the Mbed OS bare metal profile for IoT devices that require ultraconstrained resources.

<span class="images">![Mbed OS bare metal profile block diagram](../../images/bare_metal_block_diagram.png)<span>Mbed OS bare metal profile block digram</span></span>

The Mbed OS bare metal profile is a compact profile of Mbed OS without an RTOS. Most of the Mbed OS APIs are compatible with bare metal profile and below table shows the availability of various Mbed OS features and components on bare metal profile.

<table>
    <thead>
        <tr>
            <th colspan="2">Features/Components</th>
            <th>Mbed OS bare metal profile</th>
            <th> Mbed OS full profile</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="8">Core</td>
            <td >Drivers</td>
            <td>Available <br>(Except USBCDC_ECM)</td>
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
            <td >RTOS</td>
            <td><span style="color:red">Not Available</span></span></td>
            <td>Available</td>
        </tr>  
                <tr>        
            <td >RTOS APIs <br> (Semaphore, Mutex, EventFlags, ThisThread)</td>
            <td>Available</td>
            <td>Available</td>
        </tr> 
        <tr>        
            <td >Storage</td>
            <td>Available</td>
            <td>Available</td>
        </tr> 
        <tr>        
            <td >Development tools<br> (Mbed CLI, Mbed Studio, Mbed Online Compiler etc.)</td>
            <td>Available</td>
            <td>Available</td>
        </tr>      
        <tr>
            <td rowspan="9">Connectivity</td>
            <td >802.15.4_RF</td>
            <td><span style="color:red">Not Available</span></td>
            <td>Available</td>
        </tr>
        <tr>
            <td>Wifi</td>
            <td><span style="color:red">Not Available</span></td>
            <td>Available</td>
        </tr>
        <tr>
            <td>Cellular</td>
            <td><span style="color:red">Not Available</span></td>
            <td>Available</td>
        </tr>
        <tr>
            <td>LWIP stack</td>
            <td><span style="color:red">Not Available</span></td>
            <td>Available</td>
        </tr>
        <tr>
            <td>Nanostack</td>
            <td><span style="color:red">Not Available</span></td>
            <td>Available</td>
        </tr>
        <tr>
            <td>Network Socket</td>
            <td><span style="color:red">Not Available</span></td>
            <td>Available</td>
        </tr>
        </tr>
        <tr>
            <td>BLE</td>
            <td>Available <br>(Except TARGET_NORDIC_CORDIO)</td>
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
            <td><span style="color:red">Not Available</span></td>
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
