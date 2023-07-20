from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class EvaluationCriteria(models.Model):
    name = models.CharField(max_length=50, verbose_name="Evaluation Criteria Name")
    weighting = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Weighting",
        max_digits=5,
        decimal_places=5,
    )
