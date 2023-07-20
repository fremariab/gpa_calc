from django.shortcuts import render, redirect
from courses.forms import CreateAssignmentForm, CreateCourseForm, CreateMajorForm

# Create your views here.


def create_course(request):
    if request.method == "POST":
        form = CreateCourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = CreateCourseForm()
    return render(request, "create_course.html", {"form": form})


def create_major(request):
    if request.method == "POST":
        form = CreateMajorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = CreateMajorForm()
    return render(request, "add_major.html", {"form": form})


def create_assignment(request):
    if request.method == "POST":
        form = CreateAssignmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = CreateAssignmentForm()
    return render(request, "create_assignment.html", {"form": form})
