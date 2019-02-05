from network import LoRa
import pycom
import socket
import ubinascii
import struct
import time
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)
app_eui = ubinascii.unhexlify('00250C0000010001')
app_key = ubinascii.unhexlify('998B0CE21F8EAE6732D6CCBC32DA345D')
lora.init(mode=LoRa.LORAWAN, frequency=915000000, tx_power=14, bandwidth=LoRa.BW_125KHZ, sf=7, preamble=8, coding_rate=LoRa.CODING_4_5, power_mode=LoRa.ALWAYS_ON, tx_iq=False, rx_iq=False, adr=True, public=True, tx_retries=0, device_class=LoRa.CLASS_C)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), dr=0, timeout=0)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 4)
