##
# From about 1/3 the way down on this page:
#   https://code.tutsplus.com/tutorials/an-introduction-to-pythons-flask-framework--net-28822
# Added more code from the second page of the tutorial:
#   https://code.tutsplus.com/tutorials/intro-to-flask-adding-a-contact-page--net-28982
#
from flask import Flask, render_template, request, flash
from forms import ContactForm

app = Flask(__name__)
#
# Update the app's configuration for CSRF prevention
#
app.secret_key = 'development key'

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route( '/contact', methods=['GET', 'POST'] )
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      return 'Form posted.'
  elif request.method == 'GET':
    return render_template('contact.html', form=form)

  return 'Request.method not equal to "POST" nor "GET" .'

if __name__ == '__main__':
  app.run(debug=True)
