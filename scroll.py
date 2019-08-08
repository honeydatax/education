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
    sss="                   hello world.                  ";    c=0
    cc=20
    ccc=cc
    cccc=len(sss)
    while t > 0:
        s =sss[c:ccc] 
        ss.set(s)
        time.sleep(1)
        c=c+1
        ccc=c+20
        if ccc > cccc:
            c=0
            ccc=c+20
    print "exit timer"
    return 


   
thread.start_new_thread(checkers,())
root.mainloop()            
t=0
time.sleep(3)
print "exit program"    
