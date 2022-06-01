from socket import socket, AF_INET, SOCK_STREAM
import sys
import hashlib


server_addr = ((sys.argv[1], int(sys.argv[2]))

proxy = socket(AF_INET, SOCK_STREAM)


proxy_addr = (sys.argv[3], int(sys.argv[4]))

with socket(AF_INET, SOCK_STREAM) as server:
    server.bind(server_addr)
    server.listen(3)
    
    client, client_addr = server.accept()
    end = False
    m = hashlib.md5()
    with open(sys.argv[6], "wb") as f:
        while not end:
            data  = client.recv(128)
            m.update(data)
            if data:
                f.write(data)
            else:
                client.close()
                end = True
                

proxy.connect(proxy_addr)

msg = 'KI|' + sys.argv[5]


proxy.sendall(msg.encode('utf-8'))

data = proxy.recv(128)

d = str(data, 'utf-8').split('|')

if int(d[0]) != 0 and d[1] == m:
	print('CSUM OK')
else:
	print('CSUM CORRUPTED')