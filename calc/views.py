from django.shortcuts import render
from django.http import HttpResponse

d= { 'a':'Jai', 'b':'Shree', 'var':'SINTU aka don', 'c': 'Ram'}
def home(request):
    return render(request, 'home.html', d)

def add(request):
    v1= int(request.POST["num1"])
    v2= int(request.POST["num2"])
    v3= int(request.POST["num3"])
    res= v1+ v2 + v3
    return render(request, 'result.html', {'result':res})




