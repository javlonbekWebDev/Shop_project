from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout


def sign_up(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('sign_in')
    form=SignUpForm()
    return render(request, 'sign_up.html', {'form':form})



def sign_in(request):
    if request.method=='POST':
        form=SignInForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('product_list')
    form=SignInForm()
    return render(request, 'sign_in.html', {'form':form})



def sign_out(request):
    logout(request)
    return redirect('sign_in')


def edit_profile(request):
    form =EditProfileForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

from django.contrib.auth import update_session_auth_hash

def reset_password(request):
    form = ChangePasswordForm(request.user, request.POST)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        return redirect('sign_in')
    form = ChangePasswordForm(request.user)
    return render(request, 'reset_password.html', {'form': form})