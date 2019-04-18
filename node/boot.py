from machine import UART
from network import LoRa
import os
import time
import pycom
import socket
import ubinascii

#Change default uart from UART(1,9600) to have pass through USB
drone_uart = UART(0,115200)

#LoRa setup
#COMMENTED OUT SINCE NO ANTENNA
pycom.heartbeat(False)     #No heartbeat on boot
lora = LoRa(mode=LoRa.LORAWAN, power_mode= LoRa.ALWAYS_ON, region=LoRa.US915)
lora.init(mode=LoRa.LORAWAN, adr=False, public=True, tx_retries=0, device_class=LoRa.CLASS_C)
app_eui = ubinascii.unhexlify('00250C000100021E')
app_key = ubinascii.unhexlify('3C660D6DBFCA6B02BBF6189CD23B6E28')     #put the right value here.
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
while not lora.has_joined():
    time.sleep(2)
    print('Not yet joined...')
pycom.heartbeat(True)      #Once joined network, turn on
print('Joined')
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 4)
s.setblocking(False)
