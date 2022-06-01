from socket import socket, AF_INET, SOCK_STREAM
import sys
from datetime import datetime, timedelta
import hashlib, select, struct

proxy = socket(AF_INET,SOCK_STREAM)

proxy_addr = (argv[1],int(argv[2]))


proxy.bind(proxy_addr)

proxy.listen(3)

inputs = [proxy]

msg = []

while True:
        timeout = 1
        r, w, e = select.select(inputs,inputs,inputs,timeout)
        if not (r or w or e):
            continue
        for s in r:
            if s is proxy:
                client, client_addr = s.accept()
                inputs.append(client)
            else:
                data = s.recv(128)
                if data:
                    msg = str(data, 'utf-8').split('|')
                    if msg[0] == 'BE':
                        t = int(msg[2])
                        md5_size = int(message[3])
                        m = message[4]
                        time_now = datetime.now()
                        s.send(b'OK')

                    elif msg[0] == 'KI':
                        if md5_size != 0:
                            if datetime.now() - d_time < timedelta(seconds=time):
                                msg = str(md5_size) + '|' + m
                            else:
                                msg = '0|'
                        else:
                            msg = '0|'
                        s.sendall(msg.encode('utf-8'))
                else:
                    inputs.remove(s)
                    s.close()