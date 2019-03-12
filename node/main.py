#Global Variables
latitude = 0
longitude = 0
altitude = 0

#*************************
#Drone <-> LoPy Connection
#*************************
buffer_receive_uart = ""    #Do I need these declared outside of functions to stay in scope?
buffer_send_lora = []

def receive_uart_data():
    buffer_receive_uart = drone_uart.readall()
    latitude,longitude,altitude = buffer_receive_uart.split(",")
    buffer_send_lora = [latitude,longitude,altitude]    #Packetize for send_lora_data

def send_uart_data():
    drone_uart.write(buffer_send_uart)   #Will this just be a hand off of buffer_send_uart, or an interpretation of the command?


#*************************
#Cloud <-> LoPy Connection
#*************************
buffer_receive_lora = ""    #Determine type
buffer_send_uart = []

def recieve_lora_data():
    s.setblocking(False)    #Do I need to set this again if send_lora_data --> False
    buffer_send_uart = s.recv(128)  #Determine size


def send_lora_data():
    s.setblocking(True)    #Block in order to send data
    s.send(buffer_send_lora)    #Need loop with s.send(buffer_send_lora[i])?
    s.setblocking(False)    #Listen by default


#*************************
#Cloud Command Definitions
#*************************

#I believe this would actually be on the drone


#*****************
#Looping Structure
#*****************

#IN DEVELOPMENT
# while True:
#     i = 0
#     while i < 5:
#         receive_uart_data()
#         i += 1
#
#     send_lora_data()
#
#     j = 0
#     while j < 5:
#         recieve_lora_data()
#         j += 1
#
#     send_uart_data()

#TEST
for i in range(100):
    s.setblocking(True)
    something = drone_uart.readall()
    s.send(str(something))
    time.sleep(1)
