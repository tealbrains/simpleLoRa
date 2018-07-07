""" LoPy LoRaWAN Nano Gateway configuration options """

import machine
import ubinascii

try:
    from keys import *
except:
    print('Please create a keys.py file in the /lib folder, and add your credentials')

WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()

# for EU868
# LORA_FREQUENCY = 868100000
# LORA_GW_DR = "SF7BW125" # DR_5
# LORA_NODE_DR = 5

# for US915
# LORA_FREQUENCY = 903900000
# LORA_GW_DR = "SF7BW125" # DR_3
# LORA_NODE_DR = 3

# for AU915
LORA_FREQUENCY = 915000000
LORA_GW_DR = "SF7BW125" # DR_5
LORA_NODE_DR = 0
