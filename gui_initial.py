import tkinter as tk #pip install tk
import time
import tkinter.messagebox as tkm 
from PIL import ImageTk , Image #pip install pillow
import csv


#WRITING IN A CSV FILE
f = open('dinner.csv','w')
writer = csv.writer(f)
writer.writerow(["day","main_dish","side_dish1","side_dish2","side_dish3","spl_dish"])
writer.writerow(["monday","kal dosai","sambar","chutney","pickle","badam milk"])
writer.writerow(["tuesday","chappati","mushroom gravy","dhall","pickle","lemon juice"])
writer.writerow(["wednesday","chicken biriyani","chicken kuruma","chicken 65","onion raitha","icecream"])
writer.writerow(["thursday","kal dosai","sambar","chutney","pickle","badam milk"])
writer.writerow(["friday","chappati","mushroom gravy","dhall","pickle","lemon juice"])
writer.writerow(["saturday","chicken biriyani","chicken kuruma","chicken 65","onion raitha","icecream"])
writer.writerow(["sunday","chicken biriyani","chicken kuruma","chicken 65","onion raitha","icecream"])
f.close()

#retriving data from csv file
f = open('dinner.csv','r')
reader = csv.DictReader(f,delimiter = ',')
local_time = time.localtime(1545925769)
day = local_time.tm_wday
now = time.strftime('%H:%M:%S %p')
d = dict()
i=0
for row in reader:
    d = dict(row)
    if (i==day):
        break
    i+=1
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
text1=tk.Entry(main, width=20)
text1.grid(row=3,column=41)
tk.Label(main, text=f'Todays menu: ', font=1500).grid(row=4, column=30, columnspan=12)
tk.Label(main, text='Main Dish: ', font=500).grid(row=5, column=30)
tk.Label(main, text='{}'.format(d['main_dish']), font=500).grid(row=5, column=31)
tk.Label(main, text='Side Dish 1:', font=500).grid(row=6, column=30)
tk.Label(main, text='{}'.format(d['side_dish1']), font=500).grid(row=6, column=31)
tk.Label(main, text='Side Dish 2:', font=500).grid(row=7, column=30)
tk.Label(main, text='{}'.format(d['side_dish2']), font=500).grid(row=7, column=31)
tk.Label(main, text='Side Dish 3:', font=500).grid(row=9, column=30)
tk.Label(main, text='{}'.format(d['side_dish3']), font=500).grid(row=9, column=31)
tk.Label(main, text='Special Dish:', font=500).grid(row=11, column=30)
tk.Label(main, text='{}'.format(d['spl_dish']), font=500).grid(row=11, column=31)
tk.Label(main, text='Have a great day!!!', font=500).grid(row=13, column=40)
button3 = tk.Button(main, text='SUBMIT', width=25, command=getvalues)
button3.grid(row=7, column=25)

menubar = tk.Menu(main)  
menu = tk.Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='MENU', menu = menu) 
'''quizmenu.add_command(label ='TEACHERS INTERFACE', command = push) 
quizmenu.add_command(label ='STUDENT INTERFACE', command = student)  '''
menu.add_separator() 
menu.add_command(label ='Exit', command = main.destroy)
main.config(menu = menubar) 
tk.mainloop()
