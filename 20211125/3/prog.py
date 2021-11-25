import struct, random

fil = open('test', 'wb')
f = 'fI'
for i in range(10):
    fil.write(struct.pack(f, random.random(), random.randint(0, 20)))
fil.close()
fil = open('test', 'rb')
print(fil.read())
