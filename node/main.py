s.setblocking(True)
with open('sampletext.txt', 'r') as f:
    for line in f:
        l=line.rstrip('\n')
        s.send(l)
s.setblocking(False)
for i in range(60):
    data = s.recv(64)
    time.sleep(1)
    print(data)
