from django.shortcuts import render
from status.models import Account,Loan,FixedDeposits,Shares,User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def custlogin(request):
    if request.user.is_staff:
        return redirect('/csadmin/')
    else:
        return redirect('/status/details')




def index(request):
    '''code for fetching any data from the models
    for embedding it into the html template
    to be called here and saved into variables and then
    pass it as the third parameter to the render Function
    '''



    #space left for fetcing data from the models and populating the teplates


    return render(request,'cards.html')

@login_required
def details(request):
    '''this view return the details of the logged in user '''

    name=str(Account.accountholder)

    context={
    'name':name
    }

    return render(request,'details.html',context=context)


def test(request):
    return render (request,'dashboard.html')

def shares(request):
    return render (request,'shares.html')

def fixedDeposits(request):
    return render (request,'fixedDeposits.html')

def Loans(request):
    return render (request,'Loans.html')
