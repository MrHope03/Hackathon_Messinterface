import socket
import tqdm
import os

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))

n = 3


for i in range(n):
    s.listen(5)
    client_socket, address = s.accept()
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "ab") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:    
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))

client_socket.close()

s.close()
