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
	context={}
	context['message']=""
	if request.method=='POST':

		name=request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		data=Contact.objects.create(
			name=name,
			email=email,
			subject=subject,
			message=message)
		data.save()
		context["message"]="file is uploded"
		return render(request,'contact.html',context)
	elif request.method=='GET':
		return render(request,'contact.html',context)


def elements(request):
	return render(request,'elements.html')

def portfolio(request):
	return render(request,'portfolio.html')

def price(request):
	return render(request,'price.html')		

def services(request):
	return render(request,'services.html')								