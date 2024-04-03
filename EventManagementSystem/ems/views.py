from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm, ProfileCompletionForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def homepage(request):

    return render(request, 'ems/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_login')
    context = {'registerform' : form}
    return render(request, 'ems/register.html', context = context)

def my_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
    else:
        form = LoginForm()
    context = {'loginform': form}
    return render(request, 'ems/my_login.html', context=context)

@login_required(login_url="my_login")
def dashboard(request):
    print(request.user)
    print(request.user.biography)
    if request.method == 'POST':
        print(request.POST)
        profile_form = ProfileCompletionForm(request.POST, user=request.user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard')
    else:
        profile_form = ProfileCompletionForm(user=request.user)
   
    return render(request, 'ems/dashboard.html', {'profile_form': profile_form})


def search(request):
    return render(request, 'ems/search.html')

@login_required(login_url="my_login")
def profile(request):
    return render(request, 'ems/profile.html')

@login_required(login_url="my_login")
def edit_profile(request):
    if request.method == 'POST':
        print(request.POST)
        profile_form = ProfileCompletionForm(request.POST, user=request.user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile') 
    else:
        profile_form = ProfileCompletionForm(user=request.user)
    
    return render(request, 'ems/edit_profile.html', {'profile_form': profile_form})

def user_logout(request):
    auth.logout(request)
    return redirect("")