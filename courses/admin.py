from django.contrib import admin
from courses.models import Assignment, Course, Major


# Register your models here.
admin.site.register(Major)
# admin.site.register(Course)
admin.site.register(Assignment)


class CourseAdmin(admin.ModelAdmin):
    """Admin View for"""

    list_display = ("course_id", "course_name", "credits_worth")

    ordering = ("course_id",)


admin.site.register(Course, CourseAdmin)
