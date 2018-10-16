from pywinusb import hid

# Whenever the host computer receives data from the 
# Mbed board, the received data is printed
def on_data(data):
    print("Got message %s" % data)

'''
Gets all HIDs currently connected to host computer, 
and sets the first device with string "mbed" in its
vendor name equal to variable mbed. This variable 
will be used to send data to the Mbed board.
'''
all_devices = hid.find_all_hid_devices()
mbeds = [dev for dev in all_devices if dev.vendor_name.find("mbed") >= 0]
if len(mbeds) == 0:
    print("No HID devices found")
    exit(-1)
mbed = mbeds[0]

# Sends 8 bytes of data to the Mbed board
# The Mbed board should receive the data "1 2 3 4 5 6 7 8"
mbed.open()
mbed.set_raw_data_handler(on_data)
message = bytearray(9)
message[1] = 1
message[2] = 2
message[3] = 3
message[4] = 4
message[5] = 5
message[6] = 6
message[7] = 7
message[8] = 8

mbed.find_output_reports()[0].send(message)
