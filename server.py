#!/usr/bin/python
print "Content-type:text/text\r\n\r\n"
print "python -m CGIHTTPServer 8080"
print "mkdir cgi-bin"
print "chmod 755 cgi-bin/*.py"
print "http://localhost:8080/cgi-bin/server.py"
print "web html server .!"
