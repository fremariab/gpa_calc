from django.urls import path
from courses.views import add_course, add_major,add_assignment

urlpatterns = [
    path("add_course/", add_course, name="add-course"),
    path("add_major/", add_major, name="add-major"),
    path("add_assignment/", add_assignment, name="add-assignment"),
]
