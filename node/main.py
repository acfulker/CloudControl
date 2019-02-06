from network import LoRa
import socket
import ubinascii
import time
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)
app_eui = ubinascii.unhexlify('00250C0000010001')
app_key = ubinascii.unhexlify('')#put the right value here.
while not lora.has_joined():
    time.sleep(2)
    print('Not yet joined...')
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 4)
s.setblocking(True)
with open('sampletext.txt', 'r') as f:
    for line in f:
        l=line.rstrip('\n')
        s.send(l)
s.setblocking(False)
for i in range(5):
    data = s.recv(64)
    time.sleep(1)
    print(data)
