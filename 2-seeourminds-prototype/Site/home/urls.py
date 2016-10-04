##
## From the Writing the code section of
##    http://dfpp.readthedocs.io/en/latest/chapter_01.html
##
## Updated to fix import error ("cannot import name 'patterns'")
## Reference: http://stackoverflow.com/questions/8074955/cannot-import-name-patterns
##
## from django.conf.urls import patterns, url
from django.conf.urls import *

from home.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
]

