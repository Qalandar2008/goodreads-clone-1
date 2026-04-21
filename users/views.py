from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from .forms import LoginForm, RegisterForm, ProfileEditForm

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')  # O'zgartiring kerakli URL ga
        return render(request, 'user/login.html', {'form': form})

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')  # O'zgartiring kerakli URL ga
        return render(request, 'user/register.html', {'form': form})


class ProfileView(View):

    def get(self, request):
        return render(request, 'user/profile.html', {'user': request.user})


class ProfileEditView(View):
    
    def get(self, request):
        form = ProfileEditForm(instance=request.user)
        return render(request, 'user/profile_edit.html', {'form': form})

    def post(self, request):
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # O'zgartiring kerakli URL ga
        return render(request, 'user/profile_edit.html', {'form': form})




