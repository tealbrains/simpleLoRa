""" OTAA Node example compatible with the LoPy Nano Gateway """

from network import LoRa
import socket
import binascii
import struct
import time
import config

try:
    from keys import *
except:
    print('Please create a keys.py file in the /lib folder, and add your credentials')

# initialize LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.AU915)

#Set AppEUI and AppKey - use your values from the device settings --> https://console.thethingsnetwork.org/
dev_eui = binascii.unhexlify(MY_DEV_EUI)
app_eui = binascii.unhexlify(MY_APP_EUI)
app_key = binascii.unhexlify(MY_APP_KEY)

# remove all the non-default channels
# for i in range(0, 72):
#     lora.remove_channel(i)

# set the 3 default channels to the same frequency (must be before sending the OTAA join request)
lora.add_channel(8, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=0)
# lora.add_channel(1, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)
# lora.add_channel(2, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)


# join a network using OTAA
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0, dr=config.LORA_NODE_DR)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not joined yet...')

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, config.LORA_NODE_DR)

# make the socket blocking
s.setblocking(False)

time.sleep(5.0)



for i in range (200):
    pkt = b'PKT #' + bytes([i])
    print('Sending:', pkt)
    s.send(pkt)
    time.sleep(4)
    rx, port = s.recvfrom(256)
    if rx:
        print('Received: {}, on port: {}'.format(rx, port))
time.sleep(6)
