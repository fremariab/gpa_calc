from django.shortcuts import render, redirect
from courses.forms import AddCourseForm, AddMajorForm, AddAssignmentForm

# Create your views here.


def add_course(request):
    if request.method == "POST":
        form = AddCourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = AddCourseForm()
    return render(request, "add_course.html", {"form": form})


def add_major(request):
    if request.method == "POST":
        form = AddMajorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = AddMajorForm()
    return render(request, "add_major.html", {"form": form})


def add_assignment(request):
    if request.method == "POST":
        form = AddAssignmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = AddAssignmentForm()
    return render(request, "add_assignment.html", {"form": form})
