from django.shortcuts import render
from .models import dairy

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import Http404 
from .forms import EntryCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.




class EntriesList(LoginRequiredMixin, ListView):
    model = dairy
    template_name = "dairy/entrie_list.html"
    context_object_name = 'entry'
    def get_context_data(self, **kwargs): #this si so only the user get's his own data 
        context = super().get_context_data(**kwargs)
        context['entry'] = context['entry'].filter(user=self.request.user)
        return context

class EntriesCreate(LoginRequiredMixin, CreateView):
     model = dairy
     template_name = "dairy/entrie_creation_form.html"
     # fields = ["text", "color_type"]
     form_class = EntryCreateForm
     success_url = "/dairy/entrie/list"
     context_object_name = 'entry'
     def form_valid(self, form): #so that you cannot see other users from models.users
        form.instance.user = self.request.user
        return super(EntriesCreate, self).form_valid(form)
     

class EntriesUpdate(LoginRequiredMixin, UpdateView):
     model = dairy
     template_name = "dairy/entrie_update_form.html"
     fields = ["text", "color_type"]
     success_url = "/dairy/entrie/list"
     context_object_name = 'entry'

class EntriesDelete(LoginRequiredMixin, DeleteView):
     model = dairy
     template_name = "dairy/entrie_delete_form.html"
     success_url = "/dairy/entrie/list"
     context_object_name = 'entry'
    #  fields = ["text"]  there’s no need to add in fields since if we’re deleting an instance,
    #   we’ll delete everything associated with that instance.

    