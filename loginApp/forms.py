from django import forms
from django.forms.formsets import BaseFormSet,formset_factory
from bootstrap3.tests import TestForm
from django.forms import ModelForm,Textarea,TextInput
from .models import Blog
class ContactForm(TestForm):
    pass

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        #fields = "__all__"
        fields = ['title', 'content', 'tagName' ]
        widgets = {
            'title' : TextInput(attrs={'size': 100}),
            'content': Textarea(attrs={'cols': 100, 'rows': 20}),
           }                         
