from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render (request,'index.html')


@login_required
def commander(request):
    return render (request,'base.html')
