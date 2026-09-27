from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import LoginForm,StudentRegistrationForm
from .models import Student

def login_view(request):
    form=LoginForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        u=authenticate(request,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
        if u:
            login(request,u); return redirect('home')
        form.add_error(None,'Invalid username or password.')
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    logout(request); return redirect('home')

def register_student(request):
    form=StudentRegistrationForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        d=form.cleaned_data
        u=User.objects.create_user(username=d['username'],password=d['password'],first_name=d['first_name'],last_name=d['last_name'],email=d['email'])
        Student.objects.create(user=u,student_id=d['student_id'],phone=d['phone'],room_number=d['room_number'],hostel_block=d['hostel_block'])
        messages.success(request,'Account created. Please log in.')
        return redirect('login')
    return render(request,'accounts/register.html',{'form':form})

@login_required
def profile(request):
    student=getattr(request.user,'student_profile',None)
    return render(request,'accounts/profile.html',{'student':student})
