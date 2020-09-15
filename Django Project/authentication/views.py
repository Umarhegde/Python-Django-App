from django.shortcuts import render, redirect

def register(request):
  return render(request,'authentication/register.html')

def login(request):
  return render(request,'authentication/login.html')

def logout(request):
  return redirect('index')

def dashboard(request):
  return render(request,'authentication/dashboard.html')