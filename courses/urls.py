from django.urls import path
from courses.views import create_assignment, create_course, create_major

urlpatterns = [
    path("create_course/", create_course, name="create-course"),
    path("create_major/", create_major, name="create-major"),
    path("create_assignment/", create_assignment, name="create-assignment"),
]
