import socket
import sys

if len(sys.argv) < 3:
    raise Exception()

path = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50000))
s.listen(1)
try:
    komm, addr = s.accept()
    with open(path, 'w') as file:
        while 1:
            data = komm.recv(1024).decode('utf-8')
            if not data:
                break
            else:
                file.write(data)
finally:
    s.close()
