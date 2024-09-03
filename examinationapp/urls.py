from django.urls import path

from . import views

app_name = "examinationapp"

urlpatterns = [
    path("", views.courses_page, name="home"),
    path("course/<int:id>/", views.course_detail, name="detail"),
    path("rate/<int:id>/", views.rate, name="rate"),
    path("login/", views.user_login, name="login"),
    path("registration/", views.register, name="register")
]
