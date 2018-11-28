# Static Global API
The KVStore static API is presented in the file mbed-os\features\storage\kvstore\global_api\kvstore_global_api.h
This API should be the only API used by applications to access the instances of KVStore components allocated by the selected configuration.

## Allocation of KVStore Components
The function kv_init_storage_config()in file mbed-os\features\storage\kvstore\conf\kv_config.h will allocate and initialize all the components required for the execution of the global API.It will be implicitly called by the API, and can be called several times without side effects.

The allocation and setup of KVStore components and blockdevices required, will be done according to the configuration parameters present in the json files at mbed-os\features\storage\kvstore\conf and subfolders, or overridden by the application json file (mbed_app.json). See configuration of storage for details.

## Parameter Details
Please find below an explanation for the non-trivial parameters that are part of the global API
 
### full_name_key
This is a string composed from characters valid for filenames in the form of **/path/myfilename**

**/path/** is used by the global API to identify the KVStore component that will receive the call. The global API will remove the /path/ from the string passed to the KVStore API. The **path** string must be equal to the string defined for parameter **default_kv** in file mbed-os\features\storage\kvstore\conf\mbed_lib.json (/kv/ by default). Use **/kv/myfilename** when using the default configuration.

>Note: The configuration passes the value of the parameter default_kv to the function kv_map.attach(STR(MBED_CONF_STORAGE_DEFAULT_KV),&kvstore_config) to create the relation between the path string and the allocated KVStore component. 

### Creation Flags
The flags explained below can be "ored" (|) and passed to the function set in parameter create_flags. These flags indicate the security required for the data saved. This security behavior can be overriding by explicitly selecting a configuration in the storage_type parameter

**KV_WRITE_ONCE_FLAG:** The system will not allow deletion or replacement of the data in the file by additional call to function set with the same filename.

**KV_REQUIRE_CONFIDENTIALITY_FLAG:** The system will encrypt the data using a AES CTR, a random IV and a key derived from devicekey. This flag will be ignored if selecting TDB_INTERNAL configuration, as the internal memory is seen as protected from physical attacks.

**KV_REQUIRE_INTEGRITY_FLAG:** The system will calculate a CMAC using a key derived from the devicekey and will check the data validity when reading from the file (function get). 

**KV_REQUIRE_REPLAY_PROTECTION_FLAG:** The system will keep a copy of the data CMAC in internal memory and will check that the data CMAC corresponds to this saved CMAC, to avoid an attacker from replacing the latest data with a valid old version of the data. This flag will be ignored if selecting the configurations TDB_EXTERNAL_NO_RBP or FILESYSTEM_NO_RBP.

### full_prefix
The function kv_iterator_open uses this parameter to define the subset of filenames that will be returned by kv_iterator_next. The function uses the string as a prefix, and each name that starts with exact string passed in full_prefix will be retruned by kv_iterator_next.
>Note: The full_prefix string must include the /path/ (e.g. /kv/)



