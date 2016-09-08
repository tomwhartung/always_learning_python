# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

##
## From Edit views.py section of
##    http://www.bogotobogo.com/python/Django/Python_Django_hello_world.php
##
from django.http import HttpResponse
def foo(request):
    return HttpResponse("Hello World!")

