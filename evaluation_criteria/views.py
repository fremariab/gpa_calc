from django.shortcuts import render, redirect
from evaluation_criteria.forms import CreateEvaluationCriteriaForm

# Create your views here.


def create_evaluation_criteria(request):
    if request.method == "POST":
        form = CreateEvaluationCriteriaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = CreateEvaluationCriteriaForm()
    return render(request, "create_evaluationcriteria.html", {"form": form})
