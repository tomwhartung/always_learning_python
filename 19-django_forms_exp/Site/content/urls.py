#
# urls.py for our content app
#
from django.conf.urls import *

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^galleries$', views.galleries, name='galleries'),
    url(r'^gallery/(?P<gallery_name>\w+)/$', views.gallery, name='gallery'),
    url(r'^quiz$', views.quiz, name='quiz'),
    url(r'^google428ef5aab2bc0870.html$',
      views.google_verification, name='google_verification'),
    #
    # Urls for experimenting with forms
    #
    url(r'^quiz/name_form$', views.quiz, name='quiz_name_form'),
    url(r'^quiz/contact_form$', views.quiz, name='quiz_contact_form'),
]
