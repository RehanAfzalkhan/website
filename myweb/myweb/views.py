
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse('<h1>Welome this response is working</h1>')
    return render(request,'index.html')