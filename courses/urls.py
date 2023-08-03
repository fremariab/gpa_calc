from django.urls import path
from courses import views

urlpatterns = [
    path("create_course/", views.create_course, name="create-course"),
    path("create_major/", views.create_major, name="create-major"),
    path("create_assignment/", views.create_assignment, name="create-assignment"),
    path("all_courses/", views.course_list, name="view-courses"),
    path("add_course/", views.add_course, name="add-course"),
    path(
        "create_evaluation_criteria/",
        views.create_evaluation_criteria,
        name="create-evaluation-criteria",
    ),
]
