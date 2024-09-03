from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "rate"]

class LectureAdmin(admin.ModelAdmin):
    list_display = ["user", "age"]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lecture,LectureAdmin)
admin.site.register(ExaminationUser)
