from django.shortcuts import render
from .models import *
# Create your views here.
def register(request):
    return render(request,'dayday/register.html')
