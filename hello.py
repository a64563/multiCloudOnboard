def add(x,y):
    return x+y

#!/usr/bin/env python3

import socket
import sys



PORT = int(sys.argv[1])        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', PORT))
    s.listen()


    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = b''
            while True:
                data += conn.recv(1024)

                print(data)

                if data[-4:] == b'\r\n\r\n' or len(data) == 0:
                    print("YYEEAAAA")
                    break


            contint = "<h2>hello my friend, did you want to see what the request you sent looks like? here it is:<h2>".encode(encoding='UTF-8')+data
            header = (
                "HTTP/1.1 200 OK\r\n"
                "Date: Mon, 27 Jul 2009 12:28:53 GMT\r\n"
                "Server: Apache/2.2.14 (Win32)\r\n"
                "Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT\r\n"
                "Content-Length: " + str(len(contint)) + "\r\n"
                "Content-Type: text/html\r\n"
                "Connection: Closed\r\n"
                "\r\n"
            )

            conn.sendall(header.encode(encoding='UTF-8') + contint)
            conn.close()
