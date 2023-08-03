from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from authentication.forms import SignUpForm
from django.contrib.auth import authenticate,login

# Create your views here.
def signup(request):
    if request.method == "POST":
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
