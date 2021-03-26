import socket
import tqdm
import os
import csv


SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))

print("Enter no. of students : ")
n = int(input())

for i in range(n):
    s.listen(n)
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

dish_quan = [0, 0, 0, 0, 0]
no = 0
food = []
with open('appetite_data.txt', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row != []:
            food = row[7:]
            for i in range(5):
                dish_quan[i] += int(row[i+2])
            no+=1

for j in range(5):
    print("\nThe mean appetite for "+food[j]+" is "+str(dish_quan[j]/no))

