#!/usr/bin/python

print "Content-type:text/html"

print ""

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
		header
		
	    </div>
	    <div id='slidder'>
		slidder
		
	    </div>
	    <div id='login'>
		login
		
	    </div>
	   <div id='footer'>
		footer
		
	    </div>
</body>

</html>

"""
