import random;
import calendar;
import time;
import thread;
from Tkinter import *
import tkMessageBox;

t=1
root=Tk()
frame=Frame(root)
frame2=Frame(root)
global ss
ss=StringVar()
ss.set(" ")
sbitmaps=Canvas(frame2,bg="blue",height=200,width=500)
iiput=Text(root)
ball=sbitmaps.create_oval(0,0,20,20,fill="red")

def checkers():
    x=0
    y=0
    while t > 0:
        if ss.get() != " ":
            if ss.get() == "a":
                if y > 9:
                    sbitmaps.move(ball,0,-8)
                    y=y-8
            if ss.get() == "b":
                if x > 9:
                    sbitmaps.move(ball,-8,0)
                    x=x-8
            if ss.get() == "c":
                if x < 480:
                    sbitmaps.move(ball,8,0)
                    x=x+8
            if ss.get() == "d":
                if y < 180:
                    sbitmaps.move(ball,0,8)
                    y=y+8
        ss.set(" ")
  
        time.sleep(1)
    print "exit timer"
    return 

def ups():
    ss.set("a")
    return 

def lefts():
    ss.set("b")
    return 

def rigs():
    ss.set("c")
    return 

def downs():
    ss.set("d")
    return 


frame.pack()
frame2.pack(side =BOTTOM)
sups=Button(frame,text="up",command=ups)
slefts=Button(frame,text="<",command=lefts)
srigs=Button(frame,text=">",command=rigs)
sdowns=Button(frame,text="down",command=downs)
sups.pack(side =LEFT) 
slefts.pack(side =LEFT) 
srigs.pack(side =LEFT)
sdowns.pack(side =LEFT)
sbitmaps.pack(side =BOTTOM) 
thread.start_new_thread(checkers,())
root.mainloop()            
t=0
time.sleep(3)
print "exit program"    


















