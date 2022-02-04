from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request) :
    return render(request, 'my_site/home.html')

def portfolio(request):
    return render(request, 'my_site/portfolio.html')

def about(request):
    return render(request, 'my_site/about.html')

def contact(request):
    return render(request, 'my_site/contact.html')