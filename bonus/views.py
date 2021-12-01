from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Prize, Winner


def index(request):
    prizeList = Prize.objects.all()
    winnerList = Winner.objects.all()
    winnerDict = {}
    winnerMap = {}

    for p in prizeList:
        wList = [w.last_ssn for w in Winner.objects.filter(prize_id=p)]
        print(wList)
        winnerDict[p.pid] = wList
        winnerMap[p.pid] = p.cname

    return render(
        request,
        'bonus/index.html',
        context={'prize_list': prizeList,
                 'winner_list': winnerList,
                 'winner_dict': winnerDict,
                 'winner_map': winnerMap,}
    )
