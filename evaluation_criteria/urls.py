from django.urls import path
from evaluation_criteria.views import add_evaluation_criteria

urlpatterns = [
    path("add_evaluation_criteria/", add_evaluation_criteria, name="add-evaluation-criteria"),
]