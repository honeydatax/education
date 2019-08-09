import os

dos=os.system("ls > out.txt")
f= open("out.txt", "r+")
s= f.read()
f.close
print s
