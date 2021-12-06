import sys
latin1 = sys.stdin.buffer.read().decode(errors='replace')
byte = latin1.encode('latin1', errors='replace')
cp1251 = byte.decode('cp1251', errors='replace')
print(cp1251)
