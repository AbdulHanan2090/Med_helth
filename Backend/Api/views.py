from django.http import request
from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import mixins
from rest_framework import generics
from .serializers import Contactserializer
from .serializers import Customerserializer
from .models import Contact
from .models import Customer
from twilio.rest import Client 
from rest_framework.renderers import JSONRenderer
class Contactviewset(viewsets.ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=Contactserializer
class Customerviewset(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=Customerserializer
class Login(APIView):
    def get(self,request,data,password):
        try:
            
            if Customer.objects.filter(email=data).exists():
                
                try:
                    queryset= Customer.objects.filter(email=data).values()
                    lastSourceId = queryset[0]
                    response = {"data": lastSourceId["id"],"statusCode": status.HTTP_200_OK}
                    json = JSONRenderer().render(response)
                except Exception as e:
                    print(e)
                if lastSourceId['password']==password:
                    return Response(response)
                else:
                    return Response({"status": status.HTTP_400_BAD_REQUEST})
            else:
                return Response({"status": status.HTTP_400_BAD_REQUEST})
        except:
            return Response({"status": status.HTTP_400_BAD_REQUEST})
class Otp(APIView):
    def get(self,request,data,otp):
        try:
            if Customer.objects.filter(phone=data).exists():
                return Response({"status": status.HTTP_401_UNAUTHORIZED})
            else:
                try:
                    account_sid = 'ACc0fb50a0a88e4aa9761b80a59ffc4cba' 
                    auth_token = 'c298fa6b470a49c3b9d16e431af8c6b7' 
                    client = Client(account_sid, auth_token) 
                    
                    message = client.messages.create(         
                                                from_='+17577045416',
                                                to=f'{data}',
                                                body=f'Med Health App Your Verication Pin Is {otp} This and For Any Problem Contact With Us On This Number +971528888685 ') 
                    
                    # print(message.sid)
                    response = {"statusCode": status.HTTP_200_OK}
                    json = JSONRenderer().render(response)                    
                except Exception as e:
                    print(e)
                return Response(response)
                
        except:
            return Response({"status": status.HTTP_400_BAD_REQUEST})
class Check(APIView):
    def get(self,request,data):
        try:
            if Customer.objects.filter(phone=data).exists():
                return Response({"status": status.HTTP_401_UNAUTHORIZED})
            else:
                response = {"statusCode": status.HTTP_200_OK}
                json = JSONRenderer().render(response)
                return Response(response)
              
        except:
            return Response({"status": status.HTTP_400_BAD_REQUEST})