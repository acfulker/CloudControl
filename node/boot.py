from network import LoRa
import socket
import time
import ubinascii

# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)

# create an OTAA authentication parameters
app_eui = ubinascii.unhexlify('00250C000100021E')
app_key = ubinascii.unhexlify('5C6F83079DC0C01B9F77E41B84277C5C')

# join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(0.5)
    print('Not yet joined...')
    
print('Joined')
# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 4)
