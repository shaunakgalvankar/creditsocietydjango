from django.shortcuts import render
from status.models import Account,Loan,FixedDeposits,Shares,User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

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

    return render(request,'dashboard.html',context=context)



@login_required
def shares(request):
    current_user_id=request.user.username
    print(current_user_id)
    shares=Shares.objects.filter(shareholdersName__username__icontains=current_user_id).get()
    context={
        'shares':shares,

    }


    return render (request,'shares.html',context=context)

@login_required
def fixedDeposits(request):
    return render (request,'fixedDeposits.html')

@login_required
def Loansuser(request):
    return render (request,'Loansuser.html')

@login_required
def MonthlyDeduction(request):
    current_user_name=request.user.username
    MonthlyDeduction=Account.objects.filter(accountholder__username__icontains=current_user_name).get()

    return render (request,'MonthlyDeduction.html',{'MonthlyDeduction':MonthlyDeduction,'current_user_name':current_user_name})

@login_required
def Investment(request):
    return render (request,'investment.html')
