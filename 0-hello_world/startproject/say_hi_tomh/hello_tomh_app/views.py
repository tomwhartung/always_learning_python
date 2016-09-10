from django.shortcuts import render

# Create your views here.

##
## From the Writing the code section of
##    http://dfpp.readthedocs.io/en/latest/chapter_01.html
##
import textwrap

from django.http import HttpResponse
from django.views.generic.base import View


class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Tom's Title</title>
            </head>
            <body>
                <h1>Hi there world</h1>
                <p>Hello to the world from Tom H.!</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)

