from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Semester(models.Model):
    number_of_courses = models.IntegerField(
        verbose_name="Number of Courses",
        validators=[MaxValueValidator(6), MinValueValidator(4)],
    )

    class AcademicTerms(models.TextChoices):
        yearone_semesterone = "Y1S1", "Year 1 Semester 1"
        yearone_semestertwo = "Y1S2", "Year 1 Semester 2"
        yeartwo_semesterone = "Y2S1", "Year 2 Semester 1"
        yeartwo_semestertwo = "Y2S2", "Year 2 Semester 2"
        yearthree_semesterone = "Y3S1", "Year 3 Semester 1"
        yearthree_semestertwo = "Y3S2", "Year 3 Semester 2"
        yearfour_semesterone = "Y4S1", "Year 4 Semester 1"
        yearfour_semesterrwo = "Y4S2", "Year 4 Semester 2"

    academic_term = models.CharField(
        max_length=5,
        verbose_name="Academic Term",
        choices=AcademicTerms.choices,
        default=AcademicTerms.yearone_semesterone,
    )
    semester_gpa = models.DecimalField(
        verbose_name="Semester GPA", max_digits=3, decimal_places=2, null=True
    )

    def __str__(self):
        return self.field
