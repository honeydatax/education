#!/usr/bin/python
import sys;
import os;

def head():
    print "Content-type:text/txt\r\n\r\n"
    return

def tail():
    print ("\nweb server")
    return

def body():
    dos=os.system("sudo ifconfig -a  > shell.dat")
    f= open("shell.dat", "r+")
    s= f.read()
    f.close
    print (s)


head()
body()
tail()
