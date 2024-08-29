from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

def courses_page(request):
    courses = Course.objects.all()
    title = [course.title for course in courses]
    descr = [course.description for course in courses]
    rate = [course.rate for course in courses]

    print(title)
    context = {
        "courses": courses,
        "title": title,
        "descr": descr,
        "rate": rate,
    }

    return render(request, "courses.html", context)


def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    context = {
        "title": course.title,
        "rate": course.rate,
        "descr": course.description
    }
    return render(request, "course_detail.html", context)


def rate(request):
    return render(request, "rate.html", {})

