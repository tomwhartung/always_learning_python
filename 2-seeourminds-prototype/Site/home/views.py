from django.shortcuts import render

# Create your views here.

##
## From the Writing the code section of
##    http://dfpp.readthedocs.io/en/latest/chapter_01.html#writing-the-code
##
import textwrap

from django.http import HttpResponse
from django.views.generic.base import View


class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>SeeOurMinds.com</title>
            </head>
            <body>
                <h1>Welcome!</h1>
                <p>Welcome to SeeOurMinds.com!</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)

