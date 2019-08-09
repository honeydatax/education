import os
from Tkinter import *

t=1
root=Tk()
root.title("Shell")
root.geometry("500x300")
frame=Frame(root)
frame2=Frame(root)
global ss
ss=StringVar()
ss.set(" ")
iiput=Text(frame2)
iiput2=Entry(frame)


def ups():
    dos=os.system(iiput2.get()+ " > shell.dat")
    f= open("shell.dat", "r+")
    s= f.read()
    f.close
    iiput.insert(INSERT,s)
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
sups=Button(frame,text="shell",command=ups)
sups.pack(side =LEFT) 
iiput2.pack(side =LEFT) 
iiput.pack(side =BOTTOM) 
root.mainloop()            
t=0



















