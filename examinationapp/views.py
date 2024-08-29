from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def courses_page(request):
    courses = Course.objects.all()
    title = [course.title for course in courses]
    context = {
        "courses": courses,
        "name": title,
    }

    return render(request, "courses.html", context)