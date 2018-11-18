## Static Global API

Applications should use the KVStore static API to access the instances of KVStore components that the selected configuration allocates.

### Allocation of KVStore components

The function `kv_init_storage_config()` allocates and initializes all the components required for the execution of the global API. The API implicitly calls it and can call it several times without side effects.

The configuration parameters present in the API's `.json` files determine the allocation and setup of required KVStore components and block devices. The application's `.json` file, `mbed_app.json`, can override these parameters. Please see the [storage configuration documentation](../config/configuration-storage.html) for details.

### Parameter details

Below are the nontrivial parameters that are part of the global API.
 
#### `full_name_key`

This is a string composed of characters valid for file names in the form of **/path/myfilename**.

The global API uses **/path/** to identify the KVStore component that receives the call. The global API removes the **/path/** from the string passed to the KVStore API. The **path** string must be equal to the string defined for the **default_kv** parameter in the API's `mbed_lib.json` file (`/kv/` by default). Use **/kv/myfilename** when using the default configuration.

<span class="notes">**Note:** The configuration passes the value of the parameter `default_kv` to the function `kv_map.attach(STR(MBED_CONF_STORAGE_DEFAULT_KV),&kvstore_config)` to create the relation between the path string and the allocated KVStore component.</span>

#### Creation flags

You can "or" (|) the flags below and pass them to the function set in the parameter `create_flags`. These flags indicate the security required for the data saved. You can override this security behavior by explicitly selecting a configuration in the `storage_type` parameter:

- **KV_WRITE_ONCE_FLAG:** The system does not an additional call to the function set with the same file name to delete or replace data.
- **KV_REQUIRE_CONFIDENTIALITY_FLAG:** The system encrypts the data using an AES CTR, a random IV and a key derived from DeviceKey. This flag will be ignored if you select the `TDB_INTERNAL` configuration because the internal memory is seen as protected from physical attacks.
- **KV_REQUIRE_INTEGRITY_FLAG:** The system calculates a CMAC using a key derived from DeviceKey and checks the data validity when reading from the file (function `get`).
- **KV_REQUIRE_REPLAY_PROTECTION_FLAG:** The system keeps a copy of the data CMAC in internal memory and checks that the data CMAC corresponds to this saved CMAC. It does this to prevent an attacker replacing the latest data with a valid old version of the data. This flag will be ignored if you select the configuration `TDB_EXTERNAL_NO_RBP` or `FILESYSTEM_NO_RBP`.

#### `full_prefix`

This parameter is used in the iterator `kv_iterator_open` function to define the subset of file names that `kv_iterator_next` returns. The string is used as a prefix, and `kv_iterator_next` returns each name that starts with the exact string passed in `full_prefix`.

<span class="notes">**Note:** The full_prefix string must include the `/path/`. For example: `/kv/`.</span>

### Static Global API class reference

<insert link>
 
### Static Global API example

<insert link>

### Related content

<insert links>
