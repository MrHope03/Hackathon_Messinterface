#file transfer code taken from https://www.thepythoncode.com/article/send-receive-files-using-sockets-python

import socket
import tqdm
import os

import datetime
import calendar

import csv

x = datetime.datetime.now()
day = x.strftime("%a")
time = int(x.strftime("%H"))

if (time>6 and time <12):
    greet = "Morning"
    inf = "Afternoon"
    fday = day
elif (time>=12 and time<18):
    greet = "Afternoon"
    inf = "Night"
    fday = day
elif (time>=18 and time <21):
    greet = "Evening"
    inf = "Night"
    fday = day
else:
    greet = "Night"
    inf = "Tomorrow"
    fday = (x + datetime.timedelta(days=1)).strftime("%A")

print("Good " + greet + "! Here's " + inf + "'s menu\n")

food = []

with open(fday + '_' + inf + '.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            food += [[row[0], row[1]]]
            line_count += 1

for i in food:
    print(i[0] + '\n')

fields = ['Food', 'Category', 'Appetite']

data = []

foo = sorted(food, key = lambda x: x[1])

for i in foo:
    if i[1]=='1':
        print("How much quanity of " + i[0] + " do you feel you can eat? (on a scale of 0 to 5)\n")
        data += [[i[0], i[1], input()]]
    elif i[1]=='2':
        print("How many cups of " + i[0] + " do you feel you can drink?")
        data += [[i[0], i[1], input()]]
    elif i[1]=='3':
        print("How many nos. of " + i[0] + " do you feel like eating?")
        data += [[i[0], i[1], input()]]
    elif i[1]=='4':
        print("Do you feel like having " + i[0] + " along with the main dish?")
        data += [[i[0], i[1], input()]]
        
filen = "appetite_data.txt"

with open(filen, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(data)

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 

host = "192.168.1.101"

port = 5001

filename = "student1.txt"

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
