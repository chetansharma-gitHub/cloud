#!/usr/bin/python
import cgi
print "Content-type:text/html"

print ""




print """


<html>
<head>
	<style>
	   #header
		{
			//border:2px solid blue;
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
	   #login
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
			//background-image:url('/c.png');	
			//background-color:red;
		}
	   #fullslidder
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
			#background-image:url('/c.png');	
			z-index:-1;
			//background-color:red;
		}
	   
	   #signup
		{
			//border:2px solid blue;
			position:absolute;
			top:72px;
			left:70%;
			width:30%;
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
	fieldset
		{
			border-radius:10px;
		}	
	#div1   {
			border:2px solid blue;
			position:relative;
			left:5%;
			top:20%;
			width:10%;
			height:25%;
			border-radius:30px;
			transform: rotate(+45deg);		
			z-index:1;

		}
	#div2   {
			border:2px solid blue;
			position:relative;
			left:25%;
			top:50%;
			width:10%;
			height:25%;
			border-radius:30px;
			transform: rotate(+45deg);
			z-index:1;

		}
	#div3   {
			border:2px solid blue;
			position:relative;
			left:45%;
			top:20%;
			width:10%;
			height:25%;
			border-radius:30px;
			transform: rotate(+45deg);
			z-index:1;

		}
	#div4   {
			border:2px solid blue;
			position:relative;
			left:65%;
			top:50%;
			width:10%;
			height:25%;
			border-radius:30px;
			transform: rotate(+45deg);
			z-index:1;

		}
	#div5   {
			border:2px solid blue;
			position:relative;
			left:85%;
			top:20%;
			width:10%;
			height:25%;
			border-radius:30px;
			transform: rotate(+45deg);
			z-index:1;
			text-transform:rotate(-45deg);
		}
	#div2:hover
		{
			width:15%;
		}
	</style>
	<script> 
		function loginshow()
			{
				//alert('ok');
					
				document.getElementById('slidder1').style.width='70%';
				document.getElementById('slidder1').style.transition='width 1s';
				document.getElementById('slidder2').style.width='70%';
				document.getElementById('slidder2').style.transition='width 1s';
				document.getElementById('slidder3').style.width='70%';
				document.getElementById('slidder3').style.transition='width 1s';
				document.getElementById('slidder4').style.width='70%';
				document.getElementById('slidder4').style.transition='width 1s';
				document.getElementById('slidder4').style.width='70%';
				document.getElementById('slidder4').style.transition='width 1s';
				document.getElementById('slidder5').style.width='70%';
				document.getElementById('slidder5').style.transition='width 1s';
				
				//document.getElementById('login').style.opacity='1';
				var a=0;
				//var d=new Date();
				var ss=new Date().getSeconds();
				/*alert('ok');
				if(ss<55)
					ss=ss+2;
				else
					ss=0;
				while(a==0) 
				{
					s=new Date().getSeconds();
					if(s==ss)
					    break;
				}*/
				document.getElementById('signup').style.visibility='visible';
				document.getElementById('signup').style.opacity='1';
				document.getElementById('signup').style.transition='opacity 4s';
				
	
				
	
			}
	</script>	
</head>
	
<body>
	    <div id='header'>
		header
		
	    </div>
		
	    <div id='slidder1'>
		slidder
		<div id='div1'>1</div>
	    </div>
	    <div id='slidder2'>	
		slidder
	    	<div id='div2'> 2</div>
	    </div>
	    <div id='slidder3'>	
	    <div id='div3'> 3</div>
	    </div>
	     <div id='slidder4'>	
	    <div id='div4'> 4</div>
	    </div>
	     <div id='slidder5'>	
	    <div id='div5'> 5</div>
	    </div>
	    <div id='signup'>
		<form action='dbentry.py'>
			<fieldset><legend>sign-up</legend>
			<br/>
			name : <input type='text' id='in' name='name'/><br/>
			username:<input type='text' id=in' name='uname'/><br/>
			password:<input type='password' id='in' name='password'/><br/>
			confirm password:<input type='password' id='in' name='passwordc'/><br/>
			email:<input type='email' name='email' id='in'/><br/>
			gender: <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
			Male &nbsp;: <input type='radio' name='gender' value='Male'/>
			Female:<input type='radio' name='gender' value='Female'/><br/><br/>
			phone_no:<input type='number' length='3' name='phone' id='in'/><br/>
			usertype:<input type='text' name='utype' id='in' /><br/>
			address :<input type='textarea' name='address' id='in' maxlength='50'/><br/>
			<input type='submit'/></fieldset>
		</form>
		
	    </div>
	   <div id='footer'>
		footer
		
	    </div>
	    <div id='login'>
		<form action='dbcheck.py' method='post'>
			username : <input type='text' id='inbox' name='uname '/> 
			password : <input type='password' id='inbox' name='pass'/>
			<input type='submit' id='bt' value='login'/>
			<input type='button' id='bt' value='signup' onclick='loginshow()'/>
		</form>
	    </div>
	    <div id='fullslidder'>
	    </div>	
</body>

</html>

"""
