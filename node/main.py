s.setblocking(True)
with open('sampletext.txt', 'r') as f:
    for line in f:
        l=line.rstrip('\n')
        s.send(l)
