from django.shortcuts import render

# Create your views here.

def new(request):
    d={'a': 10}
    return render(request,'welcome.html',context=d)