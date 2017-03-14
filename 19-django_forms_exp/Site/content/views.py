from django.shortcuts import render
import textwrap

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.template import loader
import json
import os

##
# load and render the Home page template
#
def home(request):
  context_home_selected = 'selected'
  template = loader.get_template('content/home.html')
  context = {
    'context_home_selected': context_home_selected,
  }
  return HttpResponse(template.render(context, request))

##
# load and render the Galleries page template
#
def galleries(request):
  context_galleries_selected = 'selected'
  template = loader.get_template('content/galleries.html')
  context = {
    'context_galleries_selected': context_galleries_selected,
  }
  return HttpResponse(template.render(context, request))

##
# load and render the template for a single Gallery page
#
def gallery(request, gallery_name='all'):
  context_gallery_name = gallery_name
  site_content_dir = os.path.abspath(os.path.dirname(__file__))
  data_file_name = gallery_name + '.json'
  data_file_path = site_content_dir + '/static/content/json/galleries/' + data_file_name
  gallery_json_file = open( data_file_path )
  gallery_json_string = gallery_json_file.read()
  gallery_json_file.close()
  gallery_dictionary = json.loads(gallery_json_string)
  name_of_gallery = gallery_dictionary['name_of_gallery']
  description_of_gallery = gallery_dictionary['description_of_gallery']
  image_file_dir = 'content/images/galleries/' + gallery_name + '/'
  image_list = gallery_dictionary['image_list']
  image_list_with_path = []
  for img in image_list:
    img_to_add = img
    img_to_add['image_file_path'] = image_file_dir + img['image_file_name']
    image_list_with_path.append( img_to_add )
  row_separator_markup = "\n</div><!-- .row -->\n<div class='row'>\n"
  template = loader.get_template('content/gallery.html')
  context = {
    'name_of_gallery': name_of_gallery,
    'description_of_gallery': description_of_gallery,
    'image_file_dir': image_file_dir,
    'data_file_path': data_file_path,
    'image_list_with_path': image_list_with_path,
    'row_separator_markup': row_separator_markup,
  }
  return HttpResponse(template.render(context, request))

##
# load and render the Quiz page template
#
def quiz(request):
  context_quiz_selected = 'selected'
  template = loader.get_template('content/quiz.html')
  context = {
    'context_quiz_selected': context_quiz_selected,
  }
  return HttpResponse(template.render(context, request))

##
# load and render the google verification template
#
def google_verification(request):
  template = loader.get_template('content/google428ef5aab2bc0870.html')
  context = { }
  return HttpResponse(template.render(context, request))

##
#  Using the Quiz page template to experiment with django forms
#  Reference:
#     https://docs.djangoproject.com/en/1.10/topics/forms/
#
from .forms import NameForm
def quiz_name_form( request ):
   if request.method == 'POST':
      name_form = NameForm( request.POST )
      if name_form.is_valid():
         # process the data in name_form.cleaned_data as required
         your_name = name_form.cleaned_data['your_name']
         print( 'Got your_name:', your_name )
         # redirect to a new URL:
         return HttpResponseRedirect('/quiz/')
   else:
      name_form = NameForm()

   ## return render(request, 'quiz.html', {'name_form': name_form})
   template = loader.get_template('content/quiz.html')
   context = { 'name_form': name_form }
   return HttpResponse(template.render(context, request))

##
#  Experimenting with ContactForm
#  Reference (same as above):
#     https://docs.djangoproject.com/en/1.10/topics/forms/
#
from .forms import ContactForm
def quiz_contact_form( request ):
   if request.method == 'POST':
      contact_form = ContactForm( request.POST )
      if contact_form.is_valid():
         # process the data in contact_form.cleaned_data as required
         subject = contact_form.cleaned_data['subject']
         message = contact_form.cleaned_data['message']
         sender = contact_form.cleaned_data['sender']
         cc_myself = contact_form.cleaned_data['cc_myself']
         print( 'Got subject:', subject )
         print( 'Got message:', message )
         print( 'Got sender:', sender )
         print( 'Got cc_myself:', cc_myself )
         # redirect to a new URL:
         return HttpResponseRedirect('/quiz/')
   else:
      contact_form = ContactForm()

   return render(request, 'content/quiz.html', {'contact_form': contact_form})

##
#  RenewBookForm
#  Reference:
#     https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
#
from .forms import RenewBookForm
def renew_book_librarian(request, pk):
   book_inst=get_object_or_404(BookInstance, pk = pk)

   # If this is a POST request then process the Form data
   if request.method == 'POST':

      form = RenewBookForm(request.POST)    # Create a form instance and populate it with data from the request (binding):

      if form.is_valid():
         ## # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
         ## book_inst.due_back = form.cleaned_data['renewal_date']
         ## book_inst.save()
         print( "form.cleaned_data['renewal_date']", form.cleaned_data['renewal_date'] )

         ## # redirect to a new URL:
         ## return HttpResponseRedirect(reverse('all-borrowed') )
         return HttpResponseRedirect('/quiz/')

   #  If this is a GET (or any other method) create the default form.
   else:
      proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
      form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

   return render(request, 'content/book_renew_librarian.html', {'form': form})
