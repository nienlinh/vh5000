from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Prize, Winner


def index(request):
    prizeList = Prize.objects.all()
    winnerList = Winner.objects.all()

    return render(
        request,
        'bonus/index.html',
        context={'prize_list': prizeList, 'winner_list': winnerList})
