from courses.models import Course, Major,Assignment
from django import forms


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            "course_id",
            "course_name",
            "evaluation_criteria",
            "credits_worth",
            "associated_majors",
        ]


class AddMajorForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = ["name", "total_credits"]

class AddAssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields=('name', 'grade_given')