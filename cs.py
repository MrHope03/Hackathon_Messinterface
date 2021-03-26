#file transfer code taken from https://www.thepythoncode.com/article/send-receive-files-using-sockets-python

# modules for file transfer
import socket
import tqdm
import os
        
filename = "appetite_data.txt"

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 

host = "192.168.1.9"

port = 5001

filesize = os.path.getsize(filename)

s = socket.socket()

s.connect((host, port))

s.send(f"{filename}{SEPARATOR}{filesize}".encode())

progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        s.sendall(bytes_read)
        progress.update(len(bytes_read))

s.close()
