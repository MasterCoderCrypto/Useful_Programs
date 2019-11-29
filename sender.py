import socket
import os
import sys

IP = ''

class PATHERROR(Exception):
    def __init__(self, path):
        super().__init__()
        self.path = path
    def __str__(self):
        return self.path + ' does not exist'

if len(sys.argv) <= 4 or '-ip' not in sys.argv or '-p' not in sys.argv:
    raise

ip = (sys.argv[sys.argv.index('-ip')+1] if not ('-I') in sys.argv else IP)
path = sys.argv[sys.argv.index('-p')+1]

if not os.access(path, os.F_OK | os.R_OK):
    raise PATHERROR(path)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 50000))
with open(path, 'r') as file:
    for line in file.readlines():
        s.send(line.encode('utf-8'))
s.close()
