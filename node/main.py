import serial
#Global Variables
ser = 0

#Function to Initialize the Serial Port
def init_serial():
    ser = serial.Serial("/dev/cu.usbmodemPy99b4b31",115200, timeout=0) 
    #Specify the TimeOut in seconds, so that SerialPort
    #Doesn't hangs
    ser.open()          #Opens SerialPort
    # print port open or closed
    if ser.isOpen():
        print 'Open: ' + ser.portstr
#Function Ends Here
#Call the Serial Initilization Function, Main Program Starts from here
init_serial()

temp = raw_input('Type what you want to send, hit enter:\r\n')
ser.write(temp)         #Writes to the SerialPort

while 1:
    bytes = ser.readline()  #Read from Serial Port
    print 'You sent: ' + bytes      #Print What is Read from Port
    break

    #sample code for UART connection
from machine import UART
uart = UART(1, 9600)                         # init with given baudrate
uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters
while True:
    data = uart.readall()
    if data is not None:
       print(data)
       break
#Ctrl+C to Close Python Window
