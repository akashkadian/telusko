from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
d= { 'a':'Jai', 'b':'Shree', 'var':'SINTU aka don', 'c': 'Ram'}
dests = Destination.objects.all()

def index(request):

    return render(request, 'index.html', {'dabba': dests})


