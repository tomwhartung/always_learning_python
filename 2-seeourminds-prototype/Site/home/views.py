from django.shortcuts import render

# Create your views here.

##
## From the Writing the code section of
##    http://dfpp.readthedocs.io/en/latest/chapter_01.html#writing-the-code
##
import textwrap

from django.http import HttpResponse
from django.views.generic.base import View

##
## From part 1 of the polls tutorial; the simplest view:
## Reference: "Write your first view" section
##    https://docs.djangoproject.com/en/1.10/intro/tutorial01/
## Runs when we access:
##    http://127.0.0.1:8000/index
##
def index(request):
    return HttpResponse("Hello from the index function in home/views.py .")

##
## From the "dfpp" tutorial, with the html5boilerplate code pasted in:
## -> Html5boilerplate code loads ok but it cannot find css and js files
##
class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
<!doctype html>
<html class="no-js" lang="">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link rel="stylesheet" href="css/normalize.min.css">
        <link rel="stylesheet" href="css/main.css">

        <script src="js/vendor/modernizr-2.8.3-respond-1.4.2.min.js"></script>
    </head>
    <body>

        <div class="header-container">
            <header class="wrapper clearfix">
                <h1 class="title">h1.title</h1>
                <nav>
                    <ul>
                        <li><a href="#">nav ul li a</a></li>
                        <li><a href="#">nav ul li a</a></li>
                        <li><a href="#">nav ul li a</a></li>
                    </ul>
                </nav>
            </header>
        </div>

        <div class="main-container">
            <div class="main wrapper clearfix">

                <article>
                    <header>
                        <h1>abfab h1</h1>
                        <p>Say hi to the visitors, sweetie dahrlin!</p>
                    </header>
                </article>
            </div><!-- .main .wrapper .clearfix -->
        </div><!-- .main-container -->

    </body>
</html>
        ''')
        return HttpResponse(response_text)

