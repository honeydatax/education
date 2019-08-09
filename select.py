import time;
import os;
from Tkinter import *

root=Tk()
root.title("files")
lists=Listbox(root)
n=0
dos=os.system("ls > out.txt")
f= open("out.txt", "r+")
s= f.read()
f.close
list1=s.split()
ss=""
for ls in list1:
    ss=str(n)+"   "+ls
    lists.insert (n,ss)
    n=n+1

lists.pack()   
root.mainloop()            











