""" LoPy LoRaWAN Nano Gateway configuration options """

import machine
import ubinascii

try:
    from keys import *
except:
    print('Please create a keys.py file in the /lib folder, and add your credentials')

WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()
# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]

SERVER = 'thethings.meshed.com.au'
PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

WIFI_SSID = MY_WIFI_SSID
WIFI_PASS = MY_WIFI_PASS

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

