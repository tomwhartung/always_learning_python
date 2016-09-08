##
## From the Writing the code section of
##    http://dfpp.readthedocs.io/en/latest/chapter_01.html
##

from django.conf.urls import patterns, url

from hello.views import HomePageView

urlpatterns = patterns(
    '',

    url(r'^$', HomePageView.as_view(), name='home'),
)

