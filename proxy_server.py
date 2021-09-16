#!/usr/bin/env python3
import socket
import time

# define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024


def main():
    port = 80
    host = "www.google.com"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # bind socket to address
        s.bind((HOST, PORT))

        # set to listening mode
        s.listen(2)

        # continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                remote_ip = socket.gethostbyname(host)
                proxy_end.connect((remote_ip, port))
                # recieve data, wait a bit, then send it back
                data = conn.recv(BUFFER_SIZE)
                proxy_end.sendall(data)
                print(f"sending recieved data {data} to Google")
                proxy_end.shutdown(socket.SHUT_WR)
                full_data = proxy_end.recv(BUFFER_SIZE)
                conn.send(full_data)
            conn.close()


main()
