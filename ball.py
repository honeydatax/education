import random;
import calendar;
import time;
import thread;
from Tkinter import *
import tkMessageBox;

t=1
root=Tk()
ss=StringVar()
ss.set(" ")
sbitmaps=Canvas(root,bg="blue",height=300,width=500)
ball=sbitmaps.create_oval(0,0,20,20,fill="red")

def checkers():
    x=0
    y=0
    xt=8
    yt=8
    while t > 0:
        x=x+xt
        y=y+yt
        if x > 480:
            xt=-8
        if y > 280:
            yt=-8
        if x < 9:
            xt=8
        if y < 9:
            yt=8
        root.title(str(x)+";"+str(y))            
        sbitmaps.move(ball,xt,yt)
        time.sleep(1)
    print "exit timer"
    return 


sbitmaps.pack() 
thread.start_new_thread(checkers,())
root.mainloop()            
t=0
time.sleep(3)
print "exit program"    


















