from evaluation_criteria.models import EvaluationCriteria
from django import forms


class CreateEvaluationCriteriaForm(forms.ModelForm):
    class Meta:
        model = EvaluationCriteria
        fields = ["name"]
