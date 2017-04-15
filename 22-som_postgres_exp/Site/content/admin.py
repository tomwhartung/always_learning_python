""" Placeholder admin module is currently empty.

Purpose: placeholder for if and when we want to implement an admin module
Author: (none)
Date: Winter, 2017.
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none)
"""

from django.contrib import admin

from .models import Quiz
from .models import Score

admin.site.register(Quiz)
admin.site.register(Score)
