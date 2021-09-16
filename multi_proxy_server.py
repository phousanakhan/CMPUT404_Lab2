#!/usr/bin/env python3
import socket
import time
import sys
from multiprocessing import Process
# define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024


# TO-DO: get_remote_ip() method
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    print(f'Ip address of {host} is {remote_ip}')
    return remote_ip

# TO-DO: handle_request() method


def handle_request(addr, conn, proxy_end):
    try:
        full_data = conn.recv(BUFFER_SIZE)
        proxy_end.sendall(full_data)
        proxy_end.shutdown(socket.SHUT_RDWR)
        data = proxy_end.recv(BUFFER_SIZE)
        conn.send(data)
        # conn.close()
    except Exception as e:
        print("error message: ", e)


def main():
    # TO-DO: establish localhost, extern_host (google), port, buffer size

    # establish "start" of proxy (connects to localhosts)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        # To-DO: bind, and set to listening mode

        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind socket to address
        proxy_start.bind((HOST, PORT))
        # set to listening mode
        proxy_start.listen(2)

        while True:
            # TO-DO: accept incoming connections from proxy_start, print information about connection
            port = 80
            conn, addr = proxy_start.accept()
            print(f"conn info {conn} \n addr info {addr}")
            # establish end of proxy (connect to google)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                # TO-DO: get remote IP of goolge, connect proxy_end to it
                remote_ip = get_remote_ip("www.google.com")
                # --multiprocessing--
                proxy_end.connect((remote_ip, port))
                p = Process(target=handle_request,
                            args=(addr, conn, proxy_end))
                p.daemon = True
                p.start()
                print("Started process ", p)
                # TO-DO: allow for multiple connections with a Process daemon
                # make sure to set target = handle_request when creating the Process
                # TO-DO: close the connection
            conn.close()
