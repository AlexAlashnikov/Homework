#!/usr/local/bin/python3.11
import socket

HOST, PORT = '127.0.0.1', 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        data = input("Please input your example: ")
        data_bytes = data.encode()
        sock.sendall(data_bytes)
        data_bytes = sock.recv(1024)
        data = data_bytes.decode()
        print('Result:', data)
