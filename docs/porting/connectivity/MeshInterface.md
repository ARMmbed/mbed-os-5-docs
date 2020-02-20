<h1 id="6lowpan-port">IEEE 802.15.4 RF driver</h1>

# Porting a new RF driver

The following steps describe how you can create a new RF driver:

1. Please see the [Nanostack PHY API](https://github.com/ARMmbed/mbed-os/blob/master/features/nanostack/sal-stack-nanostack/nanostack/platform/arm_hal_phy.h).
1. Please read through the [_Example RF driver_](#example-rf-driver) section. You can use this example code to start.
1. Please see the reference implementations for [simple](https://github.com/ARMmbed/mbed-os/blob/master/components/802.15.4_RF/atmel-rf-driver/source/NanostackRfPhyAtmel.cpp) and [extended](https://github.com/ARMmbed/mbed-os/blob/master/components/802.15.4_RF/stm-s2lp-rf-driver/source/NanostackRfPhys2lp.cpp) RF drivers.
1. Please read usage of the worker thread [_Worker thread for Mbed OS_](#worker-thread-for-mbed-os).
1. Please see [_Implementing PHY API_](#implementing-phy-api) for details how to implement callbacks and API functions:
   
   - Global time stamp functionality.
   - RF driver registration.
   - Address write callback.
   - State control callback.
   - RF extension callback.
   - TX functionality.
   - RX functionality.
   
1. Build the Nanostack MAC tester application:
   
   `mbed test --clean --compile --icetea -t <toolchain> -m <platform> -DICETEA_MAC_TESTER_ENABLED --test-config NANOSTACK_MAC_TESTER -n address_read_and_write`
   
1. Verify the functionality of your implementation by running the Nanostack RF driver testcase set in the Mbed OS repository:
   
   `mbed test --run --icetea -t <toolchain> -m <platform> --test-config NANOSTACK_MAC_TESTER -n address_read_and_write,send_data,send_data_indirect,send_large_payloads,create_and_join_PAN,ED_scan`

<span class="notes">**Note:** The MAC tester application is a basic verification tool for the RF driver. When going to production, please use more specific RF driver testing.</span>

# Implementing the PHY API

PHY API guidance is separated into ***simple*** and ***extended*** implementations, which depend on the configuration you use:

- You can use the ***simple*** implementation with:

   - Thread.
   - 6LoWPAN without frequency hopping.
   
- You can use the ***extended*** implementation with:

   - Thread.
   - 6LoWPAN with and without frequency hopping.
   - Wi-SUN.
   
## Global time stamp functionality

This functionality is necessary only with the ***extended*** implementation.

The RF driver must implement a timer with a one-microsecond resolution to return a 32-bit time stamp value. The driver must be able to return the current time stamp when Nanostack requests it. The driver must store the time stamp of received packets where the time is referenced to the first byte after the SFD of the received frame.

## RF driver registration

Use `arm_net_phy_register` to register the RF driver to Nanostack. The function returns the driver ID, which you must use when creating the MAC instance. Registration is similar for both the ***simple*** and ***extended*** implementations. You must fill the structure of `phy_driver`:

Parameter|Value
-----|-----------
`link_type`|`PHY_LINK_15_4_2_4GHZ_TYPE` or `PHY_LINK_15_4_SUBGHZ_TYPE`.
`PHY_MAC`|PHY driver must deliver a unique 64-bit MAC address.
`driver_description`|Name of the driver.
`phy_channel_pages`|Default RF configurations.
`phy_MTU`|MTU size. Typical values: 127 for 802.15.4-2006, 2047 for 802.15.4g-2012.
`phy_header_length`|Extra header to be allocated for transmitted packet by MAC. Typically 0.
`phy_tail_length`|Extra tail to be allocated for transmitted packet by MAC. Typically 0.
`address_write`|RF address write callback function.
`extension`|RF extension callback function.
`state_control`|RF state control callback function.
`tx`|RF packet transmit callback function.

Any other callbacks and parameters must be nullified.

## Address write callback

Nanostack calls the address write callback `int8_t (*address_write)(phy_address_type_e, uint8_t *)` to set addresses for RF receive filtering. This callback is similar for both the ***simple*** and ***extended*** implementations.

Address type|Use
-----|-----------
`PHY_MAC_64BIT`|Driver must set given 64-bit address as the receive address filter.
`PHY_MAC_16BIT`|Driver must set given 16-bit address as the receive address filter.
`PHY_MAC_PANID`|Driver must set given 16-bit PAN ID as the receive PAN ID filter.

## State control callback

Nanostack calls the state control callback `int8_t (*state_control)(phy_interface_state_e, uint8_t)` to change the RF state. This callback is similar for both the ***simple*** and ***extended*** implementations.

State|Use
-----|-----------
`PHY_INTERFACE_RESET`|Driver must stop any active TX and RX processes and set radio to idle state.
`PHY_INTERFACE_DOWN`|Driver must stop any active TX and RX processes and set radio to sleep or idle state.
`PHY_INTERFACE_UP`|Driver must wake up the radio and enable receiver on a channel that was given as parameter.
`PHY_INTERFACE_RX_ENERGY_STATE`|Driver must initialize energy detection on a channel that was given as parameter. Nanostack reads the ED result using RF extension `PHY_EXTENSION_READ_CHANNEL_ENERGY`.
`PHY_INTERFACE_SNIFFER_STATE`|Driver must enable receiver on a channel that was given as parameter. All filtering must be disabled. This state is used only if device is set as Sniffer.

## RF extension callback

Nanostack calls the RF extension callback `int8_t (*extension)(phy_extension_type_e, uint8_t *)` to set or get various PHY parameters. Some of the extensions are needed only with ***extended*** implementations.

Mandatory for ***simple*** and ***extended*** implementations:

Extension type|Use
-----|-----------
`PHY_EXTENSION_CTRL_PENDING_BIT`|Driver must set frame pending bit of the Ack frames high or low depending on the value of given (uint8_t *) parameter. If parameter > 0, set frame pending bit to 1 and otherwise to 0.
`PHY_EXTENSION_READ_LAST_ACK_PENDING_STATUS`|Driver must return the state of the frame pending bit used in last transmitted Ack frame. State (0 or 1) must be written to given (uint8_t *) parameter.
`PHY_EXTENSION_READ_CHANNEL_ENERGY`|Driver must return the read channel energy. Value must be written in given (uint8_t *) parameter as an 8-bit integer.
`PHY_EXTENSION_ACCEPT_ANY_BEACON`|Driver must stop filtering received 802.15.4 Beacon frames and accept them all if the given (uint8_t *) parameter is > 0.

Mandatory for ***extended*** implementation:

Extension type|Use
-----|-----------
`PHY_EXTENSION_SET_CHANNEL`|Driver must enable receiver on a channel which was given as parameter. If radio is currently receiving or transmitting a frame, channel should be changed after the TX/RX process.
`PHY_EXTENSION_READ_RX_TIME`|Driver must return the time stamp of last received packet. Time stamp must be referenced to first byte after SFD field of the received packet.
`PHY_EXTENSION_DYNAMIC_RF_SUPPORTED`|Driver must return 1 if it supports ***extended*** RF driver implementation. By default, Nanostack assumes ***simple*** implementation is used. Value (0 or 1) must be written to given (`uint8_t *`) parameter.
`PHY_EXTENSION_GET_TIMESTAMP`|Driver must return 32-bit time stamp by writing it to given (`uint8_t *`) parameter.
`PHY_EXTENSION_SET_CSMA_PARAMETERS`|Driver must read `phy_csma_params_t` type structure behind given (`uint8_t *`) parameter. If parameter `backoff_time` is 0, any on-going transmission must be canceled and radio set to receive state on the current channel. 32-bit `backoff_time` and boolean `cca_enabled` must be stored because they will be used for next packet transmission.
`PHY_EXTENSION_GET_SYMBOLS_PER_SECOND`|Driver must return symbol rate as symbols per second. 32-bit value must be written to given (`uint8_t *`) parameter.
`PHY_EXTENSION_SET_RF_CONFIGURATION`|Driver must read `phy_rf_channel_configuration_s` type structure behind given (`uint8_t *`) parameter. Driver must start using given RF configuration as soon as possible. If radio is currently receiving or transmitting a frame, configuration should be changed after the TX/RX process.

Optional:

Extension type|Use
-----|-----------
`PHY_EXTENSION_FILTERING_SUPPORT`|If RF driver can support filtering and acking certain MAC frame types, it can set the corresponding bit in a given (`uint8_t *`) parameter to 1, which disables the filtering of this frame type from Nanostack.

## TX functionality

Nanostack calls the TX callback `int8_t (*tx)(uint8_t *, uint16_t, uint8_t, data_protocol_e)` to start packet transmission. To implement the TX callback, follow either the ***simple*** or ***extended*** implementation path:

1. Driver must return -1 if it is currently busy (already transmitting or receiving) or 0 if it can start transmission.
1. When TX callback allows starting the transmission by returning 0, it must tell to Nanostack when the transmission is done by calling `phy_tx_done_cb` with proper TX done status. Parameter `tx_handle` in a TX done call must be set to same value as in a corresponding TX (start) call.
1. Copy transmitted data from behind given first (`uint8_t *`) parameter to radio TX FIFO and prepare radio ready for transmission. Data behind this pointer is valid and unchanged until the driver calls the `phy_tx_done_cb`, which allows data to be copied to TX FIFO also when RF driver has returned from the TX function.

***Simple*** implementation:

1. Start optional CSMA-CA period or check CCA immediately. Using a short (1-5 ms) randomly generated CSMA-CA period significantly reduces the number of collisions when network size increases.
1. If the channel is not available, call `phy_tx_done_cb` with status `PHY_LINK_CCA_FAIL`. If the RF driver performs several CCA attempts, the `cca_retry` parameter must list the number of attempts.
1. If channel is available, start transmission immediately.
1. When transmission is finished, call `phy_tx_done_cb` with status `PHY_LINK_TX_SUCCESS`.
1. If the Ack frame was received for transmitted packet, call `phy_tx_done_cb` with status `PHY_LINK_TX_DONE` or `PHY_LINK_TX_DONE_PENDING` depending on the state of frame pending field in the Ack frame.
   
   <span class="notes">**Note:** It is the RF driver's responsibility to compare the sequence number of the transmitted data and received Ack frame.</span>
   
1. If the driver performed MAC retransmissions, the `tx_retry` parameter must list the number of retry attempt.

***Extended*** implementation:

1. Read the stored CCA mode (`cca_enabled`), which Nanostack set with the `PHY_EXTENSION_SET_CSMA_PARAMETERS` event just before the current transmission. If `cca_enabled` equals to `false`, the driver must not check CCA but proceed to next step as if the channel was available.
1. Read the stored backoff time, which Nanostack set with the `PHY_EXTENSION_SET_CSMA_PARAMETERS` event just before the current transmission. If the backoff time is 0, cancel the transmission.
1. Calculate the length of the CSMA-CA period using the time stamp and given backoff time: `csma_ca = backoff_time - current_time`.
1. Start the CSMA-CA timer with the calculated `csma_ca`. This timer must operate with 1 microsecond resolution. If `csma_ca` is larger than 65000 us, start the CSMA-CA timer with a minimum possible timeout value (1 us).
1. When the CSMA-CA timeout has passed, the driver must call `phy_tx_done_cb` with status `PHY_LINK_CCA_PREPARE` to read the state of the CSMA-CA process. State is given as a return value of the `phy_tx_done_cb` call.
1. If the state is `PHY_TX_NOT_ALLOWED`, cancel the transmission. There is no need for an additional `phy_tx_done_cb` call. Ensure the receiver is enabled.
1. If the state is `PHY_RESTART_CSMA`, check the CCA immediately. If the channel is not available, call `phy_tx_done_cb` with status `PHY_LINK_CCA_FAIL`. If the channel is available, call `phy_tx_done_cb` with status `PHY_LINK_CCA_OK`, and return to step 4. Note that Nanostack has updated CCA mode and backoff time with the `PHY_EXTENSION_SET_CSMA_PARAMETERS` event.
1. If the state is `PHY_TX_ALLOWED`, check the CCA immediately. If the channel is not available, call `phy_tx_done_cb` with status `PHY_LINK_CCA_FAIL`. If the channel is available, start transmission of the packet immediately.
1. When transmission finishes, call `phy_tx_done_cb` with status `PHY_LINK_TX_SUCCESS`.
1. If Ack frame was received for the transmitted packet, call `phy_tx_done_cb` with status `PHY_LINK_TX_DONE` or `PHY_LINK_TX_DONE_PENDING`, depending on the state of frame pending field in Ack.
   
   <span class="notes">**Note:** It is the RF driver's responsibility to compare the sequence number of the transmitted data and received Ack frame unless the IEEE 802.15.4-2015 frames are used.</span>
   
1. The driver must not generate additional CSMA-CA or MAC retransmission attempts with ***extended*** implementation because the transmitted frame contains timing critical information, which Nanostack needs to update before every attempt.

## RX functionality

When Nanostack has called `PHY_INTERFACE_UP` RF state, the receiver must be kept enabled on a channel given by the `PHY_INTERFACE_UP` or `PHY_EXTENSION_SET_CHANNEL` event unless transmission is active until the `PHY_INTERFACE_RESET` or `PHY_INTERFACE_DOWN` RF state is called. RX functionality is similar for both ***simple*** and ***extended*** implementation. Depending on your application, the driver only needs to handle the wanted frame type (for example, 802.15.4-2006 or 802.15.4-2015).

Nanostack is capable of filtering and acking IEEE 802.15.4-2015 frames. The RF driver must filter and ack any other frame version. For a received frame, the driver must call the RX callback `arm_net_phy_rx_fn *phy_rx_cb(const uint8_t *data_ptr, uint16_t data_len, uint8_t link_quality, int8_t dbm, int8_t driver_id)`, where: 
 
- `data_ptr` - Pointer to the beginning of received MAC frame.
- `data_len` - MAC frame length.
- `link_quality` - LQI of the received frame.
- `dbm` - RSSI of the received frame.
- `driver_id` - ID of the RF driver.

To handle the received frame, check the frame version of a received packet. For IEEE 802.15.4-2015 frames, call `phy_rx_cb`.

For other frame types:
   
   1. Check if the received frame is Ack. If true, check if the received frame is Ack for a packet the driver previously sent. If true, call `phy_tx_done_cb` with status `PHY_LINK_TX_DONE` or `PHY_LINK_TX_DONE_PENDING`, depending on the state of frame pending field in Ack.
   1. Otherwise, filter PAN ID and MAC address:
   
      - Drop packet by PAN ID filter if all conditions below are true:
         
         - Received destination PAN id ID not broadcast (0xffff).
         - Nodes own PAN ID is set (not 0xffff).
         - Received destination PAN ID does not equal to nodes PAN ID.
	 
      - Frame is not IEEE 802.15.4 Beacon frame. This condition is necessary only if `PHY_EXTENSION_ACCEPT_ANY_BEACON` is set by Nanostack. 
       - Drop packet by address filter if all conditions below are true:
          
          - Received destination address is not broadcast address.
          - Received destiantion address does not equal to nodes 16-bit or 64-bit MAC address.
	  
   1. If received frame passes the filtering, check if ack is required, and transmit it immediately.
   1. If received frame passes the filtering, call `phy_rx_cb`.

# Worker thread for Mbed OS

Nanostack's interfaces use mutexes for protecting the access from multiple threads. In Mbed OS, you cannot use the mutex from an interrupt. The same applies to all APIs that have internal locking and multithread support. Therefore, each driver must implement its own worker thread to handle the interrupt requests.

Example: Use the worker thread and signals from an interrupt.

```
// Signals from interrupt routines
#define SIG_RADIO       1
#define SIG_TIMER       2

// Worker thread
Thread irq_thread;

// Interrupt routines
static void rf_interrupt(void)
{
    irq_thread.signal_set(SIG_RADIO);
}

static void rf_timer_interrupt(void)
{
    irq_thread.signal_set(SIG_TIMER);
}


// Worker thread
void rf_worker_thread(void)
{
    for (;;) {
        osEvent event = irq_thread.signal_wait(0);
        if (event.status != osEventSignal) {
            continue;
        }

        if (event.value.signals & SIG_RADIO) {
            rf_process_irq();
        }
        if (event.value.signals & SIG_TIMER) {
            rf_process_timer();
        }
    }
}

...
// Somewhere in the initialization code
irq_thread.start(rf_worker_thread);

```

# Example RF driver

The following code example is not a complete driver but shows you how to use the API to create a RF driver:

```
static uint8_t mac_address[8];
static phy_device_driver_s device_driver;
static int8_t rf_radio_driver_id = -1;

const phy_rf_channel_configuration_s phy_2_4ghz = {2405000000, 5000000, 250000, 16, M_OQPSK, MODULATION_INDEX_UNDEFINED};
const phy_rf_channel_configuration_s phy_subghz = {868300000, 2000000, 250000, 11, M_OQPSK, MODULATION_INDEX_UNDEFINED};

static phy_device_channel_page_s phy_channel_pages[] = {
	{CHANNEL_PAGE_0, &phy_2_4ghz},
	{CHANNEL_PAGE_0, NULL}
};

int8_t rf_device_register(void)
{
    /* Do some initialization */
    rf_init();
    /* Set pointer to MAC address */
    device_driver.PHY_MAC = mac_address;
    /* Set driver Name */
    device_driver.driver_description = "Example";

    if(subghz_radio) /* Configuration for Sub GHz Radio */
    {
        /*Type of RF PHY is SubGHz*/
        device_driver.link_type = PHY_LINK_15_4_SUBGHZ_TYPE;
        phy_channel_pages[0].channel_page = CHANNEL_PAGE_2;
        phy_channel_pages[0].rf_channel_configuration = &phy_subghz;
    }
    else /* Configuration for 2.4 GHz Radio */
    {
        /*Type of RF PHY is 2.4 GHz*/
        device_driver.link_type = PHY_LINK_15_4_2_4GHZ_TYPE;
        phy_channel_pages[0].channel_page = CHANNEL_PAGE_0;
        phy_channel_pages[0].rf_channel_configuration = &phy_2_4ghz;
    }

    /*Maximum size of payload is 127*/
    device_driver.phy_MTU = 127;
    /*No header in PHY*/
    device_driver.phy_header_length = 0;
    /*No tail in PHY*/
    device_driver.phy_tail_length = 0;

    /*Set up driver functions*/
    device_driver.address_write = &rf_address_write;
    device_driver.extension = &rf_extension;
    device_driver.state_control = &rf_interface_state_control;
    device_driver.tx = &rf_start_cca;
    /*Set supported channel pages*/
    device_driver.phy_channel_pages = phy_channel_pages;
    //Nullify rx/tx callbacks
    device_driver.phy_rx_cb = NULL;
    device_driver.phy_tx_done_cb = NULL;
    device_driver.arm_net_virtual_rx_cb = NULL;
    device_driver.arm_net_virtual_tx_cb = NULL;

    /*Register device driver*/
    rf_radio_driver_id = arm_net_phy_register(&device_driver);

    return rf_radio_driver_id;
}

void rf_handle_rx_end(void)
{
    uint8_t rf_lqi;
    int8_t rf_rssi;
    uint16_t rf_buffer_len;
    uint8_t *rf_buffer;

    /* Get received data */
    rf_buffer_len = rf_get_rf_buffer(rf_buffer);
    if(!rf_buffer_len)
        return;

    /* If waiting for ACK, check here if the packet is an ACK to a message previously sent (non IEEE 802.15.4-2015). Remember to call phy_tx_done_cb with either PHY_LINK_TX_DONE or PHY_LINK_TX_DONE_PENDING status */

    /* Filter the packet here unless it was already done by the hardware (non IEEE 802.15.4-2015) */
	
    /* Send Ack here if needed unless it was already done by the hardware (non IEEE 802.15.4-2015) */

    /* Get link information */
    rf_rssi = rf_get_rssi();
    rf_lqi = rf_get_lqi();

    /* Note: Checksum of the packet must be checked and removed before entering here */

    /* Send received data and link information to the network stack */
    if( device_driver.phy_rx_cb ){
    	device_driver.phy_rx_cb(rf_buffer, rf_buffer_len, rf_lqi, rf_rssi, rf_radio_driver_id);
    }
}

int8_t rf_start_cca(uint8_t *data_ptr, uint16_t data_length, uint8_t tx_handle, data_protocol_e data_protocol)
{
    /*Check if transmitter is busy*/
    if(transmitter_busy)
    {
        /*Return busy*/
        return -1;
    }
    else
    {
        /*Check if transmitted data needs to be ACKed*/
        if(*data_ptr & 0x20)
            need_ack = 1;
        else
            need_ack = 0;
        /*Store the sequence number for ACK handling*/
        tx_sequence = *(data_ptr + 2);

        /* Store data and start CCA process here */
        /* When the CCA process is ready send the packet */
        /* Note: Before sending the packet you need to calculate and add a checksum to it, unless done automatically by the radio */
        /* Note: phy_tx_done_cb must be called when transmission is done (PHY_LINK_TX_SUCCESS) or when CCA returns unavailable channel (PHY_LINK_CCA_FAIL) */
    }

    /*Return success*/
    return 0;
}

static int8_t rf_interface_state_control(phy_interface_state_e new_state, uint8_t rf_channel)
{
    int8_t ret_val = 0;
    switch (new_state)
    {
        /*Reset PHY driver and set to idle*/
        case PHY_INTERFACE_RESET:
            rf_reset();
            break;
        /*Disable PHY Interface driver*/
        case PHY_INTERFACE_DOWN:
            rf_shutdown();
            break;
        /*Enable PHY Interface driver*/
        case PHY_INTERFACE_UP:
            rf_channel_set(rf_channel);
            rf_receive();
            break;
        /*Enable wireless interface ED scan mode*/
        case PHY_INTERFACE_RX_ENERGY_STATE:
            break;
        /*Enable Sniffer state*/
        case PHY_INTERFACE_SNIFFER_STATE:
            rf_setup_sniffer(rf_channel);
            break;
    }
    return ret_val;
}

static int8_t rf_extension(phy_extension_type_e extension_type, uint8_t *data_ptr)
{
    switch (extension_type)
    {
        /*Control MAC pending bit for Indirect data transmission*/
        case PHY_EXTENSION_CTRL_PENDING_BIT:
        /*Return frame pending status*/
        case PHY_EXTENSION_READ_LAST_ACK_PENDING_STATUS:
            *data_ptr = rf_if_last_acked_pending();
            break;
        /*Set channel, used for setting channel for energy scan*/
        case PHY_EXTENSION_SET_CHANNEL:
            rf_channel_set(rf_channel);
            rf_receive();
            break;
        /*Read energy on the channel*/
        case PHY_EXTENSION_READ_CHANNEL_ENERGY:
            *data_ptr = rf_get_channel_energy();
            break;
        /*Read status of the link*/
        case PHY_EXTENSION_READ_LINK_STATUS:
            *data_ptr = rf_get_link_status();
            break;
    }
    return 0;
}

static int8_t rf_address_write(phy_address_type_e address_type, uint8_t *address_ptr)
{

    switch (address_type)
    {
        /*Set 48-bit address*/
        case PHY_MAC_48BIT:
            /* Not used in this example */
            break;
        /*Set 64-bit address*/
        case PHY_MAC_64BIT:
            rf_set_mac_address(address_ptr);
            break;
        /*Set 16-bit address*/
        case PHY_MAC_16BIT:
            rf_set_short_adr(address_ptr);
            break;
        /*Set PAN Id*/
        case PHY_MAC_PANID:
            rf_set_pan_id(address_ptr);
            break;
    }

    return 0;
}
```
