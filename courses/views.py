from django.shortcuts import render, redirect
from courses.forms import (
    CreateAssignmentForm,
    CreateCourseForm,
    CreateMajorForm,
    AddCourseForm,
)
from django.views.generic import ListView
from courses.models import Course, Assignment, Major
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


@login_required
def create_course(request):
    if request.method == "POST":
        form = CreateCourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("create-course")

    else:
        form = CreateCourseForm()
    return render(request, "admin/create_course.html", {"form": form})


@login_required
def create_major(request):
    if request.method == "POST":
        form = CreateMajorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = CreateMajorForm()
    return render(request, "admin/create_major.html", {"form": form})


@login_required
def create_assignment(request):
    if request.method == "POST":
        form = CreateAssignmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = CreateAssignmentForm()
    return render(request, "user/create_assignment.html", {"form": form})


def course_list(request):
    courses_list = Course.objects.filter(student=request.user)

    return render(request, "user/view_courses.html", {"courses_list": courses_list})


@login_required
def add_course(request):
    if request.method == "POST":
        form = AddCourseForm(request.POST)

        if form.is_valid():
            course = form.save(commit=False)
            course.save()

            course.student.add(request.user)
            return redirect("index")

    else:
        form = AddCourseForm()
    return render(request, "user/add_course.html", {"form": form})
