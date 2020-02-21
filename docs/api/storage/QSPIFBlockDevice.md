# QSPIFBlockDevice

<span class="images">![](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_q_s_p_i_f_block_device.png)<span>QSPIFBlockDevice class hierarchy</span></span>


The QSPIFBlockDevice is a block device driver for NOR-based QSPI Flash devices that support the SFDP standard. NOR-based QSPI Flash supports up to 4 bits per cycle of instruction, address and data. SFDP-based QSPI Flash supports variable bus modes (single, dual and quad), several sector erase size types and multiple regions of sector size types.

For more information about the SFDP JEDEC standard, please see [its documentation](https://www.jedec.org/system/files/docs/JESD216C.pdf).

## QSPIFBlockDevice class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/development/mbed-os-api-doxy/class_q_s_p_i_f_block_device.html)

## QSPIFBlockDevice example

This example creates a QSPIFBlockDevice, erases a sector, programs it, reads the block back and cleans up.

[![View code](https://www.mbed.com/embed/?url=https://os.mbed.com/teams/mbed_example/code/QSPIFBlockDevice_example/)](https://os.mbed.com/teams/mbed_example/code/QSPIFBlockDevice_example/file/5608693b47aa/main.cpp/)
