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
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)
app_eui = ubinascii.unhexlify('00250C0000010001')
app_key = ubinascii.unhexlify('5C6F83079DC0C01B9F77E41B84277C5C')     #put the right value here.
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
while not lora.has_joined():
    time.sleep(2)
    print('Not yet joined...')
pycom.heartbeat(True)      #Once joined network, turn on
print('Joined')
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 4)
