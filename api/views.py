from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import Register
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def index(request):
    print("Get Method")
    return Response("hello get method in index")

@api_view(['GET','POST'])
def register(request):
    if request.method == 'GET':
        
        print("register get method system")
        obj=Register.objects.all()
        serialiser=UserSerializer(obj,many=True)
        return Response({"status": "success", "data": serialiser.data}, status="200")
    elif request.method == 'POST' :
        try:
           print("post method is calling")
        #    print(request.data)
        #    data=request.data
           data=request.data
           serializer = UserSerializer(data = data)
           if serializer.is_valid():
                 serializer.save()
           return Response({"status": "success", "data": serializer.data}, status="200")
        except Exception as e:
            print("error,you are a bad guys")
            return Response(e)
        
        
@api_view(['POST'])
def login(request):
    print(request.data)
    mydata = Register.objects.filter(email="kesharwaniatul9935@gmail.com",password="12345").values()
    print(mydata)
    if len(mydata) > 0:
       return Response({"status": "success", "data": mydata}, status="200")
    return Response({"status": "failure", "data": "fail data"}, status="200")
    
