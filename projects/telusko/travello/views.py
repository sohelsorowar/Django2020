from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.name = 'Dhaka'
    dest1.desc = 'The most populated city'
    dest1.price = 1000
    return render(request,"index.html", {'dest1': dest1})