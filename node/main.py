# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)

# send some data
with open('sampletext.txt', 'r') as f:
    for line in f:
        l=line.rstrip('\n')
        s.send(l)
s.setblocking(False)
for i in range(60):
    data = s.recv(64)
    time.sleep(1)
    print(data)
