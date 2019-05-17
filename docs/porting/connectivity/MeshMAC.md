<h1 id="mac-port">Porting IEEE 802.15.4 MAC drive</h1>

Nanostack has a lower level API for the IEEE 802.15.4-2006 MAC standard. This enables developers to support different MACs, be it SW or HW based solutions. Nanostack offers SW MAC, which you can use when your board does not have 15.4 MAC available.
SW MAC also supports subset of IEEE 802.15.4-2015 MAC standard. Supported features are:
- IEEE 802.15.4-2015 enhanced ack
- Header and paylod Information elements set by MAC user. 

## SW MAC

Nanostack includes an IEEE 802.15.4 based SW MAC class. You can use SW MAC when your board does not support MAC. To use the SW MAC service you must have a working RF driver registered to Nanostack. To create SW MAC, call the following function:

```
ns_sw_mac_create()
```

This creates an SW MAC class and sets a callback function to be used by Nanostack.

<span class="notes">**Note:** You must not call `ns_sw_mac_create()` more than once!</span>

### SW MAC IEEE 802.15.4-2015 subset extension

SW MAC support subset from IEEE 802.15.4-2015 standard. Subset include following supported features.

- Data frame send with Payload and Header Information elements defined by MAC user.
- Enhanced ACK generation and send by MAC
- Enhanced ACK payload and Information elements write for MAC user

Subset features need proper supported RF driver with new extented driver API commands.

## Initializing SW MAC

Deploy SW MAC as follows:

1. Call `arm_net_phy_register()` to register the configured RF driver class to Nanostack.
2. Call `ns_sw_mac_create()` to create SW MAC with needed list sizes.
    - a sleepy device needs only 1-4 as the size of the `device_decription_table_size`.
    - the minimum and recommended `key_description_table_size` for the Thread stack is 4. (2 for 6LoWPAN)
    - the recommended value for `key_lookup_size` is 1 and for `key_usage_size` 3.
3. Call `arm_nwk_interface_lowpan_init()` to create Nanostack with the created SW MAC class. Nanostack will initialize SW MAC before using it.

## Example

See a simple code snippet for creating SW MAC with 16 as neighbor table size with three key descriptions:

```
int8_t generate_6lowpan_interface(int8_t rf_phy_device_register_id)
{
    mac_description_storage_size_t storage_sizes;
    storage_sizes.device_decription_table_size = 16;
    storage_sizes.key_description_table_size = 3;
    storage_sizes.key_lookup_size = 1;
    storage_sizes.key_usage_size = 3;
    mac_api_t *mac_api = ns_sw_mac_create(rf_phy_device_register_id, &storage_sizes);
    if (!mac_api) {
        tr_error("Mac create fail!");
        return -1;
    }
    return arm_nwk_interface_lowpan_init(mac_api, "6LoWPAN_ROUTER");
}
```

## Enabling FHSS

SW MAC supports FHSS. To enable it, you need to do the following:

1. Call `arm_net_phy_register()` to register the configured RF driver class to Nanostack.
2. Call `ns_sw_mac_create()` to create SW MAC with needed list sizes.
3. Call `ns_fhss_create()` to configure and define the FHSS class.
4. Call `ns_sw_mac_fhss_register()` to register FHSS to SW MAC.
5. Call `arm_nwk_interface_lowpan_init()` to create Nanostack with the created SW MAC class.

## IEEE 802.15.4 MAC sublayer APIs

The stack uses the IEEE 802.15.4 defined MAC management service entity (MLME-SAP) and MAC data service (MCPS-SAP) interfaces. MAC API follows MCPS and MLME primitives defined by the IEEE 802.15.4-2006 standard.

The following primitives are used in MAC layer:

| Primitive | Description |
| --------- | ----------- |
| Request | Request made by service user. |
| Confirm | MAC layer response to earlier request. |
| Indication | Indication event from MAC to service user. |
| Response | Service user's response to received indication. |

MAC API is defined in the following header files:

- `mac_api.h` Main header which defines a transparent MAC API for Nanostack to use.
- `mlme.h` Definitions for MLME-SAP primitives.
- `mac_mcps.h` Definitions for MCPS-SAP primitives.
- `mac_common_defines.h` Definitions for common MAC constants.

