from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from evaluation_criteria.models import EvaluationCriteria

# Create your models here.


class Major(models.Model):
    class MajorName(models.TextChoices):
        CS = "CS", "Computer Science"
        BA = "BA", "Business Administration"
        CE = "CE", "Computer Engineering"
        EE = "EE", "Electrical Engineering"
        MIS = "MIS", "Management Information Systems"
        ME = "ME", "Mechanical Engineering"
        GN = "GN", "General"

    name = models.CharField(max_length=30, choices=MajorName.choices, default=MajorName.GN)
    total_credits = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(34)]
    )


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=8)
    course_name = models.CharField(max_length=40)

    class Credits(models.IntegerChoices):
        FULL = 1, "Full"
        HALF = 0.5, "Half"

    evaluation_criteria = models.ForeignKey(EvaluationCriteria, on_delete=models.SET_NULL,null=True)
    credits_worth = models.CharField(
        choices=Credits.choices, default=Credits.FULL, max_length=4
    )
    associated_majors = models.ForeignKey(Major, on_delete=models.SET_NULL,null=True)
