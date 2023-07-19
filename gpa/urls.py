from django.urls import path
from gpa.views import index

urlpatterns = [
    path(
        "homepage/",
        index,
        name="index",
    ),
]
