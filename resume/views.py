from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ResumeForm, LoginForm

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        resume_form = ResumeForm(request.POST)
        if user_form.is_valid() and resume_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            resume = resume_form.save(commit=False)
            resume.user = user
            resume.save()
            login(request, user)
            return redirect('profile')
    else:
        user_form = RegisterForm()
        resume_form = ResumeForm()
    return render(request, 'register.html', {'user_form': user_form, 'resume_form': resume_form})

def user_login(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('profile')
            else:
                error = 'Invalid username or password'
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'error': error})

@login_required
def profile(request):
    return render(request, 'profile.html')
