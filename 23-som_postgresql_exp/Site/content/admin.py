""" Placeholder admin module is currently empty.

Purpose: placeholder for if and when we want to implement an admin module
Author: (none)
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none)
"""

from django.contrib import admin

from .models import Answer
from .models import Quiz

admin.site.register(Answer)
admin.site.register(Quiz)
