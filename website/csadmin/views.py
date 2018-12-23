from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from status.models import Account,Loan,FixedDeposits,Shares,User,Department
from django.forms import ModelForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
def index(request):
    return render (request,'index.html')


@login_required
def commander(request):
    return render (request,'console.html')

@login_required
def members(request):
    users=User.objects.all
    accounts=Account.objects.all
    context={
        'users':users,
        'accounts':accounts
    }
    return render (request,'members.html',context=context)

@login_required
def bank(request):
    return render (request,'bank.html')

@login_required
def loansadmin(request):
    return render (request,'loansadmin.html')

@login_required
def totalmoney(request):
    return render (request,'totalmoney.html')

#class adduseraccountform(ModelForm):
class AccountCreate(CreateView):
        model=User
        fields=['first_name','last_name','username','date_joined']
