import random;
import calendar;
import time;
import thread;
import random;
from Tkinter import *
import tkMessageBox;

root=Tk()
root.title("give me a number from 0 < 100 ?")
root.geometry("500x300")
iiput=Text(root)
t=StringVar()
c=StringVar()
nn=StringVar()

def checkers():
    n=eval(c.get())
    mmm=eval(nn.get())
    getn=eval(iiput.get("1.0",END))
    if n < 10:
        if getn > mmm:
            root.title("number big ;give me a number from 0 < 100 ?")
        if getn < mmm:
            root.title("number lower ;give me a number from 0 < 100 ?")
        if getn == mmm:
            root.title("you win trys:"+c.get())
            c.set("12")
            
        n=n+1
        c.set(str(n))
        if n > 9:
            root.title("you lose trys:"+c.get())
    return 

t.set("")
c.set("0")
nn.set(str(random.randrange(1,50,1)))
cmd=Button(root,text="ok",command=checkers)
iiput.width=3
iiput.height=1
iiput.insert(INSERT,"50")
cmd.pack()
iiput.pack()   
root.mainloop()            
