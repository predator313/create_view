from .models import Student
from django import forms
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        # fields=['name','email','password']
        fields='__all__'
        widgets={'name':forms.TextInput(attrs={'class':'formclass'}),'email':forms.TextInput(attrs={'class':'emailclass'}),'password':forms.PasswordInput(attrs={'class':'passclass'})}