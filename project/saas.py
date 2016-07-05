#!/usr/bin/python2

import cgi
import cgitb
import os,commands

print "content-type:text/html"

print ""

cgitb.enable()
x=cgi.FieldStorage()
#print x
user=x.getvalue('uname')
vall=x.getvalue('size')
print user
print vall




print """

<!DOCTYPE>
<html>

<body>
<form action=""> 
user name :<input type="text" name="uname" />
Enter size not more than 12288 MB(in MB's):<input type="text" name="size"/>
<input type="submit">
</form>
</body>
</html>


"""
