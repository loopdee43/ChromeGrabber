import socket
import os
PORT = int(input("input any port over 1212: "))
s = socket.socket()
s.bind((socket.gethostname(), PORT))
s.listen(1)
print("waiting for connections...")
conn, addr = s.accept()
print(f"{addr} has connected!")
while True:
    data = conn.recv(1024)
    thingy = open(data, 'w')

