import socket
from os.path import join
PORT = int(input("input any port over 1212: "))
s = socket.socket()
s.bind((socket.gethostname(), PORT))
s.listen(1)
print("waiting for connections...")
conn, addr = s.accept()
print(f"{addr} has connected!")
path = input("input the path where everything will be saved: ")
while True:
    data = conn.recv(1024)
    thingy = open(join(path, data), 'w')

