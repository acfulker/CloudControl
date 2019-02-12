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
print('Joined')
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 4)
