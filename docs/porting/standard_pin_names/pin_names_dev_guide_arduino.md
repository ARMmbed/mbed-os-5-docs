# Arduino Uno Pin Names

The Arduino Uno connector is a standardised connector in Mbed, which has a set amount of exposed functionality. To achieve meaningful portability of application code across various Mbed boards that are Arduino Uno compliant, the pin names used for the connector pins are common across these boards.

The following diagram shows the Arduino Uno standard for Mbed boards:
![Static pinmap model](../../images/Arduino_Uno_Mbed.png) 

**Digital and Analog pins**

The Arduino Uno connector for Mbed boards supports both digital and analog pins. Please note that the Arduino Uno only supports analog inputs and does not support analog output functionality. Digital pin functionality such as GPIO output or input on the Arduino Uno header can be accessed from any of the pins labelled as ARDUINO_UNO_D0 to ARDUINO_UNO_D15 and ARDUINO_UNO_A0 to ARDUINO_UNO_A5. The analog input functionality on the Arduino Uno connector can only be accessed on pins ARDUINO_UNO_A0 to ARDUINO_UNO_A5. The full digital and analog pin alias list for the Arduino Uno connector can be seen below.  

    ARDUINO_UNO_D0 
    ARDUINO_UNO_D1 
    ARDUINO_UNO_D2 
    ARDUINO_UNO_D3 
    ARDUINO_UNO_D4 
    ARDUINO_UNO_D5 
    ARDUINO_UNO_D6 
    ARDUINO_UNO_D7 
    ARDUINO_UNO_D8 
    ARDUINO_UNO_D9 
    ARDUINO_UNO_D10 
    ARDUINO_UNO_D11 
    ARDUINO_UNO_D12 
    ARDUINO_UNO_D13 
    ARDUINO_UNO_D14 
    ARDUINO_UNO_D15 
    
    ARDUINO_UNO_A0 
    ARDUINO_UNO_A1 
    ARDUINO_UNO_A2 
    ARDUINO_UNO_A3 
    ARDUINO_UNO_A4 
    ARDUINO_UNO_A5 
    
**SPI pins**

The Arduino Uno connector for Mbed boards supports SPI functionality on specific pins and can be accessed using the pin alias's below  

    ARDUINO_UNO_SPI_CS    or ARDUINO_UNO_D10
    ARDUINO_UNO_SPI_MOSI  or ARDUINO_UNO_D11
    ARDUINO_UNO_SPI_MISO  or ARDUINO_UNO_D12
    ARDUINO_UNO_SPI_SCK   or ARDUINO_UNO_D13

if you need more SPI chip selects(CS) for your application, these can be controlled using additional digital out pins with the alias explained previously on this page 

**I2C pins**    

The Arduino Uno connector for Mbed boards supports I2C functionality on specific pins and can be accessed using the pin alias's below. 

    ARDUINO_UNO_I2C_SDA or ARDUINO_UNO_D14
    ARDUINO_UNO_I2C_SCL or ARDUINO_UNO_D15

**UART pins**    

The Arduino Uno connector for Mbed boards supports UART functionality on specific pins and can be accessed using the pin alias's below 

    ARDUINO_UNO_UART_TX or ARDUINO_UNO_D1
    ARDUINO_UNO_UART_RX or ARDUINO_UNO_D0

For more details about UART, please check the Mbed API.

**PWM/Timer pins**    

In the Arduino Uno standard, there are only 6 PWM and timers available on pins ARDUINO_UNO_D3, ARDUINO_UNO_D5, ARDUINO_UNO_D6, ARDUINO_UNO_D9, ARDUINO_UNO_D10 and ARDUINO_UNO_D11. However, Mbed boards may support the usage of PWM and timers functions on other pins as well.
