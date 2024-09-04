from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import *
from django.contrib.auth import authenticate, login, logout

def courses_page(request):
    courses = Course.objects.all()
    title = [course.title for course in courses]
    descr = [course.description for course in courses]
    rate = [course.rate for course in courses]

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
        "descr": course.description,
        "course": course,
        "count": course.count,
    }
    return render(request, "course_detail.html", context)


def user_login(request):
    if request.method == "GET":
        return render(request, "login.html", {})

    password = request.POST.get('password')
    email = request.POST.get('email')

    user = authenticate(request, password=password, email=email)
    if user:
        login(request, user)
        return HttpResponseRedirect("/home/")
    
    return render(request, "login.html", {"error": "Username or password is wrong."})


def register(request):
    if request.method == "GET":
        return render(request, "register.html", {})

    password = request.POST.get("password")
    confirm_password = request.POST.get("confirm")
    email = request.POST.get("email")

    if password == confirm_password:
        ExaminationUser.objects.create(password=password, email=email)

    return render(request, "register.html", {"error": "Username or password is wrong."})


def rate(request, id):
    course = get_object_or_404(Course, id=id)
    print("Start ", course.count)

    if request.method == "POST":
        new_rating = request.POST.get("rating")
        print("New rating raw:", new_rating)

        if new_rating:
            try:
                new_rating = float(new_rating)  # Convert to float
                updated_rate = (course.rate * course.count + new_rating) / (course.count + 1)
                course.count += 1
                print("End ", course.count)
                course.rate = updated_rate
                course.save()

                print(f"Updated Count: {course.count}, Updated Rate: {course.rate}")
            except ValueError:
                print("Invalid rating value")

            context = {
                'course': course,
                "updated_rate": course.rate,
                "count": course.count,
            }

            return render(request, 'rate.html', context)

    context = {
        'course': course,
        "updated_rate": course.rate,
        "count": course.count,
    }

    return render(request, 'rate.html', context)
