from django.shortcuts import render,HttpResponse
from django.views.generic.edit import CreateView
from .models import Student
# Create your views here.
class CreateStudent(CreateView):
    model=Student
    template_name='app/home.html'
    fields=['name','email','password']
    success_url='/'
