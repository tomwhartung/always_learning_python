#
# Sample app from:
#   https://modwsgi.readthedocs.io/en/develop/user-guides/quick-configuration-guide.html
#
# Using this to test our mod_wsgi install
#
import sys

##
#  This function must be named "application,"
#  (unless you want to change the wsgi configuration).
#
def application(environ, start_response):
   status = '200 OK'
   text  = 'Hi there, world from Site/sample_app.py , '
   text += 'where the version of python we are using is:\n' + sys.version
   output = text.encode( 'utf-8' )

   response_headers = [('Content-type', 'text/plain'),
                       ('Content-Length', str(len(output)))]
   start_response(status, response_headers)

   return [output]

##
#  Hmm well I thought that having some markup would be preferable to
#  just having "hello world" in bare text - and I was wrong.  Rats!
#
def applicationMarkup(environ, start_response):
   status = '200 OK'
   markup = '<!doctype html><html>'
   markup += '<head><meta charset="utf-8"></head>'
   markup += '<body><main>'
   markup += '<p>Hello world from Site/sample_app.py !</p>'
   markup += '<p>Python version is: ' + sys.version + '</p>'
   markup += '</main></body></html>'
   output = markup.encode( 'utf-8' )

   response_headers = [('Content-type', 'text/plain'),
                       ('Content-Length', str(len(output)))]
   start_response(status, response_headers)

   return [output]

