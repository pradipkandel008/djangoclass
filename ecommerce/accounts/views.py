from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from .forms import LoginForm, CustomRegisterForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .auth import unauthenticated_user, user_only, admin_only
from .models import Profile
from django.contrib.auth import update_session_auth_hash


@unauthenticated_user
def homepage(request):
    return render(request, 'accounts/homepage.html')


@unauthenticated_user
def register_user(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, username=user.username, email=user.email)
            # user.is_superuser = True
            # user.is_staff = True
            # user.is_active = False
            # user.save()
            messages.add_message(request, messages.SUCCESS, 'User registered.')
            return redirect('/login')
        else:
            context = {
                'form_backend': form
            }
            messages.add_message(request, messages.ERROR, 'Please verify form fields.')
            return render(request, 'accounts/register.html', context)
    context = {
        'form_backend': CustomRegisterForm
    }
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            # if user is found, it returns username
            # if user is not found, it returns None
            print(user)
            if user is not None:
                if user.is_superuser and user.is_staff:
                    login(request, user)
                    return redirect('/admin-dashboard')
                elif not user.is_staff and not user.is_superuser:
                    login(request, user)
                    return redirect('/products/products')
                # elif user.is_staff and not user.is_superuser:
                #     login(request, user)
                #     return redirect('/products/products')
                # elif not user.is_staff and user.is_superuser:
                #     login(request, user)
                #     return redirect('/products/products')
            else:
                messages.add_message(request, messages.ERROR, 'User not found')
        else:
            context = {

                'form_backend': form
            }
            messages.add_message(request, messages.ERROR, 'Please verify form fields')
            return render(request, 'accounts/login.html', context)
    context = {
        'form_backend': LoginForm
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('/login')


def profile(request):
    return render(request, 'accounts/profile.html')


def update_profile(request):
    user = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile Updated')
            return redirect('/profile')
        else:
            context = {
                'form_backend': form
            }
            messages.add_message(request, messages.ERROR, 'Please verify form fields')
            return render(request, 'accounts/update_profile.html', context)
    context = {
        'form_backend': ProfileForm(instance=user)
    }
    return render(request, 'accounts/update_profile.html', context)


def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, 'Password Updated.')
        else:
            messages.add_message(request, messages.ERROR, 'Please verify form fields')
            context = {
                'form_backend': form
            }
            return render(request, 'accounts/change_password.html', context)
    context = {
        'form_backend': PasswordChangeForm(user)
    }
    return render(request, 'accounts/change_password.html', context)





