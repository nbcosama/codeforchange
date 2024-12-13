from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create_account_api' , views.create_account_api, name='create_account_api')
]

