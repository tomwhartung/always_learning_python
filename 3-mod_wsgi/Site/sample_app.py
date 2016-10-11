#
# Sample app from:
#   https://modwsgi.readthedocs.io/en/develop/user-guides/quick-configuration-guide.html
#
# Using this to test our mod_wsgi install
#

##
#  This function must be named "application,"
#  (unless you want to change the wsgi configuration).
#
def application(environ, start_response):
   status = '200 OK'
   output = b'Hello world from Site/sample_app.py !'

   response_headers = [('Content-type', 'text/plain'),
                       ('Content-Length', str(len(output)))]
   start_response(status, response_headers)

   return [output]

