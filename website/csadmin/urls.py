from django.urls import path
from . import views

app_name='csadmin'
urlpatterns = [
    # /status
    path('', views.commander,name="commander"),


]
