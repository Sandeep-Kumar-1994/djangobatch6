from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun(request):
	return HttpResponse("27.56")

def fun1(request):
	resp ="""<!DOCTYPE html>
<html>
<title>
	title tag information
</title>
<head>
	Sandeep
</head><br/>
<!-- <body bgcolor = "crimson">-->	
	<h1>hello everybody</h1>
	<h2>hello everybody</h2>
	<h3>hello everybody</h3>
	<h4>hello everybody</h4>
	<h5>hello everybody</h5>
	<a href="www.google.com">Google</a>
    <form>
    	Name<input type = "text"></input><br>
    	Male<input type = "radio"></input><br>
    	Female<input type = "checkbox"></input><br>
    	Password<input type = "password"></input><br>
    	Address:<textarea></textarea><br>
    	<br>
    	Cousrse know:<select>
    		<option>Python</option>
    		<option>Java</option>
    		<option>C</option>
    		<option>C++</option>
    	</select><br>
    	Submit<input type = "submit"></input>
    </form>
</body>
</html>"""
	return HttpResponse(resp)

def fun2(request):
    return render(request,"cooling/index.html")
	