## MCPS-SAP interface

MCPS-SAP defines 802.15.4 data flow API with the following primitives:

| Primitive | Description |
| --------- | ----------- |
| `MCPS-DATA-REQ` | Data request primitive to MAC. |
| `MCPS-DATA-CONF` | MAC generated confirmation for ongoing `MCPS-DATA-REQ`. |
| `MCPS-DATA-IND` | MAC generated data indication event. |
| `MCPS-PURGE-REQ` | Cancel ongoing `MCPS-DATA-REQ` from MAC. |
| `MCPS-PURGE-CONF` | Confirmation from MAC to `MCPS-PURGE-REQ` operation. |

## MLME-SAP interface

MLME-SAP defines a set of different management primitives and this chapter introduces both supported and unsupported primitives in Nanostack.

### Supported MLME APIs

MLME-SAP primitives used by Nanostack:

| Primitive | Description |
| --------- | ----------- |
| `MLME-BEACON-NOTIFY` | MAC generated event for received beacons.|
| `MLME-GET-REQ` | Request information about a specified PAN Information Base (PIB) attribute. |
| `MLME-GET-CONF` | MAC generated response to `MLME-GET-REQ`. |
| `MLME-RESET-REQ` | Request to reset MAC to idle state and clean data queues. |
| `MLME-SCAN-REQ` | Start MAC scan process. Orphan scan is not supported. |
| `MLME-SCAN-CONF` | Result of the scan made by `MLME-SCAN-REQ`. |
| `MLME-COMM-STATUS-IND` | MAC generated indication about the communications status. |
| `MLME-SET-REQ` | Request to write data into a specified PIB attribute. |
| `MLME-SET-CONF` | MAC generated response to `MLME-SET-REQ`. |
| `MLME-START-REQ` | Starts or enables MAC with specified options. Nanostack uses this also for RFD devices. |
| `MLME-SYNCH-LOSS-IND` | Indicates synchronization loss from wireless PAN. Only used by SW MAC when FHSS is in use! |
| `MLME-POLL-REQ` | Request MAC to do data poll to parent. |

### Unsupported MLME APIs

Unsupported MLME-SAP primitives:

| Primitive | Support planned | Description |
| --------- | --------------- | ----------- |
| `MLME-ASSOCIATE-REQ` | Not yet | Start MAC association process. |
| `MLME-ASSOCIATE-CONF` | Not yet | MAC association process confirmation status. |
| `MLME-ASSOCIATE-IND` | Not yet | MAC association indication to indicate the reception of assocation request. |
| `MLME-ASSOCIATE-RES` | Not yet | MAC association response for indication. |
| `MLME-DISASSOCIATE-REQ` | Not yet | MAC disassociation request from service user. |
| `MLME-DISASSOCIATE-IND` | Not yet | MAC disassociation indication event to service user. |
| `MLME-DISASSOCIATE-CONF` | Not yet | MAC disassociation confirmation when the disassociation request is handled. |
| `MLME-GTS-REQ` | Not yet | MAC Guaranteed Time Slot (GTS) request. |
| `MLME-GTS-IND` | Not yet | MAC GTS allocate event indication. |
| `MLME-GTS-CONF` | Not yet | MAC GTS request confirmation. |
| `MLME-ORPHAN-IND` | Not yet | Service user indicated by orphaned device. |
| `MLME-ORPHAN-RES` | Not yet | Service user response to orphan indication event. |
| `MLME-RESET-CONF` | Yes | MAC reset confirmation. |
| `MLME-RX-ENABLE-REQ` | Yes | Enable (or disable) RX receiver for a specified time. |
| `MLME-RX-ENABLE-CONF` | Yes | Confirmation for `MLME-RX-ENABLE-REQ`. |
| `MLME-START-CONF` | Yes | Confirmation for MLME start request. |
| `MLME-SYNCH-REQ` | Not yet | Request MAC to synchronize with coordinator. |

## MAC API class introduction

