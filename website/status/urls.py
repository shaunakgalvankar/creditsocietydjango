from django.urls import path
from . import views

app_name='status'
urlpatterns = [
    # /status
    path('', views.index,name="index"),
    path('details',views.details,name="details"),
    path('custlogin',views.custlogin,name="custlogin"),
    path('shares',views.shares,name="shares"),
    path('fixedDeposits',views.fixedDeposits,name="fixedDeposits"),
    path('Loansuser',views.Loansuser,name="Loansuser"),
    path('MonthlyDeduction',views.MonthlyDeduction,name="MonthlyDeduction"),
    path('Investment',views.Investment,name="Investment")



]
