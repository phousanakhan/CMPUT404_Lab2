#!/usr/bin/env python3
import socket
import time

# define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024


def main():
    port = 80
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
                remote_ip = socket.gethostbyname("www.google.com")
                proxy_end.connect((remote_ip, port))
                # recieve data, wait a bit, then send it back
                full_data = conn.recv(BUFFER_SIZE)
                print(f"sending recieved data {full_data} to Google")
                proxy_end.shutdown(socket.SHUT_WR)
                conn.sendall(full_data)
            conn.close()


if __name__ == "__main__":
    main()
