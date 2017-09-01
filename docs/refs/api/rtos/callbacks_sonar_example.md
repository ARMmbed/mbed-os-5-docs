### Sonar Example

Here is an example that utilizes everything discussed in the form of a minimal Sonar class.

```c++
#include <mbed.h>

/**
 *  Sonar class for the HC-SR04
 */
class Sonar {
    DigitalOut   trigger;
    InterruptIn  echo;     // calls a callback when a pin changes
    Timer        timer;
    Timeout      timeout;  // calls a callback once when a timeout expires
    Ticker       ticker;   // calls a callback repeatedly with a timeout
    int32_t      begin;
    int32_t      end;
    float        distance;

public:
    /**
     *  Sonar constructor
     *  Creates a sonar object on a set of provided pins
     *  @param trigger_pin  Pin used to trigger reads from the sonar device
     *  @param echo_pin     Pin used to receive the sonar's distance measurement
     */
    Sonar(PinName trigger_pin, PinName echo_pin) : trigger(trigger_pin), echo(echo_pin) {
        trigger = 0;
        distance = -1;

        echo.rise(callback(this, &Sonar::echo_in));    // Attach handler to the rising interruptIn edge
        echo.fall(callback(this, &Sonar::echo_fall));  // Attach handler to the falling interruptIn edge
    }

    /**
     *  Start the background task to trigger sonar reads every 100ms
     */
    void start(void) {
        ticker.attach(callback(this, &Sonar::background_read), 0.01f);
    }

    /**
     *  Stop the background task that triggers sonar reads
     */
    void stop(void) {
        ticker.detach();
    }

    /**
     *  Interrupt pin rising edge interrupt handler. Reset and start timer
     */
    void echo_in(void) {
        timer.reset();
        timer.start();
        begin = timer.read_us();
    }

    /**
     *  Interrupt pin falling edge interrupt handler. Read and disengage timer.
     *  Calculate raw echo pulse length
     */
    void echo_fall(void) {
        end = timer.read_us();
        timer.stop();
        distance = end - begin;
    }

    /**
     *  Wrapper function to set the trigger pin low. Callbacks cannot take in both object and argument pointers.
     *  See use of this function in background_read().
     */
    void trigger_toggle(void) {
        trigger = 0;
    }

    /**
     *  Background callback task attached to the periodic ticker that kicks off sonar reads
     */
    void background_read(void) {
        trigger = 1;
        timeout.attach(callback(this, &Sonar::trigger_toggle), 10.0e-6);
    }

    /**
     *  Public read function that returns the scaled distance result in cm
     */
    float read(void) {
        return distance / 58.0f;
    }
};


int main() {
    // Create sonar object on pins D5 and D6
    Sonar sonar(D5, D6);
    // Begin background thread sonar acquires
    sonar.start();

    while(1) {
        wait(0.1f);
        // Periodically print results from sonar object
        printf("%f\r\n", sonar.read());
    }
}
```
