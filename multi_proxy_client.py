#!/usr/bin/env python3
import socket
from multiprocessing import Pool
# define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024


payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"


def connect(addr):
    try:
        # create socket, connect, send & recieve, then shutdown
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        full_data = s.recv(BUFFER_SIZE)
        print(full_data)
    except Exception as e:
        print("Error message: ", e)

    s.close()


def main():
    address = [(HOST, PORT)]
    with Pool() as p:
        # establish 10 different connection
        p.map(connect, address * 10)


main()
