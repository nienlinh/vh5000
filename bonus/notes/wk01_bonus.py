

from bonus.models import Prize, Winner


wk01= {
       "domesticTravel": ["21", "32", "98", "67", "97", "410"],
   "iYuan": ["64", "85"],
   "agriculture": ["89", "32", "54", "597", "453", "152"],
   "artFunE": ["96", "15", "07", "30", "73", "98", "19", "11"],
   "artFunP": ["39", "37", "23", "36", "79", "08", "14", "75"],
   "sports": ["97", "13", "19", "55", "71", "93", "381", "734", "644", "453", "985"],
   "hakka": ["81", "900"],
   "rgionalRevitalization": ["081", "105", "594", "188", "089", "396", "521", "467", "912", "798", "358", "441", "367", "941", "335"]

   }

p = Prize.objects.get(cname='國旅劵')
p = Prize.objects.get(pid='domesticTravel')



for prize in wk01:
    print (prize, end='')
    winnerList = wk01[prize]
    p = Prize.objects.get(pid = prize)
    for w in winnerList:
        winner = Winner(last_ssn=w, prize_id = p)
        winner.save()

for prize in wk01:
    print (prize, end='')
    winnerList = wk01[prize]
    p = Prize.objects.get(pid = prize)
    for w in winnerList:
        winner = Winner(last_ssn=w, prize_id = p)
        winner.save()



for p in Prize.objects.all():  
    print (p.pid, p.cname)  


for w in domesticTravel:


# clear a table
Winner.objects.all().delete()    