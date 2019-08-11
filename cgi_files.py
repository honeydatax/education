#!/usr/bin/python
import sys;
import os;

def head():
    print "Content-type:text/txt\r\n\r\n"
    return

def tail():
    print ("\n text web server python ....")
    return

def body():
    dos=os.system("ls  > shell.dat")
    f= open("shell.dat", "r+")
    s= f.read()
    f.close
    print (s)


head()
body()
tail()
