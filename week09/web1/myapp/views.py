from django.shortcuts import render, redirect
from .form import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def wrong_password(request):
  return render(request, 'wrong_password.html')


@login_required(login_url='/')
def logged_in(request):
  return render(request, 'logged_in.html')


def login2(request):
  if request.method == 'POST':
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
      cd = login_form.cleaned_data
      user = authenticate(username=cd['username'], password=cd['password'])
      if user:
        login(request, user)
        return redirect('/logged_in')
      else:
        return redirect('/wrong_password')
  if request.method == "GET":
    login_form = LoginForm()
    return render(request, 'form2.html', {'form': login_form})
