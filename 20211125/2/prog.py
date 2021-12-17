import sys
latin1 = sys.stdin.buffer.read().decode()
byte = latin1.encode('latin1', errors='replace')
cp1251 = byte.decode('cp1251', errors='replace')
sys.stdout.buffer.write(cp1251.encode('utf-8'))
