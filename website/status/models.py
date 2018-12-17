from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    """This is the schema for the account of every staff member"""
    monthlyDeduction=models.IntegerField()
    corpus=models.IntegerField()
    accountholder=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    dateofjoining=models.DateField()


    def __str__(self):
        return self.accountholder.username

class Shares(models.Model):
    '''this is the schema for the shares assigned to every member'''
    sharesStartingNumber=models.IntegerField()
    sharesEndingNumber=models.IntegerField()
    valueoftheshares=models.IntegerField()
    shareholdersName=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)


class Loan(models.Model):
    '''this is the schema for the loans given to the member only of the credit society'''
    loanAmount=models.IntegerField()
    emi=models.IntegerField()
    repaymentDue=models.DateField()
    rateOfInterest=models.FloatField()
    loanGivenTo=models.CharField(max_length=50)




class FixedDeposits(models.Model):
    '''this is the schema for the details of the FDS that the credit society invests in
    and also their return details '''
    fdCapital=models.IntegerField()
    rateOfInterest=models.FloatField()
    maturityDate=models.DateField()