This chapter introduces MAC mesh interface `mac_api_s`. It is a structure that defines the function callbacks needed by a service user.

The base class defines the functions for two-way communications between an external MAC and service user. The application creates a `mac_api_s` object by calling the MAC adapter's create function. The newly created object is then passed to Nanostack which initializes its own callback functions by calling the `mac_api_initialize()` function. A service user operates MAC by calling MLME or MCPS primitive functions.

The MAC API class structure `mac_api_t` is defined as below:

```
typedef struct mac_api_s {
    //Service user defined initialization function which is called when Nanostack takes MAC into use
    mac_api_initialize              *mac_initialize;
    mac_api_enable_mcps_ext     *mac_mcps_extension_enable;
    //MAC adapter function callbacks for MLME & MCPS SAP
    mlme_request                    *mlme_req;
    mcps_data_request               *mcps_data_req;
    mcps_data_request_ext       *mcps_data_req_ext;
    mcps_purge_request                  *mcps_purge_req;
    //Service user defined function callbacks
    mcps_data_confirm               *data_conf_cb;
    mcps_data_confirm_ext       *data_conf_ext_cb;
    mcps_data_indication                *data_ind_cb;
    mcps_data_indication_ext    *data_ind_ext_cb;
    mcps_ack_data_req_ext       *enhanced_ack_data_req_cb;
    mcps_purge_confirm                  *purge_conf_cb;
    mlme_confirm                        *mlme_conf_cb;
    mlme_indication                     *mlme_ind_cb;
    //MAC extension API for service user
    mac_ext_mac64_address_set           *mac64_set;
    mac_ext_mac64_address_get           *mac64_get;
    mac_storage_decription_sizes_get *mac_storage_sizes_get;
    int8_t                              parent_id;
    uint16_t                            phyMTU;
};
```

Member|Description
------|-----------
`mac_initialize` | MAC initialize function called by Nanostack.
`mac_mcps_extension_enable` | MAC MCPS IE extension enable function, optional feature. Enable is only possible when driver extension is supported.
`mlme_req` | MLME request function to use MLME-SAP commands, MAC defines.
`mcps_data_req` | MCPS data request function to use, MAC defines.
`mcps_data_req_ext` | MAC MCPS data request with Information element extension function to use.
`mcps_purge_req` | MCPS purge request function to use, MAC defines.
`mcps_data_confirm` | MCPS data confirm callback function, service user defines.
`mcps_data_confirm_ext` | MAC MCPS data confirm with payload callback function.
`data_ind_cb` | MCPS data indication callback function, service user defines.
`data_ind_ext_cb` | MAC MCPS data indication with IE extension's callback function.
`enhanced_ack_data_req_cb` | Enhanced ACK IE element and payload request from MAC user.
`purge_conf_cb` | MCPS purge confirm callback function, service user defines.
`mlme_conf_cb` | MLME confirm callback function, service user defines.
`mlme_ind_cb` | MLME indication callback function, service user defines.
`mac64_set` | MAC extension function to set mac64 address.
`mac64_get` | MAC extension function to get mac64 address.
`mac_storage_sizes_get` | Getter function to query data storage sizes from MAC.
`parent_id` | Service user ID used to indentify the MAC service user. Optional.
`phyMTU` | Maximum Transmission Unit (MTU) used by MAC. Standard 802.15.4 MAC must set 127.

## SW MAC Information element's and Enhanced ACK support

This chapter introduce how to use extented features.
### Initialize API

```
typedef int8_t mac_api_enable_mcps_ext(mac_api_t *api, mcps_data_indication_ext *data_ind_cb, mcps_data_confirm_ext *data_cnf_cb, mcps_ack_data_req_ext *ack_data_req_cb);
```

Parameter|Description
------|-----------
`api`|pointer, which is created by application
`data_ind_cb`|Upper layer function to handle MCPS indications with Information element's.
`data_cnf_cb`|Upper layer function to handle MCPS confirmation with Information element's.
`ack_data_req_cb`|Upper layer function for requesting Enhanced ACK payload.

Function can be called when SW MAC is created and initialization procedure is done. Enable could fail if delivered driver does not support required extension's.

