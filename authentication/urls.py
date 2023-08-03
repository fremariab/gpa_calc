from django.urls import path
from authentication import views

# from authentication.views import CustomLoginView

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    
    # path('accounts/login/',CustomLoginView.as_view(),name='login')
]
