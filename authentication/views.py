from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from authentication.forms import SignUpForm

# from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login

# from authentication.models import CustomUser
from django.contrib.auth.hashers import make_password
import uuid


# Create your views here.
def generate_random_username():
    return str(uuid.uuid4())[:8]


def signup(request):
    if request.method == "POST":
        #     form=CustomLogin
        #     username = generate_random_username()
        #     password = request.POST.get("password")
        #     hased_password = make_password(password)
        #     user = CustomUser.objects.create_user(username=username, password=password)

        #     request.session["username"] = user.username

        #     return redirect("login")
        # else:
        #     return render(request, "signup.html")
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()

            raw_password = form.cleaned_data.get("password1")

            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "user/signup.html", {"form": form})


# class CustomLoginView(LoginView):
#     template_name = "registration/login.html"
#     authentication_form = CustomLoginForm
