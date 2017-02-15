#
# Sample app from:
#   https://modwsgi.readthedocs.io/en/develop/user-guides/quick-configuration-guide.html
#
# Using this to test our mod_wsgi install
#
import sys

##
#  This function must be named "application," (unless you want to change the wsgi configuration).
#  To serve markup instead of text, it turns out we just need to change the Content-type response header
#  To display some interesting values, that may be good for debugging issues some day,
#     see the applicationDebugText function below
#
def application(environ, start_response):
   status = '200 OK'
   markup = '<!doctype html><html>'
   markup += '<head><meta charset="utf-8"></head>'
   markup += '<body><main>'
   markup += '<p>Hello world from Site/sample_app.py !</p>'
   markup += '<p>Python version is: ' + sys.version + '</p>'
   markup += '</main></body></html>'
   output = markup.encode( 'utf-8' )

   response_headers = [('Content-type', 'text/html'),
                       ('Content-Length', str(len(output)))]
   start_response(status, response_headers)

   return [output]

##
#  Found some interesting values that we can print on this page:
#     https://modwsgi.readthedocs.io/en/develop/user-guides/checking-your-installation.html
#  That page and its neighbors contain plenty of helpful trouble-shooting information
#
def applicationDebugText(environ, start_response):
   status = '200 OK'
   text  = 'Hi there, world from Site/sample_app.py !\n\n'
   text += 'The version of python we are using is:\n' + sys.version + '\n\n'
   text += 'sys.path: %s' % repr(sys.path) + '\n\n'
   text += 'sys.prefix: ' + sys.prefix + '\n'
   text += 'wsgi.multithread = %s' % repr(environ['wsgi.multithread']) + '\n'
   text += 'mod_wsgi.process_group = %s' % repr(environ['mod_wsgi.process_group'])
   text += '   ## A blank value for the mod_wsgi.process_group means we are running in embedded mode\n'

   output = text.encode( 'utf-8' )

   response_headers = [('Content-type', 'text/plain'),
                       ('Content-Length', str(len(output)))]
   start_response(status, response_headers)

   return [output]

