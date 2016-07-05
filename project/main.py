#!/usr/bin/python
import cgi
print "Content-type:text/html"

print ""




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
	   #loginf
		{
			//border:2px solid red;
			position:absolute;
			top:10px;
			left:63%;
			width:490px;
			height:40px;
			border-radius:10px;
			margin:0px;
			text-align:center;
			z-index:1;
			color:white;	
		}
	   #slidder1,#slidder2,#slidder3,#slidder4,#slidder5
		{
			//border:2px solid blue;
			position:absolute;
			top:72px;
			left:0px;
			width:100%;
			height:425px;
			border-radius:20px;
			margin:0px;
			text-align:center;	
			//background-color:red;
		}
	   
	   #login
		{
			//border:2px solid blue;
			position:absolute;
			top:72px;
			left:70%;
			width:27%;
			height:385px;
			border-radius:40px;
			margin:0px;
			visibility:hidden;
			opacity:0;
			//text-align:center;	
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
	#inbox
		{
			width:100px;
			height:25px;
		}
	#bt     
		{	 
			width:60px;
			
		}
	#btm
		{
			width:150px;
			height:50px;
			border-radius:10px;
			background-image:url('/b.jpg');
			color:white;
			font-style:italic;
			font-weight:bold;
			font-size:40px;
		}	
	fieldset
		{
			border-radius:10px;
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
	
</body>

</html>

"""
