# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)

# send some data
#with open('sampletext.txt', 'r') as f:
for i in range(100):
    s.send(bytes([i]))
