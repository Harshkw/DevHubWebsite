from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import profile

def loginUser(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username = username)
            
        except:
            messages.error(request, "Username does not exist!")

        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('profiles')

        else:
            messages.error(request, "Username or Password Invalid!")

    return render(request, "users/login_register.html")

def logoutUser(request):
    logout(request)
    messages.info(request, "User Logged Out")
    return redirect("login")

def registerUser(request):
    page = "register"
    form  = CustomUserCreationForm()

    if request.method == "POST":
        form  = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User Account Created")

            login(request, user)
            return redirect("profiles")

        else:
            messages.error(request, "Error occured in Registration")


    context = {"page": page, "form": form}
    return render(request, "users/login_register.html", context)

def profiles(request):
    profiles = profile.objects.all()
    context = {"profiles": profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profileObj = profile.objects.get(id=pk)

    topSkills = profileObj.skill_set.exclude(description__exact="")
    otherSkills = profileObj.skill_set.filter(description="")

    context = {"profile": profileObj, "topSkills": topSkills, "otherSkills": otherSkills} 
    return render(request, "users/user-profile.html", context)

@login_required(login_url="login")
def userAccount(request):
    Profile = request.user.profile

    Skills = Profile.skill_set.all()
    Projects = Profile.project_set.all()

    context = {"profile": Profile, "Skills": Skills, "Projects":Projects}
    return render(request, "users/account.html", context)

@login_required(login_url="login")
def editAccount(request):
    form = ProfileForm()
    context = {"form":form}
    return render(request, "users/profile_form.html", context)