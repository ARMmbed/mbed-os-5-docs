<h2 id="CORDIO-port">Porting the Cordio stack</h2>

Cordio BLE host and controller are a fully qualified BLE stack and a ready to use solution for your bluetooth module. Cordio can be used as just the Host stack or together with the link layer (controller).

If you're using a controller with its own link layer software you may easily connect with the host stack using the HCI separation point. Additionally you may port the Cordio link layer to your module.

### Using the Cordio Host stack with your own Link Layer

Read the detailed [porting guide](https://github.com/ARMmbed/mbed-os/blob/master/features/FEATURE_BLE/targets/TARGET_CORDIO/doc/PortingGuide.md) on writing your HCI driver.

### Using the Cordio Host stack with Cordio Link Layer

Read the [guide](https://github.com/ARMmbed/mbed-os/blob/master/features/FEATURE_BLE/targets/TARGET_CORDIO_LL/README.md) and refer to existing [port for NRF52](https://github.com/ARMmbed/mbed-os/tree/master/features/FEATURE_BLE/targets/TARGET_NORDIC/TARGET_NORDIC_CORDIO/TARGET_NRF5x).

