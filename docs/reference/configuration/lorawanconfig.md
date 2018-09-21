<h2 id="lorawan-configuration">LoRaWAN</h2>

Various parameters for Mbed LoRaWAN stack can be configured via either C++ APIs or by using the Mbed configuration system.

### Using the Mbed Configuration system

Here are the parameters that you can configure using the Mbed configuration system:

```
Configuration parameters
------------------------

Name: lora.adr-on
    Description: Turns Automatic Data Rate on/off
    Defined by: library:lora                                                                                                        
    Value: 1 (set by library:lora)                                                                                                  
Name: lora.app-port          
    Description: Set the application port                                                                                                       
    Defined by: library:lora                                                                                                        
    Value: 15 (set by library:lora)                                                                                                 
Name: lora.application-eui    
    Description: Set AppEUI (application EUI needed for OTAA)                                                                                                      
    Defined by: library:lora                                                                                                        
    Value: {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00} (set by library:lora)                                                   
Name: lora.application-key   
    Description: Set AppKey (application key needed for OTAA)                                                                                                       
    Defined by: library:lora                                                                                                        
    Value: {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00} (set by library:lora)   
Name: lora.appskey
    Description: Set AppSkey (application session key needed for ABP)                                                                
    Defined by: library:lora                                                                                                        
    Value: {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00} (set by library:lora)   
Name: lora.device-address
    Description: Set DevAddr (device address needed for ABP)                                                                                                          
    Defined by: library:lora                                                                                                        
    Value: 0x00000000 (set by library:lora)                                                                                         
Name: lora.device-eui    
    Description: Set DevEUI (device EUI needed for OTAA)                                                                                                           
    Defined by: library:lora                                                                                                        
    Value: {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00} (set by library:lora)                                                   
Name: lora.duty-cycle-on  
    Description: Turns duty cycle on/off                                                                                                          
    Defined by: library:lora                                                                                                        
    Value: 1 (set by library:lora)                                                                                                  
Name: lora.lbt-on
    Description: Turns LBT on/off                                                                                                                   
    Defined by: library:lora                                                                                                        
Name: lora.nb-trials       
    Description: Set number of retries for a join request                                                                                                         
    Defined by: library:lora                                                                                                        
    Value: 12 (set by library:lora)                                                                                                 
Name: lora.nwkskey            
    Description: Set NwkSkey (network session key needed for ABP)                                                                                                      
    Defined by: library:lora                                                                                                        
    Value: {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00} (set by library:lora)   
Name: lora.over-the-air-activation   
    Description: Enable or disable OTAA. Value set to false would enable ABP                                                                                               
    Defined by: library:lora                                                                                                        
    Value: 1 (set by library:lora)                                                                                                  
Name: lora.phy       
    Description: Set the region of operation for the device                                                                                                               
    Defined by: library:lora                                                                                                        
    Value: EU868 (set by library:lora)                                                                                                  
Name: lora.public-network   
    Description: Set the public network parameter                                                                                                        
    Defined by: library:lora                                                                                                        
    Value: 1 (set by library:lora)                                                                                                  
Name: lora.tx-max-size   
    Description: Maximum outgoing buffer size                                                                                                           
    Defined by: library:lora                                                                                                        
    Value: 64 (set by library:lora)                                                                                                 
```

For changing any of these parameters, edit the `mbed_app.json` file in the root of your application. Prefix the parameter name with `lora.`, e.g., `lora.my-parameter: value`.

```json
"target_overrides": {
    "*": {
        "lora.device-address":  "0x12345678",
        "lora.over-the-air-activation": true,
        "lora.duty-cycle-on": true
    }
}
```

### Using APIs from LoRaWANInterface

See the [API reference](/docs/v5.10/apis/lorawan.html) for information about how to use these APIs from the LoRaWANInterface.
