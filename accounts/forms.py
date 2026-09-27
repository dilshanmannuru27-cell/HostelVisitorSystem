from django import forms
from django.contrib.auth.models import User
from .models import Student

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class StudentRegistrationForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    student_id=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    room_number=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    hostel_block=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    def clean_username(self):
        x=self.cleaned_data['username']
        if User.objects.filter(username=x).exists(): raise forms.ValidationError('Username already exists.')
        return x
    def clean_student_id(self):
        x=self.cleaned_data['student_id']
        if Student.objects.filter(student_id=x).exists(): raise forms.ValidationError('Student ID already exists.')
        return x
