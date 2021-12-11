from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from .models import Prize, Winner

def how(request):
    return render(
        request,
        'bonus/how.html',
    )

def index(request):
    prizeList = Prize.objects.all()
    winnerList = Winner.objects.all()
    winnerListDict = {} # 由 pid 取得獲獎者的 list
    prizeCNameDict = {} # 由 pid 取得 p cname

    for p in prizeList:
        wList = [w.last_ssn for w in Winner.objects.filter(prize_id=p)]
        winnerListDict[p.pid] = wList
        prizeCNameDict[p.pid] = p.cname
    
    print (str(winnerListDict))
    print (str(prizeCNameDict))
    
    return render(
        request,
        'bonus/index.html',
        context={'winnerList_dict': winnerListDict,
                 'prizeCName_dict': prizeCNameDict,}
    )

from django.views.generic import ListView
from django.views.generic import DetailView

class PrizeListView(ListView):
    model=Prize

class PrizeDetailView(DetailView):
    model=Prize
