from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Major(models.Model):
    class MajorName(models.TextChoices):
        CS = "CS", "Computer Science"
        BA = "BA", "Business Administration"
        CE = "CE", "Computer Engineering"
        EE = "EE", "Electrical Engineering"
        MIS = "MIS", "Management Information Systems"
        ME = "ME", "Mechanical Engineering"

    name = models.CharField(
        max_length=30,
        choices=MajorName.choices,
        default=MajorName.BA,
        verbose_name="Major Name",
    )
    total_credits = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(35)],
        verbose_name="Total Credits",
        max_digits=3,
        decimal_places=1,
        null=True,
    )

    def __str__(self):
        return self.get_name_display()


class EvaluationCriteria(models.Model):
    name = models.CharField(max_length=50, verbose_name="Evaluation Criteria Name")
    weighting = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Weighting",
        max_digits=5,
        decimal_places=5,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Course(models.Model):
    course_id = models.CharField(
        primary_key=True, max_length=10, verbose_name="Course ID"
    )
    course_name = models.CharField(max_length=200, verbose_name="Course Name")

    class Credits(models.IntegerChoices):
        FULL = 1, "Full"
        HALF = 0.5, "Half"

    evaluation_criteria = models.ForeignKey(
        EvaluationCriteria,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Evaluation Criteria",
    )
    credits_worth = models.IntegerField(
        choices=Credits.choices,
        default=Credits.FULL,
        verbose_name="Credits Worth",
    )
    associated_majors = models.ManyToManyField(Major, verbose_name="Associated Majors")
    letter_grade = models.CharField(
        verbose_name="Letter Grade", max_length=2, null=True
    )
    final_grade = models.DecimalField(
        verbose_name="Final Grade", max_digits=5, decimal_places=5, null=True
    )
    course_gpa = models.DecimalField(
        verbose_name="Course GPA", max_digits=3, decimal_places=2, null=True
    )
    student = models.ManyToManyField(
        User,
    )

    def __str__(self):
        return self.course_name


class Assignment(models.Model):
    name = models.CharField(
        max_length=40,
        help_text="Enter name of assignment",
        verbose_name="Assignment Name",
    )
    grade_given = models.DecimalField(
        help_text="Enter grade given for the assignment",
        verbose_name="Grade Given",
        max_digits=5,
        decimal_places=5,
    )
    total_grade = models.DecimalField(
        help_text="Enter the total grade for the assignment",
        verbose_name="Total Grade",
        max_digits=5,
        decimal_places=5,
    )

    def __str__(self):
        return self.name
