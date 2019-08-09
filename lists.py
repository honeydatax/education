import os

n=0
dos=os.system("ls > out.txt")
f= open("out.txt", "r+")
s= f.read()
f.close
list1=s.split()
for ls in list1:
    print n,ls
    n=n+1
