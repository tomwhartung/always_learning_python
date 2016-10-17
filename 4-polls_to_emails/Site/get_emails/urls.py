##
# See https://docs.djangoproject.com/en/1.10/intro/tutorial01/#write-your-first-view
#
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

