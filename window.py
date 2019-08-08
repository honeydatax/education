import random;
from Tkinter import *
import tkMessageBox

root=Tk()

s="loto \n"
ss=StringVar()

for n in range (0,10):
    s=s + str(random.randrange(1,50,1))+ " , "
    
ss.set(s)
label=Label(root,textvariable=ss)
label.pack()
root.mainloop()            
            
