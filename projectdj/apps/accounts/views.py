from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def active(request):
    return HttpResponse('accounts is active')