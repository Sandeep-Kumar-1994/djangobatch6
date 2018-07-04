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
         

           
