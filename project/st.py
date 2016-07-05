#!/usr/bin/python
import cgi
import cgitb
import os,commands
print "Content-type:text/html"

print ""
cgitb.enable()
x=cgi.FieldStorage()
#print x
user=x.getvalue('uname')
size=x.getvalue('size')



print """
<html>
<head>
	<style type='text/css'>
	   #header
		{
			border:2px solid blue;
			position:absolute;
			top:0px;
			left:0px;
			width:100%;
			height:70px;
			border-radius:10px 10px 10px 10px;
			margin:0px;
			text-align:center;	
			z-index:0;
			color:white;
			background-image:url('/a.png');
			//background-color:#A52A2A;
		}
	    #lvcreate 
		{
			border:2px solid blue;
			position:absolute;
			top:90px;
			left:300px;
			width:500px;
			height:300px;
			border-radius:10px 10px 10px 10px;
			margin:0px;
			//text-align:center;	
			z-index:0;
			color:black;
			//background-image:url('/a.png');
			//background-color:#A52A2A;
		}
	   #output
		{
			border:2px solid blue;
			position:absolute;
			top:90px;
			left:800px;
			width:500px;
			height:300px;
			border-radius:10px 10px 10px 10px;
			margin:0px;
			//text-align:center;	
			z-index:0;
			color:black;
			//background-image:url('/a.png');
			//background-color:#A52A2A;
		}
	  #menu
		{	border:2px solid blue;
			position:absolute;
			left:0px;
			top:70px;
			height:73%;
			width:250px;
			text-align:center;
		}
	  #btm
		{
			width:150px;
			height:40px;
			border-radius:10px;
			background-image:url('/b.jpg');
			color:white;
			font-style:italic;
			font-weight:bold;
			font-size:30px;
		}
	</style>
	<script> 
		
	</script>	
</head>
	
<body>
	    <div id='header'>
		header
		
	    </div>
		
	   <div id='footer'>
		footer
		
	    </div>
	   <div id='menu'>
		<form ><br/><br/>
			<input type='button' id='btm' value='STAAS'/><br/><br/>
			<input type='button' id='btm'  value='SAAS'/><br/><br/>
			<input type='button' id='btm'  value='IAAS'/><br/><br/>
			<input type='button' id='btm'  value='CAAS'/><br/><br/>
			<input type='button' id='btm'  value='PAAS'/><br/>
			
		</form>
	   </div>
	<div id='lvcreate'>
	<form action='' method='get'>
		username :<input type='text' name='uname'/><br/>
		size   :<input type='text' name='size'/>
		<input type='submit'/>
	</form>	
	</div>
	<div id='output'>
"""
if user!=None and size!=None:
	print user
	print size

print """
	</div>
	
</body>

</html>

"""


