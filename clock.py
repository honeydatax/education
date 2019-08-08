import random;
import calendar;
import time;
import thread;
from Tkinter import *
import tkMessageBox;

t=1
root=Tk()
ss=StringVar()
ss.set("time:                       ")
label=Label(root,textvariable=ss,font="mono",justify="left").pack()

def checkers():
    while t > 0:
        s="time: "
        s = s + str(time.localtime(time.time())[3])+":"+str(time.localtime(time.time())[4])+":"+str(time.localtime(time.time())[5])
        ss.set(s)
        time.sleep(1)
    print "exit timer"
    return 


   
thread.start_new_thread(checkers,())
root.mainloop()            
t=0
time.sleep(3)
print "exit program"    
