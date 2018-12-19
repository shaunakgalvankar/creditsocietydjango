from django.urls import path
from . import views

app_name='status'
urlpatterns = [
    # /status
    path('', views.index,name="index"),
    path('details',views.details,name="details"),
    path('test',views.test,name="test"),
    path('custlogin',views.custlogin,name="custlogin"),
    path('shares',views.shares,name="shares"),
    path('fixedDeposits',views.fixedDeposits,name="fixedDeposits"),
    path('Loans',views.Loans,name="Loans")



]
