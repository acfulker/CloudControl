#Global Variables
latitude = 0
longitude = 0
altitude = 0

#*************************
#Drone <-> LoPy Connection
#*************************

def receiveUart():
    # buffer_receive_uart = None
    # buffer_send_lora = None
    buffer_receive_uart = drone_uart.readall()
    #latitude,longitude,altitude = buffer_receive_uart.split(",")                               #FIXME: Functionality for ON drone(figure out)
    #buffer_send_lora = [latitude,longitude,altitude]    #Packetize for sendLora
    buffer_send_lora = buffer_receive_uart
    return buffer_send_lora

def sendUart(buffer_send_uart):
    drone_uart.write(buffer_send_uart)   #Will this just be a hand off of buffer_send_uart, or an interpretation of the command?


#*************************
#Cloud <-> LoPy Connection
#*************************


def receiveLora():
    # buffer_receive_lora = None
    # buffer_send_uart = None
    s.setblocking(False)    #Do I need to set this again if sendLora --> False
    buffer_receive_lora = s.recv(128)  #Determine size
    buffer_send_uart = buffer_receive_lora
    return buffer_send_uart


def sendLora(buffer_send_lora):
    s.setblocking(True)    #Block in order to send data
    s.send(buffer_send_lora)    #Need loop with s.send(buffer_send_lora[i])?
    s.setblocking(False)    #Listen by default

#*****************
#Looping Structure
#*****************

#IN DEVELOPMENT
# while True:
#     buffer_send_lora = receiveUart()
#     if(buffer_send_lora != None):
#         sendLora(buffer_send_lora)
#
#         buffer_send_uart = recieveLora()
#         if(buffer_send_uart != None):
#             sendUart(buffer_send_uart)
while True:

    buffer_send_uart = receiveLora()
    buffer_send_lora = receiveUart()
    if(buffer_send_uart or buffer_send_lora):
        sendUart(buffer_send_uart)
        if(buffer_send_lora != None):
            sendLora(buffer_send_lora)
