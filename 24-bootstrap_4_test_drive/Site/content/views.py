""" views.py for our content app

Purpose: define the views for this app
Author: Tom W. Hartung
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none)
"""

from django.shortcuts import render
import textwrap

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.base import View

from .adsense import adsense_ads
from .forms import QuizForm
from .models import Quiz
from .models import QuizJson


def home(request):

    """ Load and render the Home page template """

    context_home_selected = 'class="disabled"'      # see seeourminds.css
    template = loader.get_template('content/home.html')
    context = {
        'adsense_ads': adsense_ads,
        'context_home_selected': context_home_selected,
    }
    return HttpResponse(template.render(context, request))


def galleries(request):

    """ Load and render the Galleries page template """

    context_galleries_selected = 'class="disabled"'      # see seeourminds.css
    template = loader.get_template('content/galleries.html')
    context = {
        'adsense_ads': adsense_ads,
        'context_galleries_selected': context_galleries_selected,
    }
    return HttpResponse(template.render(context, request))


def gallery(request, gallery_name='all'):

    """ Load and render the template for a single Gallery page """

    import json
    import os
    context_gallery_name = gallery_name
    site_content_dir = os.path.abspath(os.path.dirname(__file__))
    data_file_name = gallery_name + '.json'
    data_file_dir = site_content_dir + '/static/content/json/galleries/'
    data_file_path = data_file_dir + data_file_name
    gallery_json_file = open(data_file_path)
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
        image_list_with_path.append(img_to_add)
    row_separator_markup = "\n</div><!-- .row -->\n<div class='row'>\n"
    template = loader.get_template('content/gallery.html')
    context = {
        'adsense_ads': adsense_ads,
        'name_of_gallery': name_of_gallery,
        'description_of_gallery': description_of_gallery,
        'image_file_dir': image_file_dir,
        'data_file_path': data_file_path,
        'image_list_with_path': image_list_with_path,
        'row_separator_markup': row_separator_markup,
    }
    return HttpResponse(template.render(context, request))


def quiz(request, quiz_size_slug=Quiz.DEFAULT_QUIZ_SIZE_SLUG):

    """ Load and render the Quiz page template """

    if request.method == 'POST':
        quiz_form = QuizForm(quiz_size_slug=quiz_size_slug, data=request.POST)
        if quiz_form.is_valid():
            print('views.quiz() - len(quiz_form.cleaned_data):',
                    len(quiz_form.cleaned_data))
            email = quiz_form.cleaned_data['email']
            if email == '':
                print( 'views.quiz: No email given, not saving quiz')
            else:
                quiz_db = Quiz()
                quiz_db.save_quiz(quiz_form.cleaned_data, quiz_size_slug)
            quiz_json = QuizJson()
            score = quiz_json.score_quiz(quiz_form.cleaned_data)
            four_letter_type = "Type: " + score.as_four_letter_type()
            messages.add_message(request, messages.INFO, four_letter_type)
            score_list = score.as_list_of_pcts_and_counts()
            pcts_and_counts_html = '<ul>'
            for score_pair in score_list:
                pcts_and_counts_html += '<li>'
                for single_score in score_pair:
                    pcts_and_counts_html += single_score + '&nbsp;'
                pcts_and_counts_html += '</li>'
            pcts_and_counts_html += '</ul>'
            messages.add_message(request, messages.INFO, pcts_and_counts_html)
            return HttpResponseRedirect('/quiz/results')
    else:
        quiz_form = QuizForm(quiz_size_slug=quiz_size_slug)

    # context_quiz_selected = 'class="disabled"'  # see seeourminds.css
    # context_quiz_selected = 'class="active"'      # see http://getbootstrap.com/components/#navbar
    quiz_info = {}
    quiz_info["size_abbreviation"] = Quiz.get_quiz_size_abbreviation_for_slug(quiz_size_slug)
    quiz_info["size_text"] = quiz_size_slug
    quiz_info["question_count"] = Quiz.get_question_count_for_slug(quiz_size_slug)
    template = loader.get_template('content/quiz.html')
    context = {
        'adsense_ads': adsense_ads,
        # 'context_quiz_selected': context_quiz_selected,
        'quiz_info': quiz_info,
        'quiz_form': quiz_form
    }
    return HttpResponse(template.render(context, request))


def quiz_results(request):
    """ Render the Quiz results template """
    # quiz_results = request.session['quiz_results']
    quiz_results = 'quiz results here'
    return render(request, 'content/quiz_results.html', {'quiz_results': quiz_results})


def image(request, image_id=0):

    """ Render the single image template """

    try:
        image_id_int = int(image_id)
    except:
        print('views.image: non-numeric "image_id" from url: ' + image_id)
        image_id_int = 0

    image = {}
    image["id"] = image_id_int

    if image_id_int == 0:
        image["name"] = 'Tom H., Creator of SeeOurMinds.com and Groja.com'
        image["path"] = 'content/images/header/infp-tomh_1987-515x515.gif'
        image["description"] = 'The image contains mostly blue and red, ' \
           'indicating I am idealistic and passionate.  ' \
           'There is also plenty of green and yellow, however, indicating ' \
           'I can be logical and down-to-earth when the situation calls ' \
           'for it.' \
           'This is just the sort of person who can both conceive of ' \
           'this idea and follow through and learn the details needed to ' \
           'implement it.'
    else:
        image["name"] = 'image_id_int from url: ' + str(image_id_int)
        image["path"] = 'content/images/header/infp-tomh_1987-515x515.gif'
        image["description"] = 'description goes here'

    return render(request, 'content/image.html',
         {'adsense_ads': adsense_ads,
          'image': image,
         })


def google_verification(request):

    """ Load and render the google verification template """

    template = loader.get_template('content/google428ef5aab2bc0870.html')
    context = {}
    return HttpResponse(template.render(context, request))
