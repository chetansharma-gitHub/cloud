#!/usr/bin/python2
print "content-type:text/html"
print 
import cgi
import commands
user=cgi.FormContent()['user'][0]
vall=cgi.FormContent()['size'][0]
x=commands.getstatusoutput("sudo echo -e 'y\n'| sudo lvcreate --size "+vall+"M --name "+user+"lv staasvg")

print x[1]
	
