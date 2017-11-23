
import socket
try:
    with socket.create_connection(('192.168.3.173', 7777)) as sock:
        multiline_text = []
        while True:
            text = input()
            if text:
                multiline_text.append(text)
            else:
                break
        data = '\n'.join(multiline_text)
        sock.sendall(data.encode('utf8'))
except:
    print('Проверь сервак')
