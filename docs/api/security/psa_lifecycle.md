# PSA lifecycle

The PSA lifecycle API enables setting the lifecycle state.

Setting a lower lifecycle state - for example, factory or test state - allows you to control the target root of trust (RoT) and change the debugging policy when testing or debugging.

The following is a state machine depiction of the PSA lifecycle:

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/psa_lifecycle.png)</span>

<span class="notes"> **Note:** PSA lifecycle is not a standalone feature; it depends on PSA bootloader support, which has not yet been introduced in Mbed OS. The only lifecycle change currently supported is `PSA_LIFECYCLE_ASSEMBLY_AND_TEST` to `PSA_LIFECYCLE_ASSEMBLY_AND_TEST`, which you can use in testing to reset the device RoT state. All of the lifecycle changes represented by dashed lines in the diagram above have not yet been implemented.
</span>

You can specify the lifecycle value during build time using the `MBED_CONF_LIFECYCLE_STATE` macro. The default lifecycle value is `PSA_LIFECYCLE_ASSEMBLY_AND_TEST`.

In Mbed OS, the PSA lifecycle is implemented as part of the platform service.

## PSA lifecycle reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/lifecycle_8h.html)

## Related content

- [Platform Security Architecture - Firmware Framework](https://pages.arm.com/psa-resources-ff.html).
