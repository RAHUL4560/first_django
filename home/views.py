from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login ,logout
from django.contrib import messages
from home.models import Image_details
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
import matplotlib.pyplot as plt
import numpy as np
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import LoadedImagedata

import json

# Create your views here.
def home(request):
    return render(request,'home/index.html')
def test(request):
    return render(request,'home/database.html')
def test7(request):
    Sql_data= Image_details.objects.all()
    if request.method == 'POST':

        CDR = request.POST['CDR']
        # exampleRadios1 = request.POST['exampleRadios1']
        optradio = request.POST['optradio']
        optradio1 = request.POST['optradio1']
        optradio2 = request.POST['optradio2']
        optradio3 = request.POST['optradio3']
        optradio4 = request.POST['optradio4']
        optradio5 = request.POST['optradio5']
        optradio6 = request.POST['optradio6']
        optradio7 = request.POST['optradio7']
        optradio8 = request.POST['optradio8']
        test7 = Image_details(CDR =CDR ,optradio=optradio,optradio1=optradio1,optradio2=optradio2,optradio3=optradio3,optradio4=optradio4,optradio5=optradio5,optradio6=optradio6,optradio7=optradio7,optradio8=optradio8)
        test7.save()
    return render(request,'home/annotation_tool.html')
def test4(request):
    return render(request,'home/index.html')
def test5(request):
    return render(request,'home/services.html')
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        #cheks for error
        if len(username) > 10:
            messages.success(request,"Username must not be more than 10 words ")
            return redirect('/')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')


        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your accound has been successfully created")
        return redirect('/')

    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username = loginusername,password = loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,"successfully Loggedin")
            return redirect('/')

        else:
            messages.success(request,'invalid user')
            return redirect('/')

def handleLogout(request):
        logout(request)
        messages.success(request,"successfully Loggedout")
        return redirect('/')

def test6(request):
            return render(request,'home/demo-image.html')


def image_metadata(request):

    if request.method == 'GET':
        try:
            image_metadata = LoadedImagedata.objects.get(pk=1)
            return Response(image_metadata.content)
        except LoadedImagedata.DoesNotExist:
            return Response({})

    elif request.method == 'PATCH':
        print(type(request.data['content']))
        try:
            image_metadata = LoadedImagedata.objects.get(pk=1)
        except LoadedImagedata.DoesNotExist:
            image_metadata = LoadedImagedata()
        image_metadata.content = request.data['content']
        image_metadata.save()
        return Response(image_metadata.content, status=status.HTTP_201_CREATED)



def handle_annotation(request):
    print ('------------ fsdfa: {}'.format(request.body))
    if request.method == 'POST':
        json_data = json.loads(request.body)
        print ('---- JSON DATA ----\nDATA: {}'.format(json_data))
    return Response({})
