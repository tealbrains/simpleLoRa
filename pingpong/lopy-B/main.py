from network import LoRa
import socket
import time
import pycom

i = 0

pycom.heartbeat(False) #needs to be disabled for LED functions to work

print("Starting Lora...")

lora = LoRa(mode=LoRa.LORA, region=LoRa.AU915, frequency=915000000)
# lora = LoRa(mode=LoRa.LORA, frequency=915000000)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

print("Ok, ready to transmit.")

# s.send('Ping')

while True:
    # data = s.recv(64)
    # if data == b'Pong':
    #     pycom.rgbled(0x880088)
    #     s.send('Ping')
    #     print(data)
    # else:
    #     s.send('Ping')
    #     print("Resending Ping")
    #     pycom.rgbled(0x008800)
    # time.sleep(5)
    # pycom.rgbled(0x0)
    # time.sleep(5)
    # data = 0

    s.send('Ping')
    i+=1
    print(i)
    time.sleep(10)
