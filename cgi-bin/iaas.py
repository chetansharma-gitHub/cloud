#!/usr/bin/python
import cgitb
import cgi
import os,commands

print "Content-type:text/html"

print ""

cgitb.enable()
x=cgi.FieldStorage()
#print x
cmd=x.getvalue('uname')

print """



<html>
<head>
	<style>
	   #header
		{
			border:2px solid blue;
			position:absolute;
			top:0px;
			left:0px;
			width:100%;
			height:70px;
			border-radius:10px 40px 10px 40px;
			margin:0px;
			text-align:center;	
		}
	   #slidder
		{
			border:2px solid blue;
			position:absolute;
			top:72px;
			left:0px;
			width:80%;
			height:400px;
			border-radius:40px;
			margin:0px;
			text-align:center;	
		}
	   #slidder
		{
			border:2px solid blue;
			position:absolute;
			top:72px;
			left:0px;
			width:80%;
			height:425px;
			border-radius:40px;
			margin:0px;
			text-align:center;	
		}
	   #login
		{
			border:2px solid blue;
			position:absolute;
			top:72px;
			left:80%;
			width:20%;
			height:425px;
			border-radius:40px;
			margin:0px;
			text-align:center;	
		}
	 #footer
		{
			border:2px solid blue;
			position:absolute;
			top:500px;
			left:0px;
			width:100%;
			height:80px;
			//border-radius:40px;
			margin:0px;
			text-align:center;	
		}	
		
	</style>	
</head>
	
<body>


	    <div id='header'>
		<form action="">
			user name :<input type="text" name="uname"/>
			storage  :<input type="number" name="stroage"/>
			<input type="submit"/>
		</form>
	    </div>
	    <div id='slidder'>
"""
if cmd!=None:
	print cmd
	print "condition true"	
	cmd="sudo "+cmd
	#cmd1=x.getvalue('uname')
	#print cmd
	print commands.getstatusoutput(cmd)[1]
	print list[:]

print """		
	    </div>
	    <div id='login'>
		
		
	    </div>
	   <div id='footer'>
		footer
		
	    </div>

</body>

</html>

"""
