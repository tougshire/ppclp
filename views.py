from django.shortcuts import render
from django.http import HttpResponse

def morgan(request):
    return render(request, 'ppclp/morgan.html')

