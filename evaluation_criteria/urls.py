from django.urls import path
from evaluation_criteria.views import create_evaluation_criteria

urlpatterns = [
    path(
        "create_evaluation_criteria/",
        create_evaluation_criteria,
        name="create-evaluation-criteria",
    ),
]
