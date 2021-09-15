#!/usr/bin/env python3
import socket
import time

# define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024


def main():
    print('Creating socket')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print(
            f'Failed to create socket. Error code: {str(msg[0])} , Error message : {msg[1]}')
        sys.exit()
    print('Socket created successfully')
    payload = f'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'

    ip = 8001
    s.connect(("127.0.0.1", ip))
    s.sendall(payload.encode())
    s.shutdown(socket.SHUT_WR)
    data = s.recv(BUFFER_SIZE)
    print(data)
    s.close()


if __name__ == "__main__":
    main()