#### Data Indication API
```
typedef void mcps_data_indication_ext(const mac_api_t* api, const mcps_data_ind_t *data, const mcps_data_ie_list_t *ie_ext);
```
Parameter|Description
------|-----------
`api`|pointer, which is created by application
`data`|data MCPS-DATA.indication specific values.
`ie_ext`|Information element list.

Extented data indication handler is similar than normal indication but it includes Information element list which is defined following way:
```
typedef struct mcps_data_ie_list {
    uint8_t *headerIeList;
    uint8_t *payloadIeList;
    uint16_t headerIeListLength;
    uint16_t payloadIeListLength;
} mcps_data_ie_list_t;
```

Member|Description
------|-----------
`headerIeList`|Header information IE's list without terminator.
`payloadIeList`|Payload information IE's list without terminator.
`headerIeListLength`|Header information IE's list length in bytes.
`headerIeListLength`|Payload information IE's list length in bytes.

#### Data request API
```
typedef void mcps_data_request_ext(const mac_api_t* api, const mcps_data_req_t *data, const mcps_data_req_ie_list_t *ie_ext, const struct channel_list_s *asynch_channel_list);
```
Parameter|Description
------|-----------
`api`|pointer, which is created by application
`data`|MCPS-DATA.request specific values.
`ie_ext`|Information element list to MCPS-DATA.request.
`asynch_channel_list`|Optional channel list to asynch data request. Give NULL when normal data request.

Asynch data request is mac standard extension. asynch_channel_list include channel mask which channel message is requested to send.

Structure for IEEE 802.15.4-2015 MCPS data extension to Request.
```
typedef struct mcps_data_req_ie_list {
    ns_ie_iovec_t *headerIeVectorList;
    ns_ie_iovec_t *payloadIeVectorList;
    uint16_t headerIovLength;
    uint16_t payloadIovLength;
} mcps_data_req_ie_list_t;
```

Member|Description
------|-----------
`headerIeVectorList`|Header IE element list.
`payloadIeVectorList`|Payload IE element list.
`headerIovLength`|Header IE element list size, set 0 when no elements.
`payloadIovLength`|Payload IE element list size, set 0 when no elements.

IE element could be divided to multiple vector which MAC just write to message direct. One vector cuold also include multiple Information elements or just header part. That's enable flexible to way to generate list and should enable memory firendly way to share information element's. 

Set `headerIovLength` or `payloadIovLength` to 0 if not send any element.

Scatter-gather descriptor for MCPS request IE Element list.
```
typedef struct ns_ie_iovec {
    void *ieBase;
    uint_fast16_t iovLen;
} ns_ie_iovec_t;
```

Member|Description
------|-----------
`ieBase`|IE element pointer.
`iovLen`|IE element length.

#### Data confirmation API

```
typedef void mcps_data_confirm_ext(const mac_api_t* api, const mcps_data_conf_t *data, const mcps_data_conf_payload_t *conf_data);
```
Parameter|Description
------|-----------
`api`|pointer, which is created by application
`data`|MCPS-DATA.confirm specific values.
`conf_data`|Possible Confirmation Data.

Confirmation data is packet to next structure:

```
typedef struct mcps_data_conf_payload_s {
    uint8_t *headerIeList;
    uint8_t *payloadIeList;
    uint8_t *payloadPtr;
    uint16_t headerIeListLength;
    uint16_t payloadIeListLength;
    uint16_t payloadLength;
} mcps_data_conf_payload_t;
```

Member|Description
------|-----------
`headerIeList`|Header information IE's list without terminator
`payloadIeList`|Payload information IE's list without terminator.
`payloadPtr`|Ack payload pointer.
`headerIeListLength`|Header information IE's list length in bytes.
`payloadIeListLength`|Payload information IE's list length in bytes.
`payloadLength`|Payload length in bytes.

#### Enhanced ACK payload and IE write API

```
typedef void mcps_ack_data_req_ext(const mac_api_t* api, mcps_ack_data_payload_t *data, int8_t rssi, uint8_t lqi);
```
Parameter|Description
------|-----------
`api`|pointer, which is created by application
`data`|Pointer where MAC user set Payload and IE element pointers and length.
`rssi`|Signal strength for received packet.
`lqi`|Link quality to neighbor.

