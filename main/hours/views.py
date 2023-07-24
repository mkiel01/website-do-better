from django.shortcuts import render
from .models import hours
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import Http404 

# Create your views here.


class HoursList(ListView):
    model = hours
    template_name = "hours/inputhour_list.html"

class HoursListCreate(CreateView):
     model = hours
     template_name = "hours/inputhour_creation_form.html"
     fields = ["inputhour"]
     success_url = "/hours/inputhour/list"
     

class HoursListUpdate(UpdateView):
     model = hours
     template_name = "hours/inputhour_update_form.html"
     fields = ["inputhour"]
     success_url = "/hours/inputhour/list"

class HoursListDelete(DeleteView):
     model = hours
     template_name = "hours/inputhour__delete_form.html"
     success_url = "/hours/inputhour/list"
    #  fields = ["text"]  there’s no need to add in fields since if we’re deleting an instance,
    #   we’ll delete everything associated with that instance.

    