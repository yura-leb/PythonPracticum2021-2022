import struct, sys

data = sys.stdin.buffer.read()[:44]
fmt = '4cI4c4cIhhIIhh4cI'
try:
    data = struct.unpack(fmt, data)
    assert b''.join(data[0:4]) == b'RIFF'
    assert b''.join(data[5:13]) == b'WAVEfmt '
    assert b''.join(data[20:24]) == b'data'
    print("Size=", data[4], end=', ', sep='')
    print("Type=", data[14], end=', ', sep='')
    print("Channels=", data[15], end=', ', sep='')
    print("Rate=", data[16], end=', ', sep='')
    print("Bits=", data[19], end=', ', sep='')
    print("Data size=", data[24], sep='')
except Exception:
    print("NO")
