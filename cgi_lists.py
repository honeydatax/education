#!/usr/bin/python
import sys;
import os;

def head():
    print "Content-type:text/html\r\n\r\n"
    print ("<HTML><HEAD><TITLE>PYTHON HTTP SERVER .</TITLE><HEAD><BODY>file list python server ...<br>")
    return

def tail():
    print ("</BODY></HTML>")
    return

def body():
    n=0
    dos=os.system("ls > out.txt")
    f= open("out.txt", "r+")
    s= f.read()
    f.close
    list1=s.split()
    for ls in list1:
        print str(n)+"_   <a href = '/"+ls+"' target = '_self' >"+ls+"</a><br>"
        n=n+1


head()
body()
tail()
