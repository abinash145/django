from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
	view={}
	view["feedback"]=Feedback.objects.all()
	return render(request,'index.html',view)

def about(request):
	return render(request,'about.html')

def bloghome(request):
	return render(request,'blog-home.html')

def blogsingle(request):
	return render(request,'blog-single.html')

def contact(request):
	return render(request,'contact.html')

def elements(request):
	return render(request,'elements.html')

def portfolio(request):
	return render(request,'portfolio.html')

def price(request):
	return render(request,'price.html')		

def services(request):
	return render(request,'services.html')								