from django import forms
from .models import dairy

#forms are a way to manipulate the form_as_p method to show certain variables form your database


class EntryCreateForm(forms.ModelForm):
  class Meta:
    model = dairy
    fields = ('text','color_type',)