
# 以下程式碼片段，是在 shell (cmd 命令列) 下執行的
# 要先執行 python manage.py shell 後進入 python 的環境，才能執行以下命令

# 匯入資料模組
from bonus.models import Prize, Winner

# 印出所有的 prize 的 pid, cname
for p in Prize.objects.all():  
    print (p.pid, p.cname)  

# 取得 cname 為 '國旅劵' 的獎項物件
p = Prize.objects.get(cname='國旅劵')

# 把資料都清掉
Winner.objects.all().delete()    
Prize.objects.all().delete()

# 取得 pid 為 'domesticTravel' 的獎項物件
p = Prize.objects.get(pid='domesticTravel')
print (p)

name_mapping = {
            "domesticTravel": "國旅劵",
            "iYuan": "i 原劵",
            "agriculture": "農遊劵",
            "artFunE": "藝Fun劵 數位",
            "artFunP": "旅遊劵 紙本",
            "sports": "動滋劵",
            "hakka": "客庄劵",
            "rgionalRevitalization": "地方創生劵"
        }


# 以下程式會建立 prize 的物件
for p, n in name_mapping.items():
    p = Prize(pid=p, cname = n, amount = 100)
    p.save()
       
print (Prize.objects.all())       

# 宣告 wk01 的資料
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

for prize in wk01:
    winnerList = wk01[prize]
    p = Prize.objects.get(pid = prize)
    for w in winnerList:
        winner = Winner(last_ssn=w, prize_id = p)
        winner.save()

print (Winner.objects.all())       
