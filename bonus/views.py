from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Prize

def index(request):
    prizeList = Prize.objects.all()

    return render(
        request,
        'bonus/index.html',
        context = {'prize_list': prizeList})