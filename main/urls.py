from django.urls import path
from . import views

app_name = "main"


from . import views
from rest_framework import routers
from django.urls import path, include


urlpatterns = [


    #crypto api
    path('create-wallet/', views.WalletView),
    path('get-bnb-balance/<str:wallet_address>/', views.GetBnbBalanceView),
    path('send-bnb/', views.SendBnbCoin),

    path('get-bep-balance/<str:wallet_address>/', views.GetBepBalanceView),
    path('send-bep/', views.SendBepCoin),

    #get balance
    #send bnb
    #send bep




]

