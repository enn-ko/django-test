import datetime
from django.shortcuts import render
from django.http import HttpResponse

now= datetime.datetime.now()
# Create your views here.
def index(request):
    return render(request, "newyear/index.html",{
        "newyear" : now.year == 1 and now.month ==1
    })

def Enn(request):
    return render(request,"newyear/enn.html",{
        "age" : 24
    })