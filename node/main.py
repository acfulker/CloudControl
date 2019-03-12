from network import LoRa
import socket
import ubinascii
import time
import serial
#Setting up LoRA connection
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)
app_eui = ubinascii.unhexlify('00250C0000010001')
app_key = ubinascii.unhexlify('')#put the right value here.
while not lora.has_joined():
    time.sleep(2)
    print('Not yet joined...')
print('Joined')
LoRA_connection = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
LoRA_connection.setsockopt(socket.SOL_LORA, socket.SO_DR, 4)
#Global Variables
drone_serialport = 0
longitude = 0
latitude 0
altitude = 0
#Function to Initialize the Serial Port
def init_serial():
    drone_serialport = serial.Serial("/dev/cu.usbmodemPy99b4b31")
    drone_serialport.baudrate= 115200
    drone_serialport.port= '/dev/cu.usbmodemPy99b4b31'
    drone_serialport.timeout=0
    #Specify the TimeOut in seconds, so that SerialPort
    #Doesn't hangs
    drone_serialport.open()          #Opens SerialPort
    # print port open or closed
    if drone_serialport.isOpen():
        print 'Open: ' + drone_serialport.name
#Function Ends Here
#Call the Serial Initilization Function, Main Program Starts from here
init_serial()

buffer_receive = drone_serialport.read(500) #Reads to the SerialPort
buffer_receive_convert = map(float, buffer_receive.split(' , '))
# Splitting the string list into a float list ^^^
latitude = buffer_receive_convert(0)
longitude = buffer_receive_convert(1)
altitude = buffer_receive_convert(2)

sending_buffer = [latitude,longitude,altitude] #sending an array of float variables to CloudControl
LoRA_connection.send(sending_buffer) # sending the buffer of GPS points

#We have to figure out how to keep looking for information and
#once we see the information break out of it
received_instructions = LoRA_connection.recv(500)
drone_serialport.write(received_instructions) #Writes to the SerialPort




    #sample code for UART connection
#from machine import UART
#uart = UART(1, 9600)                         # init with given baudrate
#uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters
#while True:
#    data = uart.readall()
#    if data is not None:
#       print(data)
#       break
#Ctrl+C to Close Python Window

