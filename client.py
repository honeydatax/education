import os
from Tkinter import *

t=1
root=Tk()
root.title("add client")
root.geometry("500x300")
frame=Frame(root)
frame2=Frame(root)
global ss
ss=StringVar()
ss.set(" ")
iiput=Text(frame2)
iiput2=Entry(frame)


def ups():
    s=iiput2.get()+"\n"
    iiput.insert(INSERT,s)
    f= open("client.dat", "a")
    f.write(s)
    f.close
    return 


iiput.width=3
iiput.height=1
iiput2.width=3
iiput2.height=1
frame.pack()
frame.width=500
frame.height=80
frame2.pack(side =BOTTOM)
frame2.width=500
frame2.height=200
sups=Button(frame,text="calc",command=ups)
sups.pack(side =LEFT) 
iiput2.pack(side =LEFT) 
iiput.pack(side =BOTTOM)
s=""
try:
    f= open("client.dat", "r+")
    s= f.read()
    f.close
except IOError:
    f= open("client.dat", "w")
    f.close

iiput.insert(INSERT,s)
root.mainloop()            
t=0



















