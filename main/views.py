from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *
from .RayBnb import *





@api_view(['POST'])
def WalletView(request):

    if request.method == 'POST':

        wallet = CreateWallet()

        data = {
        "username": request.data["username"],
        "public_key": wallet["wallet_address"],
        "private_key": wallet["wallet_key"],

        }

        #return HttpResponse(str(request.data))

        serializer = WalletSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
def GetBnbBalanceView(request, wallet_address):

    if request.method == 'GET':
        balance = GetBalance(wallet_address, "ether")

        data = {
        "balance": str(balance),
        }

        #return HttpResponse(str(data))

        serializer = BalanceSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)

        else:
            return HttpResponse(str("errors!"))





@api_view(['GET'])
def GetBepBalanceView(request, wallet_address):
    if request.method == 'GET':
        balance = GetBalanceK(wallet_address, "ether")

        data = {
        "balance": str(balance),
        }

        #return HttpResponse(str(data))

        serializer = BalanceSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)

        else:
            return HttpResponse(str("errors!"))





@api_view(['POST'])
def SendBnbCoin(request):

    if request.method == 'POST':
        sender = request.data["sender"]
        receiver = request.data["receiver"]
        amount = request.data["amount"]
        sender_key = request.data["sender_key"]

        txn_hash = Send(sender, receiver, amount, "iotex", sender_key)

        data = {
        "txn_hash": str(txn_hash),

        }

        return Response(data)





@api_view(['POST'])
def SendBepCoin(request):

    if request.method == 'POST':
        sender = request.data["sender"]
        receiver = request.data["receiver"]
        amount = request.data["amount"]
        sender_key = request.data["sender_key"]

        txn_hash = SendK(sender, receiver, int(amount), "ether", sender_key)

        data = {
        "txn_hash": str(txn_hash),

        }

        return Response(data)

        #return HttpResponse(str(data))

        #serializer = TxnSerializer(data=data)

        #if serializer.is_valid():
        #    return Response(serializer.data)

        #else:
        #    return HttpResponse(str("errors!"))






