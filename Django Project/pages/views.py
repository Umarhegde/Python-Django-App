from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# def homePageView(request):
# 	return HttpResponse('<h1>Hello, World!</h1>')

def index(request):
	return render(request,'pages/index.html')

def contact(request):
	return render(request,'pages/contact.html')

def about(request):
	#return HttpResponse('<h1>Our team is Working hard to create this website</h1>')
	return render(request,'pages/about.html')






