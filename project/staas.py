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

if user!=None and vall!=None:
		print "<pre>"		
		commands.getstatusoutput("sudo echo -e 'y\n'|sudo lvcreate --size {}M --name {}lv staasvg".format(vall,user))[1]
		commands.getstatusoutput("sudo mkfs.ext4 /dev/staasvg/{}lv".format(user))
		commands.getstatusoutput("sudo mkdir /cloud/{}".format(user))
		commands.getstatusoutput("sudo mount /cloud/{0} /dev/staasvg/{0}lv".format(user))
		commands.getstatusoutput("sudo iptables -F")
		commands.getstatusoutput("setenforce 0")
		print commands.getstatusoutput("sudo chown {0} /cloud/{0}".format(user))
		print commands.getstatusoutput("sudo chmod 700 /cloud/{0}".format(user))
		print commands.getstatusoutput("sudo systemctl restart sshd")
		print commands.getstatusoutput('sudo touch /var/www/cgi-bin/client.py')
		print commands.getstatusoutput('sudo chmod 777 /var/www/cgi-bin/client.py')
		fi=open('client.py','a')
		fi.write("#!/usr/bin/python2\n")
		fi.write("import commands\n")
		fi.write("commands.getstatusoutput(\"yum install fuse-sshfs\")\n")
		fi.write("commands.getstatusoutput(\"systemctl restart sshd\")\n")
		fi.write("commands.getstatusoutput(\"mkdir /media/mycloud\")\n")
		c="commands.getstatusoutput(\"echo -e \'redhat\\n\'| sshfs -o password_stdin chetan@192.168.43.179:/cloud/chetan /media/mycloud \")"
		fi.write(c)
		fi.close()
		commands.getstatusoutput("sudo tar -cf client.tar.gz client.py")		
		commands.getstatusoutput("sudo mv /var/www/cgi-bin/client.tar.gz /var/www/html/")		
		commands.getstatusoutput("sudo rm /var/www/cgi-bin/client.py")
		print "<a href='http://192.168.43.179/client.tar.gz'>dd</a>"		
		print "</pre>"	
		print 'successfully done'

		
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
