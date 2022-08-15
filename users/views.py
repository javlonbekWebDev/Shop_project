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

