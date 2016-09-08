"""say_hi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
##
## Merging in code from the "Edit urls.py" section of the "bogo" tutorial
## ----------------------------------------------------------------------
## Reference:
##    http://www.bogotobogo.com/python/Django/Python_Django_hello_world.php
## 
## from django.conf.urls import url
## from django.contrib import admin
## 
## urlpatterns = [
##     url(r'^admin/', admin.site.urls),
## ]
## 
##
## From "Edit urls.py" section of the "bogo" tutorial
##    http://www.bogotobogo.com/python/Django/Python_Django_hello_world.php
## NOTES:
##    1) The use of "patterns" will cause an error (as we learned from the "dfpp" tutorial)
##       -> Keep the import for django.conf.urls above and comment out the one from the tutorial
##    2) The tutorial named the app "HelloWorldApp" but ours is called "hello_bogo"
##       -> Change the tutorial code as appropriate
##
## from django.conf.urls import patterns, include, url
from django.conf.urls import *
from hello_bogo.views import foo

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'HelloWorld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'hello_bogo/$', foo),
]

