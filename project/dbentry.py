#!/usr/bin/python
import cgitb
import cgi
import MySQLdb as mariadb
print "Content-type:text/html"

print ""
cgitb.enable()
x=cgi.FieldStorage()
mariadb_connection=mariadb.connect(user='root')
cursor=mariadb_connection.cursor()

name=x.getvalue('name')
uname=x.getvalue('uname')
password=x.getvalue('password')
passwordc=x.getvalue('passwordw')
email=x.getvalue('email')
gender=x.getvalue('gender')
phone=x.getvalue('phone')
utype=x.getvalue('utype')
address=x.getvalue('address')
print  name 
print uname
print password
print email
print gender
print phone
print utype
print address 

cursor.execute("use cloudlogin")
print "done"
cursor.execute("insert into login (name,userid,gender,email,password,phone_no,address,usertype)values('name','uname','gender','email','password','phone','address','utype');")
#cursor.execute("desc login")
print "don12"
for dbs in cursor:
	a=dbs
	print a




