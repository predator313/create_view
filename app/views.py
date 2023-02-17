from django.shortcuts import render,HttpResponse
from django.views.generic.edit import CreateView
from .models import Student
from django.views.generic.base import TemplateView
from django import forms
# Create your views here.
class CreateStudent(CreateView):
    model=Student
    template_name='app/home.html'
    fields=['name','email','password']
    success_url='/thank/'
    #now use the method get_from 
    #to give class to the particular label
    def get_form(self):
        form= super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget=forms.PasswordInput(attrs={'class':'pass'})
        return form

class ThankView(TemplateView):
    template_name='app/thanku.html'
