from django.contrib import admin
from courses.models import Assignment, Course, Major


# Register your models here.
admin.site.register(Major)
admin.site.register(Course)
admin.site.register(Assignment)
