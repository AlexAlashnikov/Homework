#!/usr/local/bin/python3.11
import socket

HOST, PORT = '127.0.0.1', 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
    server_sock.bind((HOST, PORT))
    server_sock.listen(1)
    conn, addr = server_sock.accept()
    with conn:
        print(f"Подключено: {addr}")
        while True:
            data = conn.recv(1024)
            data = data.decode()
            num1, op, num2 = data.split(" ")
            num1, num2 =  float(num1), float(num2)
            if op == "+":
                data = (num1 + num2)
            elif op == "-":
                data = (num1 - num2)
            elif op == "*":
                data = (num1 * num2)
            elif op == "/":
                data = (num1/num2)
            data = str(data)
            data = data.encode()
            conn.sendall(data)
