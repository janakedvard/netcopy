#xdxdxdxd
from socket import socket, AF_INET, SOCK_STREAM
import sys
import hashlib

server_addr = ('localhost', 10001)
#server_addr = (sys.argv[1], int(sys.argv[2]))


proxy = (AF_INET, SOCK_STREAM)
x='localhost'
d=10000 
#proxy_addr = ('localhost', 10000)
#proxy_addr = ((sys.argv[3], int(sys.argv[4])))

proxy.connect((x, d)



m = hashlib.md5()

with socket(AF_INET, SOCK_STREAM) as client:
    with open(sys.argv[6], "rb") as f:
        client.connect((server_addr))
        l = f.read(128)
        while l:
            client.sendall(l)
            m.update(l)
            l = f.read(128)
            

msg = ('BE|' + sys.argv[5] + '|60|' + m.digest_size + '|' + m).encode('utf-8')

proxy.sendall(msg)

d = proxy.recv(128)

print(d)



