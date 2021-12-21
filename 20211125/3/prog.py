from struct import unpack
import sys
data = sys.stdin.buffer.read()[:44]
fmt = '4cI4c4cIhhIIhh4cI'
try:
    data = unpack(fmt, data)
    if b''.join(data[0:4]) == b'RIFF'\
    and b''.join(data[5:13]) == b'WAVEfmt ':        
        print(f'Size={data[4]}, Type={data[14]}, Channels={data[15]}, Rate={data[16]}, Bits={data[19]}, Data size={data[24]}')
    else:
        print('NO')
except:
    print('NO')
