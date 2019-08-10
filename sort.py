import os
from Tkinter import *

t=1
root=Tk()
root.title("file name to short ?:sample client.dat")
root.geometry("640x350")
frame=Frame(root)
frame2=Frame(root)
global ss
ss=StringVar()
ss.set(" ")
iiput=Text(frame2)
iiput2=Entry(frame)


def ups():
    s=iiput2.get()
    f= open(s, "r+")
    ss=f.read()
    f.close
    list1=ss.split("\n")
    list1.sort()
    for ls in list1:
            sss=ls + "\n"
            iiput.insert(INSERT,sss)



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
root.mainloop()            
t=0



