Signal strength and link quality are just extra information if devices wan't share link quality both way at ack message protocol spesific way.

Structure for give ACK payload:
```
typedef struct mcps_ack_data_payload {
    struct mcps_data_req_ie_list ie_elements;
    uint8_t *payloadPtr;
    uint16_t payloadLength;
} mcps_ack_data_payload_t;
```
Member|Description
------|-----------
`ie_elements`|IE hader and payload's elements
`payloadPtr`|Ack payload pointer.
`payloadLength`|Payload length in bytes.

MAC user should set zero length of to payload or IE list when it not need to add spesific data to ACK.

## MAC API standard extensions

This chapter introduces MAC API standard extensions.

### MAC 64-bit address set and get

NanoStack uses 64-bit address set and get. There are two 64-bit addresses available:

- NVM EUI64.
- dynamic 64-bit address used at the link layer.

Thread generates a random MAC64 after commissioning. Therefore, MAC and the RF driver must support updating of radio's dynamic 64-bit address anytime.

Address set and get support two different 64-bit addresses:

| Address enumeration type | Description |
| -------------------------- | ----------- |
| `MAC_EXTENDED_READ_ONLY` | A unique EUI64. |
| `MAC_EXTENDED_DYNAMIC` | Dynamic 64-bit address. Same as EUI64 after boot. |

### MAC max storage information get

Usually, HW MAC and SW MAC have static keys and neighbor list sizes. Nanostack always asks the max size to limit its neighbor table size. The service user must define the `mac_storage_sizes_get()` function returning the following values:

- MAC Device description list size (must be > 1).
- MAC Key description list size (must be > 1).

<span class="notes">**Note:** The Key description list size must be at least 4 if using Thread!</span>

### MLME attribute extension

Nanostack uses MLME attribute extensions which have to be ported to the HW MAC adapter. To configure the extensions, use the `MLME-SET-REQ` command.

| Enumeration type | Value | Description |
| ---------------- | ----- | ----------- |
| `macAcceptByPassUnknowDevice` | `0xfc` | Accept data trough MAC if packet is data can be authenticated by group key and MIC. Security enforsment point must be handled carefully these packets. |
| `macLoadBalancingBeaconTx` | `0xfd` | Trigger to MAC layer to send a beacon. Called by the load balancer module periodically. |
| `macLoadBalancingAcceptAnyBeacon` | `0xfe` | Configure MAC layer to accept beacons from other networks. Enabled by load balancer, default value is `False`. Value size boolean, `true=enable`, `false=disable`. |
| `macThreadForceLongAddressForBeacon` | `0xff` | The Thread standard forces the beacon source address to have an extended 64-bit address. |

### Thread Sleepy End Device (SED) keepalive extension

Thread 1.1 stack defines that the sleepy end device data poll process must enable the neighbor table keepalive functionality as well. When SED finishes data polling successfully, it updates its parents keepalive value in a neighbor table. A service user at a parent device does not have a standard mechanism to indicate the data polling event. Therefore, the MAC layer must generate an `MLME-COMM-STATUS` indication callback with status `MLME_DATA_POLL_NOTIFICATION`.

Enumeration extension for MLME communication status enumeration:

| Enumeration type | Value | Description |
| ---------------- | ----- | ----------- |
| `MLME_DATA_POLL_NOTIFICATION` | `0xff` | Thread requirement for MLME-COMM-STATUS to start indicating the successful data poll events. |

## HW MAC

To use HW MAC, you need to create an adapter class that links function calls between Nanostack and HW MAC. To create the adapter class, you need to implement the functions defined in the `mac_api_s` structure. When HW MAC generates an event, the adapter must handle it and do a parameter adaptation before calling the correct function from the `mac_api_s` structure. You may need the same parameter adaptation for requests from Nanostack to HW MAC.

<span class="notes">**Note:** Function calls from Nanostack to HW MAC must be non-blocking in the adapter layer!</span>
