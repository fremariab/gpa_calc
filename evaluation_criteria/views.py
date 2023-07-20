from django.shortcuts import render, redirect
from evaluation_criteria.forms import AddEvaluationCriteriaForm

# Create your views here.


def add_evaluation_criteria(request):
    if request.method == "POST":
        form = AddEvaluationCriteriaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = AddEvaluationCriteriaForm()
    return render(request, "add_evaluationcriteria.html", {"form": form})
