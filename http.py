#!/usr/bin/python
def head():
    print "Content-type:text/html\r\n\r\n"
    print ("<HTML><HEAD><TITLE>PYTHON HTTP SERVER .</TITLE><HEAD><BODY>")
    return

def tail():
    print ("</BODY></HTML>")
    return

def body():
    print ("<H1>HELLO WORLD!</H1>")


head()
body()
tail()
