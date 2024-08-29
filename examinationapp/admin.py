from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "rate"]

admin.site.register(Course)
admin.site.register(Lecture)
