from network import LoRa
import socket
import time
import pycom

i = 0
pycom.heartbeat(False) #needs to be disabled for LED functions to work

print("Starting Lora...")

# lora = LoRa(mode=LoRa.LORA, frequency=915000000)
lora = LoRa(mode=LoRa.LORA, region=LoRa.AU915, frequency=915000000)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

print("Ok, ready to transmit.")

while True:
    data = s.recv(64)
    if data == b'Ping':
        pycom.rgbled(0x088088)
        s.send('Pong')
        print(data)
    time.sleep(5)
    pycom.rgbled(0x0)
    time.sleep(5)
    data = 0

    i+=1
    print(i)