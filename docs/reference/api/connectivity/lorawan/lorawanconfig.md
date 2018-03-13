<h2 id="lorawan-configuration">Configuring Mbed LoRaWAN Stack</h2>

Various parameters for Mbed LoRaWAN stack can be configured via either C++ APIs or by using Mbed configuration system. 

### Using Mbed Configuration system

Here are the parameters that can be configured using Mbed configuration system:

```
Configuration parameters
------------------------

Name: lora.adr-on                                                                                                                   
    Defined by: library:lora                                                                                                        
    Value: 1 (set by library:lora)                                                                                                  
Name: lora.app-port                                                                                                                 
    Defined by: library:lora                                                                                                        
    Value: 15 (set by library:lora)                                                                                                 
Name: lora.application-eui                                                                                                          
    Defined by: library:lora                                                                                                        
    Value: {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00} (set by library:lora)                                                   
Name: lora.application-key                                                                                                          
    Defined by: library:lora                                                                                                        
    Value: {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00} (set by library:lora)   
Name: lora.appskey                                                                                                                  
    Defined by: library:lora                                                                                                        
    Value: {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00} (set by library:lora)   
Name: lora.device-address                                                                                                           
    Defined by: library:lora                                                                                                        
    Value: 0x00000000 (set by library:lora)                                                                                         
Name: lora.device-eui                                                                                                               
    Defined by: library:lora                                                                                                        
    Value: {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00} (set by library:lora)                                                   
Name: lora.duty-cycle-on                                                                                                            
    Defined by: library:lora                                                                                                        
    Value: 1 (set by library:lora)                                                                                                  
Name: lora.lbt-on                                                                                                                   
    Defined by: library:lora                                                                                                        
Name: lora.nb-trials                                                                                                                
    Defined by: library:lora                                                                                                        
    Value: 12 (set by library:lora)                                                                                                 
Name: lora.nwkskey                                                                                                                  
    Defined by: library:lora                                                                                                        
    Value: {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00} (set by library:lora)   
Name: lora.over-the-air-activation                                                                                                  
    Defined by: library:lora                                                                                                        
    Value: 1 (set by library:lora)                                                                                                  
Name: lora.phy                                                                                                                      
    Defined by: library:lora                                                                                                        
    Value: 0 (set by library:lora)                                                                                                  
Name: lora.public-network                                                                                                           
    Defined by: library:lora                                                                                                        
    Value: 1 (set by library:lora)                                                                                                  
Name: lora.tx-max-size                                                                                                              
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

See API reference [here](https://os.mbed.com/docs/v5.8/reference/lorawan.html).
