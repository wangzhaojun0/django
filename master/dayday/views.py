#coding=utf-8
from django.shortcuts import render,redirect
from .models import *
from django import forms

# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

def register(request):
    return render(request,'dayday/register.html')

def login(request):
    return render(request,'dayday/login.html')

def register_handle(request):
    post = request.POST

    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')

    if upwd != upwd2:
        return redirect('/user/register/')

    user = UserInfo()
    user.uname = uname
    user.upwd = upwd
    user.uemail=uemail

    user.save()

    return redirect('/user/login/')


def login_handle(request):
    if request.method == 'POST':

        user = UserInfo.objects.filter(uname = request.POST['username'],upwd = request.POST['pwd'])
        print(user)
        if user:
            return redirect('/user/index/')



