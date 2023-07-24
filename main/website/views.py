from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView





# Create your views here.

def home(request):
  
  return render(request, 'website/introduction.html')

def calendar(request):
  
  return render(request, 'website/calendar.html')

def contact(request):
  
  return render(request, 'website/contact.html')

def header(request):
  
  return render(request, 'website/header.html')

def introduction(request):
  
  return render(request, 'website/introduction.html')

def login(request):
  
  return render(request, 'website/login.html')

def program(request):
  
  return render(request, 'website/program.html')

def signup(request):
  
  return render(request, 'website/signup.html')

def todo(request):
  
  return render(request, 'website/todo.html')

def hours(request):
  
  return render(request, 'website/hours.html')

def minutes(request):
  
  return render(request, 'website/your-name.html')

# def home_view(request):

#   if request.method == "GET" and 'number_input' in request.GET:
        
#         number = int(request.GET.get('number_input'))
        
#         hours = number * 60
        
#   else:
#         context = {}

#   # return render(request, 'home.html', context) 

#   return render(request, 'website/hours.html')
  

#   # return HttpResponse("Here is my response") 




