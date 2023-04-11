from django.shortcuts import render

# Create your views here.

def display(request):
    return render(request, 'index.html')

def display1(request):
    return render(request, 'codes.html')

def display2(request):
    return render(request, 'login.html')

def display3(request):
    return render(request, 'codes1.html')
