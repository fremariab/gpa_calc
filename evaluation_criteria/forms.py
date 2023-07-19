from evaluation_criteria.models import EvaluationCriteria
from django import forms


class AddEvaluationCriteriaForm(forms.ModelForm):
    class Meta:
        model = EvaluationCriteria
        fields = ["name", "weighting"]
