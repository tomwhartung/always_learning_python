"""seeourminds URL Configuration

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
## Commenting out the generated code
##
# from django.conf.urls import url
# from django.contrib import admin
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
##
## Adding in the code from:
##    http://dfpp.readthedocs.io/en/latest/chapter_01.html
## Notes:
##    (1) Updated "from..." statement to fix import error ("cannot import name 'patterns'")
##       Reference: http://stackoverflow.com/questions/8074955/cannot-import-name-patterns
##    (2) Changed "hello.urls" to "home.urls"
##
## from django.conf.urls import patterns, include, url
from django.conf.urls import *

##
## Adding more urls, inspired by the "Write your first view" section in:
##    https://docs.djangoproject.com/en/1.10/intro/tutorial01/
##
urlpatterns = [
    url(r'', include('home.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^index/', include('home.urls')),
]

