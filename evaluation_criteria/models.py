from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class EvaluationCriteria(models.Model):
    name = models.CharField(max_length=50)
    weighting = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
