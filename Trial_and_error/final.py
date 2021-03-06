import tkinter as tk #pip install tk
import time
import datetime
import os
import tqdm
import socket
import calendar
import tkinter.messagebox as tkm 
from PIL import ImageTk , Image #pip install pillow
import csv

data = []

def getvalues():
    global name,rollno,value1,value2,value3,value4,value5
    name = text1.get()
    rollno = text2.get()
    value1 = scale1.get()
    value2 = scale2.get()
    value3 = scale3.get()
    value4 = scale4.get()
    value5 = scale5.get()
    data = [value1,value2,value3,value4,value5]

def transfer():
    filename = "appetite_data.txt"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)
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

#WRITING IN A CSV FILE
local_time = time.localtime(1545925769)
day = local_time.tm_wday
now = time.strftime('%H:%M:%S %p')
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
#retriving data from csv file
f = open(fday + '_' + inf + '.txt','r')
reader = csv.DictReader(f,delimiter = ',')
for row in reader:
    d = dict(row)
    break

#graphical user interface
    
main=tk.Tk()
main.title('FOOD MANAGEMENT')
main.attributes("-fullscreen", True)
img=ImageTk.PhotoImage(Image.open("anna_university.png"))
text=tk.Label(main, text='                       ',font=500).grid(row=2,column=0,pady=10)
image=tk.Label(main, image=img).grid(row=0,column=10, columnspan=7, rowspan=7)
text1=tk.Label(main, text='     WELCOME    TO   JUNIOR    MESS   COLLEGE   OF    ENGINEERING    GUINDY    ',font=500).grid(row=1,column=25,columnspan=20)
tk.Label(main, text='Day: ', font=500).grid(row=2, column=30)
tk.Label(main, text='{}'.format(d['day']), font=500).grid(row=2, column=31)
tk.Label(main, text='Time:', font=500).grid(row=2, column=40)
tk.Label(main, text=f'{now}', font=500).grid(row=2, column=41)
tk.Label(main, text='Name: ', font=500).grid(row=3, column=30)
text1=tk.Entry(main, width=20)
text1.grid(row=3,column=31)
tk.Label(main, text='Roll No: ', font=500).grid(row=3, column=40)
text2=tk.Entry(main, width=20)
text2.grid(row=3,column=41)
tk.Label(main, text='Todays menu: ', font=1500).grid(row=4, column=30)
tk.Label(main, text='Apetite: ', font=1500).grid(row=4, column=40)
tk.Label(main, text='Main Dish: ', font=500).grid(row=5, column=30)
tk.Label(main, text='{}'.format(d['main_dish']), font=500).grid(row=5, column=31)
scale1 = tk.Scale(main,orient = 'horizontal',from_=0,to=5)
scale1.grid(row=5,column=40)
tk.Label(main, text='Side Dish 1:', font=500).grid(row=6, column=30)
tk.Label(main, text='{}'.format(d['side_dish1']), font=500).grid(row=6, column=31)
scale2 = tk.Scale(main,orient = 'horizontal',from_=0,to=5)
scale2.grid(row=6,column=40)
tk.Label(main, text='Side Dish 2:', font=500).grid(row=7, column=30)
tk.Label(main, text='{}'.format(d['side_dish2']), font=500).grid(row=7, column=31)
scale3 = tk.Scale(main,orient = 'horizontal',from_=0,to=5)
scale3.grid(row=7,column=40)
tk.Label(main, text='Side Dish 3:', font=500).grid(row=9, column=30)
tk.Label(main, text='{}'.format(d['side_dish3']), font=500).grid(row=9, column=31)
scale4 = tk.Scale(main,orient = 'horizontal',from_=0,to=5)
scale4.grid(row=9,column=40)
tk.Label(main, text='Special Dish:', font=500).grid(row=11, column=30)
tk.Label(main, text='{}'.format(d['spl_dish']), font=500).grid(row=11, column=31)
scale5 = tk.Scale(main,orient = 'horizontal',from_=0,to=5)
scale5.grid(row=11,column=40)
tk.Label(main, text='                                     ', font=500).grid(row=13, column=40)
tk.Label(main, text='Have a great day!!!', font=500).grid(row=14, column=35)
tk.Label(main, text='                                     ', font=500).grid(row=15, column=40)
tk.Label(main, text='                                     ', font=500).grid(row=16, column=40)
button3 = tk.Button(main, text='SUBMIT', width=25, command=getvalues)
button3.grid(row=17, column=35)

transfer()


