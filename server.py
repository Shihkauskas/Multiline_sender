# -*- coding: UTF-8 -*-

import socket

try:
    with socket.socket() as sock:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', 7777))
        sock.listen(socket.SOMAXCONN)
except:
    print('Проверь клиента')

conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data.decode('utf8'))
    with open('text.txt', 'w') as file:
        file.write(data.decode('utf8'))
