import random;
import calendar;
import time;
from Tkinter import *
import tkMessageBox;

root=Tk()

s="calandar \n"
ss=StringVar()

s = s + calendar.month(time.localtime(time.time())[0],time.localtime(time.time())[1]) +"\n\n     "
    
ss.set(s)
label=Label(root,textvariable=ss,font="mono",justify="left")
label.pack()
root.mainloop()            
            
