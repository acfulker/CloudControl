import serial
#Global Variables
ser = 0
longitude = 0
latitude 0
altitude = 0
#Function to Initialize the Serial Port
def init_serial():
    ser = serial.Serial("/dev/cu.usbmodemPy99b4b31")
    ser.baudrate= 115200
    ser.port= '/dev/cu.usbmodemPy99b4b31'
    ser.timeout=0
    #Specify the TimeOut in seconds, so that SerialPort
    #Doesn't hangs
    ser.open()          #Opens SerialPort
    # print port open or closed
    if ser.isOpen():
        print 'Open: ' + ser.name
#Function Ends Here
#Call the Serial Initilization Function, Main Program Starts from here
init_serial()

buffer_receive = ser.read(500) #Reads to the SerialPort
buffer_transmit = ser.write(500) #Writes to the SerialPort
buffer_receive_convert = map(float, buffer_receive.split(' , '))
# Splitting the string list into a float list ^^^
latitude = buffer_receive_convert(0)
longitude = buffer_receive_convert(1)
altitude = buffer_receive_convert(2)

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
