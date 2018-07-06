# djangobatch6
 This is my Django project
 
 Demo class:
     Install Sublime text to work as the editor tow write and work the code.
     Django MVCS structure.Installation of Python and Django and working the commands.
 
 2nd July:
      Creation of a new project using startproject command and new applicatio creation using startapp command and running the server using       the runserver command.
      The reuested url in the browser looks for the url in settings.py under ROOT_URLCONF="ERP.urls".In urls.py it will look for the            function associated with url and call the function that passes the request to the HttpResponse which sends response to the HTML page.
     e.g..
       from django.http import HttpResponse
       def fun(request):
	           #return HttpResponse("Hello django")
             return HttpResponse("<h1>django</h1>")

      urlpatterns = [
            path('admin/', admin.site.urls),
            path('request_url/', fun),
          ]
         
 3rd July:
      Creation of a new project called Datacenter with the application Cooling that displays the temparatuer 27.56 on the page.
      Its a habot to write all the urls in the urls.py so we try to write all the functions in views.py
      In views.py
                 from django.http import HttpResponse
                 def fun(request):
	                         return HttpResponse("25.67")
      To call the function in the urls.py we have to import the function using from cooling.views import fun
      In urls.py:
                 from cooling.views import fun
                 urlpatterns = [
                        path('admin/', admin.site.urls),
                        path('get-temp/', fun)
                  ]
		  
 5th July:
     We write the requester urls in the urls.py page and call the functions necessary written in the views.py.In views.py,all the      
     functions are written with logic.All the content that you want to displayed on the url page can be written in views.py.
     The code is written in HTML and CSS with the help of tags and stylish sheets.The HTML code is written with the hlp of tags like
     title,head,body,from,select,header and anchor tags.All the HTML and CSS code written in var = """ """ and is assigned to a        
     variable.It is returned to the url page with the return statement return HttpResponse(var).When you run the requested url it calls
     the function in views.py page and displays the HTML code on the screen.
     
     
     
     
     
     
     
         

           
